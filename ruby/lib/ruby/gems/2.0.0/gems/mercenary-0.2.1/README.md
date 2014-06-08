# Mercenary

Lightweight and flexible library for writing command-line apps in Ruby.

[![Build Status](https://secure.travis-ci.org/jekyll/mercenary.png)](https://travis-ci.org/jekyll/mercenary)

## Installation

Add this line to your application's Gemfile:

    gem 'mercenary'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install mercenary

## Usage

```ruby
Mercenary.program(:jekyll) do |p|
  p.version Jekyll::VERSION
  p.description 'Jekyll is a blog-aware, static site generator in Ruby'

  p.command(:new) do |c|
    c.syntax "jekyll new PATH"
    c.description "Creates a new Jekyll site scaffold in PATH"

    c.action do |args, options|
      Jekyll::Commands::New.process(args)
    end
  end

  p.command(:build) do |c|
    c.syntax "jekyll build [options]"
    c.description "Builds your Jekyll site"

    c.option 'safe', '--safe', 'Run in safe mode'
    c.option 'source', '--source DIR', 'From where to collect the source files'
    c.option 'destination', '--dest DIR', 'To where the compiled files should be written'

    c.action do |_, options|
      Jekyll::Commands::Build.process(options)
    end
  end

  p.command(:import) do |c|
    c.syntax "jekyll import <platform> [options]"
    c.description "Import your old blog to Jekyll"

    c.action do |args, options|
      begin
        require "jekyll-import"
      rescue
        msg  = "You must install the 'jekyll-import' gem before continuing.\n"
        msg += "* Do this by running `gem install jekyll-import`.\n"
        msg += "* Or if you need root privileges, run `sudo gem install jekyll-import`."
        abort msg
      end

      Jekyll::Commands::Import.process(args.first, options)
    end
  end

  p.default_command(:build)
end
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
