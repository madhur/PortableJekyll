# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "toml"
  s.version = "0.1.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Jeremy McAnally", "Dirk Gadsden"]
  s.date = "2013-12-05"
  s.description = "Parse your TOML, seriously."
  s.email = "jeremy@github.com"
  s.extra_rdoc_files = ["README.md", "LICENSE"]
  s.files = ["README.md", "LICENSE"]
  s.homepage = "http://github.com/jm/toml"
  s.rdoc_options = ["--charset=UTF-8"]
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Parse your TOML."

  if s.respond_to? :specification_version then
    s.specification_version = 2

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<parslet>, ["~> 1.5.0"])
    else
      s.add_dependency(%q<parslet>, ["~> 1.5.0"])
    end
  else
    s.add_dependency(%q<parslet>, ["~> 1.5.0"])
  end
end
