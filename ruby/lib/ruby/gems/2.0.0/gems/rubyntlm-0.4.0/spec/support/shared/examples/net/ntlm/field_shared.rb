shared_examples_for 'a field' do  | value, active|

  subject do
    described_class.new({
        :value  => value,
        :active => active
    })
  end

  it { should respond_to :active }
  it { should respond_to :value }
  it { should respond_to :size }
  it { should respond_to :parse }
  it { should respond_to :serialize }


  it 'should set the value from initialize options' do
    subject.value.should == value
  end

  it 'should set active from initialize options' do
    subject.active.should == active
  end

end