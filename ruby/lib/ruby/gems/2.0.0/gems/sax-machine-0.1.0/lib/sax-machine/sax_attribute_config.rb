module SAXMachine
  class SAXConfig

    class AttributeConfig
      attr_reader :name, :setter

      def initialize(name, options)
        @name = name.to_s
        @as = options[:as]
        @setter = "#{@as}="
        @required = options[:required]
      end

      def column
        @as || @name.to_sym
      end

      def required?
        @required
      end

      def value_from_attrs(attrs)
        attrs.index(@name) ? attrs[attrs.index(@name) + 1] : nil
      end

      def attrs_match?(attrs)
        attrs.index(@name) ? true : false
      end

      def has_value_and_attrs_match?(attrs)
        attrs_match?(attrs)
      end

      def collection?
        false
      end
    end

  end
end