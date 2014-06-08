# Jekyll::Coffeescript

A CoffeeScript converter for Jekyll.

## Installation

Add this line to your application's Gemfile:

    gem 'jekyll-coffeescript'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install jekyll-coffeescript

## Usage

In your Jekyll site, create CoffeeScript files that start with the following
lines:

```text
---
---
```

You need those three dashes in order for Jekyll to recognize it as
"convertible". They won't be included in the content passed to the CoffeeScript
compiler.

## Contributing

1. Fork it ( `http://github.com/<my-github-username>/jekyll-coffeescript/fork` )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
