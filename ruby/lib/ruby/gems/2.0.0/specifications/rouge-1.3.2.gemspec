# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "rouge"
  s.version = "1.3.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Jay Adkisson"]
  s.date = "2014-01-13"
  s.description = "Rouge aims to a be a simple, easy-to-extend drop-in replacement for pygments."
  s.email = ["jjmadkisson@gmail.com"]
  s.executables = ["rougify"]
  s.files = ["bin/rougify"]
  s.homepage = "http://github.com/jayferd/rouge"
  s.licenses = ["MIT (see LICENSE file)"]
  s.require_paths = ["lib"]
  s.rubyforge_project = "rouge"
  s.rubygems_version = "2.0.3"
  s.summary = "A pure-ruby colorizer based on pygments"
end
