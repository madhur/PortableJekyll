# -*- coding: utf-8 -*-
module Handsoap
  #
  # A simple frontend for parsing XML document with Xpath.
  #
  # This provides a unified interface for multiple xpath-capable dom-parsers,
  # allowing seamless switching between the underlying implementations.
  #
  # A document is loaded using the function Handsoap::XmlQueryFront.parse_string, passing
  # the xml source string and a driver, which can (currently) be one of:
  #
  #   :rexml
  #   :nokogiri
  #   :libxml
  #
  # The resulting object is a wrapper, of the type Handsoap::XmlQueryFront::XmlElement.
  #
  module XmlQueryFront

    # This error is raised if the document didn't parse
    class ParseError < RuntimeError; end

    # Loads requirements for a driver.
    #
    # This function is implicitly called by +parse_string+.
    def self.load_driver!(driver)
      if driver == :rexml
        require 'rexml/document'
      elsif driver == :nokogiri
        require 'nokogiri'
        begin
          gem('nokogiri') # work around bug in rubygems for Ruby 1.9

          if Gem.loaded_specs['nokogiri'].version < Gem::Version.new('1.3.0')
            raise "Incompatible version of Nokogiri. Please upgrade gem."
          end
        rescue NoMethodError
        end
      elsif driver == :libxml
        require 'libxml'
      else
        raise "Unknown driver #{driver}"
      end
      return driver
    end

    # Returns a wrapped XML parser, using the requested driver.
    #
    # +driver+ can be one of the following:
    #   :rexml
    #   :nokogiri
    #   :libxml
    def self.parse_string(xml_string, driver)
      load_driver!(driver)
      if driver == :rexml
        doc = REXML::Document.new(xml_string)
        raise ParseError.new if doc.root.nil?
        XmlQueryFront::REXMLDriver.new(doc)
      elsif driver == :nokogiri
        doc = Nokogiri::XML(xml_string)
        raise ParseError.new unless (doc && doc.root && doc.errors.empty?)
        XmlQueryFront::NokogiriDriver.new(doc)
      elsif driver == :libxml
        begin
          LibXML::XML::Error.set_handler &LibXML::XML::Error::QUIET_HANDLER
          doc = XmlQueryFront::LibXMLDriver.new(LibXML::XML::Parser.string(xml_string).parse)
        rescue ArgumentError, LibXML::XML::Error => ex
          raise ParseError.new
        end
      end
    end

    # NodeSelection is a wrapper around Array, that implicitly delegates XmlElement methods to the first element.
    #
    # It makes mapping code prettier, since you often need to access the first element of a selection.
    class NodeSelection < Array
      def to_i
        self.first.to_i if self.any?
      end
      def to_f
        self.first.to_f if self.any?
      end
      def to_boolean
        self.first.to_boolean if self.any?
      end
      def to_date
        self.first.to_date if self.any?
      end
      def to_big_decimal(decimal_places = 2)
        self.first.to_big_decimal(decimal_places) if self.any?
      end
      def to_s
        self.first.to_s if self.any?
      end
      def node_name
        self.first.node_name if self.any?
      end
      def node_namespace
        self.first.node_namespace if self.any?
      end
      def xpath(expression, ns = nil)
        self.first.xpath(expression, ns)
      end
      def /(expression)
        self.first.xpath(expression)
      end
      def to_xml
        self.first.to_xml if self.any?
      end
      def to_raw
        self.first.to_raw if self.any?
      end
    end

    # Wraps the underlying (native) xml driver, and provides a uniform interface.
    module XmlElement
      def initialize(element, namespaces = {})
        @element = element
        @namespaces = namespaces
      end
      # Registers a prefix to refer to a namespace.
      #
      # You can either register a nemspace with this function or pass it explicitly to the +xpath+ method.
      def add_namespace(prefix, uri)
        @namespaces[prefix] = uri
      end
      # Checks that an xpath-query doesn't refer to any undefined prefixes in +ns+
      def assert_prefixes!(expression, ns)
        expression.scan(/([a-zA-Z_][a-zA-Z0-9_.-]*):[^:]+/).map{|m| m[0] }.each do |prefix|
          raise "Undefined prefix '#{prefix}' in #{ns.inspect}" if ns[prefix].nil?
        end
      end
      # Returns the value of the element as an integer.
      #
      # See +to_s+
      def to_i
        t = self.to_s
        return if t.nil?
        t.to_i
      end
      # Returns the value of the element as a float.
      #
      # See +to_s+
      def to_f
        t = self.to_s
        return if t.nil?
        t.to_f
      end
      # Returns the value of the element as an boolean.
      #
      # See +to_s+
      def to_boolean
        t = self.to_s
        return if t.nil?
        t.downcase == 'true'
      end
      # Returns the value of the element as a ruby Time object.
      #
      # See +to_s+
      def to_date
        t = self.to_s
        return if t.nil?
        Time.iso8601(t)
      end
      # Returns the value of the element as an instance of BigDecimal
      #
      # See +to_s+
      def to_big_decimal(decimal_places = 2)
        t = self.to_s
        return if t.nil?
        BigDecimal.new t, decimal_places
      end
      # Returns the inner text content of this element, or the value (if it's an attr or textnode).
      #
      # The output is a UTF-8 encoded string, without xml-entities.
      def to_s
        raise NotImplementedError.new
      end
      # Returns the underlying native element.
      #
      # You shouldn't need to use this, since doing so would void portability.
      def native_element
        @element
      end
      # Returns the node name of the current element.
      def node_name
        raise NotImplementedError.new
      end
      # Returns the node namespace uri of the current element if any, +nil+ otherwise.
      # Result returned for attribute nodes varies for different drivers, currently.
      def node_namespace
        raise NotImplementedError.new
      end
      # Queries the document with XPath, relative to the current element.
      #
      # +ns+ Should be a Hash of prefix => namespace
      #
      # Returns a +NodeSelection+
      #
      # See add_namespace
      def xpath(expression, ns = nil)
        raise NotImplementedError.new
      end
      # Returns a +NodeSelection+
      def children
        raise NotImplementedError.new
      end
      # Returns the outer XML for this element.
      def to_xml
        raise NotImplementedError.new
      end
      # Returns the outer XML for this element, preserving the original formatting.
      def to_raw
        raise NotImplementedError.new
      end
      # alias of +xpath+
      def /(expression)
        self.xpath(expression)
      end
      # Returns the attribute value of the underlying element.
      #
      # Shortcut for:
      #
      #     (node/"@attribute_name").to_s
      def [](attribute_name)
        raise NotImplementedError.new
      end
    end

    # Driver for +libxml+.
    #
    # http://libxml.rubyforge.org/
    class LibXMLDriver
      include XmlElement
      def node_name
        @element.name
      end
      def node_namespace
        if @element.respond_to? :namespaces
          if namespace = @element.namespaces.namespace
            namespace.href
          end
        end
      end
      def xpath(expression, ns = nil)
        ns = {} if ns.nil?
        ns = @namespaces.merge(ns)
        assert_prefixes!(expression, ns)
        NodeSelection.new(@element.find(expression, ns.map{|k,v| "#{k}:#{v}" }).to_a.map{|node| LibXMLDriver.new(node, ns) })
      end
      def children
        NodeSelection.new(@element.children.map{|node| LibXMLDriver.new(node) })
      end
      def [](attribute_name)
        raise ArgumentError.new unless attribute_name.kind_of? String
        @element[attribute_name]
      end
      def to_xml
        @element.to_s(:indent => true)
      end
      def to_raw
        @element.to_s(:indent => false)
      end
      def to_s
        if @element.kind_of? LibXML::XML::Attr
          @element.value
        else
          @element.content
        end
      end
    end

    # Driver for +REXML+
    #
    # http://www.germane-software.com/software/rexml/
    class REXMLDriver
      include XmlElement
      def node_name
        if @element.respond_to? :name
          @element.name
        else
          @element.class.name.gsub(/.*::([^:]+)$/, "\\1").downcase
        end
      end
      def node_namespace
        if @element.respond_to? :namespace
          namespace = @element.namespace
          return if namespace == ''
        end
        namespace
      end
      def xpath(expression, ns = nil)
        ns = {} if ns.nil?
        ns = @namespaces.merge(ns)
        assert_prefixes!(expression, ns)
        NodeSelection.new(REXML::XPath.match(@element, expression, ns).map{|node| REXMLDriver.new(node, ns) })
      end
      def children
        NodeSelection.new(@element.children.map{|node| REXMLDriver.new(node) })
      end
      def [](attribute_name)
        raise ArgumentError.new unless attribute_name.kind_of? String
        @element.attributes[attribute_name]
      end
      def to_xml
        require 'rexml/formatters/pretty'
        formatter = REXML::Formatters::Pretty.new
        out = String.new
        formatter.write(@element, out)
        # patch for REXML's broken formatting
        out.gsub(/>\n\s+([^<]+)\n\s+<\//, ">\\1</")
      end
      def to_raw
        @element.to_s
      end
      def to_s
        if @element.respond_to? :text
          @element.text
        else
          @element.value
        end
      end
    end

    # Driver for +Nokogiri+
    #
    # http://nokogiri.rubyforge.org/nokogiri/
    class NokogiriDriver
      include XmlElement
      def node_name
        @element.name
      end
      def node_namespace
        @element.namespace.href if @element.namespace
      end
      def xpath(expression, ns = nil)
        ns = {} if ns.nil?
        ns = @namespaces.merge(ns)
        assert_prefixes!(expression, ns)
        NodeSelection.new(@element.xpath(expression, ns).map{|node| NokogiriDriver.new(node, ns) })
      end
      def children
        NodeSelection.new(@element.children.map{|node| NokogiriDriver.new(node) })
      end
      def [](attribute_name)
        raise ArgumentError.new unless attribute_name.kind_of? String
        @element[attribute_name]
      end
      def to_xml
        @element.serialize(:encoding => 'UTF-8')
      end
      def to_raw
        @element.serialize(:encoding => 'UTF-8', :save_with => Nokogiri::XML::Node::SaveOptions::AS_XML)
      end
      def to_s
        if @element.kind_of?(Nokogiri::XML::Text) || @element.kind_of?(Nokogiri::XML::CDATA)
          element = @element
        elsif @element.kind_of?(Nokogiri::XML::Attr)
          return @element.value
        else
          element = @element.children.first
        end
        return if element.nil?
        # This looks messy because it is .. Nokogiri's interface is in a flux
        if element.kind_of?(Nokogiri::XML::CDATA)
          element.serialize(:encoding => 'UTF-8').gsub(/^<!\[CDATA\[/, "").gsub(/\]\]>$/, "")
        else
          element.serialize(:encoding => 'UTF-8').gsub('&lt;', '<').gsub('&gt;', '>').gsub('&quot;', '"').gsub('&apos;', "'").gsub('&amp;', '&')
        end
      end
    end
  end
end
