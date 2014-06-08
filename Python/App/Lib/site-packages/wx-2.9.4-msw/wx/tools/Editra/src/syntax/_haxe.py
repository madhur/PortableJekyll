###############################################################################
# Name: haxe.py                                                               #
# Purpose: Syntax Definitions for haXe web language                           #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2008 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
@summary: Lexer configuration module for haXe web programming language

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: _haxe.py 68798 2011-08-20 17:17:05Z CJP $"
__revision__ = "$Revision: 68798 $"

#-----------------------------------------------------------------------------#
# Imports
import wx.stc as stc

# Local Imports
import synglob
import syndata
import _cpp

#-----------------------------------------------------------------------------#

#---- Keyword Definitions ----#
HAXE_KW = (0, "abstract break case catch class const continue trace do else "
              "enum extends finally for function goto if implements import in "
              "instanceof int interface new package private public return "
              "static super switch this throw throws transient try typeof var "
              "void volatile while with" )

HAXE_TYPES = (1, "Bool Enum false Float Int null String true Void ")

#---- End Keyword Definitions ----#

#-----------------------------------------------------------------------------#

class SyntaxData(syndata.SyntaxDataBase):
    """SyntaxData object for HaXe""" 
    def __init__(self, langid):
        super(SyntaxData, self).__init__(langid)

        # Setup
        self.SetLexer(stc.STC_LEX_CPP)
        self.RegisterFeature(synglob.FEATURE_AUTOINDENT, _cpp.AutoIndenter)

    def GetKeywords(self):
        """Returns Specified Keywords List """
        return [HAXE_KW, HAXE_TYPES, _cpp.DOC_KEYWORDS]

    def GetSyntaxSpec(self):
        """Syntax Specifications """
        return _cpp.SYNTAX_ITEMS

    def GetProperties(self):
        """Returns a list of Extra Properties to set """
        return [_cpp.FOLD,]

    def GetCommentPattern(self):
        """Returns a list of characters used to comment a block of code """
        return ['//']
