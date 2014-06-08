# -*- Mode: Python -*-

import unittest

from common import gtk


class Tests(unittest.TestCase):

    def test_constructor(self):
        """ Test GdkColor creation """

        c = gtk.gdk.Color(1, 2, 3)
        self.assertEqual(c.red, 1)
        self.assertEqual(c.green, 2)
        self.assertEqual(c.blue, 3)

        c = gtk.gdk.Color(1.0, 0.7, 0.2)
        self.assertAlmostEqual(c.red_float, 1.0, 4)
        self.assertAlmostEqual(c.green_float, 0.7, 4)
        self.assertAlmostEqual(c.blue_float, 0.2, 4)

        # Mixing integers and floats is not allowed.
        self.assertRaises(TypeError, lambda: gtk.gdk.Color(0, 0.5))

        c = gtk.gdk.Color(pixel=0xffff)
        self.assertEqual(c.pixel, 0xffff)

        c = gtk.gdk.Color(pixel=0xffffL)
        self.assertEqual(c.pixel, 0xffff)

        c = gtk.gdk.Color(pixel=0xffffffffL)
        self.assertEqual(c.pixel, 0xffffffffL)

        c = gtk.gdk.Color('red')
        self.assertEqual(c.red, 65535)
        self.assertEqual(c.green, 0)
        self.assertEqual(c.blue, 0)

        c = gtk.gdk.Color('#ff0000')
        self.assertEqual(c.red, 65535)
        self.assertEqual(c.green, 0)
        self.assertEqual(c.blue, 0)

        self.assertRaises(TypeError, lambda: gtk.gdk.Color([]))

    def test_color_from_hsv(self):
        self.assertEqual(gtk.gdk.Color('red'), gtk.gdk.color_from_hsv(0.0, 1.0, 1.0))

    # See bug #594347.
    def test_color_from_hsv_kwargs(self):
        self.assertEqual(gtk.gdk.Color('black'), gtk.gdk.color_from_hsv(hue=0.0,
                                                                        saturation=0.0,
                                                                        value=0.0))

    def test_float_attributes(self):
        c = gtk.gdk.Color(0, 10000, 65535)
        self.assertAlmostEqual(c.red_float, 0.0)
        self.assertAlmostEqual(c.green_float, 10000.0 / 65535.0)
        self.assertAlmostEqual(c.blue_float, 1.0)

        c.red_float = 0.57
        self.assert_(c.red == int(0.57 * 65535) or c.red == int(0.57 * 65535) + 1)
        self.assertAlmostEqual(c.red_float, 0.57, 4)

        c.green = 12345
        self.assertAlmostEqual(c.green_float, 12345.0 / 65535.0)

    def test_hue(self):
        self.assertAlmostEqual(gtk.gdk.Color('red').hue, 0 * 1.0 / 6)
        self.assertAlmostEqual(gtk.gdk.Color('yellow').hue, 1 * 1.0 / 6)
        self.assertAlmostEqual(gtk.gdk.Color('green').hue, 2 * 1.0 / 6)
        self.assertAlmostEqual(gtk.gdk.Color('cyan').hue, 3 * 1.0 / 6)
        self.assertAlmostEqual(gtk.gdk.Color('blue').hue, 4 * 1.0 / 6)
        self.assertAlmostEqual(gtk.gdk.Color('magenta').hue, 5 * 1.0 / 6)

    def test_saturation(self):
        self.assertAlmostEqual(gtk.gdk.Color('red').saturation, 1.0)
        self.assertAlmostEqual(gtk.gdk.Color('gray').saturation, 0.0)

    def test_value(self):
        self.assertAlmostEqual(gtk.gdk.Color('black').value, 0.0)
        self.assertAlmostEqual(gtk.gdk.Color('white').value, 1.0)

    def test_equal(self):
        self.assertEqual(gtk.gdk.Color(0, 0, 0), gtk.gdk.Color(0, 0, 0))
        self.assertEqual(gtk.gdk.Color(100, 200, 300), gtk.gdk.Color(100, 200, 300))
        self.assertEqual(gtk.gdk.Color('#abc'), gtk.gdk.Color('#aabbcc'))
        self.assertEqual(gtk.gdk.Color('#100020003000'), gtk.gdk.Color(0x1000, 0x2000, 0x3000))

    def test_not_equal(self):
        self.assertNotEqual(gtk.gdk.Color('red'), gtk.gdk.Color('blue'))
        self.assertNotEqual(gtk.gdk.Color(1, 0, 0), gtk.gdk.Color(0, 0, 0))
        self.assertNotEqual(gtk.gdk.Color(0, 1, 0), gtk.gdk.Color(0, 0, 0))
        self.assertNotEqual(gtk.gdk.Color(0, 0, 1), gtk.gdk.Color(0, 0, 0))

    def test_non_hashable(self):
        self.assertRaises(TypeError, lambda: hash(gtk.gdk.Color()))

        def dict_key():
            {} [gtk.gdk.Color()] = 'must raise'
        self.assertRaises(TypeError, dict_key)

    def test_repr(self):
        for color in self._test_color_list():
            self.assertEqual(color, eval(repr(color)))

    def test_str(self):
        for color in self._test_color_list():
            self.assertEqual(color, gtk.gdk.Color(str(color)))

    def _test_color_list(self):
        return [gtk.gdk.Color(),
                gtk.gdk.Color(10, 20, 30),
                gtk.gdk.Color(65535, 65535, 65535),
                gtk.gdk.Color('red'),
                gtk.gdk.Color('#aaa'),
                gtk.gdk.Color('#f0a000'),
                gtk.gdk.Color('#123abcdef'),
                gtk.gdk.Color('#123412341234'),
                gtk.gdk.Color('#fedcfedcfedc')]


if __name__ == '__main__':
    unittest.main()
