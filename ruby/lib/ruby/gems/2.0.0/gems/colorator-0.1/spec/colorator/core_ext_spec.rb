require 'spec_helper'

describe String do
  let(:string) { "i am a test string, y'know?" }

  it "contains all the methods from Colorator::ANSI_COLORS" do
    Colorator::ANSI_COLORS.keys.each do |color|
      string.methods.should include(color)
    end
  end

  it "colors the text properly" do
    Colorator::ANSI_COLORS.each do |color, code|
      string.send(color.to_sym).should include(code.to_s)
      string.send(color.to_sym).should eq("\e[#{code}m#{string}\e[0m")
    end
  end
end