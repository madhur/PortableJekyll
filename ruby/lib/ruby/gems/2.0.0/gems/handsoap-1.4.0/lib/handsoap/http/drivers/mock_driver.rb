# -*- coding: utf-8 -*-
require 'handsoap/http/drivers/abstract_driver'

module Handsoap
  module Http
    module Drivers
      # A mock driver for your testing needs.
      #
      # To use it, create a new instance and assign to +Handsoap::Http.drivers+. Then configure +Handsoap::Service+ to use it:
      #
      #     Handsoap::Http.drivers[:mock] = Handsoap::Http::Drivers::MockDriver.new :status => 200, :headers => headers, :content => body
      #     Handsoap.http_driver = :mock
      #
      # Remember that headers should use \r\n, rather than \n.
      class MockDriver < AbstractDriver
        attr_accessor :mock, :last_request, :is_loaded

        def initialize(mock)
          @mock = mock
          @is_loaded = false
        end

        def load!
          is_loaded = true
        end

        def new
          self
        end

        def send_http_request(request)
          @last_request = request
          (mock.kind_of? Hash) ?
            parse_http_part(mock[:headers], mock[:content], mock[:status], mock[:content_type]) : mock
        end
      end
    end
  end
end
