$:.unshift File.dirname(__FILE__)

module Colorator
  VERSION = "0.1"
  ANSI_COLORS = {
    :black   => 30,
    :red     => 31,
    :green   => 32,
    :yellow  => 33,
    :blue    => 34,
    :magenta => 35,
    :cyan    => 36,
    :white   => 37,
    :bold    => 1
  }
end

require "colorator/core_ext"
