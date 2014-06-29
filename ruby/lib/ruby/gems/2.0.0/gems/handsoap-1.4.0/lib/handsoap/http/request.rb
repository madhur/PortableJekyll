# -*- coding: utf-8 -*-

module Handsoap
  module Http

    # Represents a HTTP Request.
    class Request
      attr_reader :url, :http_method, :headers, :body, :username, :password, :trust_ca_file, :client_cert_file, :client_cert_key_file,:ssl_verify_mode
      attr_writer :body, :http_method
      def initialize(url, http_method = :get)
        @url = url
        @http_method = http_method
        @headers = {}
        @body = nil
        @username = nil
        @password = nil
        @trust_ca_file = nil
        @client_cert_file = nil
        @client_cert_key_file = nil
        @ssl_verify_mode = nil
      end
      def set_trust_ca_file(ca_file)
        @trust_ca_file = ca_file
      end
      def set_client_cert_files(client_cert_file,client_cert_key_file)
        @client_cert_file = client_cert_file
        @client_cert_key_file = client_cert_key_file
      end
      def set_ssl_verify_mode(mode)
        @ssl_verify_mode = mode
      end
      def set_auth(username, password)
        @username = username
        @password = password
      end
      def add_header(key, value)
        if @headers[key].nil?
          @headers[key] = []
        end
        @headers[key] << value
      end
      def set_header(key, value)
        if value.nil?
          @headers[key] = nil
        else
          @headers[key] = [value]
        end
      end
      def inspect
        "===============\n" +
          "--- Request ---\n" +
          "#{http_method.to_s.upcase} #{url}\n" +
          (
           if username && password
             "Auth credentials: #{username}:#{password}\n"
           else
             ""
           end
           ) +
          (
           if headers.any?
             "---\n" + headers.map { |key,values| values.map {|value| key + ": " + value + "\n" }.join("")  }.join("")
           else
             ""
           end
           ) +
          (
           if body
             "---\n" + body
           else
             ""
           end
           )
      end
    end
  end
end
