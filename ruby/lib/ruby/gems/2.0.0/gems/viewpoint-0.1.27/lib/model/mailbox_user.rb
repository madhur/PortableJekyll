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

    # This represents a Mailbox object in the Exchange data store
    # @see http://msdn.microsoft.com/en-us/library/aa565036.aspx MSDN docs
    # @todo Design a Class method that resolves to an Array of MailboxUsers
    class MailboxUser
      include Model

      # Resolve a user in the Exchange Data Store
      # @param [String] resolve A user to resolve to.
      # @return [MailboxUser,Array] If it resolves to one user then it returns a MailboxUser.
      #   If it resolves to more than one user an Array of MailboxUsers are returned.  If an
      #   error ocurrs an exception is raised.
      # @todo - rename "resolve" to something more descriptive
      #   - standardize on a common return type???
      def self.find_user(resolve)
        resp = (Viewpoint::EWS::EWS.instance).ews.resolve_names(resolve)
        if(resp.status == 'Success')
          return self.new(resp.items.first[:mailbox])
        elsif(resp.code == 'ErrorNameResolutionMultipleResults')
          users = []
          resp.items.each do |u|
            users << self.new(u[:mailbox])
          end
          return users
        else
          raise EwsError, "Find User produced an error: #{resp.code}: #{resp.message}"
        end
      end

      # Get information about when the user with the given email address is available.
      # @param [String] email_address The email address of the person to find availability for.
      # @param [String] start_time The start of the time range to check as an xs:dateTime.
      # @param [String] end_time The end of the time range to check as an xs:dateTime.
      # @see http://msdn.microsoft.com/en-us/library/aa494212.aspx
      def self.get_user_availability(email_address, start_time, end_time)
        resp = (Viewpoint::EWS::EWS.instance).ews.get_user_availability(email_address, start_time, end_time)
        if(resp.status == 'Success')
          return resp.items
        else
          raise EwsError, "GetUserAvailability produced an error: #{resp.code}: #{resp.message}"
        end
      end

      def initialize(mbox_user)
        super() # Calls initialize in Model (creates @ews_methods Array)
        @ews_item = mbox_user
        define_str_var :name, :email_address, :routing_type, :mailbox_type, :item_id
      end

      def get_oof
        mailbox = {:mailbox => {:address => {:text => email_address}}}
        resp = (Viewpoint::EWS::EWS.instance).ews.get_user_oof_settings(mailbox)
        s = resp[:oof_settings]
        @oof_state = s[:oof_state][:text]
        @oof_ext_audience = s[:external_audience][:text]
        @oof_start = DateTime.parse(s[:duration][:start_time][:text])
        @oof_end = DateTime.parse(s[:duration][:end_time][:text])
        @oof_internal_reply = s[:internal_reply][:message][:text]
        @oof_external_reply = s[:internal_reply][:message][:text]
        true
      end
      
      # Get information about when this user is available.
      # @param [String] start_time The start of the time range to check as an xs:dateTime.
      # @param [String] end_time The end of the time range to check as an xs:dateTime.
      # @see http://msdn.microsoft.com/en-us/library/aa494212.aspx
      def get_user_availability(start_time, end_time)
        return MailboxUser.get_user_availability(self.email_address, start_time, end_time)
      end

      # Adds one or more delegates to a principal's mailbox and sets specific access permissions
      # @see http://msdn.microsoft.com/en-us/library/bb856527.aspx
      #
      # @param [String,MailboxUser] delegate_email The user you would like to give delegate access to.
      #   This can either be a simple String e-mail address or you can pass in a MailboxUser object.
      # @param [Hash] permissions A hash of folder type keys and permission type values. An example
      #   would be {:calendar_folder_permission_level => 'Editor'}.  Possible keys are:
      #   :calendar_folder_permission_level, :tasks_folder_permission_level, :inbox_folder_permission_level
      #   :contacts_folder_permission_level, :notes_folder_permission_level, :journal_folder_permission_level
      #   and possible values are:  None/Editor/Reviewer/Author/Custom
      # @return [true] This method either returns true or raises an error with the message
      #   as to why this operation did not succeed.
      def add_delegate!(delegate_email, permissions)
        # Use a new hash so the passed hash is not modified in case we are in a loop.
        # Thanks to Markus Roberts for pointing this out.
        formatted_perms = {}
        # Modify permissions so we can pass it to the builders
        permissions.each_pair do |k,v|
          formatted_perms[k] = {:text => v}
        end

        resp = (Viewpoint::EWS::EWS.instance).ews.add_delegate(self.email_address, delegate_email, formatted_perms)
        if(resp.status == 'Success')
          return true
        else
          raise EwsError, "Could not add delegate access for user #{delegate_email}: #{resp.code}, #{resp.message}"
        end
      end

      def update_delegate!(delegate_email, permissions)
        # Modify permissions so we can pass it to the builders
        formatted_perms = {}
        permissions.each_pair do |k,v|
          formatted_perms[k] = {:text => v}
        end

        resp = (Viewpoint::EWS::EWS.instance).ews.update_delegate(self.email_address, delegate_email, formatted_perms)
        if(resp.status == 'Success')
          return true
        else
          raise EwsError, "Could not update delegate access for user #{delegate_email}: #{resp.code}, #{resp.message}"
        end
      end

      def get_delegate_info()
        resp = (Viewpoint::EWS::EWS.instance).ews.get_delegate(self.email_address)
       # if(resp.status == 'Success')
       #   return true
       # else
       #   raise EwsError, "Could not update delegate access for user #{delegate_email}: #{resp.code}, #{resp.message}"
       # end
      end

    end # MailboxUser
  end # EWS
end # Viewpoint
