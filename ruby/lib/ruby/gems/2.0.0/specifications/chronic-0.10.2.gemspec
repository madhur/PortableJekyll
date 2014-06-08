# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "chronic"
  s.version = "0.10.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Tom Preston-Werner", "Lee Jarvis"]
  s.date = "2013-09-09"
  s.description = "Chronic is a natural language date/time parser written in pure Ruby."
  s.email = ["tom@mojombo.com", "ljjarvis@gmail.com"]
  s.extra_rdoc_files = ["README.md", "HISTORY.md", "LICENSE"]
  s.files = ["README.md", "HISTORY.md", "LICENSE"]
  s.homepage = "http://github.com/mojombo/chronic"
  s.licenses = ["MIT"]
  s.rdoc_options = ["--charset=UTF-8"]
  s.require_paths = ["lib"]
  s.rubyforge_project = "chronic"
  s.rubygems_version = "2.0.3"
  s.summary = "Natural language date/time parsing."

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<rake>, [">= 0"])
      s.add_development_dependency(%q<simplecov>, [">= 0"])
      s.add_development_dependency(%q<minitest>, ["~> 5.0"])
      s.add_development_dependency(%q<activesupport>, [">= 0"])
    else
      s.add_dependency(%q<rake>, [">= 0"])
      s.add_dependency(%q<simplecov>, [">= 0"])
      s.add_dependency(%q<minitest>, ["~> 5.0"])
      s.add_dependency(%q<activesupport>, [">= 0"])
    end
  else
    s.add_dependency(%q<rake>, [">= 0"])
    s.add_dependency(%q<simplecov>, [">= 0"])
    s.add_dependency(%q<minitest>, ["~> 5.0"])
    s.add_dependency(%q<activesupport>, [">= 0"])
  end
end
