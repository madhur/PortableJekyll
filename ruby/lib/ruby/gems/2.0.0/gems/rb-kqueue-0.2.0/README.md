# rb-kqueue

This is a simple wrapper over the [kqueue](http://en.wikipedia.org/wiki/Kqueue)
BSD event notification interface (supported on FreeBSD, NetBSD, OpenBSD, and Darwin).
It uses the [FFI](http://wiki.github.com/ffi/ffi) gem to avoid having to compile a C extension.

[API documentation is available on rdoc.info](http://rdoc.info/projects/mat813/rb-kqueue).

## WARNING

This code is incomplete, and didn't work last I had a chance to test it.
I don't have time to continue working on it at the moment,
so I'm posting it online for posterity and in case anyone wants to take a crack at it.

If anyone wants commit rights, just email me at nex342@gmail.com.

## Usage

The API is similar to the kqueue C API, but with a more Rubyish feel.
First, create a queue:

    queue = KQueue::Queue.new

Then, tell it to watch the events you're interested in:

    queue.watch_file("path/to/foo.txt", :write) {puts "foo.txt was modified!"}
    queue.watch_process(Process.pid, :fork, :exec) do |event|
      puts "This process has #{event.flags.map {|f| f.to_s + "ed"}.join(" and ")}"
    end

KQueue can monitor for all sorts of events.
For a full list, see the `watch_*` methods on {Queue}.

Finally, run the queue:

    queue.run

This will loop infinitely, calling the appropriate callbacks when the events are fired.
If you don't want infinite looping,
you can also block until there are available events,
process them all at once,
and then continue on your merry way:

    queue.process
