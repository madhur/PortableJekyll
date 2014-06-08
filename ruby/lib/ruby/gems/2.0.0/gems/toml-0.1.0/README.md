# TOML

A sane configuration format from @mojombo.  More information here: https://github.com/mojombo/toml

This is far superior to YAML and JSON because it doesn't suck.  Really it doesn't.

**There is a bug in Rails 2.3's vendored version of BlankSlate (a dependency of Parslet which is used for parsing TOML) that breaks Parslet; please see this [Gist](https://gist.github.com/dirk/5264004) for a workaround.**

## Usage

Add to your Gemfile:

```ruby
gem "toml", "~> 0.0.3"
```

It's simple, really.

```ruby
content = <<-TOML

# Hello, this is an example.
[things]
other = "things"
what = 900000

TOML

parser = TOML::Parser.new(content).parsed
# => { "things" => { "other" => "things", "what" => 900000 } }
```

You can also use the same API as `YAML` if you'd like:

```ruby
TOML.load("thing = 9")
# => {"thing" => 9}

TOML.load_file("my_file.toml")
# => {"whatever" => "keys"}
```

There's also a beta feature for generating a TOML file from a Ruby hash. Please note this will likely not give beautiful output right now.

```ruby
hash = {
  "integer" => 1,
  "float" => 3.14159,
  "true" => true,
  "false" => false,
  "string" => "hi",
  "array" => [[1], [2], [3]],
  "key" => {
    "group" => {
      "value" => "lol"
    }
  }
}
doc = TOML::Generator.new(hash).body
# doc will be a string containing a proper TOML document.
```

## Contributors

Written by Jeremy McAnally (@jm) and Dirk Gadsden (@dirk) based on TOML from Tom Preston-Werner (@mojombo).
