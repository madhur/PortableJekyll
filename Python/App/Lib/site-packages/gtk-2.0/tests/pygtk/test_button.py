import unittest

from common import gtk

class TextButton(unittest.TestCase):
    # Bug #524187.
    def test_constructor(self):
        button = gtk.Button()
        self.assert_(button.props.use_underline)

if __name__ == '__main__':
    unittest.main()
