# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'jekyll-coffeescript'

Gem::Specification.new do |spec|
  spec.name          = "jekyll-coffeescript"
  spec.version       = Jekyll::Coffeescript::VERSION
  spec.authors       = ["Parker Moore"]
  spec.email         = ["parkrmoore@gmail.com"]
  spec.summary       = %q{A CoffeeScript converter for Jekyll.}
  spec.homepage      = "https://github.com/jekyll/jekyll-coffeescript"
  spec.license       = "MIT"

  spec.files         = `git ls-files`.split($/)
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "coffee-script", "~> 2.2"

  spec.add_development_dependency "jekyll", "~> 1.0"
  spec.add_development_dependency "bundler", "~> 1.5"
  spec.add_development_dependency "rake"
  spec.add_development_dependency "rspec"
end
