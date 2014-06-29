module Net
  module NTLM
    class Message

      # @private false
      class Type3 < Message

        string          :sign,          {:size => 8, :value => SSP_SIGN}
        int32LE         :type,          {:value => 3}
        security_buffer :lm_response,   {:value => ""}
        security_buffer :ntlm_response, {:value => ""}
        security_buffer :domain,        {:value => ""}
        security_buffer :user,          {:value => ""}
        security_buffer :workstation,   {:value => ""}
        security_buffer :session_key,   {:value => "", :active => false }
        int64LE         :flag,          {:value => 0, :active => false }

        class << Type3
          # Parse a Type 3 packet
          # @param [String] str A string containing Type 3 data
          # @return [Type2]
          def parse(str)
            t = new
            t.parse(str)
            t
          end

          # Builds a Type 3 packet
          # @note All options must be properly encoded with either unicode or oem encoding
          # @return [Type3]
          # @option arg [String] :lm_response The LM hash
          # @option arg [String] :ntlm_response The NTLM hash
          # @option arg [String] :domain The domain to authenticate to
          # @option arg [String] :workstation The name of the calling workstation
          # @option arg [String] :session_key The session key
          # @option arg [Integer] :flag Flags for the packet
          def create(arg, opt ={})
            t = new
            t.lm_response = arg[:lm_response]
            t.ntlm_response = arg[:ntlm_response]
            t.domain = arg[:domain]
            t.user = arg[:user]

            if arg[:workstation]
              t.workstation = arg[:workstation]
            end

            if arg[:session_key]
              t.enable(:session_key)
              t.session_key = arg[session_key]
            end

            if arg[:flag]
              t.enable(:session_key)
              t.enable(:flag)
              t.flag = arg[:flag]
            end
            t
          end
        end
      end


    end
  end
end


