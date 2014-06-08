# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "highline"
  s.version = "1.6.19"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["James Edward Gray II"]
  s.date = "2013-05-13"
  s.description = "A high-level IO library that provides validation, type conversion, and more for\ncommand-line interfaces. HighLine also includes a complete menu system that can\ncrank out anything from simple list selection to complete shells with just\nminutes of work.\n"
  s.email = "james@graysoftinc.com"
  s.extra_rdoc_files = ["README.rdoc", "INSTALL", "TODO", "CHANGELOG", "LICENSE"]
  s.files = ["README.rdoc", "INSTALL", "TODO", "CHANGELOG", "LICENSE"]
  s.homepage = "http://highline.rubyforge.org"
  s.licenses = ["Ruby"]
  s.rdoc_options = ["--title", "HighLine Documentation", "--main", "README"]
  s.require_paths = ["lib"]
  s.rubyforge_project = "highline"
  s.rubygems_version = "2.0.3"
  s.summary = "HighLine is a high-level command-line IO library."
end
