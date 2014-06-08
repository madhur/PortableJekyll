begin
  require 'coolio'
  DirectoryWatcher::HAVE_COOLIO = true
rescue LoadError
  DirectoryWatcher::HAVE_COOLIO = false
end

if DirectoryWatcher::HAVE_COOLIO

# The CoolioScanner uses the Coolio loop to monitor changes to files in the
# watched directory. This scanner is more efficient than the pure Ruby
# scanner because it relies on the operating system kernel notifictions
# instead of a periodic polling and stat of every file in the watched
# directory (the technique used by the Scanner class).
#
class DirectoryWatcher::CoolioScanner < ::DirectoryWatcher::Scanner

  # call-seq:
  #    CoolioScanner.new { |events| block }
  #
  # Create a Coolio based scanner that will generate file events and pass
  # those events (as an array) to the given _block_.
  #
  def initialize( &block )
    super(&block)
    @watchers = {}
  end

  # Start the Coolio scanner loop. If the scanner is already running, this method
  # will return without taking any action.
  #
  def start
    return if running?

    @timer = Timer.new self
    @thread = Thread.new {
      coolio_loop = Thread.current._coolio_loop
      @files.keys.each do |fn|
        if test ?e, fn
          _watch_file fn
          next
        end

        @files.delete fn
        @events << ::DirectoryWatcher::Event.new(:removed, fn)
      end

      @timer.attach(coolio_loop)
      coolio_loop.run
    }
  end

  # Stop the Coolio scanner loop. If the scanner is already stopped, this method
  # will return without taking any action.
  #
  def stop
    return unless running?

    @timer.detach
    @timer = nil

    @watchers.each_value {|w| w.detach}
    @watchers.clear

    notify

    @thread._coolio_loop.stop rescue nil
    @thread.kill    # for some reason the rev loop is not returning after stopping
    @thread = nil
  end

  # :stopdoc:
  #
  # This callback is invoked by a Watcher instance when some change has
  # occured on the file. The scanner determines if the file has been
  # modified or deleted and notifies the directory watcher accordingly.
  #
  def _on_change( watcher )
    fn = watcher.path
    stat = watcher.stat

    if stat
      if @files[fn] != stat
        @files[fn] = stat
        @events << ::DirectoryWatcher::Event.new(:modified, fn)
      end
    else
      watcher.detach
      @watchers.delete fn
      @files.delete fn
      @events << ::DirectoryWatcher::Event.new(:removed, fn)
    end

    notify
  end

  # This callback is invoked by the Timer instance when it is triggered by
  # the Coolio loop. This method will check for added files and stable files
  # and notify the directory watcher accordingly.
  #
  def _on_timer
    _find_added
    _find_stable
    notify
  end
  # :startdoc:


  private

  # From the list of files in the watched directory, find those that we are
  # not currently watching and add them to the watch list. Generate "added"
  # events for those newly found files.
  #
  def _find_added
    cur = list_files
    prev = @files.keys
    added = cur - prev

    added.each do |fn|
      @files[fn] = _watch_file(fn).stat
      @events << ::DirectoryWatcher::Event.new(:added, fn)
    end
  end

  # Iterate over the FileStat instances looking for those with non-nil
  # stable counts. Decrement these counts and generate "stable" events for
  # those files whose count reaches zero.
  #
  def _find_stable
    @files.each do |fn, stat|
      next if stat.stable.nil?
      stat.stable -= 1
      if stat.stable <= 0
        @events << ::DirectoryWatcher::Event.new(:stable, fn)
        stat.stable = nil
      end
    end
  end

  # Create and return a new Watcher instance for the given filename _fn_.
  #
  def _watch_file( fn )
    w = Watcher.new(fn, self)
    w.attach(@thread ? @thread._coolio_loop : Thread.current._coolio_loop)
    @watchers[fn] = w
  end

  # :stopdoc:
  #
  class Watcher < Coolio::StatWatcher
    def initialize( fn, scanner )
      super(fn, scanner.interval)
      @scanner = scanner
    end

    def on_change( *args )
      @scanner._on_change self
    end

    def stat
      return unless test ?e, path
      stat = File.stat path
      ::DirectoryWatcher::FileStat.new(stat.mtime, stat.size, @scanner.stable)
    end
  end

  class Timer < Coolio::TimerWatcher
    def initialize( scanner )
      super(scanner.interval, true)
      @scanner = scanner
    end

    def on_timer( *args )
      @scanner._on_timer
    end
  end
  # :startdoc:

end  # class DirectoryWatcher::CoolioScanner

end  # if DirectoryWatcher::HAVE_COOLIO

# EOF
