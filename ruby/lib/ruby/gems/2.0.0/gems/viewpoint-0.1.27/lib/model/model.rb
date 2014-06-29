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
    # This is the base model Module for shared code among all Model classes.
    # @attr_reader [Array] :ews_methods The EWS methods created for this Model.
    module Model

      # These are convenience methods to quickly create instance methods for
      # the various Model types when passed a Hash from the SOAP parser.
      # These functions depend on each model type saving the passed Hash
      # in an instance variable called @ews_item.

      attr_reader :ews_methods, :ews_methods_undef

      def initialize
        # Defined EWS methods
        @ews_methods = []
        # Undefined EWS methods
        @ews_methods_undef = []
      end

      protected

      # Define a method that returns a string.  The vars are the keys in the 
      # hash that contain a :text key.  In the original SOAP packet this would
      # look something like this:
      # @param [Array<Symbol,Hash>] *vars the symbols to map to methods.  If the
      #   last item is a hash it will be used to map methods names.  For instance
      #   UID comes through like this :u_i_d so we can map it like so {:u_i_d => :uid}
      # @example
      #   <method_name>
      #      This is the text
      #   </method_name>
      def define_str_var(*vars)
        map = ( vars.last.is_a?(Hash) ? vars.pop : {})
        vars.each do |var|
          mname = ( map.has_key?(var) ? map[var] : var )
          if(@ews_item[var])
            @ews_methods << mname
            self.instance_eval <<-EOF
            def #{mname}
              @ews_item[:#{var}][:text]
            end
            EOF
          else
            @ews_methods_undef << var
          end
          if(Item::FIELD_URIS.has_key?(var.to_sym) && Item::FIELD_URIS[var.to_sym][:writable])
            self.instance_eval <<-EOF
            def #{mname}=(newtext)
              @ews_item[:#{var}] = {} unless @ews_item[:#{var}]
              @ews_item[:#{var}][:text] = newtext
              @updates[:#{var}] = @ews_item[:#{var}]
            end
            EOF
          end
        end
      end

      # This is similar to the #define_str_var method except of the text value
      # is from an XML attribute in the original SOAP so the text won't be pointed
      # to by :text.  In the orignal SOAP it may have looked like this:
      # @example
      #   <node my_method='this is the text'/>
      #   so you would specify this...
      #   define_attr_str_var :node, :my_method
      def define_attr_str_var(parent, *vars)
        return unless @ews_item[parent]
        vars.each do |var|
          @ews_methods << var
          if(@ews_item[parent][var].is_a?(Hash) && @ews_item[parent][var].has_key?(:text))
            self.instance_eval <<-EOF
            def #{var}
              @ews_item[:#{parent}][:#{var}][:text]
            end
            EOF
          elsif(@ews_item[parent][var])
            self.instance_eval <<-EOF
            def #{var}
              @ews_item[:#{parent}][:#{var}]
            end
            EOF
          else
            @ews_methods_undef << var
          end
        end
      end


      def define_int_var(*vars)
        vars.each do |var|
          if(@ews_item[var])
            @ews_methods << var
            self.instance_eval <<-EOF
            def #{var}
              @ews_item[:#{var}][:text].to_i
            end
            EOF
          else
            @ews_methods_undef << var
          end
          if(Item::FIELD_URIS.has_key?(var.to_sym) && Item::FIELD_URIS[var.to_sym][:writable])
            self.instance_eval <<-EOF
            def #{var}=(newint)
              @ews_item[:#{var}] = {} unless @ews_item[:#{var}]
              @ews_item[:#{var}][:text] = newint.to_s
              @updates[:#{var}] = @ews_item[:#{var}]
            end
            EOF
          end
        end
      end

      def define_bool_var(*vars)
        vars.each do |var|
          if(@ews_item[var])
            @ews_methods << "#{var}?".to_sym
            self.instance_eval <<-EOF
            def #{var}?
              (@ews_item[:#{var}][:text] == 'true') ? true : false
            end
            EOF
          else
            @ews_methods_undef << "#{var}?".to_sym
          end
          if(Item::FIELD_URIS.has_key?(var.to_sym) && Item::FIELD_URIS[var.to_sym][:writable])
            self.instance_eval <<-EOF
            def #{var}=(newbool)
              raise EwsError, "Value not boolean for method #{var}=" unless(newbool.is_a?(TrueClass) || newbool.is_a?(FalseClass))
              @ews_item[:#{var}] = {} unless @ews_item[:#{var}]
              @ews_item[:#{var}][:text] = newbool.to_s
              @updates[:#{var}] = @ews_item[:#{var}]
            end
          EOF
          end
        end
      end

      def define_datetime_var(*vars)
        vars.each do |var|
          if(@ews_item[var])
            @ews_methods << var
            self.instance_eval <<-EOF
            def #{var}
              DateTime.parse(@ews_item[:#{var}][:text])
            end
            EOF
          else
            @ews_methods_undef << var
          end
          if(Item::FIELD_URIS.has_key?(var.to_sym) && Item::FIELD_URIS[var.to_sym][:writable])
            self.instance_eval <<-EOF
            def #{var}=(newdate)
              @ews_item[:#{var}] = {} unless @ews_item[:#{var}]
              @ews_item[:#{var}][:text] = newdate.to_s
              @updates[:#{var}] = @ews_item[:#{var}]
            end
            EOF
          end
        end
      end

      def define_mbox_users(*vars)
        vars.each do |var|
          if(@ews_item[var])
            @ews_methods << var
            self.instance_eval <<-EOF
            def #{var}
              return @#{var} if defined?(@#{var})
              deepen! if !@ews_item[:#{var}]
              if( (@ews_item[:#{var}][:mailbox]).is_a?(Hash) )
                @#{var} = [MailboxUser.new(@ews_item[:#{var}][:mailbox])]
              elsif( (@ews_item[:#{var}][:mailbox]).is_a?(Array) )
                @#{var} = []
                @ews_item[:#{var}][:mailbox].each do |i|
                  @#{var} << MailboxUser.new(i)
                end
              else
                raise EwsError, "Bad value for mailbox: " + @ews_item[:#{var}][:mailbox]
              end
              @#{var}
            end
            EOF
          else
            @ews_methods_undef << var
          end
        end
      end


      def define_mbox_user(*vars)
        vars.each do |var|
          if(@ews_item[var])
            @ews_methods << var
            self.instance_eval <<-EOF
            def #{var}
              deepen! if !@ews_item[:#{var}]
              @#{var} ||= MailboxUser.new(@ews_item[:#{var}][:mailbox])
            end
            EOF
          else
            @ews_methods_undef << var
          end
        end
      end
      

      # Define meeting attendees
      # @param [String] *attendee_types the type of attendee we are defining :required_attendees, :optional_attendees
      def define_attendees(*attendee_types)
        attendee_types.each do |attendee_type|
          if(@ews_item.has_key?(attendee_type))
            @ews_methods << attendee_type
            self.instance_eval <<-EOF
            def #{attendee_type}
              return @#{attendee_type} if(defined?(@#{attendee_type}) && !@#{attendee_type}.nil?)
              if( (@ews_item[:#{attendee_type}][:attendee]).is_a?(Hash) )
                @#{attendee_type} = [Attendee.new(@ews_item[:#{attendee_type}][:attendee])]
              elsif( (@ews_item[:#{attendee_type}][:attendee]).is_a?(Array) )
                @#{attendee_type} = []
                @ews_item[:#{attendee_type}][:attendee].each do |i|
                  @#{attendee_type} << Attendee.new(i)
                end
              else
                raise EwsError, "Bad value for mailbox: " + @ews_item[:#{attendee_type}][:attendee]
              end
              @#{attendee_type}
            end
            EOF
          else
            @ews_methods_undef << attendee_type
          end
        end
      end

      # After a delete is called on an object this method will clear
      # out all of the defined EWS methods so they can't be called on the
      # instantiated object.
      def clear_object!
        @ews_methods.each do |m|
          self.instance_variables.each do |iv|
            self.instance_variable_set("#{iv}",nil)
          end
        end
      end

    end # Model
  end # EWS
end # Viewpoint
