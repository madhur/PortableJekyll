# -*- coding: utf-8 -*-

module Handsoap
  module Http
    module Drivers
      class EventMachineDriver < AbstractDriver
        def self.load!
          require 'eventmachine'
          require 'em-http'
        end

        def send_http_request_async(request)
          emr = EventMachine::HttpRequest.new(request.url)

          if request.username && request.password
            # TODO: Verify that this is actually supported?
            request.headers['authorization'] = [request.username, request.password]
          end

          case request.http_method
          when :get
            emdef = emr.get(:head => request.headers)
          when :post
            emdef = emr.post(:head => request.headers, :body => request.body)
          when :put
            emdef = emr.put(:head => request.headers, :body => request.body)
          when :delete
            emdef = emr.delete
          else
            raise "Unsupported request method #{request.http_method}"
          end

          deferred = Handsoap::Deferred.new
          emdef.callback do
            http_response = parse_http_part(emdef.response_header, emdef.response, emdef.response_header.status)
            deferred.trigger_callback http_response
          end
          emdef.errback do
            deferred.trigger_errback emdef
          end
          deferred
        end
      end
    end
  end
end
