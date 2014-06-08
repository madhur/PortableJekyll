# -*- Mode: Python -*-

import unittest

import gobject
import testhelper


GUnknown = gobject.type_from_name("TestUnknown")
Unknown = GUnknown.pytype


class MyUnknown(Unknown, testhelper.Interface):
    some_property = gobject.property(type=str)

    def __init__(self):
        Unknown.__init__(self)
        self.called = False

    def do_iface_method(self):
        self.called = True
        Unknown.do_iface_method(self)
gobject.type_register(MyUnknown)


class MyObject(gobject.GObject, testhelper.Interface):
    some_property = gobject.property(type=str)

    def __init__(self):
        gobject.GObject.__init__(self)
        self.called = False

    def do_iface_method(self):
        self.called = True
gobject.type_register(MyObject)


class TestIfaceImpl(unittest.TestCase):

    def testReImplementInterface(self):
        m = MyUnknown()
        m.iface_method()
        self.assertEqual(m.called, True)

    def testImplementInterface(self):
        m = MyObject()
        m.iface_method()
        self.assertEqual(m.called, True)

