require File.join(File.dirname(__FILE__), "..", "spec_helper")

describe SafeYAML::Transform::ToDate do
  it "returns true when the value matches a valid Date" do
    subject.transform?("2013-01-01").should == [true, Date.parse("2013-01-01")]
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

  it "correctly parses the remaining formats of the YAML spec" do
    equivalent_values = [
      "2001-12-15T02:59:43.1Z", # canonical
      "2001-12-14t21:59:43.10-05:00", # iso8601
      "2001-12-14 21:59:43.10 -5", # space separated
      "2001-12-15 2:59:43.10" # no time zone (Z)
    ]

    equivalent_values.each do |value|
      success, result = subject.transform?(value)
      success.should be_true
      result.should == Time.utc(2001, 12, 15, 2, 59, 43, 100000)
    end
  end

  it "converts times to the local timezone" do
    success, result = subject.transform?("2012-12-01 10:33:45 +11:00")
    success.should be_true
    result.should == Time.utc(2012, 11, 30, 23, 33, 45)
    result.gmt_offset.should == Time.now.gmt_offset
  end

  it "returns strings for invalid dates" do
    subject.transform?("0000-00-00").should == [true, "0000-00-00"]
    subject.transform?("2013-13-01").should == [true, "2013-13-01"]
    subject.transform?("2014-01-32").should == [true, "2014-01-32"]
  end

  it "returns strings for invalid date/times" do
    subject.transform?("0000-00-00 00:00:00 -0000").should == [true, "0000-00-00 00:00:00 -0000"]
    subject.transform?("2013-13-01 21:59:43 -05:00").should == [true, "2013-13-01 21:59:43 -05:00"]
    subject.transform?("2013-01-32 21:59:43 -05:00").should == [true, "2013-01-32 21:59:43 -05:00"]
    subject.transform?("2013-01-30 25:59:43 -05:00").should == [true, "2013-01-30 25:59:43 -05:00"]
    subject.transform?("2013-01-30 21:69:43 -05:00").should == [true, "2013-01-30 21:69:43 -05:00"]

    # Interesting. It seems that in some older Ruby versions, the below actually parses successfully
    # w/ DateTime.parse; but it fails w/ YAML.load. Whom to follow???

    # subject.transform?("2013-01-30 21:59:63 -05:00").should == [true, "2013-01-30 21:59:63 -05:00"]
  end
end
