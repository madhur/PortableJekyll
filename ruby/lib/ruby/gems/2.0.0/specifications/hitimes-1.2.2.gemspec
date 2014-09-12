# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "hitimes"
  s.version = "1.2.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Jeremy Hinegardner"]
  s.date = "2014-07-09"
  s.description = "Hitimes is a fast, high resolution timer library for recording performance metrics.  It uses the appropriate low method calls for each system to get the highest granularity time increments possible.   It currently supports any of the following systems: * any system with the POSIX call `clock_gettime()` * Mac OS X * Windows * JRuby Using Hitimes can be faster than using a series of `Time.new` calls, and it will have a much higher granularity. It is definitely faster than using `Process.times`."
  s.email = "jeremy@copiousfreetime.org"
  s.extensions = ["ext/hitimes/c/extconf.rb"]
  s.extra_rdoc_files = ["CONTRIBUTING.md", "HISTORY.md", "Manifest.txt", "README.md"]
  s.files = ["CONTRIBUTING.md", "HISTORY.md", "Manifest.txt", "README.md", "ext/hitimes/c/extconf.rb"]
  s.homepage = "http://github.com/copiousfreetime/hitimes"
  s.licenses = ["ISC"]
  s.rdoc_options = ["--main", "README.md", "--markup", "tomdoc"]
  s.require_paths = ["lib"]
  s.rubygems_version = "2.0.3"
  s.summary = "Hitimes is a fast, high resolution timer library for recording performance metrics.  It uses the appropriate low method calls for each system to get the highest granularity time increments possible."

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<rake>, ["~> 10.0"])
      s.add_development_dependency(%q<minitest>, ["~> 5.3"])
      s.add_development_dependency(%q<rdoc>, ["~> 4.1"])
      s.add_development_dependency(%q<json>, ["~> 1.7.7"])
      s.add_development_dependency(%q<rake-compiler>, ["~> 0.9"])
    else
      s.add_dependency(%q<rake>, ["~> 10.0"])
      s.add_dependency(%q<minitest>, ["~> 5.3"])
      s.add_dependency(%q<rdoc>, ["~> 4.1"])
      s.add_dependency(%q<json>, ["~> 1.7.7"])
      s.add_dependency(%q<rake-compiler>, ["~> 0.9"])
    end
  else
    s.add_dependency(%q<rake>, ["~> 10.0"])
    s.add_dependency(%q<minitest>, ["~> 5.3"])
    s.add_dependency(%q<rdoc>, ["~> 4.1"])
    s.add_dependency(%q<json>, ["~> 1.7.7"])
    s.add_dependency(%q<rake-compiler>, ["~> 0.9"])
  end
end
