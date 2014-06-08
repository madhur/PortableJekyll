
# The Scanner is responsible for polling the watched directory at a regular
# interval and generating events when files are modified, added or removed.
# These events are passed to the DirectoryWatcher which notifies the
# registered observers.
#
# The Scanner is a pure Ruby class, and as such it works across all Ruby
# interpreters on the major platforms. This also means that it can be
# processor intensive for large numbers of files or very fast update
# intervals. Your mileage will vary, but it is something to keep an eye on.
#
class DirectoryWatcher::Scanner

  attr_accessor :glob
  attr_accessor :interval
  attr_accessor :stable
  attr_accessor :files

  # call-seq:
  #    Scanner.new { |events| block }
  #
  # Create a thread-based scanner that will generate file events and pass
  # those events (as an array) to the given _block_.
  #
  def initialize( &block )
    @events = []
    @thread = nil
    @notify = block;
  end

  # Returns +true+ if the scanner is currently running. Returns +false+ if
  # this is not the case.
  #
  def running?
    !@thread.nil?
  end

  # Start the scanner thread. If the scanner is already running, this method
  # will return without taking any action.
  #
  def start
    return if running?

    @stop = false
    @thread = Thread.new(self) {|scanner| scanner.__send__ :run_loop}
    self
  end

  # Stop the scanner thread. If the scanner is already stopped, this method
  # will return without taking any action.
  #
  def stop
    return unless running?

    @stop = true
    @thread.wakeup if @thread.status == 'sleep'
    @thread.join
    self
  ensure
    @thread = nil
  end

  # call-seq:
  #    reset( pre_load = false )
  #
  # Reset the scanner state by clearing the stored file list. Passing +true+
  # to this method will cause the file list to be pre-loaded after it has
  # been cleared effectively skipping the initial round of file added events
  # that would normally be generated.
  #
  def reset( pre_load = false )
    @events.clear
    @files = (pre_load ? scan_files : Hash.new)
  end

  # call-seq:
  #    join( limit = nil )
  #
  # If the scanner thread is running, the calling thread will suspend
  # execution and run the scanner thread. This method does not return until
  # the scanner thread is stopped or until _limit_ seconds have passed.
  #
  # If the scanner thread is not running, this method returns immediately
  # with +nil+.
  #
  def join( limit = nil )
    return unless running?
    @thread.join limit
  end

  # Performs exactly one scan of the directory for file changes and notifies
  # the observers.
  #
  def run_once
    files = scan_files
    keys = [files.keys, @files.keys]  # current files, previous files

    find_added(files, *keys)
    find_modified(files, *keys)
    find_removed(*keys)

    notify
    @files = files    # store the current file list for the next iteration
    self
  end


  private

  # Using the configured glob pattern, scan the directory for all files and
  # return a hash with the filenames as keys and +FileStat+ objects as the
  # values. The +FileStat+ objects contain the mtime and size of the file.
  #
  def scan_files
    files = {}
    @glob.each do |glob|
      Dir.glob(glob).each do |fn|
        begin
          stat = File.stat fn
          next unless stat.file?
          files[fn] = ::DirectoryWatcher::FileStat.new(stat.mtime, stat.size)
        rescue SystemCallError; end
      end
    end
    files
  end

  # Using the configured glob pattern, scan the directory for all files and
  # return an array of the filenames found.
  #
  def list_files
    files = []
    @glob.each do |glob|
      Dir.glob(glob).each {|fn| files << fn if test ?f, fn}
    end
    files
  end


  # Calling this method will enter the scanner's run loop. The
  # calling thread will not return until the +stop+ method is called.
  #
  # The run loop is responsible for scanning the directory for file changes,
  # and then dispatching events to registered listeners.
  #
  def run_loop
    until @stop
      start = Time.now.to_f

      run_once

      nap_time = @interval - (Time.now.to_f - start)
      sleep nap_time if nap_time > 0
    end
  end

  # call-seq:
  #    find_added( files, cur, prev )
  #
  # Taking the list of current files, _cur_, and the list of files found
  # previously, _prev_, figure out which files have been added and generate
  # a new file added event for each.
  #
  def find_added( files, cur, prev )
    added = cur - prev
    added.each do |fn|
      files[fn].stable = @stable
      @events << ::DirectoryWatcher::Event.new(:added, fn)
    end
    self
  end

  # call-seq:
  #    find_removed( cur, prev )
  #
  # Taking the list of current files, _cur_, and the list of files found
  # previously, _prev_, figure out which files have been removed and
  # generate a new file removed event for each.
  #
  def find_removed( cur, prev )
    removed = prev - cur
    removed.each {|fn| @events << ::DirectoryWatcher::Event.new(:removed, fn)}
    self
  end

  # call-seq:
  #    find_modified( files, cur, prev )
  #
  # Taking the list of current files, _cur_, and the list of files found
  # previously, _prev_, find those that are common between them and determine
  # if any have been modified. Generate a new file modified event for each
  # modified file. Also, by looking at the stable count in the _files_ hash,
  # figure out if any files have become stable since being added or modified.
  # Generate a new stable event for each stabilized file.
  #
  def find_modified( files, cur, prev )
    (cur & prev).each do |key|
      cur_stat, prev_stat = files[key], @files[key]

      # if the modification time or the file size differs from the last
      # time it was seen, then create a :modified event
      if cur_stat != prev_stat
        @events << ::DirectoryWatcher::Event.new(:modified, key)
        cur_stat.stable = @stable

      # otherwise, if the count is not nil see if we need to create a
      # :stable event
      elsif !prev_stat.stable.nil?
        cur_stat.stable = prev_stat.stable - 1
        if cur_stat.stable <= 0
          @events << ::DirectoryWatcher::Event.new(:stable, key)
          cur_stat.stable = nil
        end
      end
    end
    self
  end

  # If there are queued files events, then invoke the notify block given
  # when the scanner was created. The file events array is cleared at the
  # end of this method call.
  #
  def notify
    @notify.call(@events) unless @events.empty?
  ensure
    @events.clear
  end

end  # class DirectoryWatcher::Scanner
