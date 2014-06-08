# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "classifier"
  s.version = "1.3.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Lucas Carlson"]
  s.autorequire = "classifier"
  s.date = "2010-07-06"
  s.description = "   A general classifier module to allow Bayesian and other types of classifications.\n"
  s.email = "lucas@rufy.com"
  s.homepage = "http://classifier.rufy.com/"
  s.require_paths = ["lib"]
  s.requirements = ["A porter-stemmer module to split word stems."]
  s.rubygems_version = "2.0.3"
  s.summary = "A general classifier module to allow Bayesian and other types of classifications."

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<fast-stemmer>, [">= 1.0.0"])
    else
      s.add_dependency(%q<fast-stemmer>, [">= 1.0.0"])
    end
  else
    s.add_dependency(%q<fast-stemmer>, [">= 1.0.0"])
  end
end
