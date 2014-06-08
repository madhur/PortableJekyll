require File.dirname(__FILE__) + '/../spec_helper'

describe "SAXMachine" do
  describe "element" do
    describe "when parsing a single element" do
      before :each do
        @klass = Class.new do
          include SAXMachine
          element :title
        end
      end

      it "should provide an accessor" do
        document = @klass.new
        document.title = "Title"
        document.title.should == "Title"
      end

      it "should allow introspection of the elements" do
        @klass.column_names.should =~ [:title]
      end

      it "should not overwrite the getter is there is already one present" do
        @klass = Class.new do
          def title
            "#{@title} ***"
          end

          include SAXMachine
          element :title
        end
        document = @klass.new
        document.title = "Title"
        document.title.should == "Title ***"
      end

      it "should not overwrite the setter if there is already one present" do
        @klass = Class.new do
          def title=(val)
            @title = "#{val} **"
          end

          include SAXMachine
          element :title
        end
        document = @klass.new
        document.title = "Title"
        document.title.should == "Title **"
      end
      describe "the class attribute" do
        before(:each) do
          @klass = Class.new do
            include SAXMachine
            element :date, :class => DateTime
          end
          @document = @klass.new
          @document.date = DateTime.now.to_s
        end
        it "should be available" do
          @klass.data_class(:date).should == DateTime
        end
      end
      describe "the required attribute" do
        it "should be available" do
          @klass = Class.new do
            include SAXMachine
            element :date, :required => true
          end
          @klass.required?(:date).should be_true
        end
      end

      it "should not overwrite the accessor when the element is not present" do
        document = @klass.new
        document.title = "Title"
        document.parse("<foo></foo>")
        document.title.should == "Title"
      end

      it "should overwrite the value when the element is present" do
        document = @klass.new
        document.title = "Old title"
        document.parse("<title>New title</title>")
        document.title.should == "New title"
      end

      it "should save the element text into an accessor" do
        document = @klass.parse("<title>My Title</title>")
        document.title.should == "My Title"
      end

      it "should save cdata into an accessor" do
        document = @klass.parse("<title><![CDATA[A Title]]></title>")
        document.title.should == "A Title"
      end

      it "should save the element text into an accessor when there are multiple elements" do
        document = @klass.parse("<xml><title>My Title</title><foo>bar</foo></xml>")
        document.title.should == "My Title"
      end

      it "should save the first element text when there are multiple of the same element" do
        document = @klass.parse("<xml><title>My Title</title><title>bar</title></xml>")
        document.title.should == "My Title"

      end
    end

    describe "when parsing multiple elements" do
      before :each do
        @klass = Class.new do
          include SAXMachine
          element :title
          element :name
        end
      end

      it "should save the element text for a second tag" do
        document = @klass.parse("<xml><title>My Title</title><name>Paul</name></xml>")
        document.name.should == "Paul"
        document.title.should == "My Title"
      end


      it "should not overwrite the getter is there is already one present" do
        @klass = Class.new do
          def items
            []
          end

          include SAXMachine
          elements :items
        end
        document = @klass.new
        document.items = [1, 2, 3, 4]
        document.items.should == []
      end

      it "should not overwrite the setter if there is already one present" do
        @klass = Class.new do
          def items=(val)
            @items = [1, *val]
          end

          include SAXMachine
          elements :items
        end
        document = @klass.new
        document.items = [2, 3]
        document.items.should == [1, 2, 3]
      end

    end

    describe "when using options for parsing elements" do
      describe "using the 'as' option" do
        before :each do
          @klass = Class.new do
            include SAXMachine
            element :description, :as => :summary
          end
        end

        it "should provide an accessor using the 'as' name" do
          document = @klass.new
          document.summary = "a small summary"
          document.summary.should == "a small summary"
        end

        it "should save the element text into the 'as' accessor" do
          document = @klass.parse("<description>here is a description</description>")
          document.summary.should == "here is a description"
        end
      end

      describe "using the :with option" do
        describe "and the :value option" do
          before :each do
            @klass = Class.new do
              include SAXMachine
              element :link, :value => :href, :with => {:foo => "bar"}
            end
          end

          it "should save the value of a matching element" do
            document = @klass.parse("<link href='test' foo='bar'>asdf</link>")
            document.link.should == "test"
          end

          it "should save the value of the first matching element" do
            document = @klass.parse("<xml><link href='first' foo='bar' /><link href='second' foo='bar' /></xml>")
            document.link.should == "first"
          end

          describe "and the :as option" do
            before :each do
              @klass = Class.new do
                include SAXMachine
                element :link, :value => :href, :as => :url, :with => {:foo => "bar"}
                element :link, :value => :href, :as => :second_url, :with => {:asdf => "jkl"}
              end
            end

            it "should save the value of the first matching element" do
              document = @klass.parse("<xml><link href='first' foo='bar' /><link href='second' asdf='jkl' /><link href='second' foo='bar' /></xml>")
              document.url.should == "first"
              document.second_url.should == "second"
            end

          end
        end

        describe "with only one element" do
          before :each do
            @klass = Class.new do
              include SAXMachine
              element :link, :with => {:foo => "bar"}
            end
          end

          it "should save the text of an element that has matching attributes" do
            document = @klass.parse("<link foo=\"bar\">match</link>")
            document.link.should == "match"
          end

          it "should not save the text of an element that doesn't have matching attributes" do
            document = @klass.parse("<link>no match</link>")
            document.link.should be_nil
          end

          it "should save the text of an element that has matching attributes when it is the second of that type" do
            document = @klass.parse("<xml><link>no match</link><link foo=\"bar\">match</link></xml>")
            document.link.should == "match"

          end

          it "should save the text of an element that has matching attributes plus a few more" do
            document = @klass.parse("<xml><link>no match</link><link asdf='jkl' foo='bar'>match</link>")
            document.link.should == "match"
          end
        end

        describe "with multiple elements of same tag" do
          before :each do
            @klass = Class.new do
              include SAXMachine
              element :link, :as => :first, :with => {:foo => "bar"}
              element :link, :as => :second, :with => {:asdf => "jkl"}
            end
          end

          it "should match the first element" do
            document = @klass.parse("<xml><link>no match</link><link foo=\"bar\">first match</link><link>no match</link></xml>")
            document.first.should == "first match"
          end

          it "should match the second element" do
            document = @klass.parse("<xml><link>no match</link><link foo='bar'>first match</link><link asdf='jkl'>second match</link><link>hi</link></xml>")
            document.second.should == "second match"
          end
        end
      end # using the 'with' option

      describe "using the 'value' option" do
        before :each do
          @klass = Class.new do
            include SAXMachine
            element :link, :value => :foo
          end
        end

        it "should save the attribute value" do
          document = @klass.parse("<link foo='test'>hello</link>")
          document.link.should == 'test'
        end

        it "should save the attribute value when there is no text enclosed by the tag" do
          document = @klass.parse("<link foo='test'></link>")
          document.link.should == 'test'
        end

        it "should save the attribute value when the tag close is in the open" do
          document = @klass.parse("<link foo='test'/>")
          document.link.should == 'test'
        end

        it "should save two different attribute values on a single tag" do
          @klass = Class.new do
            include SAXMachine
            element :link, :value => :foo, :as => :first
            element :link, :value => :bar, :as => :second
          end
          document = @klass.parse("<link foo='foo value' bar='bar value'></link>")
          document.first.should == "foo value"
          document.second.should == "bar value"
        end

        it "should not fail if one of the attribute hasn't been defined" do
          @klass = Class.new do
            include SAXMachine
            element :link, :value => :foo, :as => :first
            element :link, :value => :bar, :as => :second
          end
          document = @klass.parse("<link foo='foo value'></link>")
          document.first.should == "foo value"
          document.second.should be_nil
        end
      end

      describe "when desiring both the content and attributes of an element" do
        before :each do
          @klass = Class.new do
            include SAXMachine
            element :link
            element :link, :value => :foo, :as => :link_foo
            element :link, :value => :bar, :as => :link_bar
          end
        end

        it "should parse the element and attribute values" do
          document = @klass.parse("<link foo='test1' bar='test2'>hello</link>")
          document.link.should == 'hello'
          document.link_foo.should == 'test1'
          document.link_bar.should == 'test2'
        end
      end

    end
  end

  describe "elements" do
    describe "when parsing multiple elements" do
      before :each do
        @klass = Class.new do
          include SAXMachine
          elements :entry, :as => :entries
        end
      end

      it "should provide a collection accessor" do
        document = @klass.new
        document.entries << :foo
        document.entries.should == [:foo]
      end

      it "should parse a single element" do
        document = @klass.parse("<entry>hello</entry>")
        document.entries.should == ["hello"]
      end

      it "should parse multiple elements" do
        document = @klass.parse("<xml><entry>hello</entry><entry>world</entry></xml>")
        document.entries.should == ["hello", "world"]
      end

      it "should parse multiple elements when taking an attribute value" do
        attribute_klass = Class.new do
          include SAXMachine
          elements :entry, :as => :entries, :value => :foo
        end
        doc = attribute_klass.parse("<xml><entry foo='asdf' /><entry foo='jkl' /></xml>")
        doc.entries.should == ["asdf", "jkl"]
      end
    end

    describe "when using the with and class options" do
      before :each do
        class Bar
          include SAXMachine
          element :title
        end

        class Foo
          include SAXMachine
          element :title
        end

        class Item
          include SAXMachine

        end
        @klass = Class.new do
          include SAXMachine
          elements :item, :as => :items, :with => {:type => 'Bar'}, :class => Bar
          elements :item, :as => :items, :with => {:type => 'Foo'}, :class => Foo
        end
      end

      it "should cast into the correct class" do
        document = @klass.parse("<items><item type=\"Bar\"><title>Bar title</title></item><item type=\"Foo\"><title>Foo title</title></item></items>")
        document.items.size.should == 2
        document.items.first.should be_a(Bar)
        document.items.first.title.should == "Bar title"
        document.items.last.should be_a(Foo)
        document.items.last.title.should == "Foo title"
      end
    end

    describe "when using the class option" do
      before :each do
        class Foo
          include SAXMachine
          element :title
        end
        @klass = Class.new do
          include SAXMachine
          elements :entry, :as => :entries, :class => Foo
        end
      end

      it "should parse a single element with children" do
        document = @klass.parse("<entry><title>a title</title></entry>")
        document.entries.size.should == 1
        document.entries.first.title.should == "a title"
      end

      it "should parse multiple elements with children" do
        document = @klass.parse("<xml><entry><title>title 1</title></entry><entry><title>title 2</title></entry></xml>")
        document.entries.size.should == 2
        document.entries.first.title.should == "title 1"
        document.entries.last.title.should == "title 2"
      end

      it "should not parse a top level element that is specified only in a child" do
        document = @klass.parse("<xml><title>no parse</title><entry><title>correct title</title></entry></xml>")
        document.entries.size.should == 1
        document.entries.first.title.should == "correct title"
      end

      it "should parse elements, and make attributes and inner text available" do
        class Related
          include SAXMachine
          element 'related', :as=>:item
          element 'related', :as=>:attr, :value=>'attr'
        end
        class Foo
          elements 'related', :as=>'items', :class=>Related
        end

        doc = Foo.parse(%{<xml><collection><related attr='baz'>something</related><related>somethingelse</related></collection></xml>})
        doc.items.first.should_not be_nil
        doc.items.size.should == 2
        doc.items.first.item.should == 'something'
        doc.items.last.item.should == 'somethingelse'
      end

      it "should parse out an attribute value from the tag that starts the collection" do
        class Foo
          element :entry, :value => :href, :as => :url
        end
        document = @klass.parse("<xml><entry href='http://pauldix.net'><title>paul</title></entry></xml>")
        document.entries.size.should == 1
        document.entries.first.title.should == "paul"
        document.entries.first.url.should == "http://pauldix.net"
      end
    end
  end

  describe "full example" do
    before :each do
      @xml = File.read('spec/sax-machine/atom.xml')
      class AtomEntry
        include SAXMachine
        element :title
        element :name, :as => :author
        element "feedburner:origLink", :as => :url
        element :summary
        element :content
        element :published
      end

      class Atom
        include SAXMachine
        element :title
        element :link, :value => :href, :as => :url, :with => {:type => "text/html"}
        element :link, :value => :href, :as => :feed_url, :with => {:type => "application/atom+xml"}
        elements :entry, :as => :entries, :class => AtomEntry
      end
    end # before

    it "should parse the url" do
      f = Atom.parse(@xml)
      f.url.should == "http://www.pauldix.net/"
    end
  end

  describe "parsing a tree" do
    before do
      @xml = %[
      <categories>
        <category id="1">
          <title>First</title>
          <categories>
            <category id="2">
              <title>Second</title>
            </category>
          </categories>
        </category>
      </categories>
      ]
      class CategoryCollection;
      end
      class Category
        include SAXMachine
        attr_accessor :id
        element :category, :value => :id, :as => :id
        element :title
        element :categories, :as => :collection, :class => CategoryCollection
        ancestor :ancestor
      end
      class CategoryCollection
        include SAXMachine
        elements :category, :as => :categories, :class => Category
      end
      @collection = CategoryCollection.parse(@xml)
    end

    it "should parse the first category" do
      @collection.categories.first.id.should == "1"
      @collection.categories.first.title.should == "First"
      @collection.categories.first.ancestor.should == @collection
    end

    it "should parse the nested category" do
      @collection.categories.first.collection.categories.first.id.should == "2"
      @collection.categories.first.collection.categories.first.title.should == "Second"
    end
  end

  describe "parsing a tree without a collection class" do
    before do
      @xml = %[
      <categories>
        <category id="1">
          <title>First</title>
          <categories>
            <category id="2">
              <title>Second</title>
            </category>
          </categories>
        </category>
      </categories>
      ]
      class CategoryTree
        include SAXMachine
        attr_accessor :id
        element :category, :value => :id, :as => :id
        element :title
        elements :category, :as => :categories, :class => CategoryTree
      end
      @collection = CategoryTree.parse(@xml)
    end

    it "should parse the first category" do
      @collection.categories.first.id.should == "1"
      @collection.categories.first.title.should == "First"
    end

    it "should parse the nested category" do
      @collection.categories.first.categories.first.id.should == "2"
      @collection.categories.first.categories.first.title.should == "Second"
    end
  end

  describe "with element deeper inside the xml structure" do
    before do
      @xml = %[
        <item id="1">
          <texts>
            <title>Hello</title>
          </texts>
        </item>
      ]
      @klass = Class.new do
        include SAXMachine
        attr_accessor :id
        element :item, :value => "id", :as => :id
        element :title
      end
      @item = @klass.parse(@xml)
    end

    it "should have an id" do
      @item.id.should == "1"
    end

    it "should have a title" do
      @item.title.should == "Hello"
    end
  end

  describe "with config to pull multiple attributes" do
    before do
      @xml = %[
        <item id="1">
          <author name="John Doe" role="writer" />
        </item>
      ]
      class AuthorElement
        include SAXMachine
        attribute :name
        attribute :role
      end
      class ItemElement
        include SAXMachine
        element :author, :class => AuthorElement
      end
      @item = ItemElement.parse(@xml)
    end

    it 'should have the child element' do
      @item.author.should_not be_nil
    end

    it 'should have the author name' do
      @item.author.name.should == 'John Doe'
    end

    it 'should have the author role' do
      @item.author.role.should == 'writer'
    end
  end

  describe "with multiple elements and multiple attributes" do
    before do
      @xml = %[
        <item id="1">
          <author name="John Doe" role="writer" />
          <author name="Jane Doe" role="artist" />
        </item>
      ]
      class AuthorElement2
        include SAXMachine
        attribute :name
        attribute :role
      end
      class ItemElement2
        include SAXMachine
        elements :author, :as => :authors, :class => AuthorElement2
      end
      @item = ItemElement2.parse(@xml)
    end

    it 'should have the child elements' do
      @item.authors.should_not be_nil
      @item.authors.count.should == 2
    end

    it 'should have the author names' do
      @item.authors.first.name.should == 'John Doe'
      @item.authors.last.name.should == 'Jane Doe'
    end

    it 'should have the author roles' do
      @item.authors.first.role.should == 'writer'
      @item.authors.last.role.should == 'artist'
    end
  end

  describe "with mixed attributes and element values" do
    before do
      @xml = %[
        <item id="1">
          <author role="writer">John Doe</author>
        </item>
      ]
      class AuthorElement3
        include SAXMachine
        value :name
        attribute :role
      end
      class ItemElement3
        include SAXMachine
        element :author, :class => AuthorElement3
      end
      @item = ItemElement3.parse(@xml)
    end

    it 'should have the child elements' do
      @item.author.should_not be_nil
    end

    it 'should have the author names' do
      @item.author.name.should == 'John Doe'
    end

    it 'should have the author roles' do
      @item.author.role.should == 'writer'
    end
  end

  describe "with multiple mixed attributes and element values" do
    before do
      @xml = %[
        <item id="1">
          <title>sweet</title>
          <author role="writer">John Doe</author>
          <author role="artist">Jane Doe</author>
        </item>
      ]
      class AuthorElement4
        include SAXMachine
        value :name
        attribute :role
      end
      class ItemElement4
        include SAXMachine
        element :title
        elements :author, :as => :authors, :class => AuthorElement4

        def title=(blah)
          #raise 'woo'
          @title = blah
        end
      end
      @item = ItemElement4.parse(@xml)
    end

    it 'should have the title' do
      @item.title.should == 'sweet'
    end

    it 'should have the child elements' do
      @item.authors.should_not be_nil
      @item.authors.count.should == 2
    end

    it 'should have the author names' do
      @item.authors.first.name.should == 'John Doe'
      @item.authors.last.name.should == 'Jane Doe'
    end

    it 'should have the author roles' do
      @item.authors.first.role.should == 'writer'
      @item.authors.last.role.should == 'artist'
    end
  end
end
