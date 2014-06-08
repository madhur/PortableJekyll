module KQueue
  class Watcher
    # The {Watcher} subclass for events
    # fired when a socket can be read from or written to
    # (which of these is determined by \{ReadWrite#type}).
    # Read events are watched via {Queue#watch_socket_for_read},
    # and write events are watched via {Queue#watch_socket_for_write}.
    #
    # Note that read and write events for non-socket streams
    # use the {ReadWrite} class.
    class SocketReadWrite < ReadWrite
      # The custom low-water mark for the amount of data necessary
      # to trigger an event,
      # or `nil` if none has been set.
      #
      # @return [Fixnum, nil]
      attr_reader :low_water

      # Creates a new socket Watcher.
      #
      # @private
      def initialize(queue, fd, type, low_water, callback)
        if fd.is_a?(IO)
          @io = fd
          fd = fd.fileno
        end

        @fd = fd
        @type = type

        if low_water
          fflags = [:lowat]
          data = low_water
        else
          fflags = []
          data = nil
        end

        super(queue, @fd, type, fflags, data, callback)
      end
    end
  end
end
