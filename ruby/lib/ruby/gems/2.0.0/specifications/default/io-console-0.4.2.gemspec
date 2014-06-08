# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "io-console"
  s.version = "0.4.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Nobu Nakada"]
  s.date = "2013-02-24"
  s.description = "add console capabilities to IO instances."
  s.email = "nobu@ruby-lang.org"
  s.extensions = ["extconf.rb"]
  s.files = ["io/console/size.rb", "io/console.so", "extconf.rb"]
  s.homepage = "http://www.ruby-lang.org"
  s.licenses = ["ruby"]
  s.require_paths = ["."]
  s.rubygems_version = "2.0.3"
  s.summary = "Console interface"
end
