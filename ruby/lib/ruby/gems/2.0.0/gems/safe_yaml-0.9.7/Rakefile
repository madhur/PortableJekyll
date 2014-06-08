require "rspec/core/rake_task"

desc "Run specs"
RSpec::Core::RakeTask.new(:spec) do |t|
  t.rspec_opts = %w(--color)
end

namespace :spec do
  desc "Run only specs tagged 'solo'"
  RSpec::Core::RakeTask.new(:solo) do |t|
    t.rspec_opts = %w(--color --tag solo)
  end
end
