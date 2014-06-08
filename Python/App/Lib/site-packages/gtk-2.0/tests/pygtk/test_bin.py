import unittest

from common import gtk

class MyBin(gtk.Bin):
    __gtype_name__ = 'MyBin'
    def __init__(self):
        gtk.Bin.__init__(self)

class BinTest(unittest.TestCase):
    def testSet(self):
        bin = MyBin()
        self.assertEqual(bin.child, None)
        child = gtk.Label()
        bin.child = child
        self.assertEqual(bin.child, child)
        bin.child = None
        self.assertEqual(bin.child, None)
