# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = "bigdecimal"
  s.version = "1.2.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Kenta Murata", "Shigeo Kobayashi"]
  s.date = "2012-02-19"
  s.description = "This library provides arbitrary-precision decimal floating-point number class."
  s.email = "mrkn@mrkn.jp"
  s.extensions = ["extconf.rb"]
  s.files = ["bigdecimal/jacobian.rb", "bigdecimal/ludcmp.rb", "bigdecimal/math.rb", "bigdecimal/newton.rb", "bigdecimal/util.rb", "bigdecimal.so", "extconf.rb"]
  s.homepage = "http://www.ruby-lang.org"
  s.require_paths = ["."]
  s.rubygems_version = "2.0.3"
  s.summary = "Arbitrary-precision decimal floating-point number library."
end
