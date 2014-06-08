require "rspec/core/rake_task"

desc "Run specs"
task :spec => ['spec:app', 'spec:lib']

namespace :spec do
  desc "Run only specs tagged 'solo'"
  RSpec::Core::RakeTask.new(:solo) do |t|
    t.rspec_opts = %w(--color --tag solo)
  end

  desc "Run only specs tagged NOT tagged 'libraries' (for applications)"
  RSpec::Core::RakeTask.new(:app) do |t|
    puts "Running specs w/ monkeypatch"
    t.rspec_opts = %w(--color --tag ~libraries)
  end

  desc "Run only specs tagged 'libraries'"
  RSpec::Core::RakeTask.new(:lib) do |t|
    puts "Running specs w/o monkeypatch"
    t.rspec_opts = %w(--color --tag libraries)
  end
end
