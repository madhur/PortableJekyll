# -*- coding: utf-8 -*-

module Handsoap
  class Deferred
    def initialize
      @callback = nil
      @callback_cache = nil
      @errback = nil
      @errback_cache = nil
    end
    def has_callback?
      !! @callback
    end
    def has_errback?
      !! @errback
    end
    def callback(&block)
      raise "Already assigned a block for callback" if @callback
      @callback = block
      if @callback_cache
        payload = @callback_cache
        trigger_callback(*payload)
      end
      self
    end
    def errback(&block)
      raise "Already assigned a block for errback" if @errback
      @errback = block
      if @errback_cache
        payload = @errback_cache
        trigger_errback(*payload)
      end
      self
    end
    def trigger_callback(*args)
      if @callback
        @callback.call(*args)
      else
        @callback_cache = args
      end
    end
    def trigger_errback(*args)
      if @errback
        @errback.call(*args)
      else
        @errback_cache = args
      end
    end
  end
end
