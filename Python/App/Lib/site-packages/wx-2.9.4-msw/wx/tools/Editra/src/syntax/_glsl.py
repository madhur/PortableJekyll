###############################################################################
# Name: glsl.py                                                                #
# Purpose: Define C/CPP/ObjC/Vala syntax for highlighting and other features  #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2008 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
FILE: glsl.py                                                                
@author: Cody Precord                                                       
@summary: Lexer configuration file for GLSL source files.
                                                                         
"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id$"
__revision__ = "$Revision$"

#-----------------------------------------------------------------------------#
# Imports
import wx.stc as stc
import re

# Local imports
import synglob
import syndata

import _cpp

#-----------------------------------------------------------------------------#

#---- Keyword Specifications ----#

# C Keywords
GLSL_KEYWORDS = (0, "attribute uniform varying const layout centroid varying flat "
              "smooth noperspective patch sample break continue do for while "
              "switch case default if else subroutine in out inout true false "
              "invariant discard return lowp mediump highp precision")

# C Types/Structures/Storage Classes
GLSL_TYPES = (1, "mat2 mat3 float double int void bool mat4 dmat2 dmat3 dmat4 mat2x2 "
           "mat2x3 mat2x4 dmat2x2 dmat2x3 dmat2x4 mat3x2 mat3x3 mat3x4 dmat3x2 "
           "dmat3x3 dmat3x4 mat4x2 mat4x3 mat4x4 dmat4x2 dmat4x3 dmat4x4 vec2 "
           "vec3 vec4 ivec2 ivec3 ivec4 bvec2 bvec3 bvec4 dvec2 dvec3 dvec4 uint "
           "uvec2 uvec3 uvec4 sampler1D sampler2D sampler3D samplerCube "
           "sampler1DShadow sampler2DShadow samplerCubeShadow sampler1DArray "
           "sampler2DArray sampler1DArrayShadow sampler2DArrayShadow isampler1D "
           "isampler2D isampler3D isamplerCube isampler1DArray isampler2DArray "
           "usampler1D usampler2D usampler3D usamplerCube usampler1DArray "
           "usampler2DArray sampler2DRect sampler2DRectShadow isampler2DRect "
           "usampler2DRect samplerBuffer isamplerBuffer usamplerBuffer sampler2DMS "
           "isampler2DMS usampler2DMS sampler2DMSArray isampler2DMSArray "
           "usampler2DMSArray samplerCubeArray samplerCubeArrayShadow "
           "isamplerCubeArray usamplerCubeArray struct")

#------------------------------------------------------------------------------#

class SyntaxData(_cpp.SyntaxData):
    """SyntaxData object for many C like languages""" 
    def __init__(self, langid):
        super(SyntaxData, self).__init__(langid)

    def GetKeywords(self):
        """Returns Specified Keywords List"""
        return [GLSL_KEYWORDS, GLSL_TYPES, _cpp.DOC_KEYWORDS]
