
require 'rubygems'
require 'bundler/setup'

require 'toml'

doc = "
a = [true, false]
"

puts TOML.load(doc).inspect

# puts TOML.load("a = [[[[1]]]]")["a"].inspect
# puts "[[[[1]]]] <- expected"
# 
# puts TOML.load("a = [1]")["a"].inspect
# puts "[1] <- expected"
# 
# puts TOML.load("a = [1, 2, 3]")["a"].inspect
# puts "[1, 2, 3] <- expected"
# 
# puts TOML.load("a = [[[1], 2], 3]")["a"].inspect
# puts "[[[1], 2], 3] <- expected"
# 
# puts TOML.load("a = [[]]")["a"].inspect
