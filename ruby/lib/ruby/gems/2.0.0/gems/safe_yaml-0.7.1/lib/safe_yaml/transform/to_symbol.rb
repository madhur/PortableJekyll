module SafeYAML
  class Transform
    class ToSymbol
      MATCHER = /\A:\w+\Z/.freeze

      def transform?(value)
        return false unless SafeYAML::OPTIONS[:enable_symbol_parsing] && MATCHER.match(value)
        return true, value[1..-1].to_sym
      end
    end
  end
end
