module KQueue
  class Watcher
    # The {Watcher} subclass for process events.
    # Process events are watched via {Queue#watch_process}.
    class Process < Watcher
      # The process id of the process being watched.
      #
      # @return [Fixnum]
      attr_reader :pid

      # Creates a new process Watcher.
      #
      # @private
      def initialize(queue, pid, flags, callback)
        @pid = pid
        super(queue, pid, :proc, flags, nil, callback)
      end
    end
  end
end
