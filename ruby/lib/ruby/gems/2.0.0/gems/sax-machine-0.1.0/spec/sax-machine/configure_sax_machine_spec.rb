require 'spec_helper'

class A

  SAXMachine.configure(A) do |c|
    c.element :title
  end

end

class B < A

  SAXMachine.configure(B) do |c|
    c.element :b
  end

end

class C < B

  SAXMachine.configure(C) do |c|
    c.element :c
  end

end

describe "SAXMachine configure" do
  before do
    xml = "<top><title>Test</title><b>Matched!</b><c>And Again</c></top>"
    @a = A.new
    @a.parse xml
    @b = B.new
    @b.parse xml
    @c = C.new
    @c.parse xml
  end
  it { @a.should be_a(A) }
  it { @a.should_not be_a(B) }
  it { @a.should be_a(SAXMachine) }
  it { @a.title.should == "Test" }
  it { @b.should be_a(A) }
  it { @b.should be_a(B) }
  it { @b.should be_a(SAXMachine) }
  it { @b.title.should == "Test" }
  it { @b.b.should == "Matched!" }
  it { @c.should be_a(A) }
  it { @c.should be_a(B) }
  it { @c.should be_a(C) }
  it { @c.should be_a(SAXMachine) }
  it { @c.title.should == "Test" }
  it { @c.b.should == "Matched!" }
  it { @c.c.should == "And Again" }
end
