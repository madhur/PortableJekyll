import unittest

from common import pango

class MarkupTest(unittest.TestCase):
    def testMarkupAccelMarker(self):
        self.assertRaises(TypeError, pango.parse_markup, 'test', 0)
        self.assertEqual(pango.parse_markup('test')[2], u'\x00')
        self.assertEqual(pango.parse_markup('test', u't')[2], u'e')


class TestColor(unittest.TestCase):
    def testStr(self):
        col = pango.Color('red')
        self.assertEqual(str(col), '#ffff00000000')


class TestLanguage(unittest.TestCase):
    def testStr(self):
        lang = pango.Language('sv')
        self.assertEqual(str(lang), 'sv')


class TestFontDescription(unittest.TestCase):
    def testStr(self):
        fontdescr = pango.FontDescription('monospace 10')
        self.assertEqual(str(fontdescr), 'monospace 10')

    def testHash(self):
        fontdescr = pango.FontDescription('monospace 10')
        fontdescr2 = pango.FontDescription('monospace 10')
        self.assertEqual(hash(fontdescr), hash(fontdescr2))

    def testEquals(self):
        fontdescr = pango.FontDescription('monospace 10')
        fontdescr2 = pango.FontDescription('monospace 10')
        fontdescr3 = pango.FontDescription('monospace 12')
        self.assertEqual(fontdescr, fontdescr2)
        self.assertNotEqual(fontdescr, fontdescr3)
