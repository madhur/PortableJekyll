import unittest

from common import gtk, gobject
import weakref
import gc

class TestGlade(unittest.TestCase):

    class SimpleTest:
        def __init__(self, test):
            xml = gtk.glade.XML('leak.glade')
            xml.signal_autoconnect(self)
            self.test = test
            self.window = xml.get_widget("window1")
            self.window.destroy()
        def on_window1_destroy(self, window):
            gobject.idle_add(self.test.leak_check, weakref.ref(self), weakref.ref(self.window))

    def leak_check(self, objref, windowref):
        while gc.collect():
            pass
        gtk.main_quit()
        self.assertEqual(objref(), None)
        self.windowref = windowref

    def testAutoconnectLeak(self):
        self.SimpleTest(self)
        gtk.main()
        self.assertEqual(self.windowref(), None)


if __name__ == '__main__':
    unittest.main()
