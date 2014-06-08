module KQueue
  class Watcher
    # The {Watcher} subclass for events fired when a signal is received.
    # Signal events are watched via {Queue#watch_for_signal}.
    class Signal < Watcher
      # The name of the signal, e.g. "KILL" for SIGKILL.
      #
      # @return [String]
      attr_reader :name

      # The number of the signal, e.g. 9 for SIGKILL.
      #
      # @return [Fixnum]
      attr_reader :number

      # Creates a new signal Watcher.
      #
      # @private
      def initialize(queue, signal, callback)
        if signal.is_a?(String)
          @name = signal
          @number = Signal.list[signal]
        else
          @name = Signal.list.find {|_, n| n == signal}.first
          @number = signal
        end

        super(queue, @number, :signal, [], nil, callback)
      end
    end
  end
end
