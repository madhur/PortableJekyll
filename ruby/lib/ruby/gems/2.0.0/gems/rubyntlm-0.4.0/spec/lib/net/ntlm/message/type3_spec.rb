require 'spec_helper'

describe Net::NTLM::Message::Type3 do

  fields = [
      { :name => :sign, :class => Net::NTLM::String, :value => Net::NTLM::SSP_SIGN, :active => true },
      { :name => :type, :class => Net::NTLM::Int32LE, :value => 3, :active => true },
      { :name => :flag, :class => Net::NTLM::Int64LE, :value =>  0, :active => false },
      { :name => :lm_response, :class => Net::NTLM::SecurityBuffer, :value => '', :active => true },
      { :name => :ntlm_response, :class => Net::NTLM::SecurityBuffer, :value =>  '', :active => true },
      { :name => :domain, :class => Net::NTLM::SecurityBuffer, :value =>  '', :active => true },
      { :name => :user, :class => Net::NTLM::SecurityBuffer, :value =>  '', :active => true },
      { :name => :workstation, :class => Net::NTLM::SecurityBuffer, :value =>  '', :active => true },
      { :name => :session_key, :class => Net::NTLM::SecurityBuffer, :value =>  '', :active => false },
  ]
  flags = []
  it_behaves_like 'a fieldset', fields
  it_behaves_like 'a message', flags

end