module SafeYAML
  class Transform
    class ToInteger
      MATCHER = /\A\d+\Z/.freeze

      def transform?(value)
        return false unless MATCHER.match(value)
        return true, value.to_i
      end
    end
  end
end
