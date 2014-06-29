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
    class CalendarItem < Message

      # This is a class method that creates a new CalendarItem in the Exchange Data Store.
      # @param [Hash] item A Hash of values based on values found here:
      #   http://msdn.microsoft.com/en-us/library/aa564765.aspx
      # @param [String, Symbol] folder_id The folder to create this item in. Either a
      #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
      # @param [String] send_invites "SendToNone/SendOnlyToAll/SendToAllAndSaveCopy"
      #   See:  http://msdn.microsoft.com/en-us/library/aa565209.aspx
      # @example Typical Usage
      #   item = { :subject => {:text => 'Planning'},
      #     :body => {:body_type => 'Text', :text => 'This is a test'},
      #     :start => {:text => '2010-07-29T14:00:00'},
      #     :end => {:text => '2010-07-29T15:00:00'},
      #     :is_all_day_event => {:text => 'false'},
      #     :location => {:text => 'Room 234'},
      #     :required_attendees => {:attendee => {:mailbox => {:email_address => {:text => 'test@test.com'}}}}
      #   }
      # @example Minimal Usage
      #   item = { :subject => {:text => 'Planning'},
      #     :start => {:text => '2010-07-29T14:00:00'},
      #     :end => {:text => '2010-07-29T15:00:00'}
      #   }
      def self.create_item_from_hash(item, folder_id = :calendar, send_invites = 'SendToAllAndSaveCopy')
        conn = Viewpoint::EWS::EWS.instance
        resp = conn.ews.create_calendar_item(folder_id, item, send_invites)
        if(resp.status == 'Success')
          resp = resp.items.shift
          self.new(resp[resp.keys.first])
        else
          raise EwsError, "Could not create CalendarItem. #{resp.code}: #{resp.message}"
        end
      end
      
      # Format attendees (usually called from #add_attendees!
      # @param [Array,String,Hash,MailboxUser] attendees
      # @param [Symbol] type the type of the attendees :required_attendees/:optional_attendees/:resources
      def self.format_attendees(attendees, type=:required_attendees)
        case attendees.class.to_s
        when 'String'
          return {type => [{:attendee => {:mailbox => {:email_address => {:text => attendees}}}}]}
        when /Attendee|MailboxUser/
          return {type => [{:attendee => {:mailbox => [{:name => {:text => attendees.name}}, {:email_address => {:text => attendees.email_address}}]}}]}
        when 'Hash'
          return {type => [{:attendee => {:mailbox => [{:name => {:text => attendees[:name]}}, {:email_address => {:text => attendees[:email_address]}}]}}]}
        when 'Array'
          as = {type => []}
          attendees.each do |a|
            as.merge!(format_attendees(a, type)) {|k,v1,v2| v1 + v2}
          end
          return as
        end
      end

      # Create a new CalendarItem.
      # If a block is given it is passed an opts hash with the keys :folder_id and :send_invites.
      #   See ::create_item_from_hash for details
      # @param [DateTime] v_start The date and time when the CalendarItem begins
      # @param [DateTime] v_end The date and time when the CalendarItem ends
      # @param [String] subject The subject of this Item
      # @param [String,optional] body The body of this object
      # @param [String,optional] location The location where this calendar item will ocurr
      # @param [Array<String,MailboxUser,Attendee>,optional] required_attendees An Array of e-mail addresses of required attendees
      # @param [Array<String,MailboxUser,Attendee>,optional] optional_attendees An Array of e-mail addresses of optional attendees
      # @param [Array<String,MailboxUser,Attendee>,optional] resources An Array of e-mail addresses of resources
      def self.create_item(v_start, v_end, subject, body = nil, location = nil, required_attendees=[], optional_attendees=[], resources=[])
        item = {}
        opts = {:folder_id => :calendar, :send_invites => 'SendToAllAndSaveCopy'}
        yield opts if block_given?
        item[:start] = {:text => v_start.to_s}
        item[:end] = {:text => v_end.to_s}
        item[:subject] = {:text => subject}
        item[:body] = {:text => body, :body_type => 'Text'} unless body.nil?
        item[:location] = {:text => location} unless location.nil?
        item.merge!(self.format_attendees(required_attendees)) unless required_attendees.empty?
        item.merge!(self.format_attendees(optional_attendees, :optional_attendees)) unless optional_attendees.empty?
        resources.each do |a|
          item[:resources] = [] unless item[:resources].is_a?(Array)
          item[:resources] << {:attendee => {:mailbox => {:email_address => {:text => a}}}}
        end
        self.create_item_from_hash(item, opts[:folder_id], opts[:send_invites])
      end

      # Initialize an Exchange Web Services item of type CalendarItem
      def initialize(ews_item, opts={})
        super(ews_item, opts)
      end
      
      # Add attendees to this CalendarItem. This does not commit the changes so you will have to use #save! to
      #   commit them back. If you want to commit them at once look at the #add_attendees! method.
      # @param [Array] required Required attendees to add to this object
      #   Array values of attendees may be simple email strings, MailboxUser items or Hashes in the form
      #   {:email_address => 'email@test', :name => 'My Name'}.
      # @param [Array] optional Optional attendees to add to this object
      #   see the notes for the 'required' parameter.
      # @example
      #   ['user1@example.org', 'user2@example.org']
      #   or
      #   [{:name => 'User1', :email_address => 'user1@example.org'}, {:name => 'User2', :email_address => 'user2@example.org'}]
      #   or
      #   ['user1@example.org', 'user2@example.org'], ['user3@example.org', 'user4@example.org']
      #   or
      #   [{:name => 'User1', :email_address => 'user1@example.org'}, {:name => 'User2', :email_address => 'user2@example.org'}],
      #     [{:name => 'User3', :email_address => 'user3@example.org'}, {:name => 'User4', :email_address => 'user4@example.org'}]
      # @return [Boolean] true on success, false otherwise
      # @todo add ability to add resources
      def add_attendees(required, optional = [], resources = [])
        update = {}
        update.merge!(self.class.format_attendees(required)) unless required.empty? || required.nil?
        update.merge!(self.class.format_attendees(optional, :optional_attendees)) unless optional.empty? || optional.nil?

        return false if update.empty?

        @required_attendees, @optional_attendees = nil, nil
        changes = update_attribs(update, :append)
        @updates.merge!({:preformatted => changes}) {|k,v1,v2| v1 + v2}
        true
      end

      # This is the same as the #add_attendees method, but it actually commits the change back to Exchange
      # @see #add_attendees
      def add_attendees!(required, optional = [], resources = [])
        add_attendees(required, optional, resources)
        save!
      end

      # Remove the attendees from the attendee list. This does not commit the changes so you will have to use
      #   #save! to commit them back. If you want to commit them at once look at the #remove_attendees! method.
      # @param [Array] attendees the attendees to remove from this CalendarItem
      #   [Viewpoint::EWS::Attendee<user1>, Viewpoint::EWS::Attendee<user2>] or
      #   ['user1@example.org', 'user2@example.org']
      # @return [Boolean] false if the object is not updated, true otherwise
      def remove_attendees(attendees)
        return false if attendees.empty?

        emails = attendees.is_a?(Array) ? attendees : attendees.values
        emails = emails.collect do |v|
          case v.class.to_s
          when 'String'
            v
          when /MailboxUser|Attendee/
            v.email_address
          when 'Hash'
            v[:email_address]
          end
        end

        update = {}
        [:required_attendees, :optional_attendees].each do |type|
          ivar = self.send(type.to_s)
          next if ivar.nil?

          required_a = ivar.select {|v| !emails.include?(v.email_address) }
          formatted_a = self.class.format_attendees(required_a, type)
          if formatted_a[type].empty?
            update[:preformatted] ||= []
            update[:preformatted] << {:delete_item_field => [{:field_uRI => {:field_uRI=>FIELD_URIS[type][:text]}}]}
            self.instance_eval "undef #{type}"
          else
            update.merge!(formatted_a)
          end
        end

        return false if update.empty?

        @required_attendees, @optional_attendees = nil, nil
        @updates.merge!(update) {|k,v1,v2| v1 + v2}
        true
      end

      # This is the same as the #remove_attendees method, but it actually commits the change back to Exchange
      # @see #remove_attendees
      def remove_attendees!(attendees)
        remove_attendees(attendees)
        save!
      end

      # Call UpdateItem for this item with the passed updates
      # @param [Hash] updates a well-formed update hash
      # @example {:set_item_field=>{:field_u_r_i=>{:field_u_r_i=>"message:IsRead"}, :message=>{:is_read=>{:text=>"true"}}}}
      # TODO: This is a stand-in for the Item#update! method until I can firm it up a bit. It is neccessary for the SendMeetingInvitationsOrCancellations attrib
      def update!(updates)
        conn = Viewpoint::EWS::EWS.instance
        resp = conn.ews.update_item([{:id => @item_id, :change_key => @change_key}], {:updates => updates},
                                    {:message_disposition => 'SaveOnly', :conflict_resolution => 'AutoResolve', :send_meeting_invitations_or_cancellations => 'SendOnlyToChanged'})
        if resp.status == 'Success'
          @item_id = resp.items.first[resp.items.first.keys.first][:item_id][:id]
          @change_key = resp.items.first[resp.items.first.keys.first][:item_id][:change_key]
          @shallow = true
          deepen!
        else
          raise EwsError, "Trouble updating Item. #{resp.code}: #{resp.message}"
        end

      end

      # Delete this item
      # @param [Boolean] soft Whether or not to do a soft delete.  By default EWS will do a 
      #   hard delete of this item.  See the MSDN docs for more info:
      #   http://msdn.microsoft.com/en-us/library/aa562961.aspx
      # @param [String] cancel_type "SendToNone/SendOnlyToAll/SendToAllAndSaveCopy"
      #   Default is SendOnlyToAll
      # @return [Boolean] Whether or not the item was deleted
      # @todo Add exception handling for failed deletes
      #
      def delete!(soft=false, cancel_type='SendOnlyToAll')
        deltype = soft ? 'SoftDelete' : 'HardDelete'
        resp = (Viewpoint::EWS::EWS.instance).ews.delete_item([@item_id], deltype, cancel_type)
        self.clear_object!
        resp.status == 'Success'
      end

      # Delete this item by moving it to the Deleted Items folder
      # @see  http://msdn.microsoft.com/en-us/library/aa562961.aspx
      # @return [Boolean] Whether or not the item was deleted
      # @todo Add exception handling for failed deletes
      def recycle!(cancel_type='SendOnlyToAll')
        resp = (Viewpoint::EWS::EWS.instance).ews.delete_item([@item_id], 'MoveToDeletedItems', cancel_type)
        self.clear_object!
        resp.status == 'Success'
      end


      private

      def init_methods
        super
        define_str_var :calendar_item_type, :duration, :time_zone, :when, :location, :u_i_d, {:u_i_d => :uid}
        define_str_var :legacy_free_busy_status, :my_response_type, :meeting_workspace_url, :net_show_url
        define_int_var :adjacent_meeting_count, :appointment_sequence_number, :appointment_state
        define_int_var :conference_type, :conflicting_meeting_count
        define_mbox_user :organizer
        define_bool_var :is_all_day_event, :is_cancelled, :is_meeting, :is_online_meeting, :is_recurring
        define_bool_var :allow_new_time_proposal, :meeting_request_was_sent
        define_datetime_var :appointment_reply_time, :start, :end, :original_start
        define_attendees :required_attendees, :optional_attendees, :resources

        # @todo Handle:
        #   <AdjacentMeetings/> <ConflictingMeetings/> <DeletedOccurrences/>
        #   <FirstOccurrence/> <LastOccurrence/> <ModifiedOccurrences/>
        #   <StartTimeZone/> <EndTimeZone/> <MeetingTimeZone/>
        #   <Recurrence/>
      end

    end # CalendarItem
  end # EWS
end # Viewpoint
