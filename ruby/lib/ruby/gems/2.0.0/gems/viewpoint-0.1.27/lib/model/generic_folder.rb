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

# This class is inherited by all folder subtypes such as Mail, Calendar,
# Tasks and Search.  It will serve as the brain for all of the methods that
# each of these folder types have in common.
module Viewpoint
  module EWS
    # This class is a generic folder that should typically not be instantiated
    # on it's own.  It represents all the commonalities among folders found
    # in the Exchange Data Store of which there are many.
    # @see http://msdn.microsoft.com/en-us/library/aa564009.aspx
    class GenericFolder
      include Viewpoint
      include Model

      @@distinguished_folder_ids = %w{calendar contacts deleteditems drafts inbox journal
      notes outbox sentitems tasks msgfolderroot root junkemail searchfolders voicemail
      recoverableitemsroot recoverableitemsdeletions recoverableitemsversions
      recoverableitemspurges archiveroot archivemsgfolderroot archivedeleteditems
      archiverecoverableitemsroot archiverecoverableitemsdeletions
      archiverecoverableitemsversions archiverecoverableitemspurges publicfoldersroot}

      @@event_types = %w{CopiedEvent CreatedEvent DeletedEvent ModifiedEvent MovedEvent NewMailEvent}

      # Get a specific folder by its ID.
      # @param [String,Symbol] folder_id either a DistinguishedFolderID or simply a FolderID
      # @param [String,nil] act_as User to act on behalf as.  This user must have been given
      #   delegate access to this folder or else this operation will fail.
      # @param [Hash] folder_shape
      # @option folder_shape [String] :base_shape IdOnly/Default/AllProperties
      # @raise [EwsError] raised when the backend SOAP method returns an error.
      def self.get_folder(folder_id, act_as = nil, folder_shape = {:base_shape => 'Default'})
        resp = (Viewpoint::EWS::EWS.instance).ews.get_folder( [normalize_id(folder_id)], folder_shape, act_as )
        if(resp.status == 'Success')
          folder = resp.items.first
          f_type = folder.keys.first.to_s.camel_case
          return(eval "#{f_type}.new(folder[folder.keys.first])")
        else
          raise EwsError, "Could not retrieve folder. #{resp.code}: #{resp.message}"
        end
      end

      # Find subfolders of the passed root folder.  If no parameters are passed
      # this method will search from the Root folder.
      # @param [String,Symbol] root An folder id, either a DistinguishedFolderId (must me a Symbol)
      #   or a FolderId (String). This is where to start the search from. Usually :root,:msgfolderroot,:publicfoldersroot
      # @param [String] traversal Shallow/Deep/SoftDeleted
      # @param [String] shape the shape to return IdOnly/Default/AllProperties
      # @param [optional, String] folder_type an optional folder type to limit the search to like 'IPF.Task'
      # @return [Array] Returns an Array of Folder or subclasses of Folder
      # @raise [EwsError] raised when the backend SOAP method returns an error.
      def self.find_folders(root = :msgfolderroot, traversal = 'Shallow', shape = 'Default', folder_type = nil)
        if( folder_type.nil? )
          resp = (Viewpoint::EWS::EWS.instance).ews.find_folder( [normalize_id(root)], traversal, {:base_shape => shape} )
        else
          restr = {:restriction => 
            {:is_equal_to => [{:field_uRI => {:field_uRI=>'folder:FolderClass'}}, {:field_uRI_or_constant=>{:constant => {:value => folder_type}}}]}
          }
          resp = (Viewpoint::EWS::EWS.instance).ews.find_folder( [normalize_id(root)], traversal, {:base_shape => shape}, restr)
        end

        if(resp.status == 'Success')
          folders = []
          resp.items.each do |f|
            f_type = f.keys.first.to_s.camel_case
            folders << (eval "#{f_type}.new(f[f.keys.first])")
          end
          return folders
        else
          raise EwsError, "Could not retrieve folders. #{resp.code}: #{resp.message}"
        end
      end

      # Return a list of folder names
      # @param [String,Symbol] root An folder id, either a DistinguishedFolderId (must me a Symbol)
      #   or a FolderId (String). This is where to start the search from. Usually :root,:msgfolderroot,:publicfoldersroot
      # @return [Array<String>] Return an Array of folder names.
      # @raise [EwsError] raised when the backend SOAP method returns an error.
      def self.folder_names(root = :msgfolderroot)
        resp = (Viewpoint::EWS::EWS.instance).ews.find_folder([root], 'Shallow')
        if(resp.status == 'Success')
          flds = []
          resp.items.each do |f|
            flds << f[f.keys.first][:display_name][:text]
          end
          flds
        else
          raise EwsError, "Could not retrieve folders. #{resp.code}: #{resp.message}"
        end
      end

      # Gets a folder by name.  This name must match the folder name exactly.
      # @param [String] name The name of the folder to fetch.
      # @param [String,Symbol] root An folder id, either a DistinguishedFolderId (must me a Symbol)
      #   or a FolderId (String). This is where to start the search from. Usually :root,:msgfolderroot,:publicfoldersroot
      # @param [String] shape the shape of the object to return IdOnly/Default/AllProperties
      # @return [GenericFolder] will return the folder by the given name.
      # @raise [EwsFolderNotFound] raised when a folder requested is not found
      # @raise [EwsError] raised when the backend SOAP method returns an error.
      def self.get_folder_by_name(name, root = :msgfolderroot, shape = 'Default', opts = {})
        opts[:traversal] = 'Deep' unless opts.has_key?(:traversal)
        # For now the :field_uRI and :field_uRI_or_constant must be in an Array for Ruby 1.8.7 because Hashes
        # are not positional at insertion until 1.9
        restr = {:restriction =>
          {:is_equal_to => 
            [{:field_uRI => {:field_uRI=>'folder:DisplayName'}}, {:field_uRI_or_constant =>{:constant => {:value=>name}}}]}}
        resp = (Viewpoint::EWS::EWS.instance).ews.find_folder([root], opts[:traversal], {:base_shape => shape}, restr)
        if(resp.status == 'Success')
          raise EwsFolderNotFound, "The folder requested is invalid or unavailable" if resp.items.empty?
          f = resp.items.first
          f_type = f.keys.first.to_s.camel_case
          eval "#{f_type}.new(f[f.keys.first])"
        else
          raise EwsError, "Could not retrieve folder. #{resp.code}: #{resp.message}"
        end
      end

      # Gets a folder by the given path. The default search path is :msgfolderroot so if you want to
      # specify a path at a different root change that parameter.
      # @param [String] path the fully qualified path to a folder at the given root
      #   @example "/myfolders/folder a/personal calendar"
      # @param [String,Symbol] root An folder id, either a DistinguishedFolderId (must me a Symbol)
      #   or a FolderId (String). This is where to start the search from. Usually :root,:msgfolderroot,:publicfoldersroot
      # @param [String] shape the shape of the object to return IdOnly/Default/AllProperties
      # @return [GenericFolder] will return the folder by the given path
      # @raise [EwsFolderNotFound] raised when a folder requested is not found
      # @raise [EwsError] raised when the backend SOAP method returns an error.
      def self.get_folder_by_path(path, root = :msgfolderroot, shape = 'Default')
        parts = path.split(/\//)
        parts = parts.slice(1..(parts.length)) if parts.first.empty?
        retfld = nil
        parts.each do |p|
          fld = self.get_folder_by_name(p, root, shape, {:traversal => 'Shallow'})
          root = fld.id
          retfld = fld if(fld.display_name.downcase == p.downcase)
        end
        retfld
      end

      attr_accessor :folder_id, :change_key, :parent_id, :sync_state
      attr_reader :subscription_id, :watermark
      alias :id :folder_id

      def initialize(ews_item)
        super() # Calls initialize in Model (creates @ews_methods Array)
        @ews_item = ews_item
        @folder_id = ews_item[:folder_id][:id]
        @ews_methods << :folder_id
        @ews_methods << :id
        @change_key = ews_item[:folder_id][:change_key]
        @ews_methods << :change_key
        unless ews_item[:parent_folder_id].nil?
          @parent_id = ews_item[:parent_folder_id]
          @ews_methods << :parent_id
        end
        define_str_var :display_name, :folder_class
        define_int_var :child_folder_count, :total_count
        # @todo Handle:
        #   <EffectiveRights/>, <ExtendedProperty/>, <ManagedFolderInformation/>, <PermissionSet/>

        @sync_state = nil # Base-64 encoded sync data
        @synced = false   # Whether or not the synchronization process is complete
        @subscription_id = nil
        @watermark = nil
        @shallow = true
      end

      # Subscribe this folder to events.  This method initiates an Exchange pull
      # type subscription.
      #
      # @param [Array] event_types Which event types to subscribe to.  By default
      #   we subscribe to all Exchange event types: CopiedEvent, CreatedEvent,
      #   DeletedEvent, ModifiedEvent, MovedEvent, NewMailEvent, FreeBusyChangedEvent
      # @return [Boolean] Did the subscription happen successfully?
      # @todo Add custom Exception for EWS
      def subscribe(event_types = @@event_types)
        # Refresh the subscription if already subscribed
        unsubscribe if subscribed?

        resp = (Viewpoint::EWS::EWS.instance).ews.subscribe([folder_id],event_types)
        if(resp.status == 'Success')
          @subscription_id = resp.items.first[:subscription_id][:text]
          @watermark = resp.items.first[:watermark][:text]
          return true
        else
          raise StandardError, "Error: #{resp.message}"
        end
      end

      # Check if there is a subscription for this folder.
      # @return [Boolean] Are we subscribed to this folder?
      def subscribed?
        ( @subscription_id.nil? or @watermark.nil? )? false : true
      end


      # Unsubscribe this folder from further Exchange events.
      # @return [Boolean] Did we unsubscribe successfully?
      # @todo Add custom Exception for EWS
      def unsubscribe
        return true if @subscription_id.nil?

        resp = (Viewpoint::EWS::EWS.instance).ews.unsubscribe(@subscription_id)
        if(resp.status == 'Success')
          @subscription_id, @watermark = nil, nil
          return true
        else
          raise StandardError, "Error: #{resp.message}"
        end
      end

      # Checks a subscribed folder for events
      # @return [Array] An array of Event items
      # @todo check for subscription expiry
      def get_events
        begin
          if(subscribed?)
            resp = (Viewpoint::EWS::EWS.instance).ews.get_events(@subscription_id, @watermark)
            parms = resp.items.shift
            @watermark = parms[:watermark]
            # @todo if parms[:more_events] # get more events
            return resp.items
          else
            raise StandardError, "Folder <#{self.display_name}> not subscribed to. Issue a Folder#subscribe before checking events."
          end
        rescue EwsSubscriptionTimeout => e
          @subscription_id, @watermark = nil, nil
          raise e
        end
      end

      # Find Items
      def find_items(opts = {})
        opts = opts.clone # clone the passed in object so we don't modify it in case it's being used in a loop
        item_shape = opts.has_key?(:item_shape) ? opts.delete(:item_shape) : {:base_shape => 'Default'}
        shallow = item_shape[:base_shape] != 'AllProperties'
        unless item_shape.has_key?(:additional_properties) # Don't overwrite if specified by caller
          item_shape[:additional_properties] = {:field_uRI => ['item:ParentFolderId']}
        end
        resp = (Viewpoint::EWS::EWS.instance).ews.find_item([@folder_id], 'Shallow', item_shape, opts)
        if(resp.status == 'Success')
          parms = resp.items.shift
          items = []
          resp.items.each do |i|
            i_type = i.keys.first
            items << (eval "#{i_type.to_s.camel_case}.new(i[i_type], :shallow => #{shallow})")
          end
          return items
        else
          raise EwsError, "Could not find items. #{resp.code}: #{resp.message}"
        end
      end

      # Fetch only items from today (since midnight)
      def todays_items(opts = {})
        #opts = {:query_string => ["Received:today"]}
        #This is a bit convoluted for pre-1.9.x ruby versions that don't support to_datetime
        items_since(DateTime.parse(Date.today.to_s), opts)
      end

      # Fetch items since a give DateTime
      # @param [DateTime] date_time the time to fetch Items since.
      def items_since(date_time, opts = {})
        restr = {:restriction =>
          {:is_greater_than_or_equal_to => 
            [{:field_uRI => {:field_uRI=>'item:DateTimeReceived'}},
            {:field_uRI_or_constant =>{:constant => {:value=>date_time}}}]
          }}
        find_items(opts.merge(restr))
      end

      # Fetch items between a given time period
      # @param [DateTime] start_date the time to start fetching Items from
      # @param [DateTime] end_date the time to stop fetching Items from
      def items_between(start_date, end_date, opts={})
        restr = {:restriction =>  {:and => [
          {:is_greater_than_or_equal_to => 
            [{:field_uRI => {:field_uRI=>'item:DateTimeReceived'}},
            {:field_uRI_or_constant=>{:constant => {:value =>start_date}}}]},
          {:is_less_than_or_equal_to =>
            [{:field_uRI => {:field_uRI=>'item:DateTimeReceived'}},
            {:field_uRI_or_constant=>{:constant => {:value =>end_date}}}]}
        ]}}
        find_items(opts.merge(restr))
      end

      # Search on the item subject
      # @param [String] match_str A simple string paramater to match against the subject.  The search ignores
      #   case and does not accept regexes... only strings.
      # @param [String,nil] exclude_str A string to exclude from matches against the subject.  This is optional.
      def search_by_subject(match_str, exclude_str = nil)
        match = {:contains =>
          [
            {:containment_mode => 'Substring'},
            {:containment_comparison => 'IgnoreCase'},
            {:field_uRI => {:field_uRI=>'item:Subject'}},
            {:constant => {:value =>match_str}}
          ]
        }
        unless exclude_str.nil?
          excl = {:not =>
            {:contains =>
              [
                {:containment_mode => 'Substring'},
                {:containment_comparison => 'IgnoreCase'},
                {:field_uRI => {:field_uRI=>'item:Subject'}},
                {:constant => {:value =>exclude_str}}
              ]
            }
          }

          match[:and] = [{:contains => match.delete(:contains)}, excl]
        end

        find_items({:restriction => match})
      end

      # Get Item
      # @param [String] item_id the ID of the item to fetch
      # @param [String] change_key specify an optional change_key if you want to
      #   make sure you are fetching a specific version of the object.
      def get_item(item_id, change_key = nil)
        item_shape = {:base_shape => 'Default', :additional_properties => {:field_uRI => ['item:ParentFolderId']}}
        resp = (Viewpoint::EWS::EWS.instance).ews.get_item([item_id], item_shape)
        if(resp.status == 'Success')
          item = resp.items.shift
          type = item.keys.first
          eval "#{type.to_s.camel_case}.new(item[type])"
        else
          raise EwsError, "Could not retrieve item. #{resp.code}: #{resp.message}"
        end
      end

      # Get Items
      # @param [String] item_ids is an array of Item IDs to fetch
      # @param [String] change_key specify an optional change_key if you want to
      #   make sure you are fetching a specific version of the object.
      # @param [String] options specify an optional options hash. Supports the
      #   key :item_shape that expects a hash value with :base_shape and other
      #   optional parameters that specify the desired fields to return.
      def get_items(item_ids, change_key = nil, options={})
        item_shape = options[:item_shape] ||
          {:base_shape => 'Default', :additional_properties => {:field_uRI => ['item:ParentFolderId']}}
        shallow = item_shape[:base_shape] != 'AllProperties'
        resp = (Viewpoint::EWS::EWS.instance).ews.get_item(item_ids, item_shape)
        if(resp.status == 'Success')
          resp.items.map do |item|
            type = item.keys.first
            eval "#{type.to_s.camel_case}.new(item[type], :shallow => #{shallow})"
          end
        else
          raise EwsError, "Could not retrieve items. #{resp.code}: #{resp.message}"
        end
      end


      # Syncronize Items in this folder. If this method is issued multiple
      # times it will continue where the last sync completed.
      # @param [Integer] sync_amount The number of items to synchronize per sync
      # @param [Boolean] sync_all Whether to sync all the data by looping through.
      #   The default is to just sync the first set.  You can manually loop through
      #   with multiple calls to #sync_items!
      # @return [Hash] Returns a hash with keys for each change type that ocurred.
      #   Possible key values are (:create/:udpate/:delete).  For create and update
      #   changes the values are Arrays of Item or a subclass of Item.  For deletes
      #   an array of ItemIds are returned wich is a Hash in the form:
      #   {:id=>"item id", :change_key=>"change key"}
      #   See: http://msdn.microsoft.com/en-us/library/aa565609.aspx
      def sync_items!(sync_amount = 256, sync_all = false, opts = {})
        item_shape = opts.has_key?(:item_shape) ? opts.delete(:item_shape) : {:base_shape => 'Default'}
        shallow = item_shape[:base_shape] != 'AllProperties'
        resp = (Viewpoint::EWS::EWS.instance).ews.sync_folder_items(@folder_id, @sync_state, sync_amount, item_shape)
        parms = resp.items.shift
        @sync_state = parms[:sync_state]
        @synced = parms[:includes_last_item_in_range]
        items = {}
        resp.items.each do |i|
          key = i.keys.first
          items[key] = [] unless items[key].is_a?(Array)
          if(key == :delete || key == :read_flag_change)
            items[key] << i[key][:item_id]
          else
            i_type = i[key].keys.first
            next if !i_type
            items[key] << (eval "#{i_type.to_s.camel_case}.new(i[key][i_type], :shallow => #{shallow})")
          end
        end
        items
      end

      # Fetch current synced state (comes from synchronizing elements).
      # @return [Boolean] Current synchronization state, i.e. whether sync_items! needs to be called
      #         again to finish the pending rounds of synchronization requests.
      def synced
        @synced
      end

      # This is basically a work-around for Microsoft's BPOS hosted Exchange, which does not support
      # subscriptions at the time of this writing.  This is the best way I could think of to get
      # items from a specific period of time and track changes.
      # !! Before using this method I would suggest trying a GenericFolder#items_since then using
      # a subscription to track changes.
      # This method should be followed by subsequent calls to GenericFolder#sync_items! to fetch
      # additional items.  Calling this method again will clear the sync_state and synchronize
      # everything again.
      # @return [Array<Item>] returns an array of Items
      def sync_items_since!(datetime, opts={})
        clear_sync_state!

        begin
          items = sync_items!
        end until items.empty?

        items_since(datetime, opts)
      end

      # Clears out the @sync_state so you can freshly synchronize this folder if needed
      def clear_sync_state!
        @sync_state = nil
      end

      # Create a subfolder of this folder
      #
      # @param [String] name The name of the new folder
      def add_subfolder(name)
        resp = (Viewpoint::EWS::EWS.instance).ews.create_folder(@folder_id, name)
        folder = resp.items.first
        ftype = folder.keys.first
        GenericFolder.get_folder(folder[ftype][:folder_id][:id])
      end

      # Deletes this folder from the Exchange Data Store
      # @param [Boolean] recycle_bin Send to the recycle bin instead of deleting (default: false)
      # @return [TrueClass] This will return true because if an issue occurs it
      #   will be thrown in the SOAP Parser
      def delete!(recycle_bin = false)
        deltype = recycle_bin ? 'MoveToDeletedItems' : 'HardDelete'
        resp = (Viewpoint::EWS::EWS.instance).ews.delete_folder(@folder_id, deltype)
        true
      end

      private

      # Return the appropriate id based on whether it is a DistinguishedFolderId or
      # simply just a FolderId
      def self.normalize_id(folder_id)
        tfolder_id = folder_id.to_s.downcase
        # If the folder_id is a DistinguishedFolderId change it to a symbol so our SOAP
        # method does the right thing.
        @@distinguished_folder_ids.find_index(tfolder_id) ? tfolder_id.to_sym : folder_id
      end

    end # GenericFolder
  end # EWS
end # Viewpoint
