###############################################################################
# Name: _infobar.py                                                           #
# Purpose: Information Panel Class                                            #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2012 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows License                                                  #
###############################################################################

"""
Editra Control Library: InfoBar

Small information panel that can be used to replace popup modal dialogs.

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__cvsid__ = "$Id:  $"
__revision__ = "$Revision:  $"

__all__ = [ 'InfoBar', 'INFOBAR_INFO', 'INFOBAR_WARN', 'INFOBAR_ERROR' ]

#-----------------------------------------------------------------------------#
# Imports
import wx

# Local Imports
import eclutil

#-----------------------------------------------------------------------------#

INFOBAR_INFO, \
INFOBAR_WARN, \
INFOBAR_ERROR = range(3)

#-----------------------------------------------------------------------------#

class InfoBar(wx.PyPanel):
    """Information popup panel"""
    def __init__(self, parent, title=u"", message=u"",
                 msgType=INFOBAR_INFO,
                 style=wx.TAB_TRAVERSAL|wx.NO_BORDER):
        """Create the InfoBar"""
        super(InfoBar, self).__init__(parent, style=style)
        self.Hide() # Initially hidden

        # Attributes
        self._msgType = msgType

        # Controls
        self._bmp = wx.StaticBitmap(self)
        self._title = wx.StaticText(self, label=title)
        self._msg = wx.StaticText(self, label=message)
        self._okBtn = wx.Button(self, wx.ID_OK)
        self._cancelBtn = wx.Button(self, wx.ID_CANCEL)

        # Setup
        self.SetMessageType(msgType)
        tfont = self._title.Font
        tfont.SetWeight(wx.FONTWEIGHT_BOLD)
        tfont.SetPointSize(tfont.PointSize + 1)
        self._title.SetFont(tfont)
        self.__DoLayout()

        # Events
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        """Layout the panel"""
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Bitmap
        sizer.Add(self.Bitmap, 0, wx.ALL|wx.ALIGN_CENTER, 8)
        # Text
        txt_sz = wx.BoxSizer(wx.VERTICAL)
        txt_sz.Add(self.Title, 0, wx.ALL, 3)
        txt_sz.Add(self.Message, 0, wx.ALL, 3)
        sizer.Add(txt_sz, 0)
        # Padding
        sizer.AddStretchSpacer()
        # Buttons
        btnsz = wx.BoxSizer(wx.VERTICAL)
        btnsz.Add(self._okBtn, 0, wx.ALL|wx.ALIGN_CENTER, 3)
        btnsz.Add(self._cancelBtn, 0, wx.ALL|wx.ALIGN_CENTER, 3)
        sizer.Add(btnsz, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizer)

    def _UpdateParent(self):
        """Update parent for layout changes"""
        self.Parent.Layout()
        self.Parent.SendSizeEvent()

    #---- Properties ----#

    Bitmap = property(lambda self: self._bmp)
    Title = property (lambda self: self._title)
    Message = property(lambda self: self._msg)
    MessageType = property(lambda self: self._msgType,
                           lambda self, mtype: self.SetMessageType(mtype))
    ButtonOk = property(lambda self: self._okBtn)
    ButtonCancel = property(lambda self: self._cancelBtn)

    #---- Event Handlers ---#

    def OnButton(self, evt):
        """Handle button clicks"""
        self.Show(False)
        evt.Skip()

    #---- Implementation ----#

    def SetMessageType(self, msgType):
        """Set the message type
        @param msgType: INFOBAR_FOO identifier

        """
        bmp = wx.NullBitmap
        if msgType == INFOBAR_INFO:
            bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_CMN_DIALOG)
            self.SetBackgroundColour(wx.BLUE)
        elif msgType == INFOBAR_ERROR:
            bmp = wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_CMN_DIALOG)
            self.SetBackgroundColour(wx.Colour(230, 43, 29))
        elif msgType == INFOBAR_WARN:
            bmp = wx.ArtProvider.GetBitmap(wx.ART_WARNING, wx.ART_CMN_DIALOG)
            self.SetBackgroundColour(wx.Colour(228, 165, 40))
        else:
            raise TypeError("Unknown message type: %s" % repr(msgType))
        self._msgType = msgType
        self.Bitmap.SetBitmap(bmp)

        tcolour = eclutil.BestLabelColour(self.BackgroundColour)
        self.Title.SetOwnForegroundColour(tcolour)
        self.Message.SetOwnForegroundColour(tcolour)

        self.Refresh()

    def Show(self, show=True):
        """Override to handle parent update"""
        super(InfoBar, self).Show(show)
        self._UpdateParent()
        self.Refresh()

    def ShowMessage(self, title=u"", message=u"", msgType=INFOBAR_INFO):
        """Update the message and show the bar"""
        self.Title.SetLabel(title)
        self.Message.SetLabel(message)
        self.MessageType = msgType
        self.Show(True)
