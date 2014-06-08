# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "feedzirra"
  s.version = "0.1.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Paul Dix", "Julien Kirch"]
  s.date = "2011-09-30"
  s.description = "A feed fetching and parsing library that treats the internet like Godzilla treats Japan: it dominates and eats all."
  s.email = "feedzirra@googlegroups.com"
  s.homepage = "http://github.com/pauldix/feedzirra"
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "A feed fetching and parsing library"

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<nokogiri>, [">= 1.4.4"])
      s.add_runtime_dependency(%q<sax-machine>, ["~> 0.1.0"])
      s.add_runtime_dependency(%q<curb>, ["~> 0.7.15"])
      s.add_runtime_dependency(%q<builder>, [">= 2.1.2"])
      s.add_runtime_dependency(%q<activesupport>, ["~> 3.1.1"])
      s.add_runtime_dependency(%q<loofah>, ["~> 1.2.0"])
      s.add_runtime_dependency(%q<rdoc>, ["~> 3.8"])
      s.add_runtime_dependency(%q<rake>, [">= 0.8.7"])
      s.add_runtime_dependency(%q<i18n>, [">= 0.5.0"])
      s.add_development_dependency(%q<rspec>, ["~> 2.6.0"])
    else
      s.add_dependency(%q<nokogiri>, [">= 1.4.4"])
      s.add_dependency(%q<sax-machine>, ["~> 0.1.0"])
      s.add_dependency(%q<curb>, ["~> 0.7.15"])
      s.add_dependency(%q<builder>, [">= 2.1.2"])
      s.add_dependency(%q<activesupport>, ["~> 3.1.1"])
      s.add_dependency(%q<loofah>, ["~> 1.2.0"])
      s.add_dependency(%q<rdoc>, ["~> 3.8"])
      s.add_dependency(%q<rake>, [">= 0.8.7"])
      s.add_dependency(%q<i18n>, [">= 0.5.0"])
      s.add_dependency(%q<rspec>, ["~> 2.6.0"])
    end
  else
    s.add_dependency(%q<nokogiri>, [">= 1.4.4"])
    s.add_dependency(%q<sax-machine>, ["~> 0.1.0"])
    s.add_dependency(%q<curb>, ["~> 0.7.15"])
    s.add_dependency(%q<builder>, [">= 2.1.2"])
    s.add_dependency(%q<activesupport>, ["~> 3.1.1"])
    s.add_dependency(%q<loofah>, ["~> 1.2.0"])
    s.add_dependency(%q<rdoc>, ["~> 3.8"])
    s.add_dependency(%q<rake>, [">= 0.8.7"])
    s.add_dependency(%q<i18n>, [">= 0.5.0"])
    s.add_dependency(%q<rspec>, ["~> 2.6.0"])
  end
end
