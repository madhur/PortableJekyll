# -*- coding: utf-8 -*-
require 'httpclient'
require 'openssl'
require 'nokogiri'

module Handsoap
  # Classes for parsing a WSDL.
  #
  # Used internally by the generator.
  module Parser #:nodoc: all
    class Interface
      attr_accessor :name, :operations

      def initialize(name, operations = [])
        @name = name
        @operations = operations || []
      end
    end

    class Binding
      attr_accessor :name, :protocol, :interface, :transport, :style, :encoding, :verb, :actions

      def initialize(name, optional = {})
        @name = name
        @actions = optional[:actions] || []
        @protocol = optional[:protocol]
        @interface = optional[:interface]
        @transport = optional[:transport]
        @style = optional[:style]
        @encoding = optional[:encoding]
        @verb = optional[:verb]
      end
    end

    class Endpoint
      attr_accessor :name, :protocol, :binding, :url

      def initialize(name, protocol, binding, url)
        @name = name
        @protocol = protocol
        @binding = binding
        @url = url
      end
    end

    class Operation
      attr_accessor :name, :input, :output

      def initialize(name, optional = {})
        @name = name
        @input = optional[:input]
        @output = optional[:output]
      end
    end

    class Action
      attr_accessor :name, :soap_action, :location

      def initialize(name, optional = {})
        @name = name
        @soap_action = optional[:soap_action]
        @location = optional[:location]
      end
    end

    class Wsdl
      attr_reader :url

      def initialize(doc, url = "void://")
        @doc = doc
        @url = url
      end

      def self.read(url)
        if url =~ /^http(s?):/
          request = ::HTTPClient.new
          request.ssl_config.verify_mode = ::OpenSSL::SSL::VERIFY_NONE
          response = request.get(url)
          xml_src = response.content
        else
          xml_src = Kernel.open(url).read
        end
        self.new(Nokogiri.XML(xml_src), url)
      end

      def ns
        {
          'wsdl1' => "http://schemas.xmlsoap.org/wsdl/",
          'wsdl2' => "http://www.w3.org/ns/wsdl/",
          'soap11' => "http://schemas.xmlsoap.org/wsdl/soap/",
          'soap12' => "http://schemas.xmlsoap.org/wsdl/soap12/",
          'http' => "http://schemas.xmlsoap.org/wsdl/http/"
        }
      end
      private :ns

      def protocol_from_ns(node)
        href = node.namespace.respond_to?(:href) ? node.namespace.href : @doc.namespaces["xmlns:#{node.namespace}"]
        case href
        when "http://schemas.xmlsoap.org/wsdl/soap/"
          :soap11
        when "http://schemas.xmlsoap.org/wsdl/soap12/"
          :soap12
        when "http://schemas.xmlsoap.org/wsdl/http/"
          :http
        else
          raise "Unknown namespace '#{href}'"
        end
      end
      private :protocol_from_ns

      def is_wsdl2?(node)
        href = node.namespace.respond_to?(:href) ? node.namespace.href : @doc.namespaces["xmlns:#{node.namespace}"]
        case href
        when "http://schemas.xmlsoap.org/wsdl/"
          false
        when "http://www.w3.org/ns/wsdl/"
          true
        else
          raise "Unknown namespace '#{href}'"
        end
      end
      private :is_wsdl2?

      def service
        services = @doc.xpath("//wsdl1:service|//wsdl2:service", ns)
        raise "Expected exactly 1 service in WSDL" if services.length != 1
        services[0][:name]
      end

      def interface
        all_interfaces = self.interfaces
        if all_interfaces.length != 1
          # There are more than one portType, so we take a pick
          all_bindings = self.bindings
          all_interfaces.each do |interface|
            b = all_bindings.find {|binding| binding.name == interface.name }
            if [:soap11, :soap12].include? b.protocol
              return interface
            end
          end
          raise "Can't find a suitable soap 1.1 or 1.2 interface/portType in WSDL"
        end
        all_interfaces.first
      end

      def target_ns
        @doc.root[:targetNamespace] || raise("Attribute targetNamespace not defined")
      end

      def preferred_protocol
        e = endpoints
        if e.select { |endpoint| endpoint.protocol == :soap12 }.any?
          :soap12
        elsif e.select { |endpoint| endpoint.protocol == :soap11 }.any?
          :soap11
        else
          raise "Can't find any soap 1.1 or soap 1.2 endpoints"
        end
      end

      def interfaces
        @doc.xpath("//wsdl1:portType|//wsdl2:interface", ns).map do |port_type|
          operations = port_type.xpath("./wsdl1:operation|./wsdl2:operation", ns).map do |operation|
            if is_wsdl2?(operation)
              input_node = operation.xpath("./wsdl2:input", ns).first
              input = input_node ? input_node[:element] : nil
              output_node = operation.xpath("./wsdl2:output", ns).first
              output = output_node ? output_node[:element] : nil
            else
              input_node = operation.xpath("./wsdl1:input", ns).first
              input = input_node ? input_node[:message] : nil
              output_node = operation.xpath("./wsdl1:output", ns).first
              output = output_node ? output_node[:message] : nil
            end
            Operation.new(operation[:name], :input => input, :output => output)
          end
          Interface.new(port_type[:name], operations)
        end
      end

      def endpoints
        @doc.xpath("//wsdl1:service/wsdl1:port|//wsdl2:service/wsdl2:endpoint", ns).map do |port|
          binding = port[:binding]
          if is_wsdl2?(port)
            location = port[:address]
            protocol = :binding
          else
            address = port.xpath("./soap11:address|./soap12:address|./http:address", ns).first
            location = address[:location]
            protocol = protocol_from_ns(address)
          end
          Endpoint.new(port[:name], protocol, binding, location)
        end
      end

      def bindings
        @doc.xpath("//wsdl1:binding|//wsdl2:binding", ns).map do |binding|
          raise "WSDL 2.0 not supported" if is_wsdl2?(binding)
          soap_binding = binding.xpath("./soap11:binding|./soap12:binding|./http:binding", ns).first
          protocol = protocol_from_ns(soap_binding)
          actions = []
          style = nil
          encoding = nil
          actions = binding.xpath("./wsdl1:operation", ns).map do |operation|
            soap_operation = operation.xpath("./soap11:operation|./soap12:operation|./http:operation", ns).first
            if soap_operation[:style]
              raise "Mixed styles not supported" if style && style != soap_operation[:style]
              style = soap_operation[:style]
            end
            xquery = []
            ['soap11', 'soap12', 'http'].each do |version|
              ['input', 'output'].each do |message_name|
                ['header', 'body'].each do |part_name|
                  xquery << "./wsdl1:#{message_name}/#{version}:#{part_name}"
                end
              end
            end
            operation.xpath(xquery.join('|'), ns).each do |thing|
              raise "Mixed encodings not supported" if encoding && encoding != thing[:use]
              encoding = thing[:use]
            end
            Action.new(
                       operation[:name],
                       :soap_action => soap_operation[:soapAction],
                       :location => soap_operation[:location])
          end
          Binding.new(
                      binding[:name],
                      :protocol => protocol,
                      :interface => binding[:type],
                      :transport => soap_binding[:transport],
                      :style => style,
                      :encoding => encoding,
                      :verb => soap_binding[:verb],
                      :actions => actions)
        end
      end
    end
  end
end
