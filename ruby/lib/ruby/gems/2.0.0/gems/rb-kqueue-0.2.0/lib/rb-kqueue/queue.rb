module KQueue
  # Queue wraps a single instance of kqueue.
  # It's possible to have more than one instance,
  # but usually unnecessary.
  #
  # New event watchers are added to a queue
  # via various `watch_*` methods.
  # For example, \{#watch\_stream\_for\_read} watches for a stream
  # to become readable, and \{#watch\_file} watches for a file to change.
  #
  # Once watchers are added, \{#run} or \{#process} can be used to fire events.
  # Note that if any event-causing conditions happen
  # between adding a watcher and running one of these methods,
  # these events are also fired once the methods are called.
  #
  # @example
  #   # Create the queue
  #   queue = KQueue::Queue.new
  #
  #   # Run this callback whenever the file path/to/foo.txt is read
  #   queue.watch_file("path/to/foo.txt", :write) do
  #     puts "Foo.txt was modified!"
  #   end
  #
  #   # Run this callback whenever this process forks or execs
  #   queue.watch_process(Process.pid, :fork, :exec) do |event|
  #     # The #flags field of the event object contains the actions that happened
  #     puts "This process has #{event.flags.map {|f| f.to_s + "ed"}.join(" and ")}"
  #   end
  #
  #   # Nothing happens until you run the queue!
  #   queue.run
  class Queue
    # The file descriptor of the kqueue.
    #
    # @private
    # @return [Fixnum]
    attr_reader :fd

    # A hash from filter names and idents to {Watcher}s.
    # The kqueue API guarantees that a (filter, ident) pair
    # uniquely identifies a watcher.
    #
    # This hash allows events to retrieve their watchers.
    #
    # @private
    # @return [{(Symbol, Fixnum) => Watcher}]
    attr_reader :watchers

    # Creates a new, empty queue.
    def initialize
      @fd = Native.kqueue
      @watchers = {}
    end

    # Watches a stream and produces an event when there's data available to read.
    #
    # This can watch files, pipes, fifos, and BPF devices.
    # For files, an event is fired whenever the file pointer
    # is not at the end of the file,
    # and the {Event#data} field is set to the offset
    # from the current position to the end of the file.
    # {Event#data} may be negative.
    #
    # For pipes and fifos, an event is fired whenever there's data to read.
    # The {Event#data} field is set to the number of bytes available.
    # When the last writer disconnects, {Event#eof?} will be set.
    #
    # For BPF devices (not supported under Darwin/OS X),
    # an event is fired when the BPF buffer is full,
    # the BPF timeout has expired,
    # or when the BPF has "immediate mode" enabled
    # and there is data to read.
    # The {Event#data} field is set to the number of bytes available.
    #
    # Note that this isn't compatible with JRuby
    # unless a native-code file descriptor is passed in.
    # This means the file descriptor must be returned by an FFI-wrapped C function.
    #
    # @param fd [IO, Fixnum] A Ruby IO stream, or the file descriptor
    #   for a native IO stream.
    # @yield [event] A block that will be run when the specified stream
    #   has data to read.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_stream_for_read(fd, &callback)
      Watcher::ReadWrite.new(self, fd, :read, callback)
    end

    # Watches a socket and produces an event when there's data available to read.
    #
    # Sockets which have previously had `Socket#listen` called fire events
    # when there is an incoming connection pending.
    # In this case, {Event#data} contains the size of the listen backlog.
    #
    # Other sockets return when there is data to be read,
    # subject to the SO_RCVLOWAT value of the socket buffer.
    # This may be overridden via the `low_water` parameter,
    # which sets a new low-water mark.
    # In this case, {Event#data} contains the number of bytes
    # of protocol data available to read.
    #
    # If the read direction of the socket has shut down,
    # then {Event#eof?} is set.
    # It's possible for {Event#eof?} to be set while there's still
    # data pending in the socket buffer.
    #
    # Note that this isn't compatible with JRuby
    # unless a native-code file descriptor is passed in.
    # This means the file descriptor must be returned by an FFI-wrapped C function.
    #
    # @param fd [Socket, Fixnum] A Ruby Socket, or the file descriptor
    #   for a native Socket.
    # @param low_water [Fixnum] The low-water mark for new data.
    # @yield [event] A block that will be run when the specified socket
    #   has data to read.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_socket_for_read(fd, low_water = nil, &callback)
      Watcher::SocketReadWrite.new(self, fd, :read, low_water, callback)
    end

    # Watches a stream and produces an event
    # when it's possible to write to the stream.
    #
    # This can watch pipes and fifos.
    # The {Event#data} field is set to the amount of space
    # remaining in the write buffer.
    # When the reader disconnects, {Event#eof?} will be set.
    #
    # Note that this isn't compatible with JRuby
    # unless a native-code file descriptor is passed in.
    # This means the file descriptor must be returned by an FFI-wrapped C function.
    #
    # @param fd [IO, Fixnum] A Ruby IO stream, or the file descriptor
    #   for a native IO stream.
    # @yield [event] A block that will be run when the specified stream
    #   has data to read.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_stream_for_write(fd, &callback)
      Watcher::ReadWrite.new(self, fd, :write, callback)
    end

    # Watches a socket and produces an event when it's possible to write.
    # The {Event#data} field is set to the amount of space
    # remaining in the write buffer.
    #
    # When an event is fired is subject to the
    # subject to the SO_RCVLOWAT value of the socket buffer.
    # This may be overridden via the `low_water` parameter,
    # which sets a new low-water mark.
    #
    # If the write direction of the socket has shut down,
    # then {Event#eof?} is set.
    # It's possible for {Event#eof?} to be set while there's still
    # data pending in the socket buffer.
    #
    # Note that this isn't compatible with JRuby
    # unless a native-code file descriptor is passed in.
    # This means the file descriptor must be returned by an FFI-wrapped C function.
    #
    # @param fd [Socket, Fixnum] A Ruby Socket, or the file descriptor
    #   for a native Socket.
    # @param low_water [Fixnum] The low-water mark for new data.
    # @yield [event] A block that will be run when it's possible
    #   to write to the specified socket.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_socket_for_write(fd, low_water = nil, &callback)
      Watcher::SocketReadWrite.new(self, fd, :write, low_water, callback)
    end

    # Watches a file or directory for changes.
    # The `flags` parameter specifies which changes
    # will fire events.
    #
    # The {Event#flags} field contains the changes that caused the event to be fired.
    # {Event#data} and {Event#eof?} are unused.
    #
    # Note that this only watches a single file.
    # If the file is a direcotry,
    # it will only report changes to the directory itself,
    # not to any files within the directory.
    #
    # ## Flags
    #
    # `:delete`
    # : The file was deleted.
    #
    # `:write`
    # : The file was modified.
    #
    # `:extend`
    # : The size of the file increased.
    #
    # `:attrib`
    # : Attributes of the file, such as timestamp or permissions, changed.
    #
    # `:link`
    # : The link count of the file changed.
    #
    # `:rename`
    # : The file was renamed.
    #
    # `:revoke`
    # : Access to the file was revoked,
    #   either via the `revoke(2)` system call
    #   or because the underlying filesystem was unmounted.
    #
    # @param path [String] The path to the file or directory.
    # @param flags [Array<Symbol>] Which events to watch for.
    # @yield [event] A block that will be run when the file changes.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_file(path, *flags, &callback)
      Watcher::File.new(self, path, flags, callback)
    end

    # Watches a process for changes.
    # The `flags` parameter specifies which changes
    # will fire events.
    #
    # The {Event#flags} field contains the changes that caused the event to be fired.
    # {Event#data} and {Event#eof?} are unused.
    #
    # ## Flags
    #
    # `:exit`
    # : The process has exited.
    #
    # `:fork`
    # : The process has created a child process via `fork(2)` or similar.
    #
    # `:exec`
    # : The process has executed a new process via `exec(2)` or similar.
    #
    # `:signal`
    # : The process was sent a signal.
    #   This is only supported under Darwin/OS X.
    #
    # `:reap`
    # : The process was reaped by the parent via `wait(2)` or similar.
    #   This is only supported under Darwin/OS X.
    #
    # `:track`
    # : Follow the process across `fork(2)` calls.
    #   {Event#flags} for the parent process will contain `:fork`,
    #   while {Event#flags} for the child process will contain `:child`.
    #   If the system was unable to attach an event to the child process,
    #   {Event#flags} will contain `:trackerr`.
    #   This is not supported under Darwin/OS X.
    #
    # @param pid [Fixnum] The id of the process.
    # @param flags [Array<Symbol>] Which events to watch for.
    # @yield [event] A block that will be run when the process changes.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_process(pid, *flags, &callback)
      Watcher::Process.new(self, pid, flags, callback)
    end

    # Watches for signals to this process.
    # This coexists with other signal facilities, and has lower precedence.
    # Only signals sent to the process, not to a particular thread, will fire events.
    # Event notification happens before normal signal delivery processing.
    #
    # The {Event#data} field contains the number of times the signal has been generated
    # since the last time the event was fired.
    #
    # @param signal [String, Fixnum] The name of number of the signal.
    # @yield [event] A block that will be run when the signal is received.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_for_signal(signal, &callback)
      Watcher::Signal.new(self, signal, callback)
    end

    # Sets up a watcher that fires an event
    # once every specified interval.
    #
    # The {Event#data} field contains the number of times the interval has passed
    # since the last time the event was fired.
    #
    # @param time [Number] The interval, in seconds.
    # @yield [event] A block that will be run when the interval passes.
    # @yieldparam event [Event] The Event object containing information
    #   about the event that occurred.
    # @return [Watcher] The Watcher for this event.
    # @raise [SystemCallError] If something goes wrong when registering the Watcher.
    def watch_timer(time, &callback)
      Watcher::Timer.new(self, time, callback)
    end

    # Starts the queue watching for events.
    # Blocks until \{#stop} is called.
    #
    # @see #process
    # @return [void]
    def run
      @stop = false
      process until @stop
    end

    # Stop watching for events.
    # That is, if we're in a \{#run} loop,
    # exit out as soon as we finish handling
    # the current batch of events.
    #
    # @return [void]
    def stop
      @stop = true
    end

    # Blocks until there are one or more events
    # that this queue has watchers registered for.
    # Once there are events, the appropriate callbacks are called
    # and this function returns.
    #
    # @see #run
    # @return [void]
    def process
      read_events.each {|event| event.callback!}
    end

    def poll
      read_events(false).each {|event| event.callback!}
    end

    NULL_TIMEOUT = Native::TimeSpec.new.tap { |ts|
      ts[:tv_sec] = 0
      ts[:tv_nsec] = 0
    }

    # Blocks until there are one or more filesystem events
    # that this notifier has watchers registered for.
    # Once there are events, returns their {Event} objects.
    #
    # @private
    def read_events(blocking = true)
      size = 1024
      eventlist = FFI::MemoryPointer.new(Native::KEvent, size)

      timeout = blocking ? nil : NULL_TIMEOUT
      res = Native.kevent(@fd, nil, 0, eventlist, size, timeout)

      KQueue.handle_error if res < 0
      (0...res).map {|i| KQueue::Event.new(Native::KEvent.new(eventlist[i]), self)}
    end
  end
end
