module Jekyll
  module Converters
    class CoffeeScript < Converter
      safe true
      priority :low

      def matches(ext)
        ext.downcase == ".coffee"
      end

      def output_ext(ext)
        ".js"
      end

      def convert(content)
        ::CoffeeScript.compile(content)
      end
    end
  end
end
