###############################################################################
# Name: ecbasewin.py                                                          #
# Purpose: Eclib Base Window Classes                                          #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2009 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
Editra Control Library: Base Window Classes


"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: ecbasewin.py 69410 2011-10-13 14:20:12Z CJP $"
__revision__ = "$Revision: 69410 $"

__all__ = ["ECBaseDlg", "expose"]

#-----------------------------------------------------------------------------#
# Imports
import wx

#-----------------------------------------------------------------------------#
# Decorators

class expose(object):
    """Expose a panels method to a to a specified class
    The specified class must have a GetPanel method

    """
    def __init__(self, cls):
        """@param cls: class to expose the method to"""
        super(expose, self).__init__()
        self.cls = cls

    def __call__(self, funct):
        fname = funct.func_name
        def parentmeth(*args, **kwargs):
            self = args[0]
            return getattr(self.GetPanel(), fname)(*args[1:], **kwargs)
        parentmeth.__name__ = funct.__name__
        parentmeth.__doc__ = funct.__doc__
        setattr(self.cls, fname, parentmeth)

        return funct

#-----------------------------------------------------------------------------#

class ECBaseDlg(wx.Dialog):
    """Editra Control Library Base Dialog Class"""
    def __init__(self, parent, id=wx.ID_ANY, title=u"",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, 
                 style=wx.DEFAULT_DIALOG_STYLE, name=u"ECBaseDialog"):
        super(ECBaseDlg, self).__init__(parent, id, title, pos,
                                        size, style, name)

        # Attributes
        self._panel = None

        # Setup
        self.SetSizer(wx.BoxSizer(wx.VERTICAL))

    Panel = property(lambda self: self.GetPanel(),
                     lambda self, val: self.SetPanel(val))

    def GetPanel(self):
        """Get the dialogs main panel"""
        return self._panel

    def SetPanel(self, panel):
        """Set the dialogs main panel"""
        assert isinstance(panel, wx.Panel)
        if self._panel is not None:
            self._panel.Destroy()
        self._panel = panel
        self.Sizer.Add(self._panel, 1, wx.EXPAND)
