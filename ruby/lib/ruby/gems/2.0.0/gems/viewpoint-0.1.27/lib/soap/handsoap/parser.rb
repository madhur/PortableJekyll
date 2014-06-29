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

module Viewpoint
  module EWS
    module SOAP
      module Parser

        def initialize(response)
          # Unwrap SOAP Envelope
          @response = response
          @response_type = (response/"//#{NS_SOAP}:Body/*").first.node_name

          rmsg = (response/'//*[@ResponseClass]').first
          @response_message = EwsSoapResponse.new(rmsg['ResponseClass'],
                                                  (rmsg/'m:ResponseCode/text()').first.to_s,
                                                  (rmsg/'m:MessageText/text()').first.to_s)

          @response_message.set_soap_resp(response)
        end

        # This is the main parser method.  It takes the response type and tries to
        # call a Ruby method of the same name.
        # @todo Decide on an appropriate response if a method does not exist.
        def parse(opts)
          resp_method = @response_type.ruby_case
          if(respond_to?(resp_method))
            puts "Method Exists: #{resp_method}" if $DEBUG
            method(resp_method).call(opts)
          else
            puts "No Method: #{resp_method}" if $DEBUG
          end
          @response_message
        end

        private

        def method_exists?(method_name)
          return self.methods.include?(method_name)
        end

        # Create a Hash from a Nokogiri element tree
        # @param [Nokogiri::XML::Element, Nokogiri::XML::Text] nokoelem The Nokogiri element passed to this method
        # @example XML
        #   <tiptop>
        #     <top Id="32fss">TestText</top>
        #     <middle Id='TestTestMiddle' />
        #     <bottom />
        #   </tiptop>
        #   becomes...
        #   {:tiptop=>{:top=>{:id=>"32fss", :text=>"TestText"}, :middle=>{:id=>"TestTestMiddle"}}} 
        def xml_to_hash!(nokoelem)
          e_hash = {}
          node_name = nokoelem.name.ruby_case.to_sym

          if nokoelem.is_a? Nokogiri::XML::Element
            nokoelem.attributes.each_pair do |k, v|
              e_hash[k.ruby_case.to_sym] = v.value
            end
            nokoelem.children.each do |c|
              new_hash = xml_to_hash!(c)
              unless new_hash.nil?
                e_hash.merge!(new_hash) do |k,v1,v2|
                  if(v1.is_a?(Array))
                    v1 << v2
                  else
                    [v1, v2]
                  end
                end
              end
            end
            return e_hash.empty? ? nil : {node_name => e_hash}
          elsif nokoelem.is_a? Nokogiri::XML::Text
            # Return a :text to value hash or nil if the text is empty
            return {node_name => nokoelem.text} if nokoelem.text != "\n"
            nil
          else
            # If something strange gets passed just return nil
            return nil
          end
        end


      end # Parser
    end # SOAP
  end # SPWS
end # Viewpoint

require 'soap/handsoap/parsers/ews_parser'
