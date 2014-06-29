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

# This class is inherited by all Item subtypes such as Message, Event,
# and Task.  It will serve as the brain for all of the methods that
# each of these Item types have in common.
module Viewpoint
  module EWS
    class Item
      include Model
      include ItemFieldUriMap

      # This is a class method that fetches an existing Item from the
      #  Exchange Store.
      # @param [String] item_id The id of the item.
      # @param [Symbol] shape The optional shape of the item :id_only/:default/:all_properties
      # @return [Item] Returns an Item or subclass of Item
      # @todo Add support to fetch an item with a ChangeKey
      def self.get_item(item_id, shape = :default)
        item_shape = {:base_shape => shape.to_s.camel_case}
        shallow = item_shape[:base_shape] != 'AllProperties'
        resp = (Viewpoint::EWS::EWS.instance).ews.get_item([item_id], item_shape)
        if(resp.status == 'Success')
          item = resp.items.shift
          type = item.keys.first
          eval "#{type.to_s.camel_case}.new(item[type], :shallow => #{shallow})"
        else
          raise EwsError, "Could not retrieve item. #{resp.code}: #{resp.message}"
        end
      end

      # Add attachments to the passed in ParentId
      # @param [String,Hash] parent_id Either a String ItemId or a Hash ItemId with a ChangeKey
      # @option parent_id [String] :id The Id
      # @option parent_id [String] :change_key The ChangeKey
      # @param [Array<File>] attachments An Array of File objects to read in.
      def self.add_attachments(parent_id, attachments)
        conn = Viewpoint::EWS::EWS.instance
        b64attach = []
        attachments.each do |a|
          b64attach << {:name => {:text =>(File.basename a.path)}, :content => {:text => Base64.encode64(a.read)}}
        end
        resp = conn.ews.create_attachment(parent_id, b64attach) 
        (resp.status == 'Success') || (raise EwsError, "Could not create attachments. #{resp.code}: #{resp.message}")
        {:id => resp.items.first[:attachment_id][:root_item_id], :change_key => resp.items.first[:attachment_id][:root_item_change_key]}
      end

      attr_reader :item_id, :change_key, :parent_folder_id
      alias :id :item_id

      # Initialize an Exchange Web Services item
      # @param [Hash] ews_item A hash representing this item
      # @param [Boolean] shallow Whether or not we have retrieved all the elements for this object
      def initialize(ews_item, opts={})
        super() # Calls initialize in Model (creates @ews_methods Array)
        @ews_item = ews_item
        @shallow = opts.has_key?(:shallow) ? opts[:shallow] : true
        @item_id = ews_item[:item_id][:id]
        @change_key = ews_item[:item_id][:change_key]
        @text_only = false
        @updates = {}

        init_methods
      end


      # See if this item is set to return only text in its body.
      # @return [Boolean] if true the body will return only text, otherwise it may be HTML or text.
      def text_only?
        @text_only
      end

      # Set whether or not the body should be text-only or not
      # @param [Boolean] txt if true the body will return only text, otherwise it may be HTML or text.
      def text_only=(txt)
        @text_only = ( txt == true ? true : false)
      end

      # Save any pending updates that were manipulated via setter methods.
      def save!
        return true if @updates.empty?
        if update_attribs!(@updates)
          @updates = {}
          true
        else
          false
        end
      end

      # Clear out any pending updates
      # @return [TrueClass]
      def clear_updates!
        @updates = {}
        true
      end

      # Call UpdateItem for this item with the passed updates
      # @param [Hash] updates a well-formed update hash
      # @example {:set_item_field=>{:field_uRI=>{:field_uRI=>"message:IsRead"}, :message=>{:is_read=>{:text=>"true"}}}}
      def update!(updates)
        conn = Viewpoint::EWS::EWS.instance
        resp = conn.ews.update_item([{:id => @item_id, :change_key => @change_key}], {:updates => updates})
        if resp.status == 'Success'
          @item_id = resp.items.first[resp.items.first.keys.first][:item_id][:id]
          @change_key = resp.items.first[resp.items.first.keys.first][:item_id][:change_key]
          @shallow = true
          deepen!
        else
          raise EwsError, "Trouble updating Item. #{resp.code}: #{resp.message}"
        end

      end

      # This takes a hash of attributes with new values and builds the appropriate udpate hash.
      #   It does not commit the changes to Exchange, call #update! with the returned values from
      #   this method or look at #update_attribs! for a version of this method that autocommits the
      #   changes back.
      #
      # You can also specify a preformatted Array of data like so:
      #   {:preformatted => [misc data]}
      #   This will simply be passed to the update! method
      # @param [Hash] updates a hash that is formed like so :item_attr => newvalue
      # @param [Symbol] update_type :append, :replace, :delete
      # @example  {:sensitivity => {:text => 'Normal'}, :display_name => {:text => 'Test User'}}
      def update_attribs(updates, update_type = :replace)
        utype_map = {:append => :append_to_item_field, :replace => :set_item_field, :delete => :delete_item_field}
        changes = []
        type = self.class.name.split(/::/).last.ruby_case.to_sym

        updates.each_pair do |k,v|
          if(k == :preformatted)
            changes += v
            next
          end
          raise EwsError, "Field (#{FIELD_URIS[k][:text]}) not writable by update." unless FIELD_URIS[k][:writable]
          changes << {utype_map[update_type]=>[{:field_uRI => {:field_uRI=>FIELD_URIS[k][:text]}}, {type=>{k => v}}]}
        end

        changes
      end

      # This is the same as #update_attribs, but it will commit the changes back to Exchange.
      # @see #update_attribs
      def update_attribs!(updates, update_type = :replace)
        changes = update_attribs(updates, update_type)
        update!(changes)
      end

      # Mark this Item as read
      def mark_read!
        field = :is_read
        update!({:set_item_field=>{:field_uRI=>{:field_uRI=>FIELD_URIS[field][:text]}, :message=>{field=>{:text=>"true"}}}})
        @is_read = true
      end

      # Mark this Item as unread
      def mark_unread!
        field = :is_read
        update!({:set_item_field=>{:field_uRI=>{:field_uRI=>FIELD_URIS[field][:text]}, :message=>{field=>{:text=>"false"}}}})
        @is_read = false
        true
      end

      def deepen!
        return true unless @shallow
        conn = Viewpoint::EWS::EWS.instance
        shape = {:base_shape => 'AllProperties', :body_type => (@text_only ? 'Text' : 'Best')}
        resp = conn.ews.get_item([@item_id], shape) 
        resp = resp.items.shift
        @ews_item = resp[resp.keys.first]
        @shallow = false
        @ews_methods = []
        @ews_methods_undef = []
        init_methods
        true
      end

      # Move this item to a new folder
      # @param [String,Symbol,GenericFolder] new_folder The new folder to move it to. This should
      #   be a subclass of GenericFolder, a DistinguishedFolderId (must me a Symbol) or a FolderId (String)
      def move!(new_folder)
        new_folder = new_folder.id if new_folder.kind_of?(GenericFolder)
        resp = (Viewpoint::EWS::EWS.instance).ews.move_item([@item_id], new_folder)
        if(resp.status == 'Success')
          @item_id = resp.items.first[resp.items.first.keys.first][:item_id][:id]
          @change_key = resp.items.first[resp.items.first.keys.first][:item_id][:change_key]
          true
        else
          raise EwsError, "Could not move item. #{resp.code}: #{resp.message}"
        end
      end

      # Copy this item to a new folder
      # @param [String,Symbol,GenericFolder] new_folder The new folder to move it to. This should
      #   be a subclass of GenericFolder, a DistinguishedFolderId (must me a Symbol) or a FolderId (String)
      # @return [Item] The Item object of the copy
      def copy(new_folder)
        new_folder = new_folder.id if new_folder.kind_of?(GenericFolder)
        resp = (Viewpoint::EWS::EWS.instance).ews.copy_item([@item_id], new_folder)
        if(resp.status == 'Success')
          item = resp.items.first
          i_type = item.keys.first.to_s.camel_case
          return(eval "#{i_type}.new(item[item.keys.first])")
        else
          raise EwsError, "Could not copy item. #{resp.code}: #{resp.message}"
        end
      end

      # Return the attachments for this Item
      # @return [Array,Attachment] An array of Attachments for this Item
      def attachments
        # TODO: should an exception be raised if someone calls this method without first
        # checking has_attachments?
        return [] unless has_attachments?

        # If we've already called this don't waste the time to process attachments again.
        return @attachments if defined?(@attachments)

        deepen!
        @attachments = []
        @ews_item[:attachments].each_pair do |k,v|
          # k should be file_attachment or item_attachment
          if(v.is_a?(Hash))
            @attachments << (eval "#{k.to_s.camel_case}.new(v[:attachment_id][:id])")
          else
            v.each do |att|
              @attachments << (eval "#{k.to_s.camel_case}.new(att[:attachment_id][:id])")
            end
          end
        end
        @attachments
      end

      # Delete this item
      # @param [Boolean] soft Whether or not to do a soft delete.  By default EWS will do a 
      #   hard delete of this item.  See the MSDN docs for more info:
      #   http://msdn.microsoft.com/en-us/library/aa562961.aspx
      # @return [Boolean] Whether or not the item was deleted
      # @todo Add exception handling for failed deletes
      def delete!(soft=false)
        deltype = soft ? 'SoftDelete' : 'HardDelete'
        resp = (Viewpoint::EWS::EWS.instance).ews.delete_item([@item_id], deltype)
        self.clear_object!
        (resp.status == 'Success') || (raise EwsError, "Could not delete message. #{resp.code}: #{resp.message}")
      end

      # Delete this item by moving it to the Deleted Items folder
      # @see  http://msdn.microsoft.com/en-us/library/aa562961.aspx
      # @return [Boolean] Whether or not the item was deleted
      # @todo Add exception handling for failed deletes
      def recycle!
        resp = (Viewpoint::EWS::EWS.instance).ews.delete_item([@item_id], 'MoveToDeletedItems')
        self.clear_object!
        (resp.status == 'Success') || (raise EwsError, "Could not recycle message. #{resp.code}: #{resp.message}")
      end

      # Get the parent folder of this item
      # @return [GenericFolder] returns a GenericFolder of subclass of that type.
      def parent_folder
        #deepen!
        GenericFolder.get_folder @parent_folder_id
      end



      private

      # @todo Handle:
      #   <Attachments/> <Categories/> <InternetMessageHeaders/> <ResponseObjects/>
      #   <ExtendedProperty/> <EffectiveRights/>
      def init_methods
        @parent_folder_id = @ews_item[:parent_folder_id][:id] if @ews_item[:parent_folder_id].is_a?(Hash)
        @conversation_id  = @ews_item[:conversation_id][:id] if @ews_item[:conversation_id].is_a?(Hash)
        @ews_methods << :item_id
        define_str_var :subject, :sensitivity, :body, :item_class, :importance, :in_reply_to, :unique_body
        define_str_var :display_cc, :display_to, :culture, :last_modified_name, :mime_content
        define_str_var :web_client_read_form_query_string, :web_client_edit_form_query_string
        define_attr_str_var :body, :body_type
        define_attr_str_var :unique_body, :body_type
        define_attr_str_var :mime_content, :character_set
        define_int_var :size, :reminder_minutes_before_start
        define_bool_var :has_attachments, :is_submitted, :is_draft, :is_from_me, :is_resend, :is_unmodified, :reminder_is_set, :is_associated
        define_datetime_var :date_time_sent, :date_time_created, :date_time_received, :reminder_due_by, :last_modified_time
      end

      def method_missing(m, *args, &block)
        if(@shallow)
          deepen!
          send(m, *args, &block)
        else
          warn "!!! No such method: #{m}" if $DEBUG
          nil
        end
      end

    end # Item
  end # EWS
end # Viewpoint
