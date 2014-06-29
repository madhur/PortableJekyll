# -*- coding: utf-8 -*-
require 'handsoap/http/part'

module Handsoap
  module Http

    # Represents a HTTP Response.
    class Response < Part
      attr_reader :status
      def initialize(status, headers, body, parts = nil)
        @status = status.to_i
        super(headers, body, parts)
      end
      def primary_part
        # Strictly speaking, the main part doesn't need to be first, but until proven otherwise, we'll just assume that.
        if multipart?
          parts.first
        else
          self
        end
      end
      private
      def inspect_head
        "--- Response ---\n" + "HTTP Status: #{status}\n"
      end
    end
  end
end
