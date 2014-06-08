require "rubygems"

$LOAD_PATH.unshift(File.expand_path(File.dirname(__FILE__))) unless $LOAD_PATH.include?(File.expand_path(File.dirname(__FILE__)))

require "sax-machine/sax_document"
require "sax-machine/sax_configure"
require "sax-machine/sax_handler"
require "sax-machine/sax_config"

module SAXMachine
  VERSION = "0.0.16"
end