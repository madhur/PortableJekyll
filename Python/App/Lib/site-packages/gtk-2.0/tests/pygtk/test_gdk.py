import unittest
import gc

from common import gtk, gobject

class CallOnDel:
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback()

class GdkTest(unittest.TestCase):
    def testBitmapCreateFromData(self):
        gtk.gdk.bitmap_create_from_data(None, '\x00', 1, 1)

    #def testPixmapCreateFromData(self):
    #    black = gtk.gdk.color_parse('black')
    #    gtk.gdk.pixmap_create_from_data(None, '\x00', 1, 1, 1,
    #                                    black, black)

    def _testWindow(self):
        common = {'finalized': False}
        def on_finalize():
            common['finalized'] = True
        w = gtk.gdk.Window(None, 200, 200, gtk.gdk.WINDOW_TEMP, 0, 0)
        w.set_data('foo', CallOnDel(on_finalize))
        w.destroy()
        while gtk.events_pending():
            gtk.main_iteration(block=False)
        del w

        # Note that this depends on the mainloop processing an X event so
        # if might fail if the timing is off
        while gc.collect():
            pass
        assert common['finalized']


    def testDrawIndexedImage(self):
        w = gtk.Window()
        w.realize()
        w.window.draw_indexed_image(gtk.gdk.GC(w.window),
                                    0, 0,
                                    1, 2,
                                    gtk.gdk.RGB_DITHER_NONE,
                                    '\x00\x01',
                                    1,
                                    [0xdeadbe, 0xbebabe])

    def _collect(self):
        cnt = 0
        while True:
            x = gc.collect()
            cnt += x
            if x == 0:
                break
        return cnt

    def testDisplay(self):
        while gc.collect():
            pass

        display = gtk.gdk.Display(None)
        if gobject.pygobject_version >= (2,13):
            dispref = display.weak_ref()
            del display
            self.assertEqual(dispref(), None)
        else:
            del display
            self.assertEquals(self._collect(), 1)

        display = gtk.gdk.Display(None)
        self.assertEquals(display.__grefcount__, 1)
        display.close()
        self.assertEquals(display.__grefcount__, 1)

        if gobject.pygobject_version >= (2,13):
            dispref = display.weak_ref()
            del display
            self.assertEqual(dispref(), None)
        else:
            del display
            self.assertEquals(self._collect(), 1)
