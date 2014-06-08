require 'spec_helper'

describe(Jekyll::Converters::Sass) do
  let(:site) do
    Jekyll::Site.new(site_configuration)
  end
  let(:sass_content) do
    <<-SASS
$font-stack: Helvetica, sans-serif
body
  font-family: $font-stack
  font-color: fuschia
SASS
  end
  let(:scss_content) do
    <<-SCSS
$font-stack: Helvetica, sans-serif;
body {
  font-family: $font-stack;
  font-color: fuschia;
}
SCSS
  end
  let(:css_output) do
    <<-CSS
body {\n  font-family: Helvetica, sans-serif;\n  font-color: fuschia; }
CSS
  end

  def converter(overrides = {})
    Jekyll::Converters::Sass.new(site_configuration({"sass" => overrides}))
  end

  context "matching file extensions" do
    it "matches .scss files" do
      expect(converter.matches(".scss")).to be_true
    end

    it "matches .sass files" do
      expect(converter.matches(".sass")).to be_true
    end
  end

  context "determining the output file extension" do
    it "always outputs the .css file extension" do
      expect(converter.output_ext(".always-css")).to eql(".css")
    end
  end

  context "when building configurations" do
    it "not allow caching in safe mode" do
      verter = converter
      verter.instance_variable_get(:@config)["safe"] = true
      expect(verter.sass_configs[:cache]).to be_false
    end

    it "allow caching in unsafe mode" do
      expect(converter.sass_configs[:cache]).to be_true
    end

    it "set the load paths to the _sass dir relative to site source" do
      expect(converter.sass_configs[:load_paths]).to eql([source_dir("_sass")])
    end

    it "allow the user to specify a different sass dir" do
      expect(converter({"sass_dir" => "_scss"}).sass_configs[:load_paths]).to eql([source_dir("_scss")])
    end

    it "set syntax :scss when SCSS content" do
      expect(converter.sass_configs(scss_content)[:syntax]).to eql(:scss)
    end

    it "set syntax :sass when Sass content" do
      expect(converter.sass_configs(sass_content)[:syntax]).to eql(:sass)
    end

    it "default to :sass syntax when content is empty" do
      expect(converter.sass_configs[:syntax]).to eql(:sass)
    end

    it "not allow sass_dirs outside of site source" do
      expect(
        converter({"sass_dir" => "/etc/passwd"}).sass_dir_relative_to_site_source
      ).to eql(source_dir("etc/passwd"))
    end

    it "override user-set syntax based on content" do
      expect(
        converter({"syntax" => :scss}).sass_configs(sass_content)[:syntax]
      ).to eql(:sass)
    end
  end

  context "converting sass" do
    it "produces CSS" do
      expect(converter.convert(sass_content)).to eql(css_output)
    end
  end

  context "converting SCSS" do
    it "produces CSS" do
      expect(converter.convert(scss_content)).to eql(css_output)
    end
  end

  context "importing partials" do
    let(:test_css_file) { dest_dir("css/main.css") }
    before(:each) { site.process }

    it "outputs the CSS file" do
      expect(File.exist?(test_css_file)).to be_true
    end

    it "imports SCSS partial" do
      expect(File.read(test_css_file)).to eql(".half {\n  width: 50%; }\n")
    end
  end
end
