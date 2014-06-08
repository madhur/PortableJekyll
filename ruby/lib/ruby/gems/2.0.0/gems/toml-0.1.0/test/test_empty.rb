require 'rubygems'
require 'bundler/setup'

require 'toml'
require 'minitest/autorun'

class TestEmpty < MiniTest::Test

  def setup
    filepath = File.join(File.dirname(__FILE__), "empty.toml")
    @doc = TOML::Parser.new(File.read(filepath)).parsed
  end

  def test_empty
    assert_equal ({}), @doc, "Empty document parsed incorrectly"
  end

end
