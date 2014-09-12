#--
# Copyright (c) 2008 Jeremy Hinegardner
# All rights reserved.  See LICENSE and/or COPYING for details.
#++

#
# The top level module containing the contents of the hitimes library
#
# use the library with:
#
#   require 'hitimes'
#
module Hitimes
  #
  # Base class of all errors in Hitimes
  #
  class Error < ::StandardError; end

  # Hitimes.measure { } -> Float
  #
  # Times the execution of the block, returning the number of seconds it took
  def self.measure(&block)
    Hitimes::Interval.measure(&block)
  end
end
require 'hitimes/paths'
require 'hitimes/version'

# Load the binary extension, try loading one for the specific version of ruby
# and if that fails, then fall back to one in the top of the library.
# this is the method recommended by rake-compiler
begin
  # this will be for windows
  require "hitimes/#{RUBY_VERSION.sub(/\.\d$/,'')}/hitimes"
rescue LoadError
  # everyone else.
  require 'hitimes/hitimes'
end

require 'hitimes/stats'
require 'hitimes/mutexed_stats'

require 'hitimes/metric'
require 'hitimes/value_metric'
require 'hitimes/timed_metric'
require 'hitimes/timed_value_metric'

