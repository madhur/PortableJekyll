require 'spec_helper'

describe(Jekyll::Gist::GistTag) do
  let(:doc) { doc_with_content(content) }
  let(:content)  { "{% gist #{gist} %}" }
  let(:output) do
    doc.content = content
    doc.output  = Jekyll::Renderer.new(doc.site, doc).run
  end


  context "valid gist" do
    context "with user prefix" do
      let(:gist) { "mattr-/24081a1d93d2898ecf0f" }

      it "produces the correct script tag" do
        expect(output).to match(/<script src="https:\/\/gist.github.com\/#{gist}.js">\s<\/script>/)
      end
    end

    context "without user prefix" do
      let(:gist) { "28949e1d5ee2273f9fd3" }

      it "produces the correct script tag" do
        expect(output).to match(/<script src="https:\/\/gist.github.com\/#{gist}.js">\s<\/script>/)
      end
    end

    context "classic Gist id style" do
      let(:gist) { "1234321" }

      it "produces the correct script tag" do
        expect(output).to match(/<script src="https:\/\/gist.github.com\/#{gist}.js">\s<\/script>/)
      end
    end

    context "with file specified" do
      let(:gist)     { "mattr-/24081a1d93d2898ecf0f" }
      let(:filename) { "myfile.ext" }
      let(:content)  { "{% gist #{gist} #{filename} %}" }

      it "produces the correct script tag" do
        expect(output).to match(/<script src="https:\/\/gist.github.com\/#{gist}.js\?file=#{filename}">\s<\/script>/)
      end
    end
  end


  context "invalid gist" do

    context "no gist id present" do
      let(:gist) { "" }

      it "raises an error" do
        expect(->{ output }).to raise_error
      end
    end

  end

end
