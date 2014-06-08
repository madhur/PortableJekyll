import unittest

from common import gtk, gobject

class MyContainer(gtk.Container):
    __gtype_name__ = 'MyContainer'
    def __init__(self):
        gtk.Container.__init__(self)
        self.children = []
        self.props = {}

    def do_add(self, child):
        child.set_parent(self)
        self.children.append(child)
        self.props[child] = '' # we just have one child property

    def do_remove(self, child):
        widget_was_visible = child.flags() & gtk.VISIBLE
        child.unparent()
        self.children.remove(child)
        del self.props[child]

        if widget_was_visible:
            self.queue_resize()

    def do_forall(self, internal, callback, data):
        for child in self.children:
            callback(child, data)

    def do_set_child_property(self, child, property_id, value, pspec):
        if pspec.name == 'dumb-prop':
            self.props[child] = value

    def do_get_child_property(self, child, property_id, pspec):
        if pspec.name == 'dumb-prop':
            return self.props[child]

MyContainer.install_child_property(1,
                                   ('dumb_prop',
                                    gobject.TYPE_STRING,
                                    'Dumb Prop',
                                    'Dumb Property for testing purposes',
                                    '', gobject.PARAM_READWRITE))

class MyAlignment(gtk.Alignment):

    def __init__(self, caption):
        self.caption = gtk.Label()
        self.caption.set_markup('<b>%s</b>' % gobject.markup_escape_text(caption))

        gtk.Alignment.__init__(self)

        self.caption.set_parent(self)

    def do_forall(self, include_internals, callback, callback_data):
        callback(self.caption, callback_data)
        gtk.Alignment.do_forall(self, include_internals, callback, callback_data)

# FIXME: Why is it needed?
gobject.type_register(MyAlignment)

class FocusContainer(gtk.HBox):

    # Just call super.
    def do_set_focus_child(self, widget):
        gtk.HBox.do_set_focus_child(self, widget)

gobject.type_register(FocusContainer)

class FocusWindow(gtk.Window):

    # Just call super.
    def do_set_focus(self, focus):
        gtk.Window.do_set_focus(self, focus)

gobject.type_register(FocusWindow)

class ContainerTest(unittest.TestCase):

    def testChildProperties(self):
        obj = MyContainer()
        label = gtk.Label()
        obj.add(label)
        v = 'dumb value'
        obj.child_set_property(label, 'dumb_prop', v)
        self.assertEqual(v, obj.child_get_property(label, 'dumb_prop'))

    def testSuperclassForAll(self):
        alignment = MyAlignment('test')
        label = gtk.Label('foo')
        alignment.add(label)
        alignment.show_all()

        self.assert_(label.flags() & gtk.VISIBLE)
        self.assert_(alignment.caption.flags() & gtk.VISIBLE)

    def testFocusSignalHandlers(self):
        button = gtk.Button()
        container = FocusContainer()
        window = FocusWindow()
        container.add(button)
        window.add(container)
        window.show_all()

        button.grab_focus()
        self.assert_(button.is_focus())

        window.set_focus(None)
        self.assert_(window.get_focus() is None)

        window.set_focus(button)
        self.assert_(window.get_focus() == button)

        window.destroy()

if __name__ == '__main__':
    unittest.main()
