
begin
  require 'eventmachine'
  DirectoryWatcher::HAVE_EM = true
rescue LoadError
  DirectoryWatcher::HAVE_EM = false
end

if DirectoryWatcher::HAVE_EM
[:epoll, :kqueue].each {|poll| break if EventMachine.send(poll)}


# The EmScanner uses the EventMachine reactor loop to monitor changes to
# files in the watched directory. This scanner is more efficient than the
# pure Ruby scanner because it relies on the operating system kernel
# notifictions instead of a periodic polling and stat of every file in the
# watched directory (the technique used by the Scanner class).
#
# EventMachine cannot notify us when a file is added to the watched
# directory; therefore, added files are only picked up when we apply the
# glob pattern to the directory. This is done at the configured interval.
#
# Notes:
#
#  * Kqueue does not generate notifications when "touch" is used to update
#    a file's timestamp. This applies to Mac and BSD systems.
#
#  * New files are detected only when the watched directory is polled at the
#    configured interval.
# 
class DirectoryWatcher::EmScanner < ::DirectoryWatcher::Scanner

  # call-seq:
  #    EmScanner.new { |events| block }
  #
  # Create an EventMachine based scanner that will generate file events and
  # pass those events (as an array) to the given _block_.
  #
  def initialize( &block )
    super(&block)
    @timer = nil
    @run_loop = lambda {_run_loop}
    @watchers = {}
  end

  # Returns +true+ if the scanner is currently running. Returns +false+ if
  # this is not the case.
  #
  def running?
    !@timer.nil?
  end

  # Start the EventMachine scanner. If the scanner has already been started
  # this method will return without taking any action.
  #
  # If the EventMachine reactor is not running, it will be started by this
  # method.
  #
  def start
    return if running?

    unless EventMachine.reactor_running?
      @thread = Thread.new {EventMachine.run}
      Thread.pass until EventMachine.reactor_running?
    end

    @files.keys.each do |fn|
      if test ?e, fn
        _watch_file fn
        next
      end

      @files.delete fn
      @events << ::DirectoryWatcher::Event.new(:removed, fn)
    end

    _run_loop
  end

  # Stop the EventMachine scanner. If the scanner is already stopped this
  # method will return without taking any action.
  #
  # The EventMachine reactor will _not_ be stopped by this method. It is up
  # to the user to stop the reactor using the EventMachine#stop_event_loop
  # method.
  #
  def stop
    return unless running?

    EventMachine.cancel_timer @timer rescue nil
    @timer = nil

    @watchers.each_value {|w| w.stop_watching if w.active?}
    @watchers.clear

    notify
  end

  # call-seq:
  #    join( limit = nil )
  #
  # This is a no-op method for the EventMachine file scanner.
  #
  def join( limit = nil )
  end

  # :stopdoc:
  #
  # This callback is invoked by a Watcher instance when some event has
  # occured on the file. The scanner determines if the file has been
  # modified or deleted and notifies the directory watcher accordingly.
  #
  def _event!( watcher )
    fn = watcher.path
    stat = watcher.stat

    if stat
      _watch_file fn unless watcher.active?
      @files[fn] = stat
      @events << ::DirectoryWatcher::Event.new(:modified, fn)
    else
      if watcher.active?
        watcher.stop_watching
        @watchers.delete fn
      end
      @files.delete fn
      @events << ::DirectoryWatcher::Event.new(:removed, fn)
    end

    notify
  end
  # :startdoc:
 

  private

  # EventMachine cannot notify us when new files are added to the watched
  # directory. The event loop will run at the configured interval and look
  # for files that have been added or files that have become stable.
  #
  def _run_loop
    start = Time.now.to_f

    _find_added
    _find_stable

    notify

    nap_time = @interval - (Time.now.to_f - start)
    nap_time = 0.001 unless nap_time > 0
    @timer = EventMachine.add_timer nap_time, @run_loop
  end

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
    @watchers[fn] = EventMachine.watch_file fn, Watcher, self
  end

  # :stopdoc:
  #
  # This is our tailored implementation of the EventMachine FileWatch class.
  # It receives notifications of file events and provides a mechanism to
  # translate the EventMachine events into DirectoryWatcher events.
  #
  class Watcher < EventMachine::FileWatch
    def initialize( scanner )
      @scanner = scanner
      @active = true
    end

    def stat
      return unless test ?e, @path
      stat = File.stat @path
      ::DirectoryWatcher::FileStat.new(stat.mtime, stat.size, @scanner.stable)
    end

    def active?() @active; end
    def event!() @scanner._event!(self); end
    def unbind() @active = false; end
    def file_deleted() EventMachine.next_tick {event!}; end

    alias :file_modified :event!
    alias :file_moved :event!
  end
  # :startdoc:

end  # class DirectoryWatcher::EmScanner
end  # if HAVE_EM

# EOF
