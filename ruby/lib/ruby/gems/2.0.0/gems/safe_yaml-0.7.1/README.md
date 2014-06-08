SafeYAML
========

[![Build Status](https://travis-ci.org/dtao/safe_yaml.png)](http://travis-ci.org/dtao/safe_yaml)

The **SafeYAML** gem provides an alternative implementation of `YAML.load` suitable for accepting user input in Ruby applications. Unlike Ruby's built-in implementation of `YAML.load`, SafeYAML's version will not expose apps to arbitrary code execution exploits (such as [the one recently discovered in Rails](http://www.reddit.com/r/netsec/comments/167c11/serious_vulnerability_in_ruby_on_rails_allowing/) (or [this one](http://www.h-online.com/open/news/item/Rails-developers-close-another-extremely-critical-flaw-1793511.html))).

Installation
------------

Add this line to your application's Gemfile:

    gem "safe_yaml"

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install safe_yaml

Purpose
-------

Suppose your application were to contain some code like this:

```ruby
class ExploitableClassBuilder
  def []=(key, value)
    @class ||= Class.new

    @class.class_eval <<-EOS
      def #{key}
        #{value}
      end
    EOS
  end

  def create
    @class.new
  end
end
```

Now, if you were to use `YAML.load` on user input anywhere in your application without the SafeYAML gem installed, an attacker could make a request with a carefully-crafted YAML string to execute arbitrary code (yes, including `system("unix command")`) on your servers.

Observe:

    > yaml = <<-EOYAML
    > --- !ruby/hash:ExploitableClassBuilder
    > "foo; end; puts %(I'm in yr system!); def bar": "baz"
    > EOYAML
    => "--- !ruby/hash:ExploitableClassBuilder\n\"foo; end; puts %(I'm in yr system!); def bar\": \"baz\"\n"

    > YAML.load(yaml)
    I'm in yr system!
    => #<ExploitableClassBuilder:0x007fdbbe2e25d8 @class=#<Class:0x007fdbbe2e2510>>

With SafeYAML, that attacker would be thwarted:

    > require "safe_yaml"
    => true
    > YAML.load(yaml)
    => {"foo; end; puts %(I'm in yr system!); def bar"=>"baz"}

Usage
-----

`YAML.safe_load` will load YAML without allowing arbitrary object deserialization.

`YAML.unsafe_load` will exhibit Ruby's built-in behavior: to allow the deserialization of arbitrary objects.

By default, when you require the safe_yaml gem in your project, `YAML.load` is patched to internally call `safe_load`. The patched method also accepts a `:safe` flag to specify which version to use:

    # Ruby >= 1.9.3
    YAML.load(yaml, filename, :safe => true) # calls safe_load
    YAML.load(yaml, filename, :safe => false) # calls unsafe_load

    # Ruby < 1.9.3
    YAML.load(yaml, :safe => true) # calls safe_load
    YAML.load(yaml, :safe => false) # calls unsafe_load

The default behavior can be switched to unsafe loading by calling `YAML.enable_arbitrary_object_deserialization!`. In this case, the `:safe` flag still has the same effect, but the defaults are reversed (so calling `YAML.load` will have the same behavior as if the safe_yaml gem weren't required).

This gem will also warn you whenever you use `YAML.load` without specifying the `:safe` option. If you do not want to see these messages in your logs, you can say `SafeYAML::OPTIONS[:suppress_warnings] = true` in an initializer.

Notes
-----

The way that SafeYAML works is by restricting the kinds of objects that can be deserialized via `YAML.load`. More specifically, only the following types of objects can be deserialized by default:

- Hashes
- Arrays
- Strings
- Numbers
- Dates
- Times
- Booleans
- Nils

Additionally, deserialization of symbols can be enabled by calling `YAML.enable_symbol_parsing!` (for example, in an initializer).

Known Issues
------------

Also note that some Ruby libraries, particularly those requiring inter-process communication, leverage YAML's object deserialization functionality and therefore may break or otherwise be impacted by SafeYAML. The following list includes known instances of SafeYAML's interaction with other Ruby gems:

- [**Guard**](https://github.com/guard/guard): Uses YAML as a serialization format for notifications. The data serialized uses symbolic keys, so calling `YAML.enable_symbol_parsing!` is necessary to allow Guard to work.
- [**sidekiq**](https://github.com/mperham/sidekiq): Uses a YAML configiuration file with symbolic keys, so calling `YAML.enable_symbol_parsing!` should allow it to work.

The above list will grow over time, as more issues are discovered.

Caveat
------

This gem is quite young, and so the API may (read: *will*) change in future versions. The goal of the gem is to make it as easy as possible to protect existing applications from object deserialization exploits. Any and all feedback is more than welcome.

Requirements
------------

SafeYAML requires Ruby 1.8.7 or newer and works with both [Syck](http://www.ruby-doc.org/stdlib-1.8.7/libdoc/yaml/rdoc/YAML.html) and [Psych](http://github.com/tenderlove/psych).

If you are using a version of Ruby where Psych is the default YAML engine (e.g., 1.9.3) but you want to use Syck, be sure to set `YAML::ENGINE.yamler = "syck"` **before** requiring the safe_yaml gem.
