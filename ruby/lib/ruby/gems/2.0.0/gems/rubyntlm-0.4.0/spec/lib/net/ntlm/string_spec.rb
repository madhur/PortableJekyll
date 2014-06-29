require 'spec_helper'

describe Net::NTLM::String do

  it_behaves_like 'a field', 'Foo', false

  let(:active) {
    Net::NTLM::String.new({
        :value  => 'Test',
        :active => true,
        :size   => 4
    })
  }

  let(:inactive) {
    Net::NTLM::String.new({
        :value  => 'Test',
        :active => false,
        :size   => 4
    })
  }

  context '#serialize' do
    it 'should return the value when active' do
      active.serialize.should == 'Test'
    end

    it 'should return an empty string when inactive' do
      inactive.serialize.should == ''
    end

    it 'should coerce non-string values into strings' do
      active.value = 15
      active.serialize.should == '15'
    end

    it 'should return empty string on a nil' do
      active.value = nil
      active.serialize.should == ''
    end
  end

  context '#value=' do
    it 'should set active to false if it empty' do
      active.value = ''
      active.active.should == false
    end

    it 'should adjust the size based on the value set' do
      active.size.should == 4
      active.value = 'Foobar'
      active.size.should == 6
    end
  end

  context '#parse' do
    it 'should read in a string of the proper size' do
      active.parse('tseT').should == 4
      active.value.should == 'tseT'
    end

    it 'should not read in a string that is too small' do
      active.parse('B').should == 0
      active.value.should == 'Test'
    end

    it 'should be able to read from an offset and only for the given size' do
      active.parse('FooBarBaz',3).should == 4
      active.value.should == 'BarB'
    end
  end
end