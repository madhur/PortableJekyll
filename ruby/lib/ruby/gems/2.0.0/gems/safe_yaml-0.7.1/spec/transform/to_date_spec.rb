require File.join(File.dirname(__FILE__), "..", "spec_helper")

describe SafeYAML::Transform::ToDate do
  it "returns true when the value matches a valid Date" do
    subject.transform?("2013-01-01")[0].should == true
  end

  it "returns false when the value does not match a valid Date" do
    subject.transform?("foobar").should be_false
  end

  it "returns false when the value does not end with a Date" do
    subject.transform?("2013-01-01\nNOT A DATE").should be_false
  end

  it "returns false when the value does not begin with a Date" do
    subject.transform?("NOT A DATE\n2013-01-01").should be_false
  end
end
