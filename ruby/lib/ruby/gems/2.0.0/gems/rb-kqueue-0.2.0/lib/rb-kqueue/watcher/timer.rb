module KQueue
  class Watcher
    # The {Watcher} subclass for events fired based on a timer.
    # Timer events are watched via {Queue#watch_timer}.
    class Timer < Watcher
      # The interval on which the timer fires an event, in seconds.
      #
      # @return [Numeric]
      attr_reader :time

      # Creates a new timer Watcher.
      #
      # @private
      def initialize(time, callback)
        time, unit =
          if time < 10**-3
            [(time * 10**9).round, :nseconds]
          elsif time < 1
            [(time * 10**6).round, :useconds]
          elsif time < 10**3 && !time.is_a?(Fixnum)
            [(time * 10**3).round, nil] # milliseconds
          else
            [time.round, :seconds]
          end

        super(queue, time, :timer, Array(unit), nil, callback)
      end
    end
  end
end
