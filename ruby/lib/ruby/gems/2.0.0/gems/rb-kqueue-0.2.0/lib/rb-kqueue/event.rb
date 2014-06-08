module KQueue
  # An event produced by kqueue.
  # Each {Watcher} can fire many events,
  # which are passed to that Watcher's callback.
  class Event
    # Some integer data, the interpretation of which
    # is specific to each individual {Watcher}.
    # For specifics, see the individual Watcher subclasses.
    #
    # `data` is not meaningful for all events.
    # For example, file-change notifications do not set `data`.
    #
    # @return [Fixnum]
    attr_reader :data

    # The name of the kqueue filter that created this event,
    # e.g. `:vnode` or `:read`.
    #
    # @private
    # @return [Symbol]
    attr_reader :filter

    # The {Watcher} that produced this event.
    #
    # @return [Watcher]
    def watcher
      @watcher ||= @queue.watchers[[filter, @native[:ident]]]
    end

    # An array of flags, the interpretation of which
    # is specific to each individual {Watcher}.
    #
    # If the Watcher watches for different sorts of events,
    # this is usually the specific events that actually occurred.
    # For example, for file-change notifications this could be `[:delete]`.
    #
    # `flags` is not meaningful for all events.
    # For example, readability notifications do not set `flags`.
    #
    # @return [Array<Symbol>]
    def flags
      @fflags ||= Native::Flags.from_mask("NOTE_#{filter.to_s.upcase}", @native[:fflags])
    end

    # Returns whether the end-of-file flag has been set for this event.
    # The interpretation of this is specific to each individual {Watcher}.
    #
    # `eof?` is not meaningful for all events.
    # For example, file-change notifications don't set `eof?`.
    #
    # @return [Boolean]
    def eof?
      @flags.include?(:eof)
    end

    # Creates a new event from a native event structure.
    #
    # @private
    # @param native [Native::Event] The native event structure
    #   from which to construct this event
    # @param queue [Queue] The queue that produced this event
    # @raise [SystemCallError] If this event signals an error
    def initialize(native, queue)
      @native = native
      @queue = queue
      @data = @native[:data]
      @filter = KQueue::Native::Flags.from_flag("EVFILT", @native[:filter])
      @flags = Native::Flags.from_mask("EV", @native[:flags])

      KQueue.handle_error @native[:data] if @flags.include?(:error)
    end

    # Runs the callback for this event.
    # This callback is associated with the {Watcher}
    # that produced the event.
    #
    # @private
    # @return [void]
    def callback!
      watcher.callback! self
    end
  end
end
