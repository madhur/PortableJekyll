# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "fast-stemmer"
  s.version = "1.0.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Roman Shterenzon"]
  s.date = "2013-02-06"
  s.description = "Fast Porter stemmer based on a C version of algorithm"
  s.email = "romanbsd@yahoo.com"
  s.extensions = ["ext/extconf.rb"]
  s.extra_rdoc_files = ["LICENSE", "README"]
  s.files = ["LICENSE", "README", "ext/extconf.rb"]
  s.homepage = "http://github.com/romanbsd/fast-stemmer"
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Fast Porter stemmer based on a C version of algorithm"
end
