###############################################################################
# Name: encdlg.py                                                             #
# Purpose: Encoding Dialog                                                    #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2008 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
Editra Control Library: Encoding Dialog

A simple choice dialog for selecting a file encoding type from. The dialog
can work with either a passed in list of choices to display or by default will
list all encodings found on the system using their normalized names.

@summary: Encoding choice dialog

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: encdlg.py 70230 2012-01-01 01:47:42Z CJP $"
__revision__ = "$Revision: 70230 $"

__all__ = ['EncodingDialog', 'GetAllEncodings']

#--------------------------------------------------------------------------#
# Imports
import locale
import encodings
import wx

# Editra Control Library Imports
import choicedlg

#--------------------------------------------------------------------------#
# Globals
EncodingDialogNameStr = u"EncodingDialog"

#--------------------------------------------------------------------------#

class EncodingDialog(choicedlg.ChoiceDialog):
    """Dialog for choosing an file encoding from the list of available
    encodings on the system.

    """
    def __init__(self, parent, id=wx.ID_ANY, msg=u'', title=u'',
                  elist=list(), default=u'',
                  style=wx.CAPTION, pos=wx.DefaultPosition,
                  size=wx.DefaultSize,
                  name=EncodingDialogNameStr):
        """Create the encoding dialog
        @param parent: Parent Window
        @keyword id: Dialog ID
        @keyword msg: Dialog Message
        @keyword title: Dialog Title
        @keyword elist: list of encodings to use or None to use all
        @keyword default: Default selected encoding
        @keyword style: Dialog Style bitmask
        @keyword pos: Dialog Postion
        @keyword size: Dialog Size
        @keyword name: Dialog Name

        """
        if not len(elist):
            elist = GetAllEncodings()

        default = encodings.normalize_encoding(default)
        if default and default.lower() in elist:
            sel = default.lower()
        else:
            sel = locale.getpreferredencoding(False)

        super(EncodingDialog, self).__init__(parent, id, msg, title,
                                             elist, sel, pos, size, style)

    def GetEncoding(self):
        """Get the selected encoding
        @return: string

        """
        return self.GetStringSelection()

#--------------------------------------------------------------------------#
# Utilities

def GetAllEncodings():
    """Get all encodings found on the system
    @return: list of strings

    """
    elist = encodings.aliases.aliases.values()
    elist = list(set(elist))
    elist.sort()
    elist = [ enc for enc in elist if not enc.endswith('codec') ]
    return elist

#--------------------------------------------------------------------------#
