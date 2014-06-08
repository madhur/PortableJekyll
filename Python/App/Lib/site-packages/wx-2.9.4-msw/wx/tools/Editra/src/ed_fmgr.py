###############################################################################
# Name: ed_fmgr.py                                                            #
# Purpose: Editra's Main Window Frame Manager                                 #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2011 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""


"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id:  $"
__revision__ = "$Revision:  $"

#--------------------------------------------------------------------------#
# Dependencies
import wx
#import wx.lib.agw.aui as aui
import wx.aui as aui

#--------------------------------------------------------------------------#
# Events

EVT_AUI_PANE_CLOSE = aui.EVT_AUI_PANE_CLOSE
EVT_AUI_PANE_RESTORE = aui.EVT_AUI_PANE_RESTORE

#--------------------------------------------------------------------------#

class EdFrameManager(aui.AuiManager):
    """Frame manager for external components to abstract underlying manager"""
    def __init__(self, wnd=None, flags=0):
        """Create the frame manager object
        @param wnd: Frame to manage
        @param flags: frame manager flags

        """
        super(EdFrameManager, self).__init__(wnd, flags)
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
        self.Bind(aui.EVT_AUI_PANE_RESTORE, self.OnPaneRestore)

    def OnPaneClose(self, evt):
        """Notify pane it is being closed"""
#        pane = evt.GetPane()
#        print "Close", pane.window
#        nevt = wx.ShowEvent(pane.window.Id, False)
#        wx.PostEvent(pane.window, nevt)
        evt.Skip()

    def OnPaneRestore(self, evt):
        """Notify pane it is being opened"""
#        pane = evt.GetPane()
#        print "Restore:", pane.window
#        nevt = wx.ShowEvent(pane.window.Id, True)
#        wx.PostEvent(pane.window, nevt)
        evt.Skip()

    def AddPane(self, wnd, info=None, caption=None):
        return super(EdFrameManager, self).AddPane(wnd, info, caption)

    def IsEditorMaximized(self):
        """Is the editor pane maximized?
        return: bool

        """
        bEditMax = True
        # If any other pane is open then the editor is not maximized
        for pane in self.GetAllPanes():
            if pane.IsShown() and pane.name != "EditPane":
                bEditMax = False
                break
        return bEditMax

#--------------------------------------------------------------------------#

EdPaneInfo = aui.AuiPaneInfo
#    """Frame manager panel info"""
#    def __init__(self):
#        super(EdPaneInfo, self).__init__()
