# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "maruku"
  s.version = "0.6.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Andrea Censi", "Nathan Weizenbaum"]
  s.autorequire = "maruku"
  s.date = "2012-09-16"
  s.description = "Maruku is a Markdown interpreter in Ruby.\n\tIt features native export to HTML and PDF (via Latex). The\n\toutput is really beautiful!\n\t"
  s.email = "ben@benhollis.net"
  s.executables = ["maruku", "marutex"]
  s.files = ["bin/maruku", "bin/marutex"]
  s.homepage = "http://github.com/bhollis/maruku"
  s.licenses = ["GPL-2"]
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Maruku is a Markdown-superset interpreter written in Ruby."

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<syntax>, [">= 1.0.0"])
      s.add_development_dependency(%q<syntax>, ["~> 1.0.0"])
      s.add_development_dependency(%q<rake>, ["~> 0.9.2"])
    else
      s.add_dependency(%q<syntax>, [">= 1.0.0"])
      s.add_dependency(%q<syntax>, ["~> 1.0.0"])
      s.add_dependency(%q<rake>, ["~> 0.9.2"])
    end
  else
    s.add_dependency(%q<syntax>, [">= 1.0.0"])
    s.add_dependency(%q<syntax>, ["~> 1.0.0"])
    s.add_dependency(%q<rake>, ["~> 0.9.2"])
  end
end
