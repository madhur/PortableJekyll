# 0.2.0.rc1
* Tried to reduce the number of instances of respond_to? in the code by
  pulling common uses of it out to methods. [[#32](https://github.com/pauldix/sax-machine/pull/32)]
* The parse stack is now composed of simple objects instead of it being
  an array of arrays. [[#32](https://github.com/pauldix/sax-machine/pull/32)]
* Now using an identifier for an empty buffer instead of empty string. [[#32](https://github.com/pauldix/sax-machine/pull/32)]
* Cleaned up several variables that were not being used. [[#32](https://github.com/pauldix/sax-machine/pull/32)]
* Encapsulated stack so it's not being exposed as part of the API. [[#32](https://github.com/pauldix/sax-machine/pull/32)]
* #cdata_block is now an alias instead of delegating to characters. [[#32](https://github.com/pauldix/sax-machine/pull/32)]

# 0.1.0
* rename parent to ancestor
* added SAXMachine.configure
