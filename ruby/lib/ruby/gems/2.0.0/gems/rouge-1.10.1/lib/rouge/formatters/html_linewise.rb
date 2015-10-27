# -*- coding: utf-8 -*- #

module Rouge
  module Formatters
    class HTMLLinewise < Formatter
      def initialize(formatter, opts={})
        @formatter = formatter
        @class_format = opts.fetch(:class, '%i')
      end

      def stream(tokens, &b)
        yield "<span class=#{next_line_class}>"
        tokens.each do |tok, val|
          val.scan /\n|[^\n]+/ do |s|
            if s == "\n"
              yield "</span>\n<span class=#{next_line_class}>"
            else
              @formatter.span(tok, s)
            end
          end
        end
        yield "</span>"
      end

      def next_line_class
        @lineno ||= -1
        sprintf(@class_format, @lineno += 1).inspect
      end
    end
  end
end
