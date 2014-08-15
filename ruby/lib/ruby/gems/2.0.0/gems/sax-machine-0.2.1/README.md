# SAX Machine [![Build Status](https://secure.travis-ci.org/pauldix/sax-machine.png?branch=master)](http://travis-ci.org/pauldix/sax-machine)

[Wiki](https://github.com/pauldix/sax-machine/wiki)

## Description

A declarative SAX parsing library backed by Nokogiri

## Usage
```ruby
require 'sax-machine'

# Class for information associated with content parts in a feed.
#  Ex: <content type="text">sample</content>
#  instance.type will be "text", instance.text will be "sample"
class AtomContent
  include SAXMachine
  attribute :type
  value :text
end

# Class for parsing an atom entry out of a feedburner atom feed
class AtomEntry
  include SAXMachine
  element :title
  # the :as argument makes this available through atom_entry.author instead of .name
  element :name, :as => :author
  element "feedburner:origLink", :as => :url
  element :summary
  element :content, :class => AtomContent
  element :published
  ancestor :ancestor
end

# Class for parsing Atom feeds
class Atom
  include SAXMachine
  element :title
  # the :with argument means that you only match a link tag that has an attribute of :type => "text/html"
  # the :value argument means that instead of setting the value to the text between the tag,
  # it sets it to the attribute value of :href
  element :link, :value => :href, :as => :url, :with => {:type => "text/html"}
  element :link, :value => :href, :as => :feed_url, :with => {:type => "application/atom+xml"}
  elements :entry, :as => :entries, :class => AtomEntry
end

# you can then parse like this
feed = Atom.parse(xml_text)
# then you're ready to rock
feed.title # => whatever the title of the blog is
feed.url # => the main url of the blog
feed.feed_url # => goes to the feedburner feed

feed.entries.first.title # => title of the first entry
feed.entries.first.author # => the author of the first entry
feed.entries.first.url # => the permalink on the blog for this entry
feed.entries.first.ancestor # => the Atom ancestor
# etc ...

# you can also use the elements method without specifying a class like so
class SomeServiceResponse
  include SAXMachine
  elements :message, :as => :messages
end

response = SomeServiceResponse.parse("<response><message>hi</message><message>world</message></response>")
response.messages.first # => "hi"
response.messages.last  # => "world"

# To limit conflicts in the class used for mappping, you can use the alternate SAXMachine.configure syntax

class X < ActiveRecord::Base
  # this way no element, elements or ancestor method will be added to X
  SAXMachine.configure(X) do |c|
    c.element :title
  end
end
```

## LICENSE

The MIT License

Copyright (c) 2009-2012:

* [Paul Dix](http://www.pauldix.net)
* [Julien Kirch](http://www.archiloque.net)
* [Ezekiel Templin](http://zeke.templ.in)

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