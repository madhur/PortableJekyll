require 'rake'

begin
  require 'jeweler'
  Jeweler::Tasks.new do |s|
    s.name = "fast-stemmer"
    s.summary = %Q{Fast Porter stemmer based on a C version of algorithm}
    s.email = "romanbsd@yahoo.com"
    s.homepage = "http://github.com/romanbsd/fast-stemmer"
    s.description = s.summary
    s.authors = ["Roman Shterenzon"]
    s.extensions = ['ext/extconf.rb']
    s.files = FileList["[A-Z]*", "{ext,lib,test}/**/*"]
  end
  Jeweler::RubygemsDotOrgTasks.new
rescue LoadError
  puts "Jeweler not available. Install it with: sudo gem install technicalpickles-jeweler -s http://gems.github.com"
end

require 'rdoc/task'
Rake::RDocTask.new do |rdoc|
  rdoc.rdoc_dir = 'rdoc'
  rdoc.title = 'fast-stemmer'
  rdoc.options << '--line-numbers' << '--inline-source'
  rdoc.rdoc_files.include('README*')
  rdoc.rdoc_files.include('lib/**/*.rb')
end

require 'rake/testtask'
Rake::TestTask.new(:test) do |t|
  t.libs << 'lib' << 'test'
  t.pattern = 'test/**/*_test.rb'
  t.verbose = false
end

task :default => :test
