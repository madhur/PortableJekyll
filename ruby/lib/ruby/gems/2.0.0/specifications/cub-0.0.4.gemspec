# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "cub"
  s.version = "0.0.4"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["kano4"]
  s.date = "2012-08-26"
  s.description = "Cub fetches stock information."
  s.email = ["shinji.warp@gmail.com"]
  s.homepage = "https://github.com/kano4/cub"
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Fetch stock information"

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<nokogiri>, [">= 0"])
      s.add_development_dependency(%q<rspec>, [">= 0"])
    else
      s.add_dependency(%q<nokogiri>, [">= 0"])
      s.add_dependency(%q<rspec>, [">= 0"])
    end
  else
    s.add_dependency(%q<nokogiri>, [">= 0"])
    s.add_dependency(%q<rspec>, [">= 0"])
  end
end
