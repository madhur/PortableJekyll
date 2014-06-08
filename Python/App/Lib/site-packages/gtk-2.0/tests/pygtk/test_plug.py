import unittest

from common import gtk

class TextPlug(unittest.TestCase):

    # Bug #539365.  Just check that it doesn't raise anything.
    def test_constructor_socket_id(self):
        self.assert_(isinstance(gtk.Plug(0), gtk.Plug))
        self.assert_(isinstance(gtk.Plug(0L), gtk.Plug))

if __name__ == '__main__':
    unittest.main()
