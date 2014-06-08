###############################################################################
# Name: actionscript.py                                                       #
# Purpose: Define ActionScript syntax for highlighting and other features     #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2008 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
FILE: actionscript.py                                                                
AUTHOR: Cody Precord                                                       
@summary: Lexer configuration file for ActionScript
                                                                         
"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: _actionscript.py 70228 2011-12-31 20:39:16Z CJP $"
__revision__ = "$Revision: 70228 $"

#-----------------------------------------------------------------------------#
# Imports
import wx.stc as stc

# Local Imports
import synglob
import syndata
import _cpp

#-----------------------------------------------------------------------------#

#---- Keyword Specifications ----#

# ActionScript Keywords 0
AS_KEYWORDS = ("break case catch continue default do each else finally for if "
               "in label new return super switch throw while with "
               # Attribute Keywords
               "dynamic final internal native override private protected "
               "public static "
               # Definition Keywords
               "class const extends function get implements interface "
               "namespace package set var "
               # Directives
               "import include use "
               # Primary Expression Keywords
               "false null this true "
               # Special Types
               "void Null *")

# ActionScript Keywords 1
# Namespaces and Packages
AS_TYPES = ("AS3 flash_proxy object_proxy flash accessibility display errors "
            "events external filters geom media net printing profiler system "
            "text ui utils xml ")

#---- Syntax Style Specs ----#
# Same as cpp

#---- Extra Properties ----#
# Same as cpp

#------------------------------------------------------------------------------#

class SyntaxData(syndata.SyntaxDataBase):
    """ActionScript SyntaxData"""
    def __init__(self, langid):
        super(SyntaxData, self).__init__(langid)

        # Setup
        self.SetLexer(stc.STC_LEX_CPP)
        self.RegisterFeature(synglob.FEATURE_AUTOINDENT, _cpp.AutoIndenter)

    def GetKeywords(self):
        """Returns Specified Keywords List """
        return [(0, AS_KEYWORDS), (1, AS_TYPES)]

    def GetSyntaxSpec(self):
        """Syntax Specifications """
        return _cpp.SYNTAX_ITEMS

    def GetProperties(self):
        """Returns a list of Extra Properties to set """
        return [_cpp.FOLD, _cpp.FOLD_PRE]

    def GetCommentPattern(self):
        """Returns a list of characters used to comment a block of code """
        return [u'//']
