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

require 'handsoap'
require 'soap/handsoap/builder'
require 'soap/handsoap/parser'

Handsoap.http_driver = :http_client

module Viewpoint
  module EWS
    module SOAP
      class ExchangeWebService < Handsoap::Service
        include Viewpoint::EWS::SOAP

        SOAP_ACTION_PREFIX = "http://schemas.microsoft.com/exchange/services/2006/messages"

        @@raw_soap = false
        @@http_options = nil

        def initialize()
          if $DEBUG
            @debug = File.new('ews_debug.out', 'w')
            @debug.sync = true
          end
        end

        def self.set_auth(user,pass)
          @@user = user
          @@pass = pass
        end

        # Turn off parsing and just return the soap response
        def self.raw_soap!
          @@raw_soap = true
        end

        # Set various HTTP options like ssl_ca_trust, etc
        def self.set_http_options(option_hash)
          if @@http_options.nil?
            @@http_options = option_hash
          else
            @@http_options.merge!(option_hash)
          end
        end

        # ********* Begin Hooks *********


        def on_create_document(doc)
          doc.alias NS_EWS_TYPES, 'http://schemas.microsoft.com/exchange/services/2006/types'
          doc.alias NS_EWS_MESSAGES, 'http://schemas.microsoft.com/exchange/services/2006/messages'
          header = doc.find('Header')
          header.add("#{NS_EWS_TYPES}:RequestServerVersion") { |rsv| rsv.set_attr('Version','Exchange2007_SP1') }
        end

        # Adds knowledge of namespaces to the response object.  These have to be identical to the 
        # URIs returned in the XML response.  For example, I had some issues with the 'soap'
        # namespace because my original URI did not end in a '/'
        # @example
        #   Won't work: http://schemas.xmlsoap.org/soap/envelope
        #   Works: http://schemas.xmlsoap.org/soap/envelope/
        def on_response_document(doc)
          doc.add_namespace NS_SOAP, 'http://schemas.xmlsoap.org/soap/envelope/'
          doc.add_namespace NS_EWS_TYPES, 'http://schemas.microsoft.com/exchange/services/2006/types'
          doc.add_namespace NS_EWS_MESSAGES, 'http://schemas.microsoft.com/exchange/services/2006/messages'
        end

        def on_after_create_http_request(req)
          begin
            req.set_auth @@user, @@pass
          rescue NameError => e
            raise EwsLoginError, "Please remember to set your credential information."
          end
        end

        def on_http_error(response)
          case response.status
          when 401
            raise EwsLoginError, "Failed to login to EWS at #{uri}. Please check your credentials."
          when 404
            raise EwsError, "File not found (404): #{uri} Please check the endpoint URL. Body: #{response.body}"
          else
            raise EwsError, "Unknown error (#{response.status}): #{uri} : Body: #{response.body}"
          end
        end

        # ********** End Hooks **********


        # Resolve ambiguous e-mail addresses and display names
        # @see http://msdn.microsoft.com/en-us/library/aa565329.aspx ResolveNames
        # @see http://msdn.microsoft.com/en-us/library/aa581054.aspx UnresolvedEntry
        #
        # @param [String] name an unresolved entry
        # @param [Boolean] full_contact_data whether or not to return full contact info
        # @param [Hash] opts optional parameters to this method
        # @option opts [String] :search_scope where to seach for this entry, one of
        #   SOAP::Contacts, SOAP::ActiveDirectory, SOAP::ActiveDirectoryContacts (default),
        #   SOAP::ContactsActiveDirectory
        # @option opts [String, FolderId] :parent_folder_id either the name of a folder or
        #   it's numerical ID.  @see http://msdn.microsoft.com/en-us/library/aa565998.aspx
        def resolve_names(name, full_contact_data = true, opts = {})
          action = "#{SOAP_ACTION_PREFIX}/ResolveNames"
          resp = invoke("#{NS_EWS_MESSAGES}:ResolveNames", action) do |root|
            build!(root) do
              root.set_attr('ReturnFullContactData',full_contact_data)
              root.add("#{NS_EWS_MESSAGES}:UnresolvedEntry",name)
            end
          end
          parse!(resp)
        end


        # Exposes the full membership of distribution lists.
        # @see http://msdn.microsoft.com/en-us/library/aa494152.aspx ExpandDL
        #
        # @param [String] dist_email The e-mail address associated with the Distribution List
        # @todo Fully support all of the ExpandDL operations. Today it just supports
        #   taking an e-mail address as an argument
        def expand_dl(dist_email)
          action = "#{SOAP_ACTION_PREFIX}/ExpandDL"
          resp = invoke("#{NS_EWS_MESSAGES}:ExpandDL", action) do |root|
            build!(root) do
              mailbox!(root, {:email_address => {:text => dist_email}})
            end
          end
          parse!(resp)
        end

        # Find subfolders of an identified folder
        # @see http://msdn.microsoft.com/en-us/library/aa563918.aspx
        #
        # @param [Array] parent_folder_ids An Array of folder ids, either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [String] traversal Shallow/Deep/SoftDeleted
        # @param [Hash] folder_shape defines the FolderShape node
        #   See: http://msdn.microsoft.com/en-us/library/aa494311.aspx
        # @option folder_shape [String] :base_shape IdOnly/Default/AllProperties
        # @option folder_shape :additional_properties
        #   See: http://msdn.microsoft.com/en-us/library/aa563810.aspx
        # @param [Hash] opts optional parameters to this method
        def find_folder(parent_folder_ids = [:root], traversal = 'Shallow', folder_shape = {:base_shape => 'Default'}, opts = {})
          action = "#{SOAP_ACTION_PREFIX}/FindFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:FindFolder", action) do |root|
            build!(root) do
              restriction = opts.delete(:restriction)
              root.set_attr('Traversal', traversal)
              folder_shape!(root, folder_shape)
              root.add("#{NS_EWS_MESSAGES}:Restriction") do |r|
                add_hierarchy!(r, restriction)
              end unless restriction.nil?
              parent_folder_ids!(root, parent_folder_ids)
            end
          end
          parse!(resp)
        end

        # Identifies items that are located in a specified folder
        # @see http://msdn.microsoft.com/en-us/library/aa566107.aspx
        #
        # @param [Array] parent_folder_ids An Array of folder ids, either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [String] traversal Shallow/Deep/SoftDeleted
        # @param [Hash] item_shape defines the FolderShape node
        #   See: http://msdn.microsoft.com/en-us/library/aa494311.aspx
        # @option item_shape [String] :base_shape IdOnly/Default/AllProperties
        # @option item_shape :additional_properties
        #   See: http://msdn.microsoft.com/en-us/library/aa563810.aspx
        # @param [Hash] opts optional parameters to this method
        # @option opts [Hash] :calendar_view Limit FindItem by a start and end date
        #   {:calendar_view => {:max_entries_returned => 2, :start => <DateTime Obj>, :end => <DateTime Obj>}}
        def find_item(parent_folder_ids, traversal = 'Shallow', item_shape = {:base_shape => 'Default'}, opts = {})
          action = "#{SOAP_ACTION_PREFIX}/FindItem"
          resp = invoke("#{NS_EWS_MESSAGES}:FindItem", action) do |root|
            build!(root) do
              root.set_attr('Traversal', traversal)
              item_shape!(root, item_shape)
              query_strings = opts.delete(:query_string)
              restriction = opts.delete(:restriction)
              if(opts.has_key?(:calendar_view))
                cal_view = opts[:calendar_view]
                cal_view.each_pair do |k,v|
                  cal_view[k] = v.to_s
                end
              end
              add_hierarchy!(root, opts, NS_EWS_MESSAGES)
              #query_strings!(query_strings)
              root.add("#{NS_EWS_MESSAGES}:Restriction") do |r|
                add_hierarchy!(r, restriction)
              end unless restriction.nil?
              parent_folder_ids!(root, parent_folder_ids)
            end
          end
          parse!(resp)
        end

        # Gets folders from the Exchange store
        # @see http://msdn.microsoft.com/en-us/library/aa580274.aspx
        #
        # @param [Array] folder_ids An Array of folder ids, either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [Hash] folder_shape defines the FolderShape node
        #   See: http://msdn.microsoft.com/en-us/library/aa494311.aspx
        # @option folder_shape [String] :base_shape IdOnly/Default/AllProperties
        # @option folder_shape :additional_properties
        #   See: http://msdn.microsoft.com/en-us/library/aa563810.aspx
        # @param [String,nil] act_as User to act on behalf as.  This user must have been
        #   given delegate access to this folder or else this operation will fail.
        # @param [Hash] opts optional parameters to this method
        def get_folder(folder_ids, folder_shape = {:base_shape => 'Default'}, act_as = nil)
          action = "#{SOAP_ACTION_PREFIX}/GetFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:GetFolder", action) do |root|
            build!(root) do
              folder_shape!(root, folder_shape)
              folder_ids!(root, folder_ids, act_as)
            end
          end
          parse!(resp)
        end

        # Converts item and folder identifiers between formats that are accepted by Microsoft Exchange
        # @see http://msdn.microsoft.com/en-us/library/bb799665.aspx
        #
        # @param [String] id identifier to convert
        # @param [String] mailbox mailbox where is located the item
        # @param [String] alternate_id_format Format of the identifier to be converted, by default Exchange Web Services identifier
        # @param [String] destination_format Destination format, by default Outlook identifier
        def convert_id(id, mailbox, alternate_id_format = 'EwsId', destination_format = 'HexEntryId')
          action = "#{SOAP_ACTION_PREFIX}/ConvertId"
          resp = invoke("#{NS_EWS_MESSAGES}:ConvertId", action) do |root|
            build!(root) do
              root.set_attr('DestinationFormat', destination_format)
              root.add("#{NS_EWS_MESSAGES}:SourceIds") do |source_ids|
                source_ids.add("#{NS_EWS_TYPES}:AlternateId") do |alternate_id|
                  alternate_id.set_attr('Format', alternate_id_format)
                  alternate_id.set_attr('Id', id)
                  alternate_id.set_attr('Mailbox', mailbox)
                end
              end
            end
          end
          parse!(resp)
        end

        # Creates folders, calendar folders, contacts folders, tasks folders, and search folders.
        # @see http://msdn.microsoft.com/en-us/library/aa563574.aspx CreateFolder
        #
        # @param [String,Symbol] parent_folder_id either the name of a folder or it's
        #   numerical ID.  See: http://msdn.microsoft.com/en-us/library/aa565998.aspx
        # @param [Array,String] folder_name The display name for the new folder or folders
        def create_folder(parent_folder_id, folder_name)
          action = "#{SOAP_ACTION_PREFIX}/CreateFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:CreateFolder", action) do |root|
            build!(root) do
              root.add("#{NS_EWS_MESSAGES}:ParentFolderId") do |pfid|
                folder_id!(pfid, parent_folder_id)
              end
              folder_name = (folder_name.is_a?(Array)) ? folder_name : [folder_name]
              root.add("#{NS_EWS_MESSAGES}:Folders") do |fids|
                folder_name.each do |f|
                  add_hierarchy!(fids, {:folder => {:display_name => {:text => f}}})
                end
              end
            end
          end
          parse!(resp)
        end

        # Deletes folders from a mailbox.
        # @see http://msdn.microsoft.com/en-us/library/aa564767.aspx DeleteFolder
        #
        # @param [Array,String,Symbol] folder_id either the name of a folder or it's
        #   numerical ID.  See: http://msdn.microsoft.com/en-us/library/aa565998.aspx
        # @param [String,nil] delete_type Type of delete to do: HardDelete/SoftDelete/MoveToDeletedItems
        def delete_folder(folder_id, delete_type = 'MoveToDeletedItems')
          action = "#{SOAP_ACTION_PREFIX}/DeleteFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:DeleteFolder", action) do |root|
            build!(root) do
              root.set_attr('DeleteType', delete_type)
              folder_id = (folder_id.is_a?(Array)) ? folder_id : [folder_id]
              folder_ids!(root, folder_id)
            end
          end
          parse!(resp)
        end

        def update_folder
          action = "#{SOAP_ACTION_PREFIX}/UpdateFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:UpdateFolder", action) do |update_folder|
            build_update_folder!(update_folder)
          end
          parse_update_folder(resp)
        end

        def move_folder
          action = "#{SOAP_ACTION_PREFIX}/MoveFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:MoveFolder", action) do |move_folder|
            build_move_folder!(move_folder)
          end
          parse_move_folder(resp)
        end

        def copy_folder
          action = "#{SOAP_ACTION_PREFIX}/CopyFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:CopyFolder", action) do |copy_folder|
            build_copy_folder!(copy_folder)
          end
          parse_copy_folder(resp)
        end

        # Used to subscribe client applications to either push or pull notifications.
        # @see http://msdn.microsoft.com/en-us/library/aa566188.aspx Subscribe on MSDN
        #
        # @param [Array] folder_ids An Array of folder ids, either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [Array] event_types An Array of EventTypes that we should track.
        #   Available types are, CopiedEvent, CreatedEvent, DeletedEvent, ModifiedEvent,
        #   MovedEvent, NewMailEvent, FreeBusyChangedEvent
        # @param [Integer] timeout The number of minutes in which the subscription
        #   will timeout after not receiving a get_events operation.
        # @todo Decide how/if to handle the optional SubscribeToAllFolders attribute of
        #   the PullSubscriptionRequest element.
        def subscribe(folder_ids, event_types, timeout = 10)
          action = "#{SOAP_ACTION_PREFIX}/Subscribe"
          resp = invoke("#{NS_EWS_MESSAGES}:Subscribe", action) do |root|
            build!(root) do
              pull_subscription_request!(folder_ids, event_types, timeout)
            end
          end
          parse!(resp)
        end

        # Used to subscribe client applications to either push or pull notifications.
        # @see http://msdn.microsoft.com/en-us/library/aa566188.aspx Subscribe on MSDN
        def push_subscribe(folder_ids, event_types, url, watermark=nil, status_frequency=5)
          action = "#{SOAP_ACTION_PREFIX}/Subscribe"
          resp = invoke("#{NS_EWS_MESSAGES}:Subscribe", action) do |root|
            build!(root) do
              push_subscription_request!(folder_ids, event_types, url, watermark, status_frequency)
            end
          end
          parse!(resp)

        end

        # End a pull notification subscription.
        # @see http://msdn.microsoft.com/en-us/library/aa564263.aspx
        #
        # @param [String] subscription_id The Id of the subscription
        def unsubscribe(subscription_id)
          action = "#{SOAP_ACTION_PREFIX}/Unsubscribe"
          resp = invoke("#{NS_EWS_MESSAGES}:Unsubscribe", action) do |root|
            build!(root) do
              subscription_id!(root, subscription_id)
            end
          end
          parse!(resp)
        end

        # Used by pull subscription clients to request notifications from the Client Access server
        # @see http://msdn.microsoft.com/en-us/library/aa566199.aspx GetEvents on MSDN
        #
        # @param [String] subscription_id Subscription identifier
        # @param [String] watermark Event bookmark in the events queue
        def get_events(subscription_id, watermark)
          action = "#{SOAP_ACTION_PREFIX}/GetEvents"
          resp = invoke("#{NS_EWS_MESSAGES}:GetEvents", action) do |root|
            build!(root) do
              subscription_id!(root, subscription_id)
              watermark!(root, watermark)
            end
          end
          parse!(resp)
        end

        # Defines a request to synchronize a folder hierarchy on a client
        # @see http://msdn.microsoft.com/en-us/library/aa580990.aspx
        def sync_folder_hierarchy
          sync_state = nil
          folder_id = :publicfoldersroot
          action = "#{SOAP_ACTION_PREFIX}/SyncFolderHierarchy"
          resp = invoke("#{NS_EWS_MESSAGES}:SyncFolderHierarchy", action) do |root|
            build!(root) do
              folder_shape!(root, {:base_shape => 'Default'})
              root.add("#{NS_EWS_MESSAGES}:SyncFolderId") do |sfid|
                folder_id!(sfid, folder_id)
              end
              sync_state!(root, sync_state) unless sync_state.nil?
            end
          end
          parse!(resp)
        end

        # Synchronizes items between the Exchange server and the client
        # @see http://msdn.microsoft.com/en-us/library/aa563967.aspx
        #
        # @param [String, Symbol] folder_id either a DistinguishedFolderId
        #   (must me a Symbol) or a FolderId (String)
        # @param [String] sync_state Base-64 encoded string used to determine
        #   where we are in the sync process.
        # @param [Integer] max_changes The amount of items to sync per call
        #   to SyncFolderItems
        # @param [Hash] item_shape defines the ItemShape node
        #   See: http://msdn.microsoft.com/en-us/library/aa565261.aspx
        # @option item_shape [String] :base_shape IdOnly/Default/AllProperties
        # @option item_shape :additional_properties
        #   See: http://msdn.microsoft.com/en-us/library/aa565261.aspx
        # @param [Hash] opts optional parameters to this method
        def sync_folder_items(folder_id, sync_state = nil, max_changes = 256, item_shape = {:base_shape => 'Default'}, opts = {})
          action = "#{SOAP_ACTION_PREFIX}/SyncFolderItems"
          resp = invoke("#{NS_EWS_MESSAGES}:SyncFolderItems", action) do |root|
            build!(root) do
              item_shape!(root, item_shape)
              root.add("#{NS_EWS_MESSAGES}:SyncFolderId") do |sfid|
                folder_id!(sfid, folder_id)
              end
              sync_state!(root, sync_state) unless sync_state.nil?
              root.add("#{NS_EWS_MESSAGES}:MaxChangesReturned", max_changes)
            end
          end
          parse!(resp)
        end

        # Gets items from the Exchange store
        # @see http://msdn.microsoft.com/en-us/library/aa565934.aspx
        #
        # @param [Array] item_ids An Array of item ids
        # @param [Hash] item_shape defines the ItemShape node
        #   See: http://msdn.microsoft.com/en-us/library/aa565261.aspx
        # @option item_shape [String] :base_shape ('Default') IdOnly/Default/AllProperties
        # @option item_shape :additional_properties
        #   See: http://msdn.microsoft.com/en-us/library/aa563810.aspx
        # @param [Hash] opts optional parameters to this method
        def get_item(item_ids, item_shape = {})
          action = "#{SOAP_ACTION_PREFIX}/GetItem"
          item_shape[:base_shape] = 'Default' unless item_shape.has_key?(:base_shape)
          resp = invoke("#{NS_EWS_MESSAGES}:GetItem", action) do |root|
            build!(root) do
              item_shape!(root, item_shape)
              item_ids!(root, item_ids)
            end
          end
          parse!(resp)
        end

        # Operation is used to create e-mail messages
        # This is actually a CreateItem operation but they differ for different types
        # of Exchange objects so it is named appropriately here.
        # @see http://msdn.microsoft.com/en-us/library/aa566468.aspx
        #
        # @param [String, Symbol] folder_id The folder to save this message in. Either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [Hash, Array] items An array of item Hashes or a single item Hash. Hash
        #   This Hash will eventually be passed to add_hierarchy! in the builder so it is in that format.
        #   Values should be based on values found here: http://msdn.microsoft.com/en-us/library/aa494306.aspx
        # @param [String] message_disposition "SaveOnly/SendOnly/SendAndSaveCopy"
        #   See: http://msdn.microsoft.com/en-us/library/aa565209.aspx
        def create_message_item(folder_id, items, message_disposition = 'SaveOnly')
          action = "#{SOAP_ACTION_PREFIX}/CreateItem"
          resp = invoke("#{NS_EWS_MESSAGES}:CreateItem", action) do |node|
            build!(node) do
              create_item!(folder_id, items, message_disposition, send_invites=false, 'message')
            end
          end
          parse!(resp)
        end

        # Operation is used to create calendar items
        # @see http://msdn.microsoft.com/en-us/library/aa564690.aspx
        #
        # @param [String, Symbol] folder_id The folder to create this item in. Either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [Hash, Array] items An array of item Hashes or a single item Hash. Hash
        #   This Hash will eventually be passed to add_hierarchy! in the builder so it is in that format.
        #   Values should be based on values found here: http://msdn.microsoft.com/en-us/library/aa564765.aspx
        # @param [String] send_invites "SendToNone/SendOnlyToAll/SendToAllAndSaveCopy"
        def create_calendar_item(folder_id, items, send_invites = 'SendToAllAndSaveCopy')
          action = "#{SOAP_ACTION_PREFIX}/CreateItem"
          resp = invoke("#{NS_EWS_MESSAGES}:CreateItem", action) do |node|
            build!(node) do
              create_item!(folder_id, items, message_disposition=false, send_invites, 'calendar')
            end
          end
          parse!(resp)
        end
        
        # Operation is used to create task items
        # This is actually a CreateItem operation but they differ for different types
        # of Exchange objects so it is named appropriately here.
        # @see http://msdn.microsoft.com/en-us/library/aa563439.aspx
        #
        # @param [String, Symbol] folder_id The folder to save this task in. Either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [Hash, Array] items An array of item Hashes or a single item Hash. Hash
        #   values should be based on values found here: http://msdn.microsoft.com/en-us/library/aa494306.aspx
        #   This Hash will eventually be passed to add_hierarchy! in the builder so it is in that format.
        # @param [String] message_disposition "SaveOnly/SendOnly/SendAndSaveCopy"
        #   See: http://msdn.microsoft.com/en-us/library/aa565209.aspx
        def create_task_item(folder_id, items, message_disposition = 'SaveOnly')
          action = "#{SOAP_ACTION_PREFIX}/CreateItem"
          resp = invoke("#{NS_EWS_MESSAGES}:CreateItem", action) do |node|
            build!(node) do
              create_item!(folder_id, items, message_disposition, false, 'task')
            end
          end
          parse!(resp)
        end
        
        # Operation is used to create contact items
        # This is actually a CreateItem operation but they differ for different types
        # of Exchange objects so it is named appropriately here.
        # @see # http://msdn.microsoft.com/en-us/library/aa580529.aspx
        #
        # @param [String, Symbol] folder_id The folder to save this task in. Either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String)
        # @param [Hash, Array] items An array of item Hashes or a single item Hash. Hash
        #   values should be based on values found here: http://msdn.microsoft.com/en-us/library/aa581315.aspx
        #   This Hash will eventually be passed to add_hierarchy! in the builder so it is in that format.
        def create_contact_item(folder_id, items)
          action = "#{SOAP_ACTION_PREFIX}/CreateItem"
          resp = invoke("#{NS_EWS_MESSAGES}:CreateItem", action) do |node|
            build!(node) do
              create_item!(folder_id, items, nil, false, 'contact')
            end
          end
          parse!(resp)
        end

        # Delete an item from a mailbox in the Exchange store
        # @see http://msdn.microsoft.com/en-us/library/aa562961.aspx
        # @param [Array] item_ids An Array of item ids
        # @param [String] delete_type Type of deletion: "HardDelete/SoftDelete/MoveToDeletedItems"
        # @param [String, nil] send_meeting_cancellations "SendToNone/SendOnlyToAll/SendToAllAndSaveCopy"
        #   This is only applicable to CalendarItems and should be nil otherwise, which is the default
        # @param [String, nil] affected_task_occurrences "AllOccurrences/SpecifiedOccurrenceOnly"
        #   This is really only related to tasks and can be nil otherwise, which is the default.
        def delete_item(item_ids, delete_type, send_meeting_cancellations = nil, affected_task_occurrences = nil)
          action = "#{SOAP_ACTION_PREFIX}/DeleteItem"
          resp = invoke("#{NS_EWS_MESSAGES}:DeleteItem", action) do |root|
            build!(root) do
              root.set_attr('DeleteType', delete_type)
              root.set_attr('SendMeetingCancellations', send_meeting_cancellations) unless send_meeting_cancellations.nil?
              root.set_attr('AffectedTaskOccurrences', affected_task_occurrences) unless affected_task_occurrences.nil?
              item_ids!(root, item_ids)
            end
          end
          parse!(resp)
        end

        # Used to modify the properties of an existing item in the Exchange store
        # @see http://msdn.microsoft.com/en-us/library/aa581084.aspx
        # @param [Array] item_ids An Array of item ids
        # @param [Hash] changes a Hash of changes to be fed to auto_hierarchy!
        # @param [Hash] opts various attributes to set for this update. See the Technet docs for more info
        def update_item(item_ids, changes, opts = {:message_disposition => 'SaveOnly', :conflict_resolution => 'AutoResolve'})
          action = "#{SOAP_ACTION_PREFIX}/UpdateItem"
          resp = invoke("#{NS_EWS_MESSAGES}:UpdateItem", action) do |root|
            build!(root) do
              root.set_attr('MessageDisposition', opts[:message_disposition]) if opts.has_key?(:message_disposition)
              root.set_attr('ConflictResolution', opts[:conflict_resolution]) if opts.has_key?(:message_disposition)
              root.set_attr('SendMeetingInvitationsOrCancellations', opts[:send_meeting_invitations_or_cancellations]) if opts.has_key?(:send_meeting_invitations_or_cancellations)
              item_changes!(root, item_ids, changes)
            end
          end
          parse!(resp)
        end

        # Used to send e-mail messages that are located in the Exchange store.
        # @see http://msdn.microsoft.com/en-us/library/aa580238.aspx
        # @param [Array<Hash>] item_ids An Array of item ids.  These item_ids should be a Hash of
        #   :id and :change_key.
        # @param [Boolean] save_item Save item after sending (Think sent-items)
        # @param [String, Symbol,nil] saved_item_folder The folder to save this item in. Either a
        #   DistinguishedFolderId (must me a Symbol) or a FolderId (String).  Just leave
        #   it blank for the default :sentitems
        def send_item(item_ids, save_item=true, saved_item_folder=nil)
          action = "#{SOAP_ACTION_PREFIX}/SendItem"
          resp = invoke("#{NS_EWS_MESSAGES}:SendItem", action) do |root|
            build!(root) do
              root.set_attr('SaveItemToFolder', save_item)
              item_ids!(root,item_ids)
              saved_item_folder_id!(root,saved_item_folder) unless saved_item_folder.nil?
            end
          end
          parse!(resp)
        end

        # Used to move one or more items to a single destination folder.
        # @see http://msdn.microsoft.com/en-us/library/aa565781.aspx
        # @param [Array] item_ids An Array of item ids
        # @param [String, Symbol] folder_id either a DistinguishedFolderId
        #   (must me a Symbol) or a FolderId (String)
        def move_item(item_ids, folder_id)
          action = "#{SOAP_ACTION_PREFIX}/MoveItem"
          resp = invoke("#{NS_EWS_MESSAGES}:MoveItem", action) do |root|
            build!(root) do
              to_folder_id!(root, folder_id)
              item_ids!(root, item_ids)
            end
          end
          parse!(resp)
        end

        # Copies items and puts the items in a different folder
        # @see http://msdn.microsoft.com/en-us/library/aa565012.aspx
        # @param [Array] item_ids An Array of item ids
        # @param [String, Symbol] folder_id either a DistinguishedFolderId
        #   (must me a Symbol) or a FolderId (String)
        def copy_item(item_ids, folder_id)
          action = "#{SOAP_ACTION_PREFIX}/CopyItem"
          resp = invoke("#{NS_EWS_MESSAGES}:CopyItem", action) do |root|
            build!(root) do
              to_folder_id!(root, folder_id)
              item_ids!(root, item_ids)
            end
          end
          parse!(resp)
        end

        # Creates either an item or file attachment and attaches it to the specified item.
        # @see http://msdn.microsoft.com/en-us/library/aa565877.aspx
        # @param [String,Hash] parent_id The id of the Item.  If this is a Hash
        #   it should contain the Id and the ChangeKey.
        # @option parent_id [String] :id The item Id
        # @option parent_id [String] :change_key The ChangeKey
        # @param [Array<Hash>] files An Array of Base64 encoded Strings with an associated name
        #   hash format= :name => <name>, :content => <Base64 encoded string>
        # @param [Array] items Exchange Items to attach to this Item
        # @todo Need to implement attachment of Item types
        def create_attachment(parent_id, files = [], items = [])
          action = "#{SOAP_ACTION_PREFIX}/CreateAttachment"
          resp = invoke("#{NS_EWS_MESSAGES}:CreateAttachment", action) do |root|
            build!(root) do
              item_id!(root, parent_id, "#{NS_EWS_MESSAGES}:ParentItemId")
              attachments!(root, files, items)
            end
          end
          parse!(resp)
        end

        def delete_attachment
          action = "#{SOAP_ACTION_PREFIX}/DeleteAttachment"
          resp = invoke("#{NS_EWS_MESSAGES}:DeleteAttachment", action) do |delete_attachment|
            build_delete_attachment!(delete_attachment)
          end
          parse_delete_attachment(resp)
        end

        # Used to retrieve existing attachments on items in the Exchange store
        # @see http://msdn.microsoft.com/en-us/library/aa494316.aspx
        # @param [Array] attachment_ids Attachment Ids to fetch
        def get_attachment(attachment_ids)
          action = "#{SOAP_ACTION_PREFIX}/GetAttachment"
          resp = invoke("#{NS_EWS_MESSAGES}:GetAttachment", action) do |root|
            build!(root) do
              attachment_shape!(root)
              attachment_ids!(root, attachment_ids)
            end
          end
          parse!(resp)
        end

        def create_managed_folder
          action = "#{SOAP_ACTION_PREFIX}/CreateManagedFolder"
          resp = invoke("#{NS_EWS_MESSAGES}:CreateManagedFolder", action) do |create_managed_folder|
            build_create_managed_folder!(create_managed_folder)
          end
          parse_create_managed_folder(resp)
        end

        # Retrieves the delegate settings for a specific mailbox.
        # @see http://msdn.microsoft.com/en-us/library/bb799735.aspx
        #
        # @param [String] owner The user that is delegating permissions
        def get_delegate(owner)
          action = "#{SOAP_ACTION_PREFIX}/GetDelegate"
          resp = invoke("#{NS_EWS_MESSAGES}:GetDelegate", action) do |root|
            root.set_attr('IncludePermissions', 'true')
            build!(root) do
              mailbox!(root, {:email_address => {:text => owner}})
            end
          end
          parse!(resp)
        end

        # Adds one or more delegates to a principal's mailbox and sets specific access permissions.
        # @see http://msdn.microsoft.com/en-us/library/bb856527.aspx
        #
        # @param [String] owner The user that is delegating permissions
        # @param [String] delegate The user that is being given delegate permission
        # @param [Hash] permissions A hash of permissions that will be delegated.
        #   This Hash will eventually be passed to add_hierarchy! in the builder so it is in that format.
        def add_delegate(owner, delegate, permissions)
          action = "#{SOAP_ACTION_PREFIX}/AddDelegate"
          resp = invoke("#{NS_EWS_MESSAGES}:AddDelegate", action) do |root|
            build!(root) do
              add_delegate!(owner, delegate, permissions)
            end
          end
          parse!(resp)
        end

        # Removes one or more delegates from a user's mailbox.
        # @see http://msdn.microsoft.com/en-us/library/bb856564.aspx
        #
        # @param [String] owner The user that is delegating permissions
        # @param [String] delegate The user that is being given delegate permission
        def remove_delegate(owner, delegate)
          action = "#{SOAP_ACTION_PREFIX}/RemoveDelegate"
          resp = invoke("#{NS_EWS_MESSAGES}:RemoveDelegate", action) do |root|
            build!(root) do
              remove_delegate!(owner, delegate)
            end
          end
          parse!(resp)
        end
        
        # Updates delegate permissions on a principal's mailbox
        # @see http://msdn.microsoft.com/en-us/library/bb856529.aspx
        #
        # @param [String] owner The user that is delegating permissions
        # @param [String] delegate The user that is being given delegate permission
        # @param [Hash] permissions A hash of permissions that will be delegated.
        #   This Hash will eventually be passed to add_hierarchy! in the builder so it is in that format.
        def update_delegate(owner, delegate, permissions)
          action = "#{SOAP_ACTION_PREFIX}/UpdateDelegate"
          resp = invoke("#{NS_EWS_MESSAGES}:UpdateDelegate", action) do |root|
            build!(root) do
              add_delegate!(owner, delegate, permissions)
            end
          end
          parse!(resp)
        end

        # Provides detailed information about the availability of a set of users, rooms, and resources
        # within a specified time window.
        # @see http://msdn.microsoft.com/en-us/library/aa564001.aspx
        def get_user_availability(email_address, start_time, end_time)
          action = "#{SOAP_ACTION_PREFIX}/GetUserAvailability"
          resp = invoke("#{NS_EWS_MESSAGES}:GetUserAvailabilityRequest", action) do |root|
            build!(root) do
              get_user_availability!(email_address, start_time, end_time)
            end
          end
          parse!(resp)
        end

        # Gets a mailbox user's Out of Office (OOF) settings and messages.
        # @see http://msdn.microsoft.com/en-us/library/aa563465.aspx
        def get_user_oof_settings(mailbox)
          action = "#{SOAP_ACTION_PREFIX}/GetUserOofSettings"
          resp = invoke("#{NS_EWS_MESSAGES}:GetUserOofSettingsRequest", action) do |root|
            build!(root) do
              mailbox!(root,mailbox[:mailbox],NS_EWS_TYPES)
            end
          end
          parse!(resp)
        end

        # Sets a mailbox user's Out of Office (OOF) settings and message.
        # @see http://msdn.microsoft.com/en-us/library/aa580294.aspx
        def set_user_oof_settings(mailbox, oof_state, ext_audience, dt_start, dt_end, int_msg, ext_mg)
          action = "#{SOAP_ACTION_PREFIX}/SetUserOofSettings"
          resp = invoke("#{NS_EWS_MESSAGES}:SetUserOofSettings", action) do |root|
            build!(root)
          end
          parse!(resp)
        end


        # Private Methods (Builders and Parsers)
        private

        def build!(node, opts = {}, &block)
          EwsBuilder.new(node, opts, &block)
        end

        def parse!(response, opts = {})
          return response if @@raw_soap
          raise EwsError, "Can't parse an empty response. Please check your endpoint." if(response.nil?)
          EwsParser.new(response).parse(opts)
        end

        # Override the superclasses' invoke so we can add http_options to each request
        def invoke(msg, action)
          raise EwsError, "EWS Endpoint not set." if uri.nil?
          begin
            super(msg, {:soap_action => action, :http_options => @@http_options})
          rescue SocketError
            raise EwsError, "Could not connect to endpoint: #{uri}"
          end
        end

      end # class ExchangeWebService
    end # module SOAP
  end # EWS
end # Viewpoint
