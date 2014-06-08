module SAXMachine
  class SAXConfig
    
    class CollectionConfig
      attr_reader :name
      
      def initialize(name, options)
        @name   = name.to_s
        @class  = options[:class]
        @as     = options[:as].to_s
        
        if options.has_key?(:with)
          # for faster comparisons later
          @with = options[:with].to_a.flatten.collect {|o| o.to_s}
        else
          @with = nil
        end
      end
      
      def accessor
        as
      end
      
      def attrs_match?(attrs)
        if @with
          @with == (@with & attrs)
        else
          true
        end
      end

      def data_class
        @class || @name
      end      
      
    protected
      
      def as
        @as
      end
      
    end
    
  end
end