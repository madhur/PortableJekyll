=begin
  This file is part of Viewpoint; the Ruby library for Microsoft Exchange Web Services.

  Copyright © 2011 Dan Wanek <dan.wanek@gmail.com>

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
=end

# We only what one instance of this class so include Singleton
require 'singleton'
require 'date'
require 'base64'
require 'kconv' if(RUBY_VERSION.start_with? '1.9') # bug in rubyntlm with ruby 1.9.x


# Class Extensions
require 'extensions/string'

# Load the backend SOAP infrastructure.  Today this is Handsoap.
require 'soap/soap_provider'

# Load the model classes
# Base Models
require 'model/model'
require 'model/mailbox_user'
require 'model/attendee'
require 'model/generic_folder'
require 'model/item_field_uri_map' # supports Item
require 'model/item'
# Specific Models
# Folders
require 'model/folder'
require 'model/calendar_folder'
require 'model/contacts_folder'
require 'model/search_folder'
require 'model/tasks_folder'
# Items
require 'model/message'
require 'model/calendar_item'
require 'model/contact'
require 'model/distribution_list'
require 'model/meeting_message'
require 'model/meeting_request'
require 'model/meeting_response'
require 'model/meeting_cancellation'
require 'model/task'
require 'model/attachment'
require 'model/file_attachment'
require 'model/item_attachment'
# Third Party Libraries
require 'mail' # used to convert Message items to RFC822 compliant messages
require 'icalendar' # used to convert Calendar items to iCalendar objects

# Load the Exception classes
require 'exceptions/exceptions'


# This is the Singlenton class that controls access and presentation to Exchange
# Web Services.  It is possible to just use the SOAP classes themselves but this
# is what ties all the pieces together.
# @attr_reader [SOAP::ExchangeWebService] :ews The SOAP object used to make calls
#   to the Exchange Web Service.
module Viewpoint
  module EWS
    # @attr_reader [Viewpoint::EWS::SOAP::ExchangeWebService] :ews The EWS object used
    #   to make SOAP calls.  You typically don't need to use this, but if you want to
    #   play around with the SOAP back-end it's available.
    class EWS
      include Singleton
      include Viewpoint

      attr_reader :ews

      # Set the endpoint for Exchange Web Services.  
      # @param [String] endpoint The URL of the endpoint. This should end in
      #   'exchange.asmx' and is typically something like this:
      #   https://myexch/ews/exchange.asmx
      # @param [Integer] version The SOAP version to use.  This defaults to 1
      #   and you should not need to pass this parameter.
      def self.endpoint=(endpoint, version = 1)
        @@endpoint = endpoint
        SOAP::ExchangeWebService.endpoint(:uri => endpoint, :version => version) && true
      end

      # Fetch the current endpoint
      def self.endpoint
        @@endpoint
      end

      # Set the SOAP username and password.
      # @param [String] user The user name
      # @param [String] pass The password
      def self.set_auth(user,pass)
        @@user = user
        SOAP::ExchangeWebService.set_auth(user,pass) && true
      end

      # Set the http driver that the SOAP back-end will use.
      # @param [Symbol] driver The HTTP driver.  Available drivers:
      #   :curb, :net_http, :http_client(Default)
      def self.set_http_driver(driver)
        Handsoap.http_driver = driver
      end

      # Sets the CA path to a certificate or hashed certificate directory.
      # This is the same as HTTPClient::SSLConfig.set_trust_ca
      # @param [String] ca_path A path to an OpenSSL::X509::Certificate or a 'c-rehash'ed directory
      def self.set_trust_ca(ca_path)
        SOAP::ExchangeWebService.set_http_options(:trust_ca_file => ca_path) && true
      end

      def initialize
        @ews = SOAP::ExchangeWebService.new
      end

      # The MailboxUser object that represents the user connected to EWS.
      def me
        MailboxUser.find_user((@@user.include?('@') ? @@user : "#{@@user}@"))
      end

    end # class EWS
  end # EWS
end
