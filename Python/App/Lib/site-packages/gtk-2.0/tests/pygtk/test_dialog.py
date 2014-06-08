import sys
import unittest
import gc
import weakref

from common import gtk

class MessageDialogTest(unittest.TestCase):
    def testDialogAdd(self):
        dialog = gtk.MessageDialog()

        response_id = sys.maxint + 1
        self.assertRaises(OverflowError, dialog.add_button, "Foo", response_id)
        self.assertRaises(OverflowError, dialog.add_buttons, "Foo", response_id)

    def testSubclass(self):
        # Normal subclassing should not register a type
        sub = type('sub', (gtk.MessageDialog,), {})
        print sub.__gtype__
        print sub.__gtype__.name
        self.assertEqual(sub.__gtype__.name, 'GtkMessageDialog')

        type('Sub', (gtk.MessageDialog,), {'__gtype_name__': 'SubDialog'})
        self.assertEqual(sub.__gtype__.name, 'SubDialog')

    def testDialogLeak(self):
        dlg = gtk.Dialog()
        dlg.destroy()
        ref = weakref.ref(dlg)
        del dlg
        while gc.collect():
            pass
        self.assertEqual(ref(), None)

if __name__ == '__main__':
    unittest.main()
