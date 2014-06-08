$:.unshift File.join(File.dirname(__FILE__), *%w{ .. lib })

require 'rspec/autorun'
require 'colorator'

RSpec.configure do |config|
  config.treat_symbols_as_metadata_keys_with_true_values = true
  config.order = 'random'
end
