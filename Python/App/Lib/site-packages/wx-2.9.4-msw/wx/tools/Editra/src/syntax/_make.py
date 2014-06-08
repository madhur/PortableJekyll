###############################################################################
# Name: make.py                                                               #
# Purpose: Define Makefile syntax for highlighting and other features         #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2007 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
FILE: make.py                                                               
AUTHOR: Cody Precord                                                        
@summary: Lexer configuration module for Makefiles.

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: _make.py 68798 2011-08-20 17:17:05Z CJP $"
__revision__ = "$Revision: 68798 $"

#-----------------------------------------------------------------------------#
# Imports
import wx.stc as stc

# Local Imports
import syndata

#-----------------------------------------------------------------------------#
# Syntax Style Specs
SYNTAX_ITEMS = [ (stc.STC_MAKE_DEFAULT,      'default_style'),
                 (stc.STC_MAKE_COMMENT,      'comment_style'),
                 (stc.STC_MAKE_IDENTIFIER,   'scalar_style'),
                 (stc.STC_MAKE_IDEOL,        'ideol_style'),
                 (stc.STC_MAKE_OPERATOR,     'operator_style'),
                 (stc.STC_MAKE_PREPROCESSOR, 'pre2_style'),
                 (stc.STC_MAKE_TARGET,       'keyword_style') ]

#-----------------------------------------------------------------------------#

class SyntaxData(syndata.SyntaxDataBase):
    """SyntaxData object for Makefiles""" 
    def __init__(self, langid):
        super(SyntaxData, self).__init__(langid)

        # Setup
        self.SetLexer(stc.STC_LEX_MAKEFILE)

    def GetSyntaxSpec(self):
        """Syntax Specifications """
        return SYNTAX_ITEMS

    def GetCommentPattern(self):
        """Returns a list of characters used to comment a block of code """
        return [u'#']
