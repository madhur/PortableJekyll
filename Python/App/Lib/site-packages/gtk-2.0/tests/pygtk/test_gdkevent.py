# -*- Mode: Python -*-

import unittest

from common import gtk

class TestGdkEvent(unittest.TestCase):
    def testWindowSetter(self):
        event = gtk.gdk.Event(gtk.gdk.BUTTON_PRESS)

        win1 = gtk.Window()
        win1.realize()
        event.window = win1.window
        self.assertEqual(event.window, win1.window)

        win2 = gtk.Window()
        win2.realize()
        event.window = win2.window
        self.assertEqual(event.window, win2.window)

    # Bug #408658.
    def testEventTime(self):
        event = gtk.gdk.Event(gtk.gdk.MOTION_NOTIFY)
        event.time = 0x80000000

        # According to GTK+ source files, 'time' field is always of
        # 'guint32' type, so we must always have overflow here.
        self.assert_(event.time == -0x80000000)

if __name__ == '__main__':
    unittest.main()
