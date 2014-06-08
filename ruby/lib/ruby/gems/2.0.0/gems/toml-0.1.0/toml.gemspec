## This is the rakegem gemspec template. Make sure you read and understand
## all of the comments. Some sections require modification, and others can
## be deleted if you don't need them. Once you understand the contents of
## this file, feel free to delete any comments that begin with two hash marks.
## You can find comprehensive Gem::Specification documentation, at
## http://docs.rubygems.org/read/chapter/20
Gem::Specification.new do |s|
  s.specification_version = 2 if s.respond_to? :specification_version=
  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.rubygems_version = '1.3.5'

  ## Leave these as is they will be modified for you by the rake gemspec task.
  ## If your rubyforge_project name is different, then edit it and comment out
  ## the sub! line in the Rakefile
  s.name              = 'toml'
  s.version           = '0.1.0'
  s.date              = '2013-12-05'

  ## Make sure your summary is short. The description may be as long
  ## as you like.
  s.summary     = "Parse your TOML."
  s.description = "Parse your TOML, seriously."

  ## List the primary authors. If there are a bunch of authors, it's probably
  ## better to set the email to an email list or something. If you don't have
  ## a custom homepage, consider using your GitHub URL or the like.
  s.authors  = ["Jeremy McAnally", "Dirk Gadsden"]
  s.email    = 'jeremy@github.com'
  s.homepage = 'http://github.com/jm/toml'

  ## This gets added to the $LOAD_PATH so that 'lib/NAME.rb' can be required as
  ## require 'NAME.rb' or'/lib/NAME/file.rb' can be as require 'NAME/file.rb'
  s.require_paths = %w[lib]

  ## Specify any RDoc options here. You'll want to add your README and
  ## LICENSE files to the extra_rdoc_files list.
  s.rdoc_options = ["--charset=UTF-8"]
  s.extra_rdoc_files = %w[README.md LICENSE]
  
  s.add_dependency "parslet", "~> 1.5.0"
  
  ## Leave this section as-is. It will be automatically generated from the
  ## contents of your Git repository via the gemspec task. DO NOT REMOVE
  ## THE MANIFEST COMMENTS, they are used as delimiters by the task.
  # = MANIFEST =
  s.files = %w[
    Gemfile
    LICENSE
    README.md
    Rakefile
    lib/toml.rb
    lib/toml/generator.rb
    lib/toml/key.rb
    lib/toml/monkey_patch.rb
    lib/toml/parser.rb
    lib/toml/parslet.rb
    lib/toml/table.rb
    lib/toml/transformer.rb
    test/empty.toml
    test/hard_example.toml
    test/spec.toml
    test/test_empty.rb
    test/test_generator.rb
    test/test_parser.rb
    test/test_parser_hard.rb
    test/test_table_arrays.rb
    test/tmp.rb
    toml.gemspec
  ]
  # = MANIFEST =

  ## Test files will be grabbed from the file list. Make sure the path glob
  ## matches what you actually use.
  s.test_files = s.files.select { |path| path =~ /^test\/test_.*\.rb/ }
end
