require 'spec_helper'

describe(Jekyll::Watcher) do
  let(:base_opts) do
    {
      'source' => source_dir,
      'destination' => dest_dir
    }
  end
  let(:options) { base_opts }
  subject { described_class }

  context "#build_listener" do
    let(:listener) { subject.build_listener(options) }

    it "returns a Listen::Listener" do
      expect(listener).to be_a(Listen::Listener)
    end

    it "ignores the config and site by default" do
      expect(listener.options[:ignore]).to eql([/_config\.yml/, /_site/])
    end

    it "defaults to no force_polling" do
      expect(listener.options[:force_polling]).to be(nil)
    end

    context "with force_polling turned on" do
      let(:options)  { base_opts.merge('force_polling' => true) }
      let(:listener) { subject.build_listener(options) }

      it "respects the custom value of force_polling" do
        expect(listener.options[:force_polling]).to be(true)
      end
    end
  end

  context "#listen_ignore_paths" do
    let(:ignored) { subject.listen_ignore_paths(options) }

    it "ignores config.yml and _site by default" do
      expect(ignored).to eql([/_config\.yml/, /_site/])
    end

    context "with something excluded" do
      let(:options) { base_opts.merge('exclude' => ['README.md', 'LICENSE']) }

      it "ignores the excluded files" do
        expect(ignored).to include(/README\.md/)
        expect(ignored).to include(/LICENSE/)
      end
    end
  end
end
