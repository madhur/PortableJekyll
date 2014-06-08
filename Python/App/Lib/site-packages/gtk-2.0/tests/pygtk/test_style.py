import unittest

from common import gtk

class StylePixmapTest(unittest.TestCase):
    def setUp(self):
        win = gtk.Window()
        win.realize()
        self.window = win.window
        self.bg_pixmap = win.style.bg_pixmap

    def _test(self, pixmap):
        self.bg_pixmap[gtk.STATE_NORMAL] = pixmap
        self.assertEqual(self.bg_pixmap[gtk.STATE_NORMAL], pixmap)

    def testNormal(self):
        self._test(gtk.gdk.Pixmap(self.window, 1, 1))

    def testNone(self):
        self._test(None)

    def testParentRelative(self):
        self._test(gtk.gdk.PARENT_RELATIVE)

    def testInvalid(self):
        func = self.bg_pixmap.__setitem__
        self.assertRaises(TypeError, func, gtk.STATE_NORMAL, True)
        self.assertRaises(TypeError, func, gtk.STATE_NORMAL, 0L)
        self.assertRaises(TypeError, func, gtk.STATE_NORMAL, object())
