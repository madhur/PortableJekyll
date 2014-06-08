#!/usr/bin/env ruby
require 'test/unit'
require File.join(File.dirname(__FILE__), '..', 'lib', 'fast_stemmer')

class TestStemmer < Test::Unit::TestCase
	def setup
		@stems = { 'riding' => 'ride',
			'forestalled' => 'forestal',
			'combined' => 'combin',
			'ran' => 'ran',
			'seen' => 'seen',
			'excused' => 'excus'
		}
	end

	def test_stems
		@stems.each {|stem| assert_equal(stem[1], stem[0].stem)}
	end
end
