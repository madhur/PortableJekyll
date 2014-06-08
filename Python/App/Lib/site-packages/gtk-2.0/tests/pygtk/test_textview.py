import unittest

from common import gtk


class TextIterTest(unittest.TestCase):
    def test_assign(self):
        buffer = gtk.TextBuffer()
        buffer.insert(buffer.get_start_iter(), 'blablabla')

        iter1, iter2 = buffer.get_bounds()
        self.assert_(iter1 is not iter2)
        self.assertNotEqual(iter1.get_offset(), iter2.get_offset())

        iter2.assign(iter1)
        self.assert_(iter1 is not iter2)
        self.assertEqual(iter1.get_offset(), iter2.get_offset())

class TextViewTest(unittest.TestCase):
    def test_default_attributes(self):
        textview = gtk.TextView()
        attrs = textview.get_default_attributes()
        textview.destroy()
        self.assertEqual(attrs.font_scale, 1.0)

if __name__ == '__main__':
    unittest.main()
