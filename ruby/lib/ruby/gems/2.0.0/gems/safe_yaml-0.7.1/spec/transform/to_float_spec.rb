require File.join(File.dirname(__FILE__), "..", "spec_helper")

describe SafeYAML::Transform::ToFloat do
  it "returns true when the value matches a valid Float" do
    subject.transform?("20.00").should be_true
  end

  it "returns false when the value does not match a valid Float" do
    subject.transform?("foobar").should be_false
  end

  it "returns false when the value spans multiple lines" do
    subject.transform?("20.00\nNOT A FLOAT").should be_false
  end
end
