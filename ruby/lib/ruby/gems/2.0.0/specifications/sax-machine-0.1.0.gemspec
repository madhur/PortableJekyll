# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "sax-machine"
  s.version = "0.1.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Paul Dix", "Julien Kirch"]
  s.date = "2011-09-30"
  s.email = "paul@pauldix.net"
  s.homepage = "http://github.com/pauldix/sax-machine"
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Declarative SAX Parsing with Nokogiri"

  if s.respond_to? :specification_version then
    s.specification_version = 2

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<nokogiri>, ["> 0.0.0"])
    else
      s.add_dependency(%q<nokogiri>, ["> 0.0.0"])
    end
  else
    s.add_dependency(%q<nokogiri>, ["> 0.0.0"])
  end
end
