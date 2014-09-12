
require 'hitimes'

module Timers
  # An exclusive, monotonic timeout class.
  class Wait
    def self.for(duration, &block)
      if duration
        timeout = self.new(duration)
        
        timeout.while_time_remaining(&block)
      else
        while true
          yield(nil)
        end
      end
    end
    
    def initialize(duration)
      @duration = duration
      @remaining = true
    end
    
    attr :duration
    attr :remaining
    
    # Yields while time remains for work to be done:
    def while_time_remaining(&block)
      @interval = Hitimes::Interval.new
      @interval.start
      
      while time_remaining?
        yield @remaining
      end
    ensure
      @interval.stop
      @interval = nil
    end
    
    private
    
    def time_remaining?
      @remaining = (@duration - @interval.duration)
    
      return @remaining > 0
    end
  end
end
