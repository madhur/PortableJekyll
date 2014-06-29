# -*- coding: utf-8 -*-
module Handsoap
  # Used internally to generate Ruby source code
  class CodeWriter #:nodoc: all

    def initialize
      @buffer = ""
      @indentation = 0
    end

    def begin(text)
      puts(text)
      indent
    end

    def end(str = "end")
      unindent
      puts(str)
    end

    def puts(text = "")
      @buffer << text.gsub(/^(.*)$/, ("  " * @indentation) + "\\1")
      @buffer << "\n" # unless @buffer.match(/\n$/)
    end

    def indent
      @indentation = @indentation + 1
    end

    def unindent
      @indentation = @indentation - 1
    end

    def to_s
      @buffer
    end
  end

  # Used internally by the generator to generate a Service stub.
  class Compiler #:nodoc: all

    def initialize(wsdl, basename = nil)
      @wsdl = wsdl
      if basename
        @basename = basename.gsub(/[^a-zA-Z0-9]/, "_").gsub(/_+/, "_").gsub(/(^_+|_+$)/, '')
      else
        @basename = @wsdl.service
      end
      @basename = underscore(@basename).gsub(/_service$/, "")
    end

    def write
      writer = CodeWriter.new
      yield writer
      writer.to_s
    end

    def underscore(camel_cased_word)
      camel_cased_word.to_s.gsub(/::/, '/').
        gsub(/([A-Z]+)([A-Z][a-z])/,'\1_\2').
        gsub(/([a-z\d])([A-Z])/,'\1_\2').
        tr("-", "_").
        downcase
    end

    def camelize(lower_case_and_underscored_word)
      lower_case_and_underscored_word.to_s.gsub(/\/(.?)/) {
        "::" + $1.upcase
      }.gsub(/(^|_)(.)/) {
        $2.upcase
      }
    end

    def method_name(operation)
      if operation.name.match /^(get|find|select|fetch)/i
        "#{underscore(operation.name)}"
      else
        "#{underscore(operation.name)}!"
      end
    end

    def service_basename
      @basename
    end

    def service_name
      camelize(service_basename) + "Service"
    end

    def endpoint_name
      "#{service_basename.upcase}_SERVICE_ENDPOINT"
    end

    def detect_protocol
      if endpoints.select { |endpoint| endpoint.protocol == :soap12 }.any?
        :soap12
      elsif endpoints.select { |endpoint| endpoint.protocol == :soap11 }.any?
        :soap11
      else
        raise "Can't find any soap 1.1 or soap 1.2 endpoints"
      end
    end

    def compile_endpoints(protocol)
      version = protocol == :soap12 ? 2 : 1
      @wsdl.endpoints.select { |endpoint| endpoint.protocol == protocol }.map do |endpoint|
        write do |w|
          w.puts "# wsdl: #{@wsdl.url}"
          w.begin "#{endpoint_name} = {"
          w.puts ":uri => '#{endpoint.url}',"
          w.puts ":version => #{version}"
          w.end "}"
        end
      end
    end

    def compile_service(protocol, *options)
      binding = @wsdl.bindings.find { |b| b.protocol == protocol }
      raise "Can't find binding for requested protocol (#{protocol})" unless binding
      write do |w|
        w.puts "# -*- coding: utf-8 -*-"
        w.puts "require 'handsoap'"
        w.puts
        w.begin "class #{service_name} < Handsoap::Service"
        w.puts "endpoint #{endpoint_name}"
        w.begin "def on_create_document(doc)"
        w.puts "# register namespaces for the request"
        w.puts "doc.alias 'tns', '#{@wsdl.target_ns}'"
        w.end
        w.puts
        w.begin "def on_response_document(doc)"
        w.puts "# register namespaces for the response"
        w.puts "doc.add_namespace 'ns', '#{@wsdl.target_ns}'"
        w.end
        w.puts
        w.puts "# public methods"
        @wsdl.interface.operations.each do |operation|
          action = binding.actions.find { |a| a.name == operation.name }
          raise "Can't find action for operation #{operation.name}" unless action
          w.puts
          w.begin "def #{method_name(operation)}"
          # TODO allow :soap_action => :none
          if operation.name != action.soap_action && options.include?(:soap_actions)
            w.puts "soap_action = '#{action.soap_action}'"
            maybe_soap_action = ", soap_action"
          else
            maybe_soap_action = ""
          end
          w.begin((operation.output ? 'response = ' : '') + "invoke('tns:#{operation.name}'#{maybe_soap_action}) do |message|")
          w.puts 'raise "TODO"'
          w.end
          w.end
        end
        w.puts
        w.puts "private"
        w.puts "# helpers"
        w.puts "# TODO"
        w.end
      end
    end

    def compile_test(protocol)
      binding = @wsdl.bindings.find { |b| b.protocol == protocol }
      raise "Can't find binding for requested protocol (#{protocol})" unless binding
      write do |w|
        w.puts "# -*- coding: utf-8 -*-"
        w.puts "require 'test_helper'"
        w.puts
        w.puts "# #{service_name}.logger = $stdout"
        w.puts
        w.begin "class #{service_name}Test < Test::Unit::TestCase"
        @wsdl.interface.operations.each do |operation|
          w.puts
          w.begin "def test_#{underscore(operation.name)}"
          w.puts "result = #{service_name}.#{method_name(operation)}"
          w.end
        end
        w.end
      end
    end
  end
end
