# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "viewpoint"
  s.version = "0.1.27"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Dan Wanek"]
  s.date = "2012-07-03"
  s.description = "A Ruby client access library for Microsoft Exchange Web Services (EWS).  Examples can be found here: http://distributed-frostbite.blogspot.com"
  s.email = "dan.wanek@gmail.com"
  s.extra_rdoc_files = ["README"]
  s.files = ["README"]
  s.homepage = "http://github.com/zenchild/Viewpoint"
  s.rdoc_options = ["-x", "test/", "-x", "examples/"]
  s.require_paths = ["lib"]
  s.required_ruby_version = Gem::Requirement.new(">= 1.8.7")
  s.rubygems_version = "2.0.3"
  s.summary = "A Ruby client access library for Microsoft Exchange Web Services (EWS)"

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<handsoap>, [">= 0"])
      s.add_runtime_dependency(%q<nokogiri>, [">= 0"])
      s.add_runtime_dependency(%q<httpclient>, [">= 0"])
      s.add_runtime_dependency(%q<rubyntlm>, [">= 0"])
      s.add_runtime_dependency(%q<icalendar>, [">= 1.1.5"])
      s.add_runtime_dependency(%q<mail>, [">= 2.2.5"])
    else
      s.add_dependency(%q<handsoap>, [">= 0"])
      s.add_dependency(%q<nokogiri>, [">= 0"])
      s.add_dependency(%q<httpclient>, [">= 0"])
      s.add_dependency(%q<rubyntlm>, [">= 0"])
      s.add_dependency(%q<icalendar>, [">= 1.1.5"])
      s.add_dependency(%q<mail>, [">= 2.2.5"])
    end
  else
    s.add_dependency(%q<handsoap>, [">= 0"])
    s.add_dependency(%q<nokogiri>, [">= 0"])
    s.add_dependency(%q<httpclient>, [">= 0"])
    s.add_dependency(%q<rubyntlm>, [">= 0"])
    s.add_dependency(%q<icalendar>, [">= 1.1.5"])
    s.add_dependency(%q<mail>, [">= 2.2.5"])
  end
end
