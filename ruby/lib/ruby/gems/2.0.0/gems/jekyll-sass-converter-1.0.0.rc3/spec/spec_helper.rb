# coding: utf-8
require 'fileutils'
require 'jekyll'

lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'jekyll-sass-converter'

RSpec.configure do |config|
  config.treat_symbols_as_metadata_keys_with_true_values = true
  config.run_all_when_everything_filtered = true
  config.filter_run :focus
  config.order = 'random'

  SOURCE_DIR = File.expand_path("../source", __FILE__)
  DEST_DIR   = File.expand_path("../dest",   __FILE__)
  FileUtils.rm_rf(DEST_DIR)
  FileUtils.mkdir_p(DEST_DIR)

  def source_dir(*files)
    File.join(SOURCE_DIR, *files)
  end

  def dest_dir(*files)
    File.join(DEST_DIR, *files)
  end

  def site_configuration(overrides = {})
    Jekyll::Utils.hash_deep_merge(Jekyll::Configuration::DEFAULTS, overrides.merge({
      "source" => source_dir,
      "destination" => dest_dir
    }))
  end
end
