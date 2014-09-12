Timers
======
[![Gem Version](https://badge.fury.io/rb/timers.png)](http://rubygems.org/gems/timers)
[![Build Status](https://secure.travis-ci.org/celluloid/timers.png?branch=master)](http://travis-ci.org/celluloid/timers)
[![Code Climate](https://codeclimate.com/github/celluloid/timers.png)](https://codeclimate.com/github/celluloid/timers)
[![Coverage Status](https://coveralls.io/repos/celluloid/timers/badge.png?branch=master)](https://coveralls.io/r/celluloid/timers)

Ruby timer collections. Schedule several procs to fire after configurable delays
or at periodic intervals.

This gem is especially useful when you are faced with an API that accepts a
single timeout but you want to run multiple timers on top of it. An example of
such a library is [nio4r](https://github.com/celluloid/nio4r), a cross-platform
Ruby library for using system calls like epoll and kqueue.

Usage
-----

Create a new timer group with `Timers::Group.new`:

```ruby
require 'timers'

timers = Timers::Group.new
```

Schedule a proc to run after 5 seconds with `Timers::Group#after`:

```ruby
five_second_timer = timers.after(5) { puts "Take five" }
```

The `five_second_timer` variable is now bound to a Timers::Timer object. To
cancel a timer, use `Timers::Timer#cancel`

Once you've scheduled a timer, you can wait until the next timer fires with `Timers::Group#wait`:

```ruby
# Waits 5 seconds
timers.wait

# The script will now print "Take five"
```

You can schedule a block to run periodically with `Timers::Group#every`:

```ruby
every_five_seconds = timers.every(5) { puts "Another 5 seconds" }

loop { timers.wait }
```

If you'd like another method to do the waiting for you, e.g. `Kernel.select`,
you can use `Timers::Group#wait_interval` to obtain the amount of time to wait. When
a timeout is encountered, you can fire all pending timers with `Timers::Group#fire`:

```ruby
loop do
  interval = timers.wait_interval
  ready_readers, ready_writers = select readers, writers, nil, interval

  if ready_readers || ready_writers
    # Handle IO
    ...
  else
    # Timeout!
    timers.fire
  end
end
```

You can also pause and continue individual timers, or all timers:

```ruby
paused_timer = timers.every(5) { puts "I was paused" }

paused_timer.pause
10.times { timers.wait } # will not fire paused timer

paused_timer.resume
10.times { timers.wait } # will fire timer

timers.pause
10.times { timers.wait } # will not fire any timers

timers.resume
10.times { timers.wait } # will fire all timers
```

License
-------

Copyright (c) 2014 Celluloid timers project developers (given in the file
AUTHORS.md).

Distributed under the MIT License. See LICENSE file for further details.
