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

# This is a module that is included in the main Builder that has sub builders
# that are used from multiple root nodes.  It is basically just a way to do
# code reuse in a more natural way.  The one difference between these functions
# and the builder functions in the EwsBuilder class is that the first parameter
# is of node type.  We use that parameter to build subnodes in this module.

module Viewpoint
  module EWS
    module SOAP
      module EwsBuildHelpers

        def folder_ids!(node, folder_ids, act_as=nil, element_name="#{NS_EWS_MESSAGES}:FolderIds")
          node.add(element_name) do |p|
            folder_ids.each do |id|
              folder_id!(p,id,act_as)
            end
          end
        end

        def folder_id!(node, folder_id, act_as = nil)
          if( folder_id.is_a?(Symbol) )
            # @todo add change_key support to DistinguishedFolderId
            node.add("#{NS_EWS_TYPES}:DistinguishedFolderId") do |df|
              df.set_attr('Id', folder_id.to_s)
              # add optional delegate user
              mailbox!(df, {:email_address => {:text => act_as}}, NS_EWS_TYPES) unless act_as.nil?
            end
          else
            # @todo add change_key support to FolderId
            node.add("#{NS_EWS_TYPES}:FolderId") do |fi|
              fi.set_attr('Id', folder_id)
            end
          end
        end

        # For now this is the same as folder_ids! so just use that method
        def parent_folder_ids!(node, folder_ids)
          folder_ids!(node, folder_ids, nil, "#{NS_EWS_MESSAGES}:ParentFolderIds")
        end

        # @see http://msdn.microsoft.com/en-us/library/aa565020.aspx
        def to_folder_id!(node, folder_id)
          node.add("#{NS_EWS_MESSAGES}:ToFolderId") do |tfi|
            folder_id!(tfi, folder_id)
          end
        end

        # Create the ItemChanges Element
        def item_changes!(node, item_ids, changes)
          node.add("#{NS_EWS_MESSAGES}:ItemChanges") do |chgs|
            chgs.add("#{NS_EWS_TYPES}:ItemChange") do |chg|
              item_id!(chg, item_ids.first)
              add_hierarchy!(chg, changes)
            end
          end
        end

        # Create the ItemIds Element
        # @param [Element] node The node we are adding Mailbox elements to.
        # @param [Array] item_ids The item ids to add in.
        def item_ids!(node, item_ids)
          node.add("#{NS_EWS_MESSAGES}:ItemIds") do |ids|
            item_ids.each do |id|
              item_id!(ids,id)
            end
          end
        end

        # Builds an ItemId element out of a String or Hash object
        # @param [Element] node The node we are adding Mailbox elements to.
        # @param [String,Hash] item_id The id of the Item.  If this is a Hash
        #   it should contain the Id and the ChangeKey.
        # @option item_ids [String] :id The item Id
        # @option item_ids [String] :change_key The ChangeKey
        def item_id!(node, item_id, element_name="#{NS_EWS_TYPES}:ItemId")
          node.add(element_name) do |iid|
            if(item_id.is_a?(String))
              iid.set_attr('Id',item_id)
            else
              iid.set_attr('Id',item_id[:id])
              iid.set_attr('ChangeKey',item_id[:change_key])
            end
          end
        end

        def user_id!(node, uid)
          add_hierarchy!(node, uid)
        end

        # @param [Element] node The node we are adding Mailbox elements to.
        # @param [Hash] mailbox A Mailbox formated hash inside the :mailbox key
        #   For example: {:email_address => 'test@test.com', :name => 'Test User'}
        def mailbox!(node, mailbox, ns = NS_EWS_MESSAGES)
          node.add("#{ns}:Mailbox") do |mbx|
            add_hierarchy!(mbx, mailbox)
          end
        end

        def delegate_users!(node, d_users)
          node.add("#{NS_EWS_MESSAGES}:DelegateUsers") do |dus|
            d_users.each do |du|
              dus.add("#{NS_EWS_TYPES}:DelegateUser") do |dut|
                add_hierarchy!(dut, du)
              end
            end
          end
        end

        def saved_item_folder_id!(node, folder_id)
          node.add("#{NS_EWS_MESSAGES}:SavedItemFolderId") do |sfid|
            folder_id!(sfid, folder_id)
          end
        end

        # @todo This only supports the FieldURI extended property right now
        def folder_shape!(node, folder_shape)
          node.add("#{NS_EWS_MESSAGES}:FolderShape") do |fshape|
            fshape.add("#{NS_EWS_TYPES}:BaseShape", folder_shape[:base_shape])

            unless( folder_shape[:additional_properties].nil? )
              unless( folder_shape[:additional_properties][:FieldURI].nil? )
                fshape.add("#{NS_EWS_TYPES}:AdditionalProperties") do |addprops|
                  folder_shape[:additional_properties][:FieldURI].each do |uri|
                    addprops.add("#{NS_EWS_TYPES}:FieldURI") { |furi| furi.set_attr('FieldURI', uri) }
                  end
                end
              end
            end
          end
        end

        # @todo Finish AdditionalProperties implementation
        def item_shape!(node, item_shape)
          node.add("#{NS_EWS_MESSAGES}:ItemShape") do |is|
            is.add("#{NS_EWS_TYPES}:BaseShape", item_shape[:base_shape])
            is.add("#{NS_EWS_TYPES}:IncludeMimeContent", item_shape[:include_mime_content]) if item_shape.has_key?(:include_mime_content)
            is.add("#{NS_EWS_TYPES}:BodyType", item_shape[:body_type]) if item_shape.has_key?(:body_type)
            is.add("#{NS_EWS_TYPES}:FilterHtmlContent", item_shape[:filter_html_content]) if item_shape.has_key?(:filter_html_content)
            is.add("#{NS_EWS_TYPES}:ConvertHtmlCodePageToUTF8", item_shape[:convert_html_code_page_to_utf8]) if item_shape.has_key?(:convert_html_code_page_to_utf8)
            unless( item_shape[:additional_properties].nil? )
              unless( item_shape[:additional_properties][:field_uRI].nil? )
                is.add("#{NS_EWS_TYPES}:AdditionalProperties") do |addprops|
                  item_shape[:additional_properties][:field_uRI].each do |uri|
                    addprops.add("#{NS_EWS_TYPES}:FieldURI") { |furi| furi.set_attr('FieldURI', uri) }
                  end
                end
              end
            end
          end
        end

        def items!(node, items, type)
          node.add("#{NS_EWS_MESSAGES}:Items") do |i|
            if items.is_a? Hash
              method("#{type}_item!").call(i, items)
            else
              items.each do |item|
                method("#{type}_item!").call(i, item)
              end
            end
          end
        end

        # Creates a CalendarItem Element structure.  It matters to Exchange which order Items are added in
        # so it loops through an order Array to make sure things are added appropriately.
        # @param [Element] node The <Items> element that is the parent to all of the elements that will
        #   be created from the items param
        # @param [Hash] item The item or items that will be added to the element in the parameter node
        # @todo Make sure and watch this method for new Item elements when EWS versions change.
        def message_item!(node, item)
          order=[:mime_content,:item_id,:parent_folder_id,:item_class,:subject,:sensitivity,:body,:attachments,:date_time_received,
            :size,:categories,:importance,:in_reply_to,:is_submitted,:is_draft,:is_from_me,:is_resend,:is_unmodified,
            :internet_message_headers,:date_time_sent,:date_time_created,:response_objects,:reminder_due_by,:reminder_is_set,
            :reminder_minutes_before_start,:display_cc,:display_to,:has_attachments,:extended_property,:culture,:sender,
            :to_recipients,:cc_recipients,:bcc_recipients,:is_read_receipt_requested,:is_delivery_receipt_requested,
            :conversation_index,:conversation_topic,:from,:internet_message_id,:is_read,:is_response_requested,:references,
            :reply_to,:effective_rights,:received_by,:received_representing,:last_modified_name,:last_modified_time,
            :is_associated,:web_client_read_form_query_string,:web_client_edit_form_query_string,:conversation_id,:unique_body]

          node.add("#{NS_EWS_TYPES}:Message") do |msg|
            item!(msg, item, order)
          end
        end

        # Creates a CalendarItem Element structure.  It matters to Exchange which order Items are added in
        # so it loops through an order Array to make sure things are added appropriately.
        # @param [Element] node The <Items> element that is the parent to all of the elements that will
        #   be created from the items param
        # @param [Hash] item The item or items that will be added to the element in the parameter node
        # @todo Make sure and watch this method for new Item elements when EWS versions change.
        def calendar_item!(node, item)
          # For some reason MS thought it was a good idea to make order matter for Item creation.  This list is the current order
          # for Exchange 2003 and 2010
          order=[:mime_content,:item_id,:parent_folder_id,:item_class,:subject,:sensitivity,:body,:attachments,:date_time_received,:size,
            :categories,:in_reply_to,:is_submitted,:is_draft,:is_from_me,:is_resend,:is_unmodified,:internet_message_headers,
            :date_time_sent,:date_time_created,:response_objects,:reminder_due_by,:reminder_is_set,:reminder_minutes_before_start,
            :display_cc,:display_to,:has_attachments,:extended_property,:culture,:start,:end,:original_start,:is_all_day_event,
            :legacy_free_busy_status,:location,:when,:is_meeting,:is_cancelled,:is_recurring,:meeting_request_was_sent,
            :is_response_requested,:calendar_item_type,:my_response_type,:organizer,:required_attendees,:optional_attendees,
            :resources,:conflicting_meeting_count,:adjacent_meeting_count,:conflicting_meetings,:adjacent_meetings,:duration,:time_zone,
            :appointment_reply_time,:appointment_sequence_number,:appointment_state,:recurrence,:first_occurrence,:last_occurrence,
            :modified_occurrences,:deleted_occurrences,:meeting_time_zone,:start_time_zone,:end_time_zone,:conference_type,
            :allow_new_time_proposal,:is_online_meeting,:meeting_workspace_url,:net_show_url,:effective_rights,:last_modified_name,
            :last_modified_time,:is_associated,:web_client_read_form_query_string,:web_client_edit_form_query_string,:conversation_id,:unique_body]

          node.add("#{NS_EWS_TYPES}:CalendarItem") do |msg|
            item!(msg, item, order)
          end
        end
        
        # Creates a Contact Element structure.  It matters to Exchange which order Items are added in
        # so it loops through an order Array to make sure things are added appropriately.
        # @param [Element] node The <Items> element that is the parent to all of the elements that will
        #   be created from the items param
        # @param [Hash] item The item or items that will be added to the element in the parameter node
        # @todo Make sure and watch this method for new Item elements when EWS versions change.
        def contact_item!(node,item)
          order=[:mime_content,:item_id,:parent_folder_id,:item_class,:subject,:sensitivity,:body,:attachments,:date_time_received,:size,
            :categories,:importance,:in_reply_to,:is_submitted,:is_draft,:is_from_me,:is_resend,:is_unmodified, :internet_message_headers,
            :date_time_sent,:date_time_created,:response_objects,:reminder_due_by,:reminder_is_set,:reminder_minutes_before_start,
            :display_cc,:display_to,:has_attachments,:extended_property,:culture,:effective_rights,:last_modified_name,:last_modified_time,
            :is_associated,:web_client_read_form_query_string,:web_client_edit_form_query_string,:conversation_id,:unique_body,:file_as,
            :file_as_mapping,:display_name,:given_name,:initials,:middle_name,:nickname,:complete_name,:company_name,:email_addresses,
            :physical_addresses,:phone_numbers,:assistant_name,:birthday,:business_home_page,:children,:companies,:contact_source,
            :department,:generation,:im_addresses,:job_title,:manager,:mileage,:office_location,:postal_address_index,:profession,
            :spouse_name,:surname,:wedding_anniversary,:has_picture]

          node.add("#{NS_EWS_TYPES}:Contact") do |msg|
            item!(msg, item, order)
          end
        end
        
        # Creates a Task Element structure.  It matters to Exchange which order Items are added in
        # so it loops through an order Array to make sure things are added appropriately.
        # @param [Element] node The <Items> element that is the parent to all of the elements that will
        #   be created from the items param
        # @param [Hash] item The item or items that will be added to the element in the parameter node
        # @todo Make sure and watch this method for new Item elements when EWS versions change.
        def task_item!(node,item)
          order=[:mime_content,:item_id,:parent_folder_id,:item_class,:subject,:sensitivity,:body,:attachments,:date_time_received,
            :size,:categories,:in_reply_to,:is_submitted,:is_draft,:is_from_me,:is_resend,:is_unmodified,:internet_message_headers,
            :date_time_sent,:date_time_created,:response_objects,:reminder_due_by,:reminder_is_set,:reminder_minutes_before_start,
            :display_cc,:display_to,:has_attachments,:extended_property,:culture,:actual_work,:assigned_time,:billing_information,
            :change_count,:companies,:complete_date,:contacts,:delegation_state,:delegator,:due_date,:is_assignment_editable,
            :is_complete,:is_recurring,:is_team_task,:mileage,:owner,:percent_complete,:recurrence,:start_date,:status,
            :status_description,:total_work,:effective_rights,:last_modified_name,:last_modified_time,:is_associated,
            :web_client_read_form_query_string,:web_client_edit_form_query_string,:conversation_id,:unique_body]

          node.add("#{NS_EWS_TYPES}:Task") do |msg|
            item!(msg, item, order)
          end
        end


        # This is a convernience method used by the specific item types like
        # CalendarItem and Message to create item structures.  It is the shared
        # code between them.  
        # @param [Element] node The <*Item> element that is the parent to all of the elements that will
        #   be created from the elems param
        # @param [Hash, Array] item The subelements that will be created under node
        # @param [Array<Symbol] order The order that Exchange expects these elements to appear in
        #   the SOAP request.
        def item!(node, item, order)
          order.each do |id|
            if(item[id])
              if(item[id].is_a?(Hash))
                node.add("#{NS_EWS_TYPES}:#{id.to_s.camel_case}", item[id][:text]) do |it|
                  add_hierarchy!(it, item[id]) if item[id]
                end
              elsif(item[id].is_a?(Array))
                node.add("#{NS_EWS_TYPES}:#{id.to_s.camel_case}") do |it|
                  item[id].each do |ai|
                    add_hierarchy!(it, ai)
                  end
                end
              end
            end
          end
        end


        def event_types!(node, event_types)
          node.add("#{NS_EWS_TYPES}:EventTypes") do |ets|
            event_types.each do |event_type|
              ets.add("#{NS_EWS_TYPES}:EventType", event_type)
            end
          end
        end

        def subscription_id!(node, subscription_id)
          node.add("#{NS_EWS_MESSAGES}:SubscriptionId", subscription_id)
        end

        def watermark!(node, watermark)
          node.add("#{NS_EWS_MESSAGES}:Watermark", watermark)
        end

        def sync_state!(node, sync_state)
          node.add("#{NS_EWS_MESSAGES}:SyncState", sync_state)
        end

        def attachments!(node, files, items)
          # Order matters and ruby 1.8.x does not have ordered hashes.
          order=[:name, :content] 
          node.add("#{NS_EWS_MESSAGES}:Attachments") do |att|
            files.each do |f|
              att.add("#{NS_EWS_TYPES}:FileAttachment") do |fatt|
                item!(fatt, f, order)
              end
            end
          end
        end

        def attachment_ids!(node, attachment_ids)
          node.add("#{NS_EWS_MESSAGES}:AttachmentIds") do |att|
            attachment_ids.each do |id|
              add_hierarchy!(att, {:attachment_id => {:id => id}})
            end
          end
        end

        def attachment_shape!(node)
          node.add("#{NS_EWS_MESSAGES}:AttachmentShape")
        end

        # Add a hierarchy of elements from hash data
        # @example Hash to XML
        #   {:this => {:text =>'that'},'top' => {:id => '32fss', :text => 'TestText', :sub_elements => {'middle' => {:text => 'bottom'}}}}
        #   becomes...
        #   <this>that</this>
        #   <top Id='32fss'>
        #     <middle>bottom</middle>
        #   </top>
        def add_hierarchy!(node, e_hash, prefix = NS_EWS_TYPES)
          e_hash.each_pair do |k,v|
            if v.is_a? Hash
              if(k == :sub_elements)
                add_hierarchy!(node, v)
              else
                node.add("#{prefix}:#{k.to_s.camel_case}", v[:text]) do |n|
                  add_hierarchy!(n, v)
                end
              end
            elsif v.is_a? Array
              if(k == :sub_elements)
                v.each do |i|
                  add_hierarchy!(node, i)
                end
              else
                node.add("#{prefix}:#{k.to_s.camel_case}") do |n|
                  v.each do |i|
                    add_hierarchy!(n, i)
                  end
                end
              end
            else
              node.set_attr(k.to_s.camel_case, v) unless k == :text
            end
          end
        end

      end # EwsBuildHelpers
    end # SOAP
  end # EWS
end # Viewpoint
