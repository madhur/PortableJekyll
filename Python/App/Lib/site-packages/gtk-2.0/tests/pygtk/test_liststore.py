import unittest

from common import gtk

class ListStoreTest(unittest.TestCase):
    def testConstructor(self):
        self.assertRaises(TypeError, gtk.ListStore)

    def testInsert(self):
        store = gtk.ListStore(int)

        # Old way, with iters
        store.set_value(store.insert(0), 0, 2)
        self.assertEqual(len(store), 1)
        self.assertEqual(store[0][0], 2)

        # New way
        store.insert(0, (1,))
        self.assertEqual(len(store), 2)
        self.assertEqual(store[0][0], 1)
        self.assertEqual(store[1][0], 2)

    # TreeSortable, but...

    def testSetDefaultSortFunc(self):
        store = gtk.ListStore(int)
        self.assertFalse(store.has_default_sort_func())
        store.set_default_sort_func(lambda x: None)
        store.set_sort_column_id(0, gtk.SORT_ASCENDING)

        self.assertTrue(store.has_default_sort_func())
        store.set_default_sort_func(None)
        self.assertFalse(store.has_default_sort_func())

    # Two tests for bug 537459.  Since it is a memory corruption, we
    # use a large loop count hoping to trigger a segfault.

    def testNegativeIndexGet(self):
        store = gtk.ListStore(int)
        for i in range(200):
            store.append((i,))
            self.assertEqual(store[-1][0], i)

    def testNegativeIndexSet(self):
        store = gtk.ListStore(int)
        for i in range(200):
            store.append((i,))
            del store[-1]
            self.assert_(len(store) == 0)



if __name__ == '__main__':
    unittest.main()
