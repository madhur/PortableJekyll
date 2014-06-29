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
    class MeetingRequest < Item


      private

      def init_methods
        super()
        define_str_var :conversation_index, :conversation_topic, :internet_message_id, :references
        define_mbox_users :to_recipients, :cc_recipients, :bcc_recipients, :reply_to, :required_attendees, :optional_attendees
        define_mbox_user :from, :sender, :received_by, :received_representing, :organizer
        define_bool_var :is_read, :is_read_receipt_requested, :is_response_requested, :is_delivery_receipt_requested, :is_draft, :is_from_me
        define_bool_var :is_all_day_event, :is_cancelled, :is_delegated, :is_meeting, :is_out_of_date, :is_recurring, :is_resend
        define_bool_var :is_submitted, :is_unmodified, :allow_new_time_proposal
        define_int_var :adjacent_meeting_count, :appointment_sequence_number, :appointment_state, :conflicting_meeting_count
        define_datetime_var :start, :end
      end
    end # MeetingRequest
  end # EWS
end # Viewpoint
