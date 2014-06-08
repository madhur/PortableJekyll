import unittest

from common import gtk, gobject

class AccelClosures(unittest.TestCase):

    def testListAccelClosures(self):
        group = gtk.AccelGroup()
        window = gtk.Window()
        window.add_accel_group(group)
        button = gtk.Button()
        window.add(button)
        button.add_accelerator("clicked", group, gtk.keysyms.x, gtk.gdk.CONTROL_MASK, 0)
        for closure in button.list_accel_closures():
            group1 = gtk.accel_group_from_accel_closure(closure)
            self.assert_(group1 is group)
        window.destroy()

if __name__ == '__main__':
    unittest.main()
