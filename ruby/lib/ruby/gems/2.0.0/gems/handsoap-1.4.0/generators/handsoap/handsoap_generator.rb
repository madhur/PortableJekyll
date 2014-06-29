# -*- coding: utf-8 -*-
require "#{File.dirname(__FILE__)}/../../lib/handsoap/parser.rb"
require "#{File.dirname(__FILE__)}/../../lib/handsoap/compiler.rb"
require 'pathname'

# TODO
# options:
#   soap_actions (true/false)
#   soap_version (1/2/auto)
#   basename
class HandsoapGenerator < Rails::Generator::Base
  def initialize(runtime_args, runtime_options = {})
    super
    # Wsdl argument is required.
    usage if @args.empty?
    @wsdl_uri = @args.shift
    @basename = @args.shift
  end

  # def add_options!(opt)
  #   opt.on('--soap-actions') { |value| options[:soap_actions] = true }
  #   opt.on('--no-soap-actions') { |value| options[:soap_actions] = false }
  # end

  def banner
		"Generates the scaffold for a Handsoap binding." +
      "\n" + "You still have to fill in most of the meat, but this gives you a head start." +
			"\n" + "Usage: #{$0} #{spec.name} URI [BASENAME] [OPTIONS]" +
      "\n" + "    URI       URI of the WSDL to generate from" +
      "\n" + "    BASENAME  The basename to use for the service. If omitted, the name will be deducted from the URL."  +
      # "\n"  +
      # "\n" + "The following options are available:" +
      # "\n" + "    --soap-actions     If set, stubs will be generated with soap-action parameters. (Default)" +
      # "\n" + "    --no-soap-actions  If set, stubs will be generated without soap-action parameters." +
      # "\n" + "    --soap-version-1   If set, the generator will look for SOAP v 1.1 endpoints." +
      # "\n" + "    --soap-version-2   If set, the generator will look for SOAP v 1.2 endpoints." +
      ""
  end

  def manifest
    wsdl = Handsoap::Parser::Wsdl.read(@wsdl_uri)
    compiler = Handsoap::Compiler.new(wsdl, @basename)
    protocol = wsdl.preferred_protocol
    file_name = compiler.service_basename
    record do |m|
      m.directory "app"
      m.directory "app/models"
      m.file_contents "app/models/#{file_name}_service.rb" do |file|
        file.write compiler.compile_service(protocol, :soap_actions)
      end
      m.directory "test"
      m.directory "test/integration"
      m.file_contents "test/integration/#{file_name}_service_test.rb" do |file|
        file.write compiler.compile_test(protocol)
      end
      # TODO
      # Ask user about which endpoints to use ?
      m.message do |out|
        out.puts "----"
        out.puts "Endpoints in WSDL"
        out.puts "  You should copy these to the appropriate environment files."
        out.puts "  (Eg. `config/environments/*.rb`)"
        out.puts "----"
        out.puts compiler.compile_endpoints(protocol)
        out.puts "----"
      end
    end
  end

end

module Handsoap #:nodoc:
  module Generator #:nodoc:
    module Commands #:nodoc:
      module Create
        def file_contents(relative_destination, &block)
          destination = destination_path(relative_destination)
          temp_file = Tempfile.new("handsoap_generator")
          canonical_path = Pathname.new(source_path("/.")).realpath.to_s
          temp_file_relative_path = relative_path(temp_file.path, canonical_path)
          begin
            yield temp_file
            temp_file.close
            return self.file(temp_file_relative_path, relative_destination)
          ensure
            temp_file.unlink
          end
        end

        def message(&block)
          yield $stdout unless logger.quiet
        end

        private

        # Convert the given absolute path into a path
        # relative to the second given absolute path.
        # http://www.justskins.com/forums/file-relative-path-handling-97116.html
        def relative_path(abspath, relative_to)
          path = abspath.split(File::SEPARATOR)
          rel = relative_to.split(File::SEPARATOR)
          while (path.length > 0) && (path.first == rel.first)
            path.shift
            rel.shift
          end
          ('..' + File::SEPARATOR) * rel.length + path.join(File::SEPARATOR)
        end
      end
    end
  end
end

Rails::Generator::Commands::Create.send :include, Handsoap::Generator::Commands::Create
