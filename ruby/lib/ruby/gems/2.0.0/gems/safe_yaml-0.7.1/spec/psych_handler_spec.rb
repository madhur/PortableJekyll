require File.join(File.dirname(__FILE__), "spec_helper")

if SafeYAML::YAML_ENGINE == "psych"
  require "safe_yaml/psych_handler"

  describe SafeYAML::PsychHandler do
    let(:handler) { SafeYAML::PsychHandler.new }
    let(:parser) { Psych::Parser.new(handler) }
    let(:result) { handler.result }

    def parse(yaml)
      parser.parse(yaml.unindent)
    end

    include SharedSpecs
  end
end
