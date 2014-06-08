require File.join(File.dirname(__FILE__), "..", "spec_helper")

describe SafeYAML::Transform::ToInteger do
  it "returns true when the value matches a valid Integer" do
    subject.transform?("10")[0].should be_true
  end

  it "returns false when the value does not match a valid Integer" do
    subject.transform?("foobar").should be_false
  end

  it "returns false when the value spans multiple lines" do
    subject.transform?("10\nNOT AN INTEGER").should be_false
  end
end
