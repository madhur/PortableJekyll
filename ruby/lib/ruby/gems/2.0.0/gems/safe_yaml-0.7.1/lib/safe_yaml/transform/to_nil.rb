module SafeYAML
  class Transform
    class ToNil
      PREDEFINED_VALUES = {
        ""      => nil,
        "~"     => nil,
        "null"  => nil,
      }.freeze

      def transform?(value)
        key = value.downcase
        return PREDEFINED_VALUES.include?(key), PREDEFINED_VALUES[key]
      end
    end
  end
end
