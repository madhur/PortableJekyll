# colorator

Colorize your text for the terminal

## Example

```ruby
"this string".red
# => \e[31mthis string\e[0m
"my string".blue
# => \e[34mthis string\e[0m
# etc...
```

## Supported Colors

- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- bold

## Why

There are a bunch of gems that provide functionality like this, but none have
as simple an API as this. Just call `"string".color` and your text will be
colorized.

## License

MIT. Written as a single Ruby file by Brandon Mathis, converted into a gem by
Parker Moore.
