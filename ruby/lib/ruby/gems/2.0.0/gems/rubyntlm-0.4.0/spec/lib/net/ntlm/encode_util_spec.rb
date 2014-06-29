require 'spec_helper'

describe Net::NTLM::EncodeUtil do

  context '#encode_utf16le' do
    it 'should convert an ASCII string to UTF' do
      Net::NTLM::EncodeUtil.encode_utf16le('Test').should == "T\x00e\x00s\x00t\x00"
    end
  end

  context '#decode_utf16le' do
    it 'should convert a UTF string to ASCII' do
      Net::NTLM::EncodeUtil.decode_utf16le("T\x00e\x00s\x00t\x00").should == 'Test'
    end
  end
end