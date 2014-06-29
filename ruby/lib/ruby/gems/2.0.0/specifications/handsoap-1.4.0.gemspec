# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "handsoap"
  s.version = "1.4.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Troels Knak-Nielsen", "Jimmi Westerberg"]
  s.date = "2013-11-06"
  s.description = "Handsoap is a library for creating SOAP clients in Ruby"
  s.email = ["troelskn@gmail.com", "frontend@unwire.dk"]
  s.extra_rdoc_files = ["README.markdown"]
  s.files = ["README.markdown"]
  s.homepage = "http://github.com/unwire/handsoap"
  s.require_paths = ["lib"]
  s.requirements = ["You need to install either \"curb\" or \"httpclient\", using one of:\n    gem install curb\n    gem install httpclient", "It is recommended that you install either \"nokogiri\" or \"libxml-ruby\""]
  s.rubygems_version = "2.0.3"
  s.summary = "Handsoap is a library for creating SOAP clients in Ruby"
end
