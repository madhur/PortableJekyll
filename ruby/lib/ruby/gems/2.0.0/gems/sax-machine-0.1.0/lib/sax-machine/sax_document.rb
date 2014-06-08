require "nokogiri"

module SAXMachine

  def self.included(base)
    base.extend ClassMethods
  end

  def parse(xml_text, on_error = nil, on_warning = nil)
    sax_handler = SAXHandler.new(self, on_error, on_warning)
    parser = Nokogiri::XML::SAX::Parser.new(sax_handler)
    parser.parse(xml_text)
    self
  end

  module ClassMethods

    def inherited(subclass)
      subclass.sax_config.send(:initialize_copy, self.sax_config)
    end

    def parse(xml_text, on_error = nil, on_warning = nil)
      new.parse(xml_text, on_error, on_warning)
    end

    def element(name, options = {})
      real_name = (options[:as] ||= name).to_s
      sax_config.add_top_level_element(name, options)
      create_attr real_name
    end

    def attribute(name, options = {})
      real_name = (options[:as] ||= name).to_s
      sax_config.add_top_level_attribute(self.class.to_s, options.merge(:name => name))
      create_attr real_name
    end

    def value(name, options = {})
      real_name = (options[:as] ||= name).to_s
      sax_config.add_top_level_element_value(self.class.to_s, options.merge(:name => name))
      create_attr real_name
    end

    def ancestor(name, options = {})
      real_name = (options[:as] ||= name).to_s
      sax_config.add_ancestor(name, options)
      create_attr(real_name)
    end

    def columns
      sax_config.columns
    end

    def column(sym)
      columns.select { |c| c.column == sym }[0]
    end

    def data_class(sym)
      column(sym).data_class
    end

    def required?(sym)
      column(sym).required?
    end

    def column_names
      columns.map { |e| e.column }
    end

    def elements(name, options = {})
      options[:as] ||= name
      if options[:class]
        sax_config.add_collection_element(name, options)
      else
        class_eval <<-SRC
          def add_#{options[:as]}(value)
            #{options[:as]} << value
          end
        SRC
        sax_config.add_top_level_element(name, options.merge(:collection => true))
      end

      if !method_defined?(options[:as].to_s)
        class_eval <<-SRC
          def #{options[:as]}
            @#{options[:as]} ||= []
          end
        SRC
      end

      attr_writer options[:as] unless method_defined?("#{options[:as]}=")
    end

    def sax_config
      @sax_config ||= SAXConfig.new
    end

    # we only want to insert the getter and setter if they haven't defined it from elsewhere.
    # this is how we allow custom parsing behavior. So you could define the setter
    # and have it parse the string into a date or whatever.
    def create_attr real_name
      attr_reader real_name unless method_defined?(real_name)
      attr_writer real_name unless method_defined?("#{real_name}=")
    end
  end

end
