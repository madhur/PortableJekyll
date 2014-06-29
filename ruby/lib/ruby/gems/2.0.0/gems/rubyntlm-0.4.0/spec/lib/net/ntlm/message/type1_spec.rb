require 'spec_helper'

describe Net::NTLM::Message::Type1 do
  fields = [
      { :name => :sign, :class => Net::NTLM::String, :value => Net::NTLM::SSP_SIGN, :active => true },
      { :name => :type, :class => Net::NTLM::Int32LE, :value => 1, :active => true },
      { :name => :flag, :class => Net::NTLM::Int32LE, :value =>  Net::NTLM::DEFAULT_FLAGS[:TYPE1], :active => true },
      { :name => :domain, :class => Net::NTLM::SecurityBuffer, :value => '', :active => true },
      { :name => :workstation, :class => Net::NTLM::SecurityBuffer, :value =>  Socket.gethostname, :active => true },
      { :name => :padding, :class => Net::NTLM::String, :value => '', :active => false },
  ]
  flags = [
      :UNICODE,
      :OEM,
      :REQUEST_TARGET,
      :NTLM,
      :ALWAYS_SIGN,
      :NTLM2_KEY
  ]
  it_behaves_like 'a fieldset', fields
  it_behaves_like 'a message', flags

  let(:type1_packet) {"TlRMTVNTUAABAAAAB4IIAAAAAAAgAAAAAAAAACAAAAA="}

  it 'should deserialize' do
    t1 =  Net::NTLM::Message.decode64(type1_packet)
    t1.class.should == Net::NTLM::Message::Type1
    t1.domain.should == ''
    t1.flag.should == 557575
    t1.padding.should == ''
    t1.sign.should  == "NTLMSSP\0"
    t1.type.should == 1
    t1.workstation.should == ''
  end

  it 'should serialize' do
    t1 = Net::NTLM::Message::Type1.new
    t1.workstation = ''
    t1.encode64.should == type1_packet
  end

end