require 'jekyll'
require File.expand_path("../lib/jekyll-paginate", File.dirname(__FILE__))

RSpec.configure do |config|
  config.treat_symbols_as_metadata_keys_with_true_values = true
  config.run_all_when_everything_filtered = true
  config.filter_run :focus
  config.order = 'random'

  def test_dir(*subdirs)
    File.join(File.dirname(__FILE__), *subdirs)
  end

  def dest_dir(*subdirs)
    test_dir('dest', *subdirs)
  end

  def source_dir(*subdirs)
    test_dir('source', *subdirs)
  end

  def build_configs(overrides, base_hash = Jekyll::Configuration::DEFAULTS)
    Jekyll::Utils.deep_merge_hashes(base_hash, overrides)
  end

  def site_configuration(overrides = {})
    build_configs({
      "source"      => source_dir,
      "destination" => dest_dir
    }, build_configs(overrides))
  end

  def build_site(config = {})
    site = Jekyll::Site.new(site_configuration(
      {"paginate" => 1}.merge(config)
    ))
    site.process
    site
  end
end
