HERE = File.dirname(__FILE__) unless defined?(HERE)
ROOT = File.join(HERE, "..") unless defined?(ROOT)

$LOAD_PATH << File.join(ROOT, "lib")
$LOAD_PATH << File.join(HERE, "support")

require "yaml"
if ENV["YAMLER"] && defined?(YAML::ENGINE)
  YAML::ENGINE.yamler = ENV["YAMLER"]
  puts "Running specs in Ruby #{RUBY_VERSION} with '#{YAML::ENGINE.yamler}' YAML engine."
end

if defined?(JRUBY_VERSION) && ENV["JRUBY_OPTS"]
  puts "Running JRuby in #{RUBY_VERSION} mode."
end

# Caching references to these methods before loading safe_yaml in order to test
# that they aren't touched unless you actually require safe_yaml (see yaml_spec.rb).
ORIGINAL_YAML_LOAD      = YAML.method(:load)
ORIGINAL_YAML_LOAD_FILE = YAML.method(:load_file)

require "safe_yaml/load"
require "ostruct"
require "hashie"
require "heredoc_unindent"

require File.join(HERE, "resolver_specs")
