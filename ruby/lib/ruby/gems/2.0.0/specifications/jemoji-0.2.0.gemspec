# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "jemoji"
  s.version = "0.2.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["GitHub, Inc."]
  s.date = "2014-05-07"
  s.description = ""
  s.email = "support@github.com"
  s.homepage = "https://github.com/jekyll/jemoji"
  s.licenses = ["MIT"]
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "GitHub-flavored emoji plugin for Jekyll"

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<jekyll>, ["~> 2.0"])
      s.add_runtime_dependency(%q<html-pipeline>, ["~> 1.5.0"])
      s.add_runtime_dependency(%q<gemoji>, ["~> 1.5.0"])
      s.add_development_dependency(%q<rake>, [">= 0"])
      s.add_development_dependency(%q<rdoc>, [">= 0"])
      s.add_development_dependency(%q<shoulda>, [">= 0"])
      s.add_development_dependency(%q<minitest>, [">= 0"])
    else
      s.add_dependency(%q<jekyll>, ["~> 2.0"])
      s.add_dependency(%q<html-pipeline>, ["~> 1.5.0"])
      s.add_dependency(%q<gemoji>, ["~> 1.5.0"])
      s.add_dependency(%q<rake>, [">= 0"])
      s.add_dependency(%q<rdoc>, [">= 0"])
      s.add_dependency(%q<shoulda>, [">= 0"])
      s.add_dependency(%q<minitest>, [">= 0"])
    end
  else
    s.add_dependency(%q<jekyll>, ["~> 2.0"])
    s.add_dependency(%q<html-pipeline>, ["~> 1.5.0"])
    s.add_dependency(%q<gemoji>, ["~> 1.5.0"])
    s.add_dependency(%q<rake>, [">= 0"])
    s.add_dependency(%q<rdoc>, [">= 0"])
    s.add_dependency(%q<shoulda>, [">= 0"])
    s.add_dependency(%q<minitest>, [">= 0"])
  end
end
