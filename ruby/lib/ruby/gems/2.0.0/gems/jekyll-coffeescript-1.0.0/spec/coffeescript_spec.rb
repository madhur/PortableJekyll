require 'spec_helper'

describe(Jekyll::Converters::CoffeeScript) do
  let(:configuration) { Jekyll::Configuration::DEFAULTS }
  let(:converter) do
    Jekyll::Converters::CoffeeScript.new(configuration)
  end
  let(:coffeescript_content) do
    <<-COFFEESCRIPT
# Functions:
square = (x) -> x * x

# Arrays:
list = [1, 2, 3, 4, 5]

# Objects:
math =
  root:   Math.sqrt
  square: square
  cube:   (x) -> x * square x
COFFEESCRIPT
  end
  let(:js_content) do
    <<-JS
(function() {
  var list, math, square;

  square = function(x) {
    return x * x;
  };

  list = [1, 2, 3, 4, 5];

  math = {
    root: Math.sqrt,
    square: square,
    cube: function(x) {
      return x * square(x);
    }
  };

}).call(this);
JS
  end

  context "matching file extensions" do
    it "matches .coffee files" do
      expect(converter.matches(".coffee")).to be_true
    end
  end

  context "determining the output file extension" do
    it "always outputs the .js file extension" do
      expect(converter.output_ext(".always-js-dont-matter")).to eql(".js")
    end
  end

  context "converting CoffeeScript" do
    it "produces CSS" do
      expect(converter.convert(coffeescript_content)).to eql(js_content)
    end
  end

end
