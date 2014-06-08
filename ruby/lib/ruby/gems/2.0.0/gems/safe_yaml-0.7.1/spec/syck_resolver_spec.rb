require File.join(File.dirname(__FILE__), "spec_helper")

if SafeYAML::YAML_ENGINE == "syck"
  require "safe_yaml/syck_resolver"

  describe SafeYAML::SyckResolver do
    let(:resolver) { SafeYAML::SyckResolver.new }
    let(:result) { @result }

    def parse(yaml)
      tree = YAML.parse(yaml.unindent)
      @result = resolver.resolve_node(tree)
    end

    include SharedSpecs
  end
end
