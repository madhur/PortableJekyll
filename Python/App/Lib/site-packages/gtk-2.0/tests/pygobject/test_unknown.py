# -*- Mode: Python -*-

import unittest

import gobject
import testhelper


TestInterface = gobject.GType.from_name('TestInterface')


class TestUnknown(unittest.TestCase):
    def testFoo(self):
        obj = testhelper.get_unknown()
        TestUnknownGType = gobject.GType.from_name('TestUnknown')
        TestUnknown = gobject.new(TestUnknownGType).__class__
        assert isinstance(obj, testhelper.Interface)
        assert isinstance(obj, TestUnknown)
