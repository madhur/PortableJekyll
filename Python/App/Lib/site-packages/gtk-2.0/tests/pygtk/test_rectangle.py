# -*- Mode: Python -*-

import unittest

from common import gtk


class Tests(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(gtk.gdk.Rectangle(0, 0, 1, 1), gtk.gdk.Rectangle(0, 0, 1, 1))

    def test_not_equal(self):
        self.assertNotEqual(gtk.gdk.Rectangle(1, 0, 10, 10), gtk.gdk.Rectangle(0, 0, 10, 10))
        self.assertNotEqual(gtk.gdk.Rectangle(0, 1, 10, 10), gtk.gdk.Rectangle(0, 0, 10, 10))
        self.assertNotEqual(gtk.gdk.Rectangle(0, 0, 11, 10), gtk.gdk.Rectangle(0, 0, 10, 10))
        self.assertNotEqual(gtk.gdk.Rectangle(0, 0, 10, 11), gtk.gdk.Rectangle(0, 0, 10, 10))

    def test_non_hashable(self):
        self.assertRaises(TypeError, lambda: hash(gtk.gdk.Rectangle()))

        def dict_key():
            {} [gtk.gdk.Rectangle()] = 'must raise'
        self.assertRaises(TypeError, dict_key)

    def test_repr(self):
        for rectangle in self._test_rectangle_list():
            self.assertEqual(rectangle, eval(repr(rectangle)))

    def _test_rectangle_list(self):
        return [gtk.gdk.Rectangle(),
                gtk.gdk.Rectangle(0, 0, 100, 100),
                gtk.gdk.Rectangle(-10, 10, 30, 50),
                gtk.gdk.Rectangle(-100, -100, 20, 25),
                gtk.gdk.Rectangle(0, 0, 0, 20),
                gtk.gdk.Rectangle(1, 1, 20, 0)]


if __name__ == '__main__':
    unittest.main()
