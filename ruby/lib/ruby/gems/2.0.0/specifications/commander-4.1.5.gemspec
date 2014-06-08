# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "commander"
  s.version = "4.1.5"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["TJ Holowaychuk", "Gabriel Gilder"]
  s.date = "2013-08-11"
  s.description = "The complete solution for Ruby command-line executables. Commander bridges the gap between other terminal related libraries you know and love (OptionParser, HighLine), while providing many new features, and an elegant API."
  s.email = ["ggilder@tractionco.com"]
  s.executables = ["commander"]
  s.files = ["bin/commander"]
  s.homepage = "http://visionmedia.github.com/commander"
  s.require_paths = ["lib"]
  s.rubyforge_project = "commander"
  s.rubygems_version = "2.0.3"
  s.summary = "The complete solution for Ruby command-line executables"

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<highline>, ["~> 1.6.11"])
      s.add_development_dependency(%q<rspec>, ["~> 2"])
      s.add_development_dependency(%q<rake>, [">= 0"])
      s.add_development_dependency(%q<simplecov>, [">= 0"])
    else
      s.add_dependency(%q<highline>, ["~> 1.6.11"])
      s.add_dependency(%q<rspec>, ["~> 2"])
      s.add_dependency(%q<rake>, [">= 0"])
      s.add_dependency(%q<simplecov>, [">= 0"])
    end
  else
    s.add_dependency(%q<highline>, ["~> 1.6.11"])
    s.add_dependency(%q<rspec>, ["~> 2"])
    s.add_dependency(%q<rake>, [">= 0"])
    s.add_dependency(%q<simplecov>, [">= 0"])
  end
end
