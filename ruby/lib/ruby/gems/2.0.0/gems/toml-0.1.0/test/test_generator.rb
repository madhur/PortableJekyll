
require 'rubygems'
require 'bundler/setup'

require 'toml'
require 'minitest/autorun'

class TestGenerator < MiniTest::Test
  def setup
    @doc = {
      "integer" => 1,
      "float" => 3.14159,
      "true" => true,
      "false" => false,
      "string" => "hi",
      "array" => [[1], [2], [3]],
      "key" => {
        "group" => {
          "value" => "lol"
        }
      },
      "date" => DateTime.now
    }
    
  end
  
  def test_generator
    doc = @doc.clone
    body = TOML::Generator.new(doc).body

    doc_parsed = TOML::Parser.new(body).parsed
    
    # Extracting dates since Ruby's DateTime equality testing sucks.
    original_date = doc.delete "date"
    parsed_date = doc_parsed.delete "date"
    
    assert_equal doc, doc_parsed
    assert_equal original_date.to_time.to_s, parsed_date.to_time.to_s
  end
end
