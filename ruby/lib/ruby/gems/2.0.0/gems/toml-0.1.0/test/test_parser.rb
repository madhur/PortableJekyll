
require 'rubygems'
require 'bundler/setup'

require 'toml'
require 'minitest/autorun'

class TestParser < MiniTest::Test
  def setup
    filepath = File.join(File.dirname(__FILE__), 'spec.toml')
    @doc = TOML::Parser.new(File.read(filepath)).parsed
  end

  def test_string
    assert_equal "string\n\t\"string", @doc["strings"]["string"]
    assert_equal "", @doc["strings"]["empty"]
  end

  def test_integer
    assert_equal 42, @doc["ints"]["simple"]
  end

  def test_negative_integer
    assert_equal -42, @doc["ints"]["negative"]
  end

  def test_float
    assert_equal 3.14159, @doc["floats"]["pi"]
  end

  def test_negative_float
    assert_equal -10.0, @doc["floats"]["negative"]
  end

  def test_datetime
    assert_equal DateTime.iso8601("1979-05-27T07:32:00Z"), @doc["datetimes"]["simple"]
  end

  def test_booleans
    assert_equal true, @doc["true"]
    assert_equal false, @doc["false"]
  end

  def test_simple_array
    assert_equal [1, 2, 3], @doc["arrays"]["simple"]
  end

  def test_nested_array
    assert_equal [[1, 2], [3]], @doc["arrays"]["nested"]
  end

  def test_empty_array
    assert_equal [], @doc["arrays"]["empty"]
  end

  def test_empty_multiline_array
    assert_equal [], @doc["arrays"]["multiline_empty"]
  end

  def test_empty_multiline_array_with_comment
    assert_equal [], @doc["arrays"]["multiline_empty_comment"]
  end

  def test_multiline_arrays
    assert_equal ["lines", "are", "super", "cool", "lol", "amirite"], @doc["arrays"]["multi"]
  end

  def test_multiline_array
    assert_equal @doc["arrays"]["multiline"], [1, 2, 3]
  end

  def test_multiline_array_with_trailing_comma
    assert_equal @doc["arrays"]["multiline_trailing_comma"], [1, 2, 3]
  end

  def test_multiline_array_with_comments
    assert_equal @doc["arrays"]["multiline_comments"], [1, 2, 3]
  end

  def test_simple_keygroup
    assert_equal "test", @doc["e"]["f"]
  end

  def test_nested_keygroup
    assert_equal "test", @doc["a"]["b"]["c"]["d"]
  end

  def test_inline_comment
    assert_equal "a line", @doc["comments"]["on"]
  end
end
