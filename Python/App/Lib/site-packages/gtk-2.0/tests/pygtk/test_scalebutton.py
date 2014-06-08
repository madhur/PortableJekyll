import unittest

from common import gtk

class ScaleButtonTest(unittest.TestCase):
    def test_constructor(self):
        scalebutt = gtk.ScaleButton(gtk.ICON_SIZE_SMALL_TOOLBAR, 0, 873, 2)
        adj = scalebutt.props.adjustment
        self.assertEqual(adj.step_increment, 2)

    def test_set_icons(self):
        scalebutt = gtk.ScaleButton(gtk.ICON_SIZE_SMALL_TOOLBAR, 0, 873, 2)
        icons = [gtk.STOCK_QUIT, gtk.STOCK_CANCEL, gtk.STOCK_EXECUTE]
        scalebutt.set_icons(icons)
        self.assertEqual(scalebutt.props.icons, icons)        

if __name__ == '__main__':
    unittest.main()
