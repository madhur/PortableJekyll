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

# This file requires the appropriate SOAP Library (Handsoap today) and also
# defines certain contants that SOAP methods may use.
module Viewpoint
  module EWS
    module SOAP

      # CONSTANTS

      NS_SOAP         = 'soap' # http://schemas.xmlsoap.org/soap/envelope/
      NS_EWS_TYPES    = 't'    # http://schemas.microsoft.com/exchange/services/2006/types
      NS_EWS_MESSAGES = 'm'    # http://schemas.microsoft.com/exchange/services/2006/messages

      # used in ResolveNames to determine where names are resolved
      ActiveDirectory = 'ActiveDirectory'
      ActiveDirectoryContacts = 'ActiveDirectoryContacts'
      Contacts = 'Contacts'
      ContactsActiveDirectory = 'ContactsActiveDirectory'



      # A Generic Class for SOAP returns.
      # @attr_reader [String] :message The text from the EWS element <m:ResponseCode>
      class EwsSoapResponse

        attr_reader :status, :code, :message, :soap_response
        attr_accessor :items

        def initialize(status, code, message)
          @status, @code, @message = status, code, message

          # Items is an array where hash types get stored for return
          @items = []
        end

        def set_soap_resp(response)
          @soap_response = response
        end

      end # EwsSoapResponse


    end # SOAP
  end # EWS
end # Viewpoint

require 'soap/handsoap/ews_service'
