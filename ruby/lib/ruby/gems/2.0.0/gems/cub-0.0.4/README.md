# Cub

Fetch stock information

## Installation

Add this line to your application's Gemfile:

    gem 'cub'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install cub

## Usage

    Cub.company(7203)
    => "トヨタ自動車"

    Cub.price(7203)
    => 3275

    Cub.per(7203)
    => 35.86

    Cub.pbr(7203)
    => 0.97

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
