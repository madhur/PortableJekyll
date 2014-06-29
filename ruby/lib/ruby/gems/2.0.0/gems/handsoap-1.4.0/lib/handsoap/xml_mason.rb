# -*- coding: utf-8 -*-

module Handsoap

  # XmlMason is a simple XML builder.
  module XmlMason

    XML_ESCAPE = { '&' => '&amp;', '"' => '&quot;', '>' => '&gt;', '<' => '&lt;' }

    def self.xml_escape(s)
      s.to_s.gsub(/[&"><]/) { |special| XML_ESCAPE[special] }
    end

    class Node
      def initialize
        @namespaces = {}
      end
      def add(node_name, value = nil, options = {}) # :yields: Handsoap::XmlMason::Element
        prefix, name = parse_ns(node_name)
        node = append_child Element.new(self, prefix, name, value, options)
        if block_given?
          yield node
        end
      end
      # Registers a prefix for a namespace.
      #
      # You must register a namespace, before you can refer it.
      def alias(prefix, namespaces)
        @namespaces[prefix] = namespaces
      end
      # Finds the first element whos +node_name+ equals +name+
      #
      # Doesn't regard namespaces/prefixes.
      def find(name)
        raise NotImplementedError.new
      end
      # Finds all elements whos +node_name+ equals +name+
      #
      # Doesn't regard namespaces/prefixes.
      def find_all(name)
        raise NotImplementedError.new
      end
      def parse_ns(name)
        matches = name.match /^([^:]+):(.*)$/
        if matches
          [matches[1] == '*' ? @prefix : matches[1], matches[2]]
        else
          [nil, name]
        end
      end
      private :parse_ns
    end

    class Document < Node
      def initialize # :yields: Document
        super
        @document_element = nil
        @xml_header = true
        if block_given?
          yield self
        end
      end
      def xml_header=(xml_header)
        @xml_header = !! xml_header
      end
      def append_child(node)
        if not @document_element.nil?
          raise "There can only be one element at the top level."
        end
        @document_element = node
      end
      def find(name)
        @document_element.find(name)
      end
      def find_all(name)
        @document_element.find_all(name)
      end
      def get_namespace(prefix)
        @namespaces[prefix] || raise("No alias registered for prefix '#{prefix}'")
      end
      def defines_namespace?(prefix)
        false
      end
      def to_s
        if @document_element.nil?
          raise "No document element added."
        end
        (@xml_header ? "<?xml version='1.0' ?>\n" : "") + @document_element.to_s
      end
    end

    class TextNode
      def initialize(text)
        @text = text
      end
      def to_s(indentation = '')
        XmlMason.xml_escape(@text)
      end
    end

    class RawContent < TextNode
      def to_s(indentation = '')
        @text
      end
    end

    class Element < Node
      def initialize(parent, prefix, node_name, value = nil, options = {}) # :yields: Handsoap::XmlMason::Element
        super()
#         if prefix.to_s == ""
#           raise "missing prefix"
#         end
        @parent = parent
        @prefix = prefix
        @node_name = node_name
        @children = []
        @attributes = {}
        if options[:attributes]
          @attributes = options[:attributes]
        end
        if not value.nil?
          set_value value.to_s, options
        end
        if block_given?
          yield self
        end
      end
      # Returns the document that this element belongs to, or self if this is the document.
      def document
        @parent.respond_to?(:document) ? @parent.document : @parent
      end
      # Returns the qname (prefix:nodename)
      def full_name
        @prefix.nil? ? @node_name : (@prefix + ":" + @node_name)
      end
      # Adds a child node.
      #
      # You usually won't need to call this method, but will rather use +add+
      def append_child(node)
        if value_node?
          raise "Element already has a text value. Can't add nodes"
        end
        @children << node
        return node
      end
      # Sets the inner text of this element.
      #
      # By default the string is escaped, but you can pass the option flag :raw to inject XML.
      #
      # You usually won't need to call this method, but will rather use +add+
      def set_value(value, options = {})
        if @children.length > 0
          raise "Element already has children. Can't set value"
        end
        if options && options.include?(:raw)
          @children = [RawContent.new(value)]
        else
          @children = [TextNode.new(value)]
        end
      end
      # Sets the value of an attribute.
      def set_attr(name, value)
        full_name = parse_ns(name).join(":")
        @attributes[name] = value
      end
      def find(name)
        name = name.to_s if name.kind_of? Symbol
        if @node_name == name || full_name == name
          return self
        end
        @children.each do |node|
          if node.respond_to? :find
            tmp = node.find(name)
            if tmp
              return tmp
            end
          end
        end
        return nil
      end
      def find_all(name)
        name = name.to_s if name.kind_of? Symbol
        result = []
        if @node_name == name || full_name == name
          result << self
        end
        @children.each do |node|
          if node.respond_to? :find
            result = result.concat(node.find_all(name))
          end
        end
        return result
      end
      def value_node?
        @children.length == 1 && @children[0].kind_of?(TextNode)
      end
      def get_namespace(prefix)
        @namespaces[prefix] || @parent.get_namespace(prefix)
      end
      def defines_namespace?(prefix)
        @attributes.keys.include?("xmlns:#{prefix}") || @parent.defines_namespace?(prefix)
      end
      def to_s(indentation = '')
        # todo resolve attribute prefixes aswell
        if @prefix && (not defines_namespace?(@prefix))
          set_attr "xmlns:#{@prefix}", get_namespace(@prefix)
        end
        name = XmlMason.xml_escape(full_name)
        attr = (@attributes.any? ? (" " + @attributes.map { |key, value| XmlMason.xml_escape(key) + '="' + XmlMason.xml_escape(value) + '"' }.join(" ")) : "")
        if @children.any?
          if value_node?
            children = @children[0].to_s(indentation + "  ")
          else
            children = @children.map { |node| "\n" + node.to_s(indentation + "  ") }.join("") + "\n" + indentation
          end
          indentation + "<" + name + attr + ">" + children + "</" + name + ">"
        else
          indentation + "<" + name + attr + " />"
        end
      end
    end
  end

end
