###############################################################################
# Name: ed_mpane.py                                                           #
# Purpose: Main panel containing notebook and command bar.                    #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2008 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
This module provides the L{MainPanel} component. That contains the editors main
notebook and command bar. 

@summary: Main Panel

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: ed_mpane.py 69061 2011-09-11 17:04:41Z CJP $"
__revision__ = "$Revision: 69061 $"

#-----------------------------------------------------------------------------#
# Imports
import wx

# Editra Libraries
import ed_glob
import ed_pages
import ed_cmdbar
import eclib

#-----------------------------------------------------------------------------#

class MainPanel(eclib.ControlBox):
    """Main panel view
    @todo: Add interface for registering additional commandbars.

    """
    def __init__(self, parent):
        """Initialize the panel"""
        super(MainPanel, self).__init__(parent)

        # Attributes
        self.nb = ed_pages.EdPages(self)
        self._bars = dict()

        # Layout
        self.SetWindow(self.nb)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEB)

    def OnEB(self, evt):
        """Empty method to fix notebook flashing issue on MSW"""
        pass

    def GetNotebook(self):
        """Get the main notebook control
        @return: EdPages instance

        """
        return self.nb

    def HideCommandBar(self):
        """Hide the command bar"""
        bar = self.GetControlBar(wx.BOTTOM)
        if bar:
            bar.Hide()
        self.Layout()

    def ShowCommandControl(self, ctrlid):
        """Change the mode of the commandbar
        @param ctrlid: CommandBar control id

        """
        cur_bar = self.GetControlBar(wx.BOTTOM)
        if ctrlid in self._bars:
            nbar = self._bars[ctrlid]
        else:
            nbar = ed_cmdbar.CommandBarBase.FactoryCreate(ctrlid, self)
            if nbar:
                self._bars[ctrlid] = nbar

        if nbar and nbar is not cur_bar:
            if cur_bar is None:
                self.SetControlBar(nbar, wx.BOTTOM)
            else:
                cur_bar = self.ReplaceControlBar(nbar, wx.BOTTOM)

        if cur_bar:
            if cur_bar is not nbar:
                cur_bar.Hide()

        cbar = self.GetControlBar(wx.BOTTOM)
        if cbar is not None:
            cbar.Show()
            cbar.Layout()
            cbar.SetFocus()

        self.Layout()
