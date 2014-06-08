# See https://github.com/dtao/safe_yaml/issues/47

require File.join(File.dirname(__FILE__), "spec_helper")

describe YAML do
  context "when you've only required safe_yaml/load", :libraries => true do
    it "YAML.load doesn't get monkey patched" do
      YAML.method(:load).should == ORIGINAL_YAML_LOAD
    end

    it "YAML.load_file doesn't get monkey patched" do
      YAML.method(:load_file).should == ORIGINAL_YAML_LOAD_FILE
    end
  end
end
