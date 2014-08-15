require 'spec_helper'

describe(Jekyll::Converters::Sass) do
  let(:site) do
    Jekyll::Site.new(site_configuration)
  end
  let(:content) do
    <<-SASS
// tl;dr some sass
$font-stack: Helvetica, sans-serif
body
  font-family: $font-stack
  font-color: fuschia
SASS
  end
  let(:css_output) do
    <<-CSS
body {\n  font-family: Helvetica, sans-serif;\n  font-color: fuschia; }
CSS
  end

  def compressed(content)
    content.gsub(/\s+/, '').gsub(/;}/, '}') + "\n"
  end

  def converter(overrides = {})
    Jekyll::Converters::Sass.new(site_configuration({"sass" => overrides}))
  end

  context "matching file extensions" do
    it "does not match .scss files" do
      expect(converter.matches(".scss")).to be_falsey
    end

    it "matches .sass files" do
      expect(converter.matches(".sass")).to be_truthy
    end
  end

  context "converting sass" do
    it "produces CSS" do
      expect(converter.convert(content)).to eql(compressed(css_output))
    end
  end

end
