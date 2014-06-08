module SafeYAML
  class Transform
    class ToBoolean
      PREDEFINED_VALUES = {
        "yes"   => true,
        "on"    => true,
        "true"  => true,
        "no"    => false,
        "off"   => false,
        "false" => false
      }.freeze

      def transform?(value)
        key = value.downcase
        return PREDEFINED_VALUES.include?(key), PREDEFINED_VALUES[key]
      end
    end
  end
end
