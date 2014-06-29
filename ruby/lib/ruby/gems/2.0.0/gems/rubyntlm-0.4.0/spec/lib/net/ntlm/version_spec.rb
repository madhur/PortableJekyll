require 'spec_helper'

describe Net::NTLM::VERSION do

  it 'should contain an integer value for Major Version' do
    Net::NTLM::VERSION::MAJOR.should be_an Integer
  end

  it 'should contain an integer value for Minor Version' do
    Net::NTLM::VERSION::MINOR.should be_an Integer
  end

  it 'should contain an integer value for Patch Version' do
    Net::NTLM::VERSION::TINY.should be_an Integer
  end

  it 'should contain an aggregate version string' do
    string = [
        Net::NTLM::VERSION::MAJOR,
        Net::NTLM::VERSION::MINOR,
        Net::NTLM::VERSION::TINY
    ].join('.')
    Net::NTLM::VERSION::STRING.should be_a String
    Net::NTLM::VERSION::STRING.should == string
  end
end