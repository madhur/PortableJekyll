module Net
  module NTLM
    class Message

      # @private false
      class Type1 < Message

        string          :sign,         {:size => 8, :value => SSP_SIGN}
        int32LE         :type,         {:value => 1}
        int32LE         :flag,         {:value => DEFAULT_FLAGS[:TYPE1] }
        security_buffer :domain,       {:value => ""}
        security_buffer :workstation,  {:value => Socket.gethostname }
        string          :padding,      {:size => 0, :value => "", :active => false }

        class << Type1
          # Parses a Type 1 Message
          # @param [String] str A string containing Type 1 data
          # @return [Type1] The parsed Type 1 message
          def parse(str)
            t = new
            t.parse(str)
            t
          end
        end

        # @!visibility private
        def parse(str)
          super(str)
          enable(:domain) if has_flag?(:DOMAIN_SUPPLIED)
          enable(:workstation) if has_flag?(:WORKSTATION_SUPPLIED)
          super(str)
          if ( (len = data_edge - head_size) > 0)
            self.padding = "\0" * len
            super(str)
          end
        end
      end

    end
  end
end


