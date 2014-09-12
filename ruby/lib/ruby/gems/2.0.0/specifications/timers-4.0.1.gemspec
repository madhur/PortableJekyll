# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "timers"
  s.version = "4.0.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Tony Arcieri"]
  s.date = "2014-09-10"
  s.description = "Pure Ruby one-shot and periodic timers"
  s.email = ["tony.arcieri@gmail.com"]
  s.homepage = "https://github.com/celluloid/timers"
  s.licenses = ["MIT"]
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Schedule procs to run after a certain time, or at periodic intervals, using any API that accepts a timeout"

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<hitimes>, [">= 0"])
      s.add_development_dependency(%q<rake>, [">= 0"])
      s.add_development_dependency(%q<rspec>, ["~> 3.0.0"])
    else
      s.add_dependency(%q<hitimes>, [">= 0"])
      s.add_dependency(%q<rake>, [">= 0"])
      s.add_dependency(%q<rspec>, ["~> 3.0.0"])
    end
  else
    s.add_dependency(%q<hitimes>, [">= 0"])
    s.add_dependency(%q<rake>, [">= 0"])
    s.add_dependency(%q<rspec>, ["~> 3.0.0"])
  end
end
