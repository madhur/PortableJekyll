###############################################################################
# Name: ed_book.py                                                            #
# Purpose: Editra notebook base class                                         #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2011 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
Base class for the main tab controls

@summary: Tabbed book control base classes

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: ed_book.py 69245 2011-09-30 17:52:23Z CJP $"
__revision__ = "$Revision: 69245 $"

#-----------------------------------------------------------------------------#
# Imports
import wx

# Editra Imports
import extern.aui as aui
import ed_msg
from profiler import Profile_Get

#-----------------------------------------------------------------------------#

class EdBaseBook(aui.AuiNotebook):
    """Base notebook control"""
    def __init__(self, parent, style=0):
        style |= self.GetBaseStyles()
        super(EdBaseBook, self).__init__(parent, agwStyle=style)
        if wx.Platform == '__WXGTK__':
            self.SetArtProvider(GtkTabArt())

        # Setup
        self.UpdateFontSetting()
        font = wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.PointSize += 2
        self.NavigatorProps.Font = font
        self.NavigatorProps.MinSize = wx.Size(300, 250)
        self.SetSashDClickUnsplit(True)

        # Message Handlers
        ed_msg.Subscribe(self.OnUpdateFont, ed_msg.EDMSG_DSP_FONT)

        # Event Handlers
        self.Bind(wx.EVT_WINDOW_DESTROY, self._OnDestroy, self)

    def _OnDestroy(self, evt):
        """Unsubscribe message handlers on delete"""
        if self and evt.GetEventObject() is self:
            ed_msg.Unsubscribe(self.OnUpdateFont)
        evt.Skip()

    @staticmethod
    def GetBaseStyles():
        """Get the common base style flags
        @return: bitmask

        """
        style = aui.AUI_NB_NO_TAB_FOCUS
        if wx.Platform == '__WXMAC__':
            style |= aui.AUI_NB_CLOSE_ON_TAB_LEFT
        return style

    def OnUpdateFont(self, msg):
        """Update the font settings for the control in response to
        user settings change.

        """
        if self:
            self.UpdateFontSetting()

    def SetPageBitmap(self, pg, bmp):
        """Set a tabs bitmap
        @param pg: page index
        @param bmp: Bitmap
        @note: no action if user prefs have turned off bmp

        """
        if not self.UseIcons():
            bmp = wx.NullBitmap
        super(EdBaseBook, self).SetPageBitmap(pg, bmp)

    def UpdateFontSetting(self):
        """Update font setting using latest profile data"""
        font = Profile_Get('FONT3', 'font', None)
        if font:
            self.SetFont(font)

    def UseIcons(self):
        """Is the book using tab icons?"""
        bUseIcons = Profile_Get('TABICONS', default=True)
        return bUseIcons

#-----------------------------------------------------------------------------#

class GtkTabArt(aui.VC71TabArt):
    """Simple tab art with no gradients"""
    def __init__(self):
        super(GtkTabArt, self).__init__()

    def DrawBackground(self, dc, wnd, rect):
        """
        Draws the tab area background.

        :param `dc`: a `wx.DC` device context;
        :param `wnd`: a `wx.Window` instance object;
        :param `rect`: the tab control rectangle.
        """
        self._buttonRect = wx.Rect()

        # draw background
        r = wx.Rect(rect.x, rect.y, rect.width+2, rect.height)

        # draw base lines
        dc.SetPen(self._border_pen)
        dc.SetBrush(self._base_colour_brush)
        dc.DrawRectangleRect(r)
