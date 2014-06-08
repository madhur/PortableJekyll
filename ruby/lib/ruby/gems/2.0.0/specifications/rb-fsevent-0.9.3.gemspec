# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "rb-fsevent"
  s.version = "0.9.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Thibaud Guillaume-Gentil", "Travis Tilley"]
  s.date = "2012-12-31"
  s.description = "FSEvents API with Signals catching (without RubyCocoa)"
  s.email = ["thibaud@thibaud.me", "ttilley@gmail.com"]
  s.homepage = "http://rubygems.org/gems/rb-fsevent"
  s.require_paths = ["lib"]
  s.rubyforge_project = "rb-fsevent"
  s.rubygems_version = "2.0.3"
  s.summary = "Very simple & usable FSEvents API"

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<bundler>, ["~> 1.0"])
      s.add_development_dependency(%q<rspec>, ["~> 2.11"])
      s.add_development_dependency(%q<guard-rspec>, ["~> 1.2"])
    else
      s.add_dependency(%q<bundler>, ["~> 1.0"])
      s.add_dependency(%q<rspec>, ["~> 2.11"])
      s.add_dependency(%q<guard-rspec>, ["~> 1.2"])
    end
  else
    s.add_dependency(%q<bundler>, ["~> 1.0"])
    s.add_dependency(%q<rspec>, ["~> 2.11"])
    s.add_dependency(%q<guard-rspec>, ["~> 1.2"])
  end
end
