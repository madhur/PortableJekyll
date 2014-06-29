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

require 'soap/handsoap/builders/ews_build_helpers.rb'
module Viewpoint
  module EWS
    module SOAP

      # This class includes all the build helpers and also contains some root
      # level methods to help code reuse.  The CreateItem operation is an example
      # of this because the different item types share a lot but have a few subtle
      # differences.
      class EwsBuilder
        include EwsBuildHelpers

        def initialize(node, opts, &block)
          @node, @opts = node, opts
          instance_eval(&block) if block_given?
        end

        # @see ExchangeWebService#subscribe
        def pull_subscription_request!(folder_ids, event_types, timeout)
          @node.add("#{NS_EWS_MESSAGES}:PullSubscriptionRequest") do |ps|
            folder_ids!(ps, folder_ids, nil, "#{NS_EWS_TYPES}:FolderIds")
            event_types!(ps, event_types)
            ps.add("#{NS_EWS_TYPES}:Timeout", timeout)
          end
        end

        # @see ExchangeWebService#subscribe
        def push_subscription_request!(folder_ids, event_types, url, watermark=nil, status_frequency=5)
          @node.add("#{NS_EWS_MESSAGES}:PushSubscriptionRequest") do |ps|
            folder_ids!(ps, folder_ids, nil, "#{NS_EWS_TYPES}:FolderIds")
            event_types!(ps, event_types)
            ps.add("#{NS_EWS_TYPES}:Watermark", watermark) unless watermark.nil?
            ps.add("#{NS_EWS_TYPES}:StatusFrequency", status_frequency)
            ps.add("#{NS_EWS_TYPES}:URL", url)
          end
        end

        # @param [String] type The type of items in the items array message/calendar
        # @todo Fix max_changes_returned to be more flexible
        def create_item!(folder_id, items, message_disposition, send_invites, type)
          @node.set_attr('MessageDisposition', message_disposition) if message_disposition
          @node.set_attr('SendMeetingInvitations', send_invites) if send_invites

          saved_item_folder_id!(@node, folder_id) unless folder_id.nil?
          items!(@node, items, type)
        end

        def add_delegate!(owner, delegate, permissions)
          d_user = {
            :user_id => {:primary_smtp_address => {:text => delegate}},
            :delegate_permissions => permissions
          }
          
          mailbox!(@node, {:email_address => {:text => owner}})
          delegate_users!(@node, [d_user])
        end

        def remove_delegate!(owner, delegate)
          mailbox!(@node, {:email_address => {:text => owner}})
          @node.add("#{NS_EWS_MESSAGES}:UserIds") do |uids|
            user_id!(uids, {:user_id => {:primary_smtp_address => {:text => delegate}}})
          end
        end

        # Build the request XML for GetUserAvailability.
        # @see http://msdn.microsoft.com/en-us/library/aa494212.aspx
        def get_user_availability!(email_address, start_time, end_time)
          add_time_zone_info
          @node.add("#{NS_EWS_MESSAGES}:MailboxDataArray") do |mda|
            mda.add("#{NS_EWS_TYPES}:MailboxData") do |mbdata|
              mbdata.add("#{NS_EWS_TYPES}:Email") do |email|
                email.add("#{NS_EWS_TYPES}:Name")
                email.add("#{NS_EWS_TYPES}:Address", email_address)
              end
              mbdata.add("#{NS_EWS_TYPES}:AttendeeType", 'Required')
            end
          end
          @node.add("#{NS_EWS_TYPES}:FreeBusyViewOptions") do |fbvo|
            fbvo.add("#{NS_EWS_TYPES}:TimeWindow") do |tw|
              tw.add("#{NS_EWS_TYPES}:StartTime", start_time)
              tw.add("#{NS_EWS_TYPES}:EndTime", end_time)
            end
            fbvo.add("#{NS_EWS_TYPES}:MergedFreeBusyIntervalInMinutes", 10)
            fbvo.add("#{NS_EWS_TYPES}:RequestedView", 'MergedOnly')
          end
        end

        # This is forthcoming in Exchange 2010.  It will replace much of the Restriction
        # based code.
        # @param [Array] An array of query strings
        # @see http://msdn.microsoft.com/en-us/library/ee693615.aspx
        def query_strings!(query_strings)
          query_strings.each do |qs|
            @node.add("#{NS_EWS_MESSAGES}:QueryString", qs)
          end
        end

        private

        # Add a description of the time zone to the request XML.
        # The timezone information defaults to US/Pacific time.
        def add_time_zone_info(offset_hours_std = -8, offset_hours_dst = -7)
          base_bias = (-1 * offset_hours_std * 60).to_s
          standard_bias = '0'
          savings_bias = (offset_hours_std - offset_hours_dst).to_s
          @node.add("#{NS_EWS_TYPES}:TimeZone") do |tz|
            tz.add("#{NS_EWS_TYPES}:Bias", base_bias) # e.g. '480'
            tz.add("#{NS_EWS_TYPES}:StandardTime") do |stime|
              stime.add("#{NS_EWS_TYPES}:Bias", standard_bias) # e.g. '0'
              stime.add("#{NS_EWS_TYPES}:Time", '02:00:00')
              stime.add("#{NS_EWS_TYPES}:DayOrder", '1')
              stime.add("#{NS_EWS_TYPES}:Month", '11')
              stime.add("#{NS_EWS_TYPES}:DayOfWeek", 'Sunday')
            end
            tz.add("#{NS_EWS_TYPES}:DaylightTime") do |dtime|
              dtime.add("#{NS_EWS_TYPES}:Bias", savings_bias) # e.g. '-60'
              dtime.add("#{NS_EWS_TYPES}:Time", '02:00:00')
              dtime.add("#{NS_EWS_TYPES}:DayOrder", '2')
              dtime.add("#{NS_EWS_TYPES}:Month", '3')
              dtime.add("#{NS_EWS_TYPES}:DayOfWeek", 'Sunday')
            end
          end
        end

      end # EwsBuilder
    end # SOAP
  end # EWS
end # Viewpoint
