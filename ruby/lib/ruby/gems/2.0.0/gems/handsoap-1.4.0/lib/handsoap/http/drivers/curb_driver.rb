# -*- coding: utf-8 -*-
require 'handsoap/http/drivers/abstract_driver'

module Handsoap
  module Http
    module Drivers
      class CurbDriver < AbstractDriver
        attr_accessor :enable_cookies

        def initialize
          @enable_cookies = false
        end

        def self.load!
          require 'curb'
        end

        def get_curl(url)
          if @curl
            @curl.url = url
          else
            @curl                 = ::Curl::Easy.new(url)
            @curl.timeout         = Handsoap.timeout
            @curl.enable_cookies  = @enable_cookies

            # enables both deflate and gzip compression of responses
            @curl.encoding = ''
            
            if Handsoap.follow_redirects?
              @curl.follow_location = true
              @curl.max_redirects   = Handsoap.max_redirects
            end
          end
          @curl
        end
        
        private :get_curl

        def send_http_request(request)
          http_client = get_curl(request.url)
          # Set credentials. The driver will negotiate the actual scheme
          if request.username && request.password
            http_client.userpwd = [request.username, ":", request.password].join
          end
          http_client.cacert = request.trust_ca_file if request.trust_ca_file
          http_client.cert = request.client_cert_file if request.client_cert_file
          # I have submitted a patch for this to curb, but it's not yet supported. If you get errors, try upgrading curb.
          http_client.cert_key = request.client_cert_key_file if request.client_cert_key_file
          # pack headers
          headers = request.headers.inject([]) do |arr, (k,v)|
            arr + v.map {|x| "#{k}: #{x}" }
          end
          http_client.headers = headers
          # I don't think put/delete is actually supported ..
          case request.http_method
          when :get
            http_client.http_get
          when :post
            http_client.http_post(request.body)
          when :put
            http_client.http_put(request.body)
          when :delete
            http_client.http_delete
          else
            raise "Unsupported request method #{request.http_method}"
          end
          parse_http_part(http_client.header_str.gsub(/^HTTP.*\r\n/, ""), http_client.body_str, http_client.response_code, http_client.content_type)
        end
      end
    end
  end
end
