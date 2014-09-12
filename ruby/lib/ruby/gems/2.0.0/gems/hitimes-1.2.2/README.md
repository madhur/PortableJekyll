## hitimes

* [Homepage](http://github.com/copiousfreetime/hitimes)
* [Github project](http://github.com.org/copiousfreetime/hitimes)
* email jeremy at copiousfreetime dot org
* `git clone url git://github.com/copiousfreetime/hitimes.git`

## INSTALL

* `gem install hitimes`

## DESCRIPTION

Hitimes is a fast, high resolution timer library for recording
performance metrics.  It uses the appropriate low method calls for each
system to get the highest granularity time increments possible.  

It currently supports any of the following systems:

* any system with the POSIX call `clock_gettime()`
* Mac OS X
* Windows
* JRuby

Using Hitimes can be faster than using a series of `Time.new` calls, and
it will have a much higher granularity. It is definitely faster than
using `Process.times`. 

## SYNOPSIS

### Interval

Use Hitimes::Interval to calculate only the duration of a block of code

``` ruby
duration = Hitimes::Interval.measure do
             # some operation ...
           end

puts duration
```

### TimedMetric

Use a Hitimes::TimedMetric to calculate statistics about an iterative operation

``` ruby
timed_metric = Hitimes::TimedMetric.new('operation on items')
```

Explicitly use `start` and `stop`:

``` ruby
collection.each do |item|
  timed_metric.start
  # .. do something with item
  timed_metric.stop
end
```

Or use the block.  In TimedMetric the return value of +measure+ is the return
value of the block

``` ruby
collection.each do |item|
  result_of_do_something = timed_metric.measure { do_something( item ) }
end
```
And then look at the stats

``` ruby
puts timed_metric.mean
puts timed_metric.max
puts timed_metric.min
puts timed_metric.stddev
puts timed_metric.rate
```
### ValueMetric 

Use a Hitimes::ValueMetric to calculate statistics about measured samples

``` ruby
value_metric = Hitimes::ValueMetric.new( 'size of thing' )
loop do
  # ... do stuff changing sizes of 'thing'
  value_metric.measure( thing.size )
  # ... do other stuff that may change size of thing
end

puts value_metric.mean
puts value_metric.max
puts value_metric.min
puts value_metric.stddev
puts value_metric.rate
```

### TimedValueMetric

Use a Hitimes::TimedValueMetric to calculate statistics about batches of samples

``` ruby
timed_value_metric = Hitimes::TimedValueMetric.new( 'batch times' )
loop do 
  batch = ... # get a batch of things
  timed_value_metric.start
  # .. do something with batch
  timed_value_metric.stop( batch.size )
end

puts timed_value_metric.rate

puts timed_value_metric.timed_stats.mean
puts timed_value_metric.timed_stats.max
puts timed_value_metric.timed_stats.min
puts timed_value_metric.timed_stats.stddev

puts timed_value_metric.value_stats.mean
puts timed_value_metric.value_stats.max
puts timed_value_metric.value_stats.min
puts timed_value_metric.value_stats.stddev
```

## CHANGES

Read the HISTORY.md file.

## BUILDING FOR WINDOWS

[rake-compiler](https://github.com/luislavena/rake-compiler) is use for building
the windows version. For me, on OSX to cross compile the process is:

```
% gem install rake-compiler # in each rvm instance, 1.8.7, 1.9.3
% rvm use 2.0.0@hitimes
% rake-compiler cross-ruby VERSION=2.0.0-p0 # or latest
% rvm use 1.9.3@hitimes
% rake-compiler cross-ruby VERSION=1.9.3-p374 # or latest
% rvm use 1.8.7@hitimes
% rake-compiler cross-ruby VERSION=1.8.7-p371

# This only works via 1.8.7 at the current moment
% rake cross native gem RUBY_CC_VERSION=1.8.7:1.9.3:2.0.0
```

## CREDITS

* [Bruce Williams](https://github.com/bruce) for suggesting the idea

## ISC License

Copyright (c) 2008-2012 Jeremy Hinegardner

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
