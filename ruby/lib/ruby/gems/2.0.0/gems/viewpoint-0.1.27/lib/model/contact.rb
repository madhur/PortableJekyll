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
    # Represents a Contact Item in the Exchange datastore.
    class Contact < Item

      # This is a class method that creates a new Contact in the Exchange Data Store.
      # @param [Hash] item A Hash of values based on values found here:
      #   http://msdn.microsoft.com/en-us/library/aa581315.aspx
      # @param [String, Symbol] folder_id The folder to create this item in. Either a
      #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
      # @param [String] send_invites "SendToNone/SendOnlyToAll/SendToAllAndSaveCopy"
      #   See:  http://msdn.microsoft.com/en-us/library/aa565209.aspx
      # @example Typical Usage
      #   item = {
      #     :file_as => {:text => 'Dan Wanek'},
      #     :given_name => {:text => 'Dan Wanek'},
      #     :company_name => {:text => 'Test Company'},
      #     :email_addresses => [
      #       {:entry => {:key => 'EmailAddress1', :text => 'myemail@work.com'}},
      #       {:entry => {:key => 'EmailAddress2', :text => 'myemail@home.com'}}
      #     ],
      #     :physical_addresses => [
      #       {:entry => {:key => 'Business', :sub_elements => {:street => {:text => '6343 N Baltimore'}, :city => {:text => 'Bismarck'}, :state => {:text => 'ND'} }}}
      #     ],
      #     :phone_numbers => [
      #       {:entry => {:key => 'BusinessPhone', :text => '7012220000'}}
      #     ],
      #     :job_title => {:text => 'Systems Architect'}
      #   }
      # @example Minimal Usage
      def self.create_item_from_hash(item, folder_id = :contacts)
        conn = Viewpoint::EWS::EWS.instance
        resp = conn.ews.create_contact_item(folder_id, item)
        if(resp.status == 'Success')
          resp = resp.items.shift
          self.new(resp[resp.keys.first])
        else
          raise EwsError, "Could not create Contact. #{resp.code}: #{resp.message}"
        end
      end

      # Create a Contact in the Exchange Data Store
      def self.add_contact()
        item = {}
        
        conn = Viewpoint::EWS::EWS.instance
        resp = conn.ews.create_contact_item()

        if(resp.status == 'Success')
          resp = resp.items.shift
          self.new(resp[resp.keys.first])
        else
          raise EwsError, "Could not add contact. #{resp.code}: #{resp.message}"
        end
      end

      # Initialize an Exchange Web Services item of type Contact
      def initialize(ews_item, opts={})
        super(ews_item, opts)
      end
      
      def set_email_addresses(email1, email2=nil, email3=nil)
        changes = []
        type = self.class.name.split(/::/).last.ruby_case.to_sym
        k = :email_addresses
        v = 'EmailAddress1'
        changes << {:set_item_field => 
          [{:indexed_field_uRI => {:field_uRI => FIELD_URIS[k][:text], :field_index => v}}, {type=>{k => {:entry => {:key => v, :text => email1}}}}]} unless email1.nil?
        v = 'EmailAddress2'
        changes << {:set_item_field => 
          [{:indexed_field_uRI => {:field_uRI => FIELD_URIS[k][:text], :field_index => v}}, {type=>{k => {:entry => {:key => v, :text => email2}}}}]} unless email2.nil?
        v = 'EmailAddress3'
        changes << {:set_item_field => 
          [{:indexed_field_uRI => {:field_uRI => FIELD_URIS[k][:text], :field_index => v}}, {type=>{k => {:entry => {:key => v, :text => email3}}}}]} unless email3.nil?
        @updates.merge!({:preformatted => changes}) {|k,v1,v2| v1 + v2}
      end

      # Set the phone number. You must give a type based on the available Exchange phone number types
      # @param [Symbol] type the type of number to set. It must be one of these:
      #   :assistant_phone, :business_fax, :business_phone, :business_phone2, :callback, :car_phone, :company_main_phone,
      #   :home_fax, :home_phone, :home_phone2, :isdn, :mobile_phone, :other_fax, :other_telephone, :pager, :primary_phone,
      #   :radio_phone, :telex, :tty_tdd_phone
      # @param [String] phone_number The phone number
      def set_phone_number(phone_type, phone_number)
        valid_types = [:assistant_phone, :business_fax, :business_phone, :business_phone2, :callback, :car_phone, :company_main_phone,
          :home_fax, :home_phone, :home_phone2, :isdn, :mobile_phone, :other_fax, :other_telephone, :pager, :primary_phone,
          :radio_phone, :telex, :tty_tdd_phone]
        raise EwsError, "Invalid phone type (#{phone_type}) passed to Contact#set_phone_number." unless valid_types.index phone_type
        type = self.class.name.split(/::/).last.ruby_case.to_sym

        changes = []
        k = :phone_numbers
        v = phone_type.to_s.camel_case
        changes << {:set_item_field =>
          [{:indexed_field_uRI => {:field_uRI => FIELD_URIS[k][:text], :field_index => v}}, {type=>{k => {:entry => {:key => v, :text => phone_number}}}}]}
        @updates.merge!({:preformatted => changes}) {|k,v1,v2| v1 + v2}
      end

      # Set an address for this contact
      # @param [Symbol] address_type the type of Exchange address to set. It must be one of the following:
      #   :business, :home, :other
      # @param [Hash] address the address elements to set. It may include the following keys
      #   :street, :city, :state, :country_or_region, :postal_code
      # @todo check for empty address hash
      def set_address(address_type, address)
        valid_types = [:business, :home, :other]
        raise EwsError, "Invalid address type (#{address_type}) passed to Contact#set_address." unless valid_types.index address_type
        valid_field_types = [:street, :city, :state, :country_or_region, :postal_code]
        type = self.class.name.split(/::/).last.ruby_case.to_sym
        v = address_type.to_s.camel_case

        changes = []
        field = 'PhysicalAddresses'
        address.keys.each do |addr_item|
          raise EwsError, "Invalid address element (#{addr_item}) passed to Contact#set_address." unless valid_field_types.index addr_item
          index_field = "contacts:PhysicalAddress:#{addr_item.to_s.camel_case}"
          changes << {:set_item_field =>
            [{:indexed_field_uRI => {
              :field_uRI => index_field, :field_index => v}}, {type => {field => {:entry => {:key => v, addr_item =>{ :text => address[addr_item]}}}}}
            ]}
        end
        @updates.merge!({:preformatted => changes}) {|k,v1,v2| v1 + v2}
      end


      private

      def init_methods
        super()

        define_str_var :file_as, :file_as_mapping, :display_name, :job_title, :given_name, :surname, :company_name
        define_attr_str_var :complete_name, :first_name, :middle_name, :last_name, :initials, :full_name
        define_inet_addresses :email_addresses, :im_addresses
        define_phone_numbers :phone_numbers
        define_physical_addresses :physical_addresses
      end

            
      # Define email_addresses or im_addresses for a Contact
      def define_inet_addresses(*inet_addresses)
        inet_addresses.each do |itype|
          eval "@#{itype} ||= {}"
          return unless self.instance_variable_get("@#{itype}").empty?
          if(@ews_item.has_key?(itype))
            @ews_methods << itype
            if(@ews_item[itype][:entry].is_a?(Array))
              @ews_item[itype][:entry].each do |entry|
                next if entry.keys.length == 1
                eval "@#{itype}[entry[:key].ruby_case.to_sym] = (entry.has_key?(:text) ? entry[:text] : '')"
              end
            else
              entry = @ews_item[itype][:entry]
              next if entry.keys.length == 1
              eval "@#{itype}[entry[:key].ruby_case.to_sym] = (entry.has_key?(:text) ? entry[:text] : '')"
            end
            self.instance_eval <<-EOF
          def #{itype}
            self.instance_variable_get "@#{itype}"
          end
          EOF
          else
            @ews_methods_undef << itype
          end
        end
      end
      
      def define_phone_numbers(phone_numbers)
        @phone_numbers ||= {}
        return unless @phone_numbers.empty?
        if(@ews_item.has_key?(phone_numbers))
          if(@ews_item[phone_numbers][:entry].is_a?(Array))
            @ews_item[phone_numbers][:entry].each do |entry|
              next if entry.keys.length == 1
              @phone_numbers[entry[:key].ruby_case.to_sym] = (entry.has_key?(:text) ? entry[:text] : "")
            end
          else # it is a Hash then
            entry = @ews_item[phone_numbers][:entry]
            return if entry.keys.length == 1
            @phone_numbers[entry[:key].ruby_case.to_sym] = (entry.has_key?(:text) ? entry[:text] : "")
          end
          self.instance_eval <<-EOF
          def #{phone_numbers}
            @phone_numbers
          end
          EOF
          @ews_methods << phone_numbers
        else
          @ews_methods_undef << itype
        end
      end

      # Define physical_addresses for a Contact
      def define_physical_addresses(physical_addresses)
        @physical_addresses ||= {}
        return unless @physical_addresses.empty?
        if(@ews_item.has_key?(physical_addresses))
          @ews_methods << physical_addresses
          entries = @ews_item[physical_addresses][:entry]
          entries = entries.is_a?(Array) ? entries : [entries]
          entries.each do |entry|
            next if entry.keys.length == 1
            key = entry.delete(:key)
            @physical_addresses[key.ruby_case.to_sym] = {}
            entry.each_pair do |ekey,ev|
              @physical_addresses[key.ruby_case.to_sym][ekey] = ev[:text]
            end
          end
          self.instance_eval <<-EOF
          def #{physical_addresses}
            @physical_addresses
          end
          EOF
        else
          @ews_methods_undef << itype
        end
      end

    end # Contact
  end # EWS
end # Viewpoint
