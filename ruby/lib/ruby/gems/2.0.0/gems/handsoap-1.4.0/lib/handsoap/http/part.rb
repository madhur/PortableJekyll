# -*- coding: utf-8 -*-

module Handsoap
  module Http

    # Represents a HTTP Part.
    # For simple HTTP-requests there is only one part, which is the response.
    class Part
      attr_reader :headers, :body, :parts

      def initialize(headers, body, parts = nil)
        @headers = headers
        @body = body
        @parts = parts
      end

      # Returns a header.
      # Returns String | Array | nil
      def [](key)
        key.to_s.downcase!
        (@headers[key] && @headers[key].length == 1) ? @headers[key].first : @headers[key]
      end

      # Returns the mime-type part of the content-type header
      def mime_type
        @headers['content-type'].first.match(/^[^;]+/).to_s if @headers['content-type']
      end

      # Returns the charset part of the content-type header
      def charset
        if @headers['content-type']
          match_data = @headers['content-type'].first.match(/^[^;]+; charset=([^;]+)/)
          if match_data
            match_data[1].to_s
          end
        end
      end

      def multipart?
        !! @parts
      end

      def inspect(&block)
        str = inspect_head
        if headers.any?
          str << headers.map { |key,values| values.map {|value| normalize_header_key(key) + ": " + value + "\n" }.join("")  }.join("")
        end
        if body
          if multipart?
            if block_given?
              str << parts.map{|part| part.inspect(&block) }.join("")
            else
              str << parts.map{|part| part.inspect }.join("")
            end
          elsif body
            str <<  "---\n"
            if block_given?
              str << yield(body)
            else
              str << body
            end
            str << "\n---"
          end
        end
      end
      
    private
      
      def inspect_head
        "--- Part ---\n"
      end

      def normalize_header_key(key)
        key.split("-").map{|s| s.downcase.capitalize }.join("-")
      end
    end
  end
end
