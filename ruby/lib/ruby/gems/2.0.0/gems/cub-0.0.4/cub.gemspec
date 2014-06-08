# -*- encoding: utf-8 -*-
require File.expand_path('../lib/cub/version', __FILE__)

Gem::Specification.new do |gem|
  gem.authors       = ["kano4"]
  gem.email         = ["shinji.warp@gmail.com"]
  gem.description   = %q{Cub fetches stock information.}
  gem.summary       = %q{Fetch stock information}
  gem.homepage      = "https://github.com/kano4/cub"

  gem.files         = `git ls-files`.split($\)
  gem.executables   = gem.files.grep(%r{^bin/}).map{ |f| File.basename(f) }
  gem.test_files    = gem.files.grep(%r{^(test|spec|features)/})
  gem.name          = "cub"
  gem.require_paths = ["lib"]
  gem.version       = Cub::VERSION

  gem.add_dependency "nokogiri"
  gem.add_development_dependency "rspec"
end
