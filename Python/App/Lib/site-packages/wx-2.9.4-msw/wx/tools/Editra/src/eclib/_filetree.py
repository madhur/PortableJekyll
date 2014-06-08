###############################################################################
# Name: _dirtree.py                                                           #
# Purpose: Directory Tree                                                     #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2011 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows Licence                                                  #
###############################################################################

"""
Editra Control Library: FileTree

Base class control for displaying a file system in a hierarchical manor.

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: _filetree.py 71698 2012-06-08 15:51:35Z CJP $"
__revision__ = "$Revision: 71698 $"

__all__ = ['FileTree',]

#-----------------------------------------------------------------------------#
# Imports
import sys
import os
import types
import wx

#-----------------------------------------------------------------------------#

class FileTree(wx.TreeCtrl):
    """Simple base control for displaying directories and files in a
    hierarchical view.

    """
    def __init__(self, parent):
        super(FileTree, self).__init__(parent,
                                       style=wx.TR_HIDE_ROOT|
                                             wx.TR_FULL_ROW_HIGHLIGHT|
                                             wx.TR_LINES_AT_ROOT|
                                             wx.TR_HAS_BUTTONS|
                                             wx.TR_MULTIPLE|
                                             wx.TR_EDIT_LABELS)

        # Attributes
        self._watch = list() # Root directories to watch
        self._il = None
        self._editlabels = True

        # Setup
        self.SetupImageList()
        self.AddRoot('root')
        self.SetPyData(self.RootItem, "root")

        # Event Handlers
        self.Bind(wx.EVT_TREE_ITEM_GETTOOLTIP, self._OnGetToolTip)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self._OnItemActivated)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self._OnItemCollapsed)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDING, self._OnItemExpanding)
        self.Bind(wx.EVT_TREE_ITEM_MENU, self._OnMenu)
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self._OnBeginEdit)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self._OnEndEdit)

    def _OnBeginEdit(self, evt):
        if not self._editlabels:
            evt.Veto()
        else:
            item = evt.GetItem()
            if self.DoBeginEdit(item):
                evt.Skip()
            else:
                evt.Veto()

    def _OnEndEdit(self, evt):
        if self._editlabels:
            item = evt.GetItem()
            newlabel = evt.GetLabel()
            if self.DoEndEdit(item, newlabel):
                evt.Skip()
                return
        evt.Veto()

    def _OnGetToolTip(self, evt):
        item = evt.GetItem()
        tt = self.DoGetToolTip(item)
        if tt:
            evt.ToolTip = tt
        else:
            evt.Skip()

    def _OnItemActivated(self, evt):
        item = evt.GetItem()
        self.DoItemActivated(item)
        evt.Skip()

    def _OnItemCollapsed(self, evt):
        item = evt.GetItem()
        self.DoItemCollapsed(item)
        evt.Skip()

    def _OnItemExpanding(self, evt):
        item = evt.GetItem()
        self.DoItemExpanding(item)
        evt.Skip()

    def _OnMenu(self, evt):
        item = evt.GetItem()
        self.DoShowMenu(item)

    #---- Properties ----#

    SelectedFiles = property(lambda self: self.GetSelectedFiles())

    #---- Overridable methods ----#

    def DoBeginEdit(self, item):
        """Overridable method that will be called when
        a user has started to edit an item.
        @param item: TreeItem
        return: bool (True == Allow Edit)

        """
        return False

    def DoEndEdit(self, item, newlabel):
        """Overridable method that will be called when
        a user has finished editing an item.
        @param item: TreeItem
        @param newlabel: unicode (newly entered value)
        return: bool (True == Change Accepted)

        """
        return False

    def DoGetToolTip(self, item):
        """Get the tooltip to show for an item
        @return: string or None

        """
        data = self.GetItemPyData(item)
        return data

    def DoItemActivated(self, item):
        """Override to handle item activation
        @param item: TreeItem

        """
        pass

    def DoItemCollapsed(self, item):
        """Handle when an item is collapsed
        @param item: TreeItem

        """
        self.DeleteChildren(item)

    def DoItemExpanding(self, item):
        """Handle when an item is expanding
        @param item: TreeItem

        """
        d = self.GetPyData(item)
        if d and os.path.exists(d):
            contents = FileTree.GetDirContents(d)
            for p in contents:
                self.AppendFileNode(item, p)

    def DoShowMenu(self, item):
        """Context menu has been requested for the given item.
        @param item: wx.TreeItem

        """
        pass

    def DoSetupImageList(self):
        """Add the images to the control's ImageList. It is guaranteed
        that self.ImageList is valid and empty when this is called.

        """
        bmp = wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_MENU, (16,16))
        self.ImageList.Add(bmp)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_MENU, (16,16))
        self.ImageList.Add(bmp)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_MENU, (16,16))
        self.ImageList.Add(bmp)

    def DoGetFileImage(self, path):
        """Get the index of the image from the image list to use
        for the file.
        @param path: Absolute path of file
        @return: long

        """
        # TODO: image handling
        if not os.access(path, os.R_OK):
            img = 2
        else:
            if os.path.isdir(path):
                img = 0 # Directory image
            else:
                img = 1 # Normal file image
        return img

    #---- End Overrides ----#

    #---- Properties ----#

    WatchDirs = property(lambda self: self._watch)

    #---- FileTree Api ---#

    def AddWatchDirectory(self, dname):
        """Add a directory to the controls top level view
        @param dname: directory path
        @return: TreeItem or None
        @todo: add additional api for getting already existing nodes based
               on path.

        """
        assert os.path.exists(dname), "Path(%s) doesn't exist!" % dname
        if dname not in self._watch:
            self._watch.append(dname)
            return self.AppendFileNode(self.RootItem, dname)

    def RemoveWatchDirectory(self, dname):
        """Remove a directory from the watch list
        @param dname: directory path

        """
        if dname in self._watch:
            self._watch.remove(dname)
            nodes = self.GetChildNodes(self.RootItem)
            for node in nodes:
                data = self.GetPyData(node)
                if dname == data:
                    self.Delete(node)
                    break

    def SetupImageList(self):
        """Setup/Refresh the control's ImageList.
        Override DoSetupImageList to customize the behavior of this method.

        """
        if self._il:
            self._il.Destroy()
            self._il = None
        self._il = wx.ImageList(16, 16)
        self.SetImageList(self._il)
        self.DoSetupImageList()

    def AppendFileNode(self, item, path):
        """Append a child node to the tree
        @param item: TreeItem parent node
        @param path: path to add to node
        @return: new node

        """
        img = self.DoGetFileImage(path)
        name = os.path.basename(path)
        if not name:
            name = path
        child = self.AppendItem(item, name, img)
        self.SetPyData(child, path)
        if os.path.isdir(path):
            self.SetItemHasChildren(child, True)
        return child

    def AppendFileNodes(self, item, paths):
        """Append a list of child node to the tree. This
        method can be used instead of looping on AppendFileNode
        to get slightly better performance for large sets.
        @param item: TreeItem parent node
        @param paths: list of file paths
        @return: None

        """
        getBaseName = os.path.basename
        isDir = os.path.isdir
        getImg = self.DoGetFileImage
        appendNode = self.AppendItem
        setData = self.SetPyData
        for path in paths:
            img = getImg(path)
            name = getBaseName(path)
            if not name:
                name = path
            child = appendNode(item, name, img)
            setData(child, path)
            if isDir(path):
                self.SetItemHasChildren(child, True)

    def GetChildNodes(self, parent):
        """Get all the TreeItemIds under the given parent
        @param parent: TreeItem
        @return: list of TreeItems

        """
        rlist = list()
        child, cookie = self.GetFirstChild(parent)
        if not child or not child.IsOk():
            return rlist

        rlist.append(child)
        while True:
            child, cookie = self.GetNextChild(parent, cookie)
            if not child or not child.IsOk():
                return rlist
            rlist.append(child)
        return rlist

    def GetExpandedNodes(self):
        """Get all nodes that are currently expanded in the view
        this logically corresponds to all parent directory nodes which
        are expanded.
        @return: list of TreeItems

        """

        def NodeWalker(parent, rlist):
            """Recursively find expanded nodes
            @param parent: parent node
            @param rlist: list (outparam)

            """
            children = self.GetChildNodes(parent)
            for node in children:
                if self.IsExpanded(node):
                    rlist.append(node)
                    NodeWalker(node, rlist)

        nodes = list()
        NodeWalker(self.RootItem, nodes)
        return nodes

    def GetSelectedFiles(self):
        """Get a list of the selected files
        @return: list of strings

        """
        nodes = self.GetSelections()
        files = [ self.GetPyData(node) for node in nodes ]
        return files

    def EnableLabelEditing(self, enable=True):
        """Enable/Disable label editing. This functionality is
        enabled by default.
        @keyword enable: bool

        """
        self._editlabels = enable

    def SelectFile(self, filename):
        """Select the given path
        @param filename: full path to select
        @return: bool

        """
        bSelected = False
        # Find the root
        for node in self.GetChildNodes(self.RootItem):
            dname = self.GetPyData(node)
            if not os.path.isdir(dname):
                dname = os.path.dirname(dname)
            if not dname.endswith(os.sep):
                dname += os.sep
            if filename.startswith(dname):
                filename = filename[len(dname):].split(os.sep)
                if not self.IsExpanded(node):
                    self.Expand(node)
                folder = node
                try:
                    while filename:
                        name = filename.pop(0)
                        for item in self.GetChildNodes(folder):
                            if self.GetItemText(item) == name:
                                if not self.IsExpanded(item):
                                    self.Expand(item)
                                folder = item
                                continue
                except:
                    pass

                self.UnselectAll()
                self.EnsureVisible(folder)
                self.SelectItem(folder)
                break

    #---- Static Methods ----#

    @staticmethod
    def GetDirContents(directory):
        """Get the list of files contained in the given directory"""
        assert os.path.isdir(directory)
        files = list()
        try:
            joinPath = os.path.join
            fappend = files.append
            fs_encoding = sys.getfilesystemencoding()
            for p in os.listdir(directory):
                fullpath = joinPath(directory, p)
                if type(fullpath) != types.UnicodeType:
                    fullpath = fullpath.decode(fs_encoding)
                fappend(fullpath)
        except OSError:
            pass
        return files

#-----------------------------------------------------------------------------#
# Test
if __name__ == '__main__':
    app = wx.App(False)
    f = wx.Frame(None)
    ft = FileTree(f)
    d = wx.GetUserHome()
    ft.AddWatchDirectory(d)
    f.Show()
    app.MainLoop()
