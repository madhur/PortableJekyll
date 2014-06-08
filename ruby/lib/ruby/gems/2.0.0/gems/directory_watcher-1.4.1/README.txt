Directory Watcher
    by Tim Pease
    http://codeforpeople.rubyforge.org/directory_watcher

== DESCRIPTION:

The directory watcher operates by scanning a directory at some interval and
generating a list of files based on a user supplied glob pattern. As the file
list changes from one interval to the next, events are generated and
dispatched to registered observers. Three types of events are supported --
added, modified, and removed.

== FEATURES:

See DirectoryWatcher for detailed documentation and usage.

== REQUIREMENTS:

This is a pure ruby library. There are no requirements for using this code.

== INSTALL:

  sudo gem install directory_watcher

You will need have Mr Bones installed in order to develop or modify directory
watcher.

  sudo gem install bones

== NOTES:

The support for EventMachine based file notifications is fairly new and
experimental. Please feel free to experiment and report any issues on the
github issue tracker.

  http://github.com/TwP/directory_watcher/issues

The support for Rev based file notifications is also fairly new and subject to
the same disclaimer as the EventMachine functionality.

== LICENSE:

MIT License
Copyright (c) 2007 - 2009

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
