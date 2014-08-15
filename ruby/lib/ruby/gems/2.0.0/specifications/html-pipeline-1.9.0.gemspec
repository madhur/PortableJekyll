# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "html-pipeline"
  s.version = "1.9.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Ryan Tomayko", "Jerry Cheung"]
  s.date = "2014-07-07"
  s.description = "GitHub HTML processing filters and utilities"
  s.email = ["ryan@github.com", "jerry@github.com"]
  s.homepage = "https://github.com/jch/html-pipeline"
  s.licenses = ["MIT"]
  s.post_install_message = "-------------------------------------------------\nThank you for installing html-pipeline!\nYou must bundle Filter gem dependencies.\nSee html-pipeline README.md for more details.\nhttps://github.com/jch/html-pipeline#dependencies\n-------------------------------------------------\n"
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Helpers for processing content through a chain of filters"

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<nokogiri>, ["~> 1.4"])
      s.add_runtime_dependency(%q<activesupport>, [">= 2"])
    else
      s.add_dependency(%q<nokogiri>, ["~> 1.4"])
      s.add_dependency(%q<activesupport>, [">= 2"])
    end
  else
    s.add_dependency(%q<nokogiri>, ["~> 1.4"])
    s.add_dependency(%q<activesupport>, [">= 2"])
  end
end
