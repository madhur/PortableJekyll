HERE = File.dirname(__FILE__) unless defined?(HERE)
ROOT = File.join(HERE, "..") unless defined?(ROOT)

$LOAD_PATH << File.join(ROOT, "lib")
$LOAD_PATH << File.join(HERE, "support")

if ENV["YAMLER"] && defined?(YAML::ENGINE)
  require "yaml"
  YAML::ENGINE.yamler = ENV["YAMLER"]
  puts "Running specs in Ruby #{RUBY_VERSION} with '#{YAML::ENGINE.yamler}' YAML engine."
end

require "safe_yaml"
require "heredoc_unindent"

require File.join(HERE, "shared_specs")
