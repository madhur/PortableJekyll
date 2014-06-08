import os
import sys
import unittest

from common import gobject, gtk

class APITest(unittest.TestCase):
    def testKeysyms(self):
        self.failUnless('Escape' in dir(gtk.keysyms))
        self.failUnless(hasattr(gtk.keysyms, 'Escape'))
        self.assertEqual(gtk.keysyms.Escape, 0xFF1B)

    def testWindow(self):
        self.failUnless(hasattr(gtk, 'Window'))
        self.failUnless(issubclass(gtk.Window, gobject.GObject))
        self.failUnless(issubclass(gtk.Window, gtk.Object))
        self.failUnless(issubclass(gtk.Window, gtk.Widget))
        self.failUnless(issubclass(gtk.Window, gtk.Container))
        self.failUnless(issubclass(gtk.Window, gtk.Bin))
        w = gtk.Window()
        self.failUnless(isinstance(w, gtk.Window))

    def testAccelLabel(self):
        ra = gtk.RadioMenuItem(None, 'label')
        self.failUnless(hasattr(ra.get_child(), 'get_text'))
        self.assertEqual(ra.get_child().get_text(), 'label')

    def testGlade(self):
        self.failUnless(hasattr(gtk.glade, 'XML'))
        self.failUnless(issubclass(gtk.glade.XML, gobject.GObject))

    def testReload(self):
        # test for #349026
        del sys.modules['gtk']
        import gtk
        reload(gtk)
