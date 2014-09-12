# vim: syntax=ruby
load 'tasks/this.rb'

This.name     = "hitimes"
This.author   = "Jeremy Hinegardner"
This.email    = "jeremy@copiousfreetime.org"
This.homepage = "http://github.com/copiousfreetime/#{ This.name }"

This.ruby_gemspec do |spec|
  spec.add_development_dependency( 'rake'         , '~> 10.0')
  spec.add_development_dependency( 'minitest'     , '~> 5.3' )
  spec.add_development_dependency( 'rdoc'         , '~> 4.1'  )
  spec.add_development_dependency( 'json'         , '~> 1.7.7' )
  spec.add_development_dependency( 'rake-compiler', '~> 0.9' )

  spec.extensions.concat This.extension_conf_files
  spec.license = "ISC"
end

This.java_gemspec( This.ruby_gemspec ) do |spec|
  spec.extensions.clear
end

load 'tasks/default.rake'
load 'tasks/extension.rake'
