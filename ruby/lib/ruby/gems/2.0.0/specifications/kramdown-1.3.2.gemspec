# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "kramdown"
  s.version = "1.3.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Thomas Leitner"]
  s.date = "2014-02-16"
  s.description = "kramdown is yet-another-markdown-parser but fast, pure Ruby,\nusing a strict syntax definition and supporting several common extensions.\n"
  s.email = "t_leitner@gmx.at"
  s.executables = ["kramdown"]
  s.files = ["bin/kramdown"]
  s.homepage = "http://kramdown.gettalong.org"
  s.licenses = ["MIT"]
  s.rdoc_options = ["--main", "lib/kramdown/document.rb"]
  s.require_paths = ["lib"]
  s.rubyforge_project = "kramdown"
  s.rubygems_version = "2.0.3"
  s.summary = "kramdown is a fast, pure-Ruby Markdown-superset converter."

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<minitest>, ["~> 5.0"])
      s.add_development_dependency(%q<coderay>, ["~> 1.0.0"])
      s.add_development_dependency(%q<stringex>, ["~> 1.5.1"])
      s.add_development_dependency(%q<prawn>, ["~> 0.13"])
    else
      s.add_dependency(%q<minitest>, ["~> 5.0"])
      s.add_dependency(%q<coderay>, ["~> 1.0.0"])
      s.add_dependency(%q<stringex>, ["~> 1.5.1"])
      s.add_dependency(%q<prawn>, ["~> 0.13"])
    end
  else
    s.add_dependency(%q<minitest>, ["~> 5.0"])
    s.add_dependency(%q<coderay>, ["~> 1.0.0"])
    s.add_dependency(%q<stringex>, ["~> 1.5.1"])
    s.add_dependency(%q<prawn>, ["~> 0.13"])
  end
end
