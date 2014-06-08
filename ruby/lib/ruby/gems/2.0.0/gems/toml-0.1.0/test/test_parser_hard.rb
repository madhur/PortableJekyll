require 'rubygems'
require 'bundler/setup'
require 'toml'
require 'minitest/autorun'

class TestParserHardExample < MiniTest::Test
  def setup
    filepath = File.join(File.dirname(__FILE__), 'hard_example.toml')
    # @doc = TOML::Parser.new(File.read(filepath)).parsed
    @doc = TOML.load_file(filepath)
  end

  def test_the_test_string
    assert_equal @doc["the"]["test_string"], "You'll hate me after this - #"
  end
end
