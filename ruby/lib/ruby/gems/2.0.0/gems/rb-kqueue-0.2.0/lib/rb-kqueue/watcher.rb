module KQueue
  # Watchers monitor for a single sort of event,
  # specified by the specific subclass and its parameters.
  # A watcher is usually created via one of the `watch_*` methods
  # on {Queue}.
  #
  # One {Queue} may have many {Watcher}s.
  # The Queue actually takes care of the checking for events,
  # via \{Queue#run #run} or \{Queue#process #process}.
  #
  # Watcher objects themselves have several useful capabilities.
  # Each subclass keeps track of its own specific information.
  # In addition, all Watchers can be \{#delete! deleted from the queue},
  # \{#add! added back in}, \{#disable! disabled}, and \{#enable! enabled}.
  class Watcher
    # The {Queue} that created this Watcher.
    #
    # @return [Queue]
    attr_reader :queue

    # Creates a new Watcher.
    #
    # @private
    # @param queue [Queue] The queue for which this watcher will be used.
    # @param ident [Fixnum] The underlying kqueue identifier for this watcher.
    # @param filter [Symbol] The name of the underlying kqueue filter for this watcher.
    # @param fflags [Array<Symbol>] Filter-specific flags.
    # @param data [Fixnum] Filter-specific data.
    # @param callback [Proc{Event -> void}] The callback that will be called
    #   on any events fired by this watcher.
    # @raise [SystemCallError] If something goes wrong when registering this Watcher.
    def initialize(queue, ident, filter, fflags, data, callback)
      @queue = queue
      @ident = ident
      @filter = filter
      @flags = []
      @fflags = fflags
      @data = data
      @callback = callback
      add!
    end

    # Adds this Watcher to \{#queue its Queue}.
    # Note that this is done automatically when the Watcher is created.
    #
    # @raise [SystemCallError] If something goes wrong when adding this Watcher.
    # @return [void]
    def add!
      kevent! :add, :clear # TODO: Don't always enable :clear
      @queue.watchers[[@filter, @ident]] = self
    end

    # Removes this Watcher from \{#queue its Queue}.
    # This means that events won't be fired
    # or even checked for.
    #
    # @raise [SystemCallError] If something goes wrong when deleting this Watcher.
    # @return [void]
    def delete!
      kevent! :delete
      @queue.watchers.delete([@filter, @ident])
    end

    # Enables this Watcher.
    # Note that this is done automatically when the Watcher is created,
    # as well as whenever \{#add!} is called.
    #
    # @raise [SystemCallError] If something goes wrong when enabling this Watcher.
    # @return [void]
    def enable!
      kevent! :enable
    end

    # Disables this Watcher.
    # This means that events won't be fired,
    # but they'll still be checked for.
    #
    # @raise [SystemCallError] If something goes wrong when enabling this Watcher.
    # @return [void]
    def disable!
      kevent! :disable
    end

    # Calls this Watcher's callback with the given {Event}.
    #
    # @private
    # @param event [Event]
    # @return [void]
    def callback!(event)
      @callback.call event
    end

    private

    # Returns a C struct corresponding to this watcher.
    #
    # @param flags [Array<Symbol>] Flags for the C struct's `flags` field,
    #   in addition to the `@flags` var.
    # @return [Native::KEvent]
    def native(flags)
      native = Native::KEvent.new
      native[:ident] = @ident
      native[:filter] = Native::Flags.to_flag("EVFILT", @filter)
      native[:flags] = Native::Flags.to_mask("EV", @flags | flags)
      native[:fflags] = Native::Flags.to_mask("NOTE_#{@filter.to_s.upcase}", @fflags)
      native[:data] = @data if @data
      native
    end

    # Runs the `kevent` C call with this Watcher's kevent struct as input.
    # This effectively means telling kqueue to perform some action
    # with this Watcher as an argument.
    #
    # @param flags [Array<Symbol>] Flags specifying the action to perform
    #   as well as any additional flags.
    # @return [void]
    # @raise [SystemCallError] If something goes wrong when performing the C call.
    def kevent!(*flags)
      if Native.kevent(@queue.fd, native(flags).pointer, 1, nil, 0, nil) < 0
        KQueue.handle_error
      end
    end
  end
end
