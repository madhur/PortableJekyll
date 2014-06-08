import unittest

from common import gtk

class TreeViewTest(unittest.TestCase):
    # Check for #350252
    # Cooment out this test until we get a response
    # on bug #546005 and #498010
    #
    #def test_default_attributes(self):
    #    model = gtk.ListStore(str)
    #    treeview = gtk.TreeView(model)
    #    treeview.set_cursor(1)

    # Bug #347273
    def testTreeSelectionForeach(self):
        model = gtk.ListStore(str)
        treeview = gtk.TreeView(model)
        sel = treeview.get_selection()
        iter_ = model.append()
        model.set_value(iter_, 0, "foo")
        sel.select_path((0,))
        list_ = []
        sel.selected_foreach(lambda model, path, iter: list_.append(iter))
        list_ = [model.get_value(iter_, 0) for iter_ in list_]
        self.assertEqual(list_, ["foo"])


if __name__ == '__main__':
    unittest.main()
