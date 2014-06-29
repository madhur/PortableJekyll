# coding: utf-8

Gem::Specification.new do |spec|
  spec.name          = "jekyll-watch"
  spec.version       = "1.0.0"
  spec.authors       = ["Parker Moore"]
  spec.email         = ["parkrmoore@gmail.com"]
  spec.summary       = %q{Rebuild your Jekyll site when a file changes with the `--watch` switch.}
  spec.homepage      = "https://github.com/jekyll/jekyll-watch"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0")
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "listen", "~> 2.7"

  require 'rbconfig'
  if RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/
    spec.add_runtime_dependency "wdm", "~> 0.1.0"
  end


  spec.add_development_dependency "bundler", "~> 1.6"
  spec.add_development_dependency "rake"
end
