# -*- encoding: utf-8 -*-
require File.expand_path('../lib/sax-machine/version', __FILE__)

Gem::Specification.new do |s|
  s.name    = 'sax-machine'
  s.version = SAXMachine::VERSION

  s.authors   = ["Paul Dix", "Julien Kirch", "Ezekiel Templin"]
  s.email     = %q{paul@pauldix.net}
  s.homepage  = %q{http://github.com/pauldix/sax-machine}

  s.summary   = %q{Declarative SAX Parsing with Nokogiri}

  s.license   = %q{MIT}

  s.files         = `git ls-files`.split("\n")
  s.test_files    = `git ls-files -- {test,spec,features}/*`.split("\n")
  s.require_paths = ["lib"]

  s.platform = Gem::Platform::RUBY

  s.add_dependency 'nokogiri', "~> 1.6.0"
  s.add_development_dependency "rspec", "~> 2.13.0"
end
