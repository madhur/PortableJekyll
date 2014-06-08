# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "curb"
  s.version = "0.7.18"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Ross Bamford", "Todd A. Fisher"]
  s.date = "2012-01-16"
  s.description = "Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for the libcurl(3), a fully-featured client-side URL transfer library. cURL and libcurl live at http://curl.haxx.se/"
  s.email = "todd.fisher@gmail.com"
  s.extensions = ["ext/extconf.rb"]
  s.extra_rdoc_files = ["LICENSE", "README"]
  s.files = ["LICENSE", "README", "ext/extconf.rb"]
  s.homepage = "http://curb.rubyforge.org/"
  s.rdoc_options = ["--main", "README"]
  s.require_paths = ["lib", "ext"]
  s.rubyforge_project = "curb"
  s.rubygems_version = "2.0.3"
  s.summary = "Ruby libcurl bindings"
end
