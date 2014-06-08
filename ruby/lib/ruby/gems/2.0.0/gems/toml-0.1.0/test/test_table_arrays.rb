require 'rubygems'
require 'bundler/setup'
require 'toml'
require 'minitest/autorun'

class TestParserTableArrays < MiniTest::Test
  def setup
    doc = '
[[fruit]]
  name = "apple"

  [fruit.physical]
    color = "red"
    shape = "round"

  [[fruit.variety]]
    name = "red delicious"

  [[fruit.variety]]
    name = "granny smith"

[[fruit]]
  name = "banana"

  [[fruit.variety]]
    name = "plantain"
    '
    @doc = TOML.load(doc)
    #require 'pp'
    #PP.pp @doc
  end

  def test_doc
    assert_equal @doc, {
      "fruit"=>
        [{"name"=>"apple",
          "physical"=>{"color"=>"red", "shape"=>"round"},
          "variety"=>[{"name"=>"red delicious"}, {"name"=>"granny smith"}]},
         {"name"=>"banana", "variety"=>[{"name"=>"plantain"}]}]
    }
  end
end
