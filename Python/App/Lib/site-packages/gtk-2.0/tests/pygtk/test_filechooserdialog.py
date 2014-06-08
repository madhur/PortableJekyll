import unittest

from common import gtk

class FileChooserDialogTest(unittest.TestCase):
    def testFileChooserDialog(self):
        fc = gtk.FileChooserDialog()
        
        action = fc.get_action()
        self.assertEqual(action, gtk.FILE_CHOOSER_ACTION_OPEN)

if __name__ == '__main__':
    unittest.main()
