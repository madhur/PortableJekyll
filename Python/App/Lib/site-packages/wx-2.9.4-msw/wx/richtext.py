# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

import _richtext
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import _windows
import _core
import _controls
wx = _core 
__docfilter__ = wx.__DocFilter(globals()) 
#---------------------------------------------------------------------------

RICHTEXT_TYPE_ANY = _richtext.RICHTEXT_TYPE_ANY
RICHTEXT_TYPE_TEXT = _richtext.RICHTEXT_TYPE_TEXT
RICHTEXT_TYPE_XML = _richtext.RICHTEXT_TYPE_XML
RICHTEXT_TYPE_HTML = _richtext.RICHTEXT_TYPE_HTML
RICHTEXT_TYPE_RTF = _richtext.RICHTEXT_TYPE_RTF
RICHTEXT_TYPE_PDF = _richtext.RICHTEXT_TYPE_PDF
RICHTEXT_FIXED_WIDTH = _richtext.RICHTEXT_FIXED_WIDTH
RICHTEXT_FIXED_HEIGHT = _richtext.RICHTEXT_FIXED_HEIGHT
RICHTEXT_VARIABLE_WIDTH = _richtext.RICHTEXT_VARIABLE_WIDTH
RICHTEXT_VARIABLE_HEIGHT = _richtext.RICHTEXT_VARIABLE_HEIGHT
RICHTEXT_LAYOUT_SPECIFIED_RECT = _richtext.RICHTEXT_LAYOUT_SPECIFIED_RECT
RICHTEXT_DRAW_IGNORE_CACHE = _richtext.RICHTEXT_DRAW_IGNORE_CACHE
RICHTEXT_FORMATTED = _richtext.RICHTEXT_FORMATTED
RICHTEXT_UNFORMATTED = _richtext.RICHTEXT_UNFORMATTED
RICHTEXT_CACHE_SIZE = _richtext.RICHTEXT_CACHE_SIZE
RICHTEXT_HEIGHT_ONLY = _richtext.RICHTEXT_HEIGHT_ONLY
RICHTEXT_SETSTYLE_NONE = _richtext.RICHTEXT_SETSTYLE_NONE
RICHTEXT_SETSTYLE_WITH_UNDO = _richtext.RICHTEXT_SETSTYLE_WITH_UNDO
RICHTEXT_SETSTYLE_OPTIMIZE = _richtext.RICHTEXT_SETSTYLE_OPTIMIZE
RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY = _richtext.RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY
RICHTEXT_SETSTYLE_CHARACTERS_ONLY = _richtext.RICHTEXT_SETSTYLE_CHARACTERS_ONLY
RICHTEXT_SETSTYLE_RENUMBER = _richtext.RICHTEXT_SETSTYLE_RENUMBER
RICHTEXT_SETSTYLE_SPECIFY_LEVEL = _richtext.RICHTEXT_SETSTYLE_SPECIFY_LEVEL
RICHTEXT_SETSTYLE_RESET = _richtext.RICHTEXT_SETSTYLE_RESET
RICHTEXT_SETSTYLE_REMOVE = _richtext.RICHTEXT_SETSTYLE_REMOVE
RICHTEXT_INSERT_NONE = _richtext.RICHTEXT_INSERT_NONE
RICHTEXT_INSERT_WITH_PREVIOUS_PARAGRAPH_STYLE = _richtext.RICHTEXT_INSERT_WITH_PREVIOUS_PARAGRAPH_STYLE
RICHTEXT_INSERT_INTERACTIVE = _richtext.RICHTEXT_INSERT_INTERACTIVE
TEXT_ATTR_KEEP_FIRST_PARA_STYLE = _richtext.TEXT_ATTR_KEEP_FIRST_PARA_STYLE
RICHTEXT_HITTEST_NONE = _richtext.RICHTEXT_HITTEST_NONE
RICHTEXT_HITTEST_BEFORE = _richtext.RICHTEXT_HITTEST_BEFORE
RICHTEXT_HITTEST_AFTER = _richtext.RICHTEXT_HITTEST_AFTER
RICHTEXT_HITTEST_ON = _richtext.RICHTEXT_HITTEST_ON
RICHTEXT_HITTEST_OUTSIDE = _richtext.RICHTEXT_HITTEST_OUTSIDE
RICHTEXT_HITTEST_NO_NESTED_OBJECTS = _richtext.RICHTEXT_HITTEST_NO_NESTED_OBJECTS
RICHTEXT_HITTEST_NO_FLOATING_OBJECTS = _richtext.RICHTEXT_HITTEST_NO_FLOATING_OBJECTS
TEXT_BOX_ATTR_FLOAT = _richtext.TEXT_BOX_ATTR_FLOAT
TEXT_BOX_ATTR_CLEAR = _richtext.TEXT_BOX_ATTR_CLEAR
TEXT_BOX_ATTR_COLLAPSE_BORDERS = _richtext.TEXT_BOX_ATTR_COLLAPSE_BORDERS
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT = _richtext.TEXT_BOX_ATTR_VERTICAL_ALIGNMENT
TEXT_BOX_ATTR_BOX_STYLE_NAME = _richtext.TEXT_BOX_ATTR_BOX_STYLE_NAME
TEXT_ATTR_UNITS_TENTHS_MM = _richtext.TEXT_ATTR_UNITS_TENTHS_MM
TEXT_ATTR_UNITS_PIXELS = _richtext.TEXT_ATTR_UNITS_PIXELS
TEXT_ATTR_UNITS_PERCENTAGE = _richtext.TEXT_ATTR_UNITS_PERCENTAGE
TEXT_ATTR_UNITS_POINTS = _richtext.TEXT_ATTR_UNITS_POINTS
TEXT_ATTR_UNITS_MASK = _richtext.TEXT_ATTR_UNITS_MASK
TEXT_BOX_ATTR_POSITION_STATIC = _richtext.TEXT_BOX_ATTR_POSITION_STATIC
TEXT_BOX_ATTR_POSITION_RELATIVE = _richtext.TEXT_BOX_ATTR_POSITION_RELATIVE
TEXT_BOX_ATTR_POSITION_ABSOLUTE = _richtext.TEXT_BOX_ATTR_POSITION_ABSOLUTE
TEXT_BOX_ATTR_POSITION_MASK = _richtext.TEXT_BOX_ATTR_POSITION_MASK
#---------------------------------------------------------------------------

class TextAttrDimension(object):
    """Proxy of C++ TextAttrDimension class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> TextAttrDimension
        __init__(self, int value, int units=TEXT_ATTR_UNITS_TENTHS_MM) -> TextAttrDimension
        """
        _richtext.TextAttrDimension_swiginit(self,_richtext.new_TextAttrDimension(*args))
    __swig_destroy__ = _richtext.delete_TextAttrDimension
    __del__ = lambda self : None;
    def Reset(*args, **kwargs):
        """Reset(self)"""
        return _richtext.TextAttrDimension_Reset(*args, **kwargs)

    def EqPartial(*args, **kwargs):
        """EqPartial(self, TextAttrDimension dim) -> bool"""
        return _richtext.TextAttrDimension_EqPartial(*args, **kwargs)

    def Apply(*args, **kwargs):
        """Apply(self, TextAttrDimension dim, TextAttrDimension compareWith=None) -> bool"""
        return _richtext.TextAttrDimension_Apply(*args, **kwargs)

    def CollectCommonAttributes(*args, **kwargs):
        """
        CollectCommonAttributes(self, TextAttrDimension attr, TextAttrDimension clashingAttr, 
            TextAttrDimension absentAttr)
        """
        return _richtext.TextAttrDimension_CollectCommonAttributes(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """__eq__(self, TextAttrDimension dim) -> bool"""
        return _richtext.TextAttrDimension___eq__(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> int"""
        return _richtext.TextAttrDimension_GetValue(*args, **kwargs)

    def GetValueMM(*args, **kwargs):
        """GetValueMM(self) -> float"""
        return _richtext.TextAttrDimension_GetValueMM(*args, **kwargs)

    def SetValueMM(*args, **kwargs):
        """SetValueMM(self, float value)"""
        return _richtext.TextAttrDimension_SetValueMM(*args, **kwargs)

    def SetValue(*args):
        """
        SetValue(self, int value)
        SetValue(self, int value, TextAttrDimensionFlags flags)
        SetValue(self, TextAttrDimension dim)
        """
        return _richtext.TextAttrDimension_SetValue(*args)

    def GetUnits(*args, **kwargs):
        """GetUnits(self) -> int"""
        return _richtext.TextAttrDimension_GetUnits(*args, **kwargs)

    def SetUnits(*args, **kwargs):
        """SetUnits(self, int units)"""
        return _richtext.TextAttrDimension_SetUnits(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> int"""
        return _richtext.TextAttrDimension_GetPosition(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, int pos)"""
        return _richtext.TextAttrDimension_SetPosition(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """GetFlags(self) -> TextAttrDimensionFlags"""
        return _richtext.TextAttrDimension_GetFlags(*args, **kwargs)

    def SetFlags(*args, **kwargs):
        """SetFlags(self, TextAttrDimensionFlags flags)"""
        return _richtext.TextAttrDimension_SetFlags(*args, **kwargs)

    m_value = property(_richtext.TextAttrDimension_m_value_get, _richtext.TextAttrDimension_m_value_set)
    m_flags = property(_richtext.TextAttrDimension_m_flags_get, _richtext.TextAttrDimension_m_flags_set)
_richtext.TextAttrDimension_swigregister(TextAttrDimension)

class TextAttrDimensions(object):
    """Proxy of C++ TextAttrDimensions class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> TextAttrDimensions"""
        _richtext.TextAttrDimensions_swiginit(self,_richtext.new_TextAttrDimensions(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_TextAttrDimensions
    __del__ = lambda self : None;
    def Reset(*args, **kwargs):
        """Reset(self)"""
        return _richtext.TextAttrDimensions_Reset(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """__eq__(self, TextAttrDimensions dims) -> bool"""
        return _richtext.TextAttrDimensions___eq__(*args, **kwargs)

    def EqPartial(*args, **kwargs):
        """EqPartial(self, TextAttrDimensions dims) -> bool"""
        return _richtext.TextAttrDimensions_EqPartial(*args, **kwargs)

    def Apply(*args, **kwargs):
        """Apply(self, TextAttrDimensions dims, TextAttrDimensions compareWith=None) -> bool"""
        return _richtext.TextAttrDimensions_Apply(*args, **kwargs)

    def CollectCommonAttributes(*args, **kwargs):
        """
        CollectCommonAttributes(self, TextAttrDimensions attr, TextAttrDimensions clashingAttr, 
            TextAttrDimensions absentAttr)
        """
        return _richtext.TextAttrDimensions_CollectCommonAttributes(*args, **kwargs)

    def RemoveStyle(*args, **kwargs):
        """RemoveStyle(self, TextAttrDimensions attr) -> bool"""
        return _richtext.TextAttrDimensions_RemoveStyle(*args, **kwargs)

    def GetLeft(*args, **kwargs):
        """GetLeft(self) -> TextAttrDimension"""
        return _richtext.TextAttrDimensions_GetLeft(*args, **kwargs)

    def GetRight(*args, **kwargs):
        """GetRight(self) -> TextAttrDimension"""
        return _richtext.TextAttrDimensions_GetRight(*args, **kwargs)

    def GetTop(*args, **kwargs):
        """GetTop(self) -> TextAttrDimension"""
        return _richtext.TextAttrDimensions_GetTop(*args, **kwargs)

    def GetBottom(*args, **kwargs):
        """GetBottom(self) -> TextAttrDimension"""
        return _richtext.TextAttrDimensions_GetBottom(*args, **kwargs)

    def IsValid(*args, **kwargs):
        """IsValid(self) -> bool"""
        return _richtext.TextAttrDimensions_IsValid(*args, **kwargs)

    m_left = property(_richtext.TextAttrDimensions_m_left_get, _richtext.TextAttrDimensions_m_left_set)
    m_top = property(_richtext.TextAttrDimensions_m_top_get, _richtext.TextAttrDimensions_m_top_set)
    m_right = property(_richtext.TextAttrDimensions_m_right_get, _richtext.TextAttrDimensions_m_right_set)
    m_bottom = property(_richtext.TextAttrDimensions_m_bottom_get, _richtext.TextAttrDimensions_m_bottom_set)
_richtext.TextAttrDimensions_swigregister(TextAttrDimensions)

class TextAttrDimensionConverter(object):
    """Proxy of C++ TextAttrDimensionConverter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, DC dc, double scale=1.0, Size parentSize=DefaultSize) -> TextAttrDimensionConverter
        __init__(self, int ppi, double scale=1.0, Size parentSize=DefaultSize) -> TextAttrDimensionConverter
        """
        _richtext.TextAttrDimensionConverter_swiginit(self,_richtext.new_TextAttrDimensionConverter(*args))
    __swig_destroy__ = _richtext.delete_TextAttrDimensionConverter
    __del__ = lambda self : None;
    def GetPixels(*args, **kwargs):
        """GetPixels(self, TextAttrDimension dim, int direction=HORIZONTAL) -> int"""
        return _richtext.TextAttrDimensionConverter_GetPixels(*args, **kwargs)

    def GetTenthsMM(*args, **kwargs):
        """GetTenthsMM(self, TextAttrDimension dim) -> int"""
        return _richtext.TextAttrDimensionConverter_GetTenthsMM(*args, **kwargs)

    def ConvertTenthsMMToPixels(*args, **kwargs):
        """ConvertTenthsMMToPixels(self, int units) -> int"""
        return _richtext.TextAttrDimensionConverter_ConvertTenthsMMToPixels(*args, **kwargs)

    def ConvertPixelsToTenthsMM(*args, **kwargs):
        """ConvertPixelsToTenthsMM(self, int pixels) -> int"""
        return _richtext.TextAttrDimensionConverter_ConvertPixelsToTenthsMM(*args, **kwargs)

    m_ppi = property(_richtext.TextAttrDimensionConverter_m_ppi_get, _richtext.TextAttrDimensionConverter_m_ppi_set)
    m_scale = property(_richtext.TextAttrDimensionConverter_m_scale_get, _richtext.TextAttrDimensionConverter_m_scale_set)
    m_parentSize = property(_richtext.TextAttrDimensionConverter_m_parentSize_get, _richtext.TextAttrDimensionConverter_m_parentSize_set)
_richtext.TextAttrDimensionConverter_swigregister(TextAttrDimensionConverter)

TEXT_BOX_ATTR_BORDER_NONE = _richtext.TEXT_BOX_ATTR_BORDER_NONE
TEXT_BOX_ATTR_BORDER_SOLID = _richtext.TEXT_BOX_ATTR_BORDER_SOLID
TEXT_BOX_ATTR_BORDER_DOTTED = _richtext.TEXT_BOX_ATTR_BORDER_DOTTED
TEXT_BOX_ATTR_BORDER_DASHED = _richtext.TEXT_BOX_ATTR_BORDER_DASHED
TEXT_BOX_ATTR_BORDER_DOUBLE = _richtext.TEXT_BOX_ATTR_BORDER_DOUBLE
TEXT_BOX_ATTR_BORDER_GROOVE = _richtext.TEXT_BOX_ATTR_BORDER_GROOVE
TEXT_BOX_ATTR_BORDER_RIDGE = _richtext.TEXT_BOX_ATTR_BORDER_RIDGE
TEXT_BOX_ATTR_BORDER_INSET = _richtext.TEXT_BOX_ATTR_BORDER_INSET
TEXT_BOX_ATTR_BORDER_OUTSET = _richtext.TEXT_BOX_ATTR_BORDER_OUTSET
TEXT_BOX_ATTR_BORDER_STYLE = _richtext.TEXT_BOX_ATTR_BORDER_STYLE
TEXT_BOX_ATTR_BORDER_COLOUR = _richtext.TEXT_BOX_ATTR_BORDER_COLOUR
TEXT_BOX_ATTR_BORDER_THIN = _richtext.TEXT_BOX_ATTR_BORDER_THIN
TEXT_BOX_ATTR_BORDER_MEDIUM = _richtext.TEXT_BOX_ATTR_BORDER_MEDIUM
TEXT_BOX_ATTR_BORDER_THICK = _richtext.TEXT_BOX_ATTR_BORDER_THICK
TEXT_BOX_ATTR_FLOAT_NONE = _richtext.TEXT_BOX_ATTR_FLOAT_NONE
TEXT_BOX_ATTR_FLOAT_LEFT = _richtext.TEXT_BOX_ATTR_FLOAT_LEFT
TEXT_BOX_ATTR_FLOAT_RIGHT = _richtext.TEXT_BOX_ATTR_FLOAT_RIGHT
TEXT_BOX_ATTR_CLEAR_NONE = _richtext.TEXT_BOX_ATTR_CLEAR_NONE
TEXT_BOX_ATTR_CLEAR_LEFT = _richtext.TEXT_BOX_ATTR_CLEAR_LEFT
TEXT_BOX_ATTR_CLEAR_RIGHT = _richtext.TEXT_BOX_ATTR_CLEAR_RIGHT
TEXT_BOX_ATTR_CLEAR_BOTH = _richtext.TEXT_BOX_ATTR_CLEAR_BOTH
TEXT_BOX_ATTR_COLLAPSE_NONE = _richtext.TEXT_BOX_ATTR_COLLAPSE_NONE
TEXT_BOX_ATTR_COLLAPSE_FULL = _richtext.TEXT_BOX_ATTR_COLLAPSE_FULL
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_NONE = _richtext.TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_NONE
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_TOP = _richtext.TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_TOP
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_CENTRE = _richtext.TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_CENTRE
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_BOTTOM = _richtext.TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_BOTTOM
class TextAttrBorder(object):
    """Proxy of C++ TextAttrBorder class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> TextAttrBorder"""
        _richtext.TextAttrBorder_swiginit(self,_richtext.new_TextAttrBorder(*args, **kwargs))
    def __eq__(*args, **kwargs):
        """__eq__(self, TextAttrBorder border) -> bool"""
        return _richtext.TextAttrBorder___eq__(*args, **kwargs)

    def Reset(*args, **kwargs):
        """Reset(self)"""
        return _richtext.TextAttrBorder_Reset(*args, **kwargs)

    def EqPartial(*args, **kwargs):
        """EqPartial(self, TextAttrBorder border) -> bool"""
        return _richtext.TextAttrBorder_EqPartial(*args, **kwargs)

    def Apply(*args, **kwargs):
        """Apply(self, TextAttrBorder border, TextAttrBorder compareWith=None) -> bool"""
        return _richtext.TextAttrBorder_Apply(*args, **kwargs)

    def RemoveStyle(*args, **kwargs):
        """RemoveStyle(self, TextAttrBorder attr) -> bool"""
        return _richtext.TextAttrBorder_RemoveStyle(*args, **kwargs)

    def CollectCommonAttributes(*args, **kwargs):
        """CollectCommonAttributes(self, TextAttrBorder attr, TextAttrBorder clashingAttr, TextAttrBorder absentAttr)"""
        return _richtext.TextAttrBorder_CollectCommonAttributes(*args, **kwargs)

    def SetStyle(*args, **kwargs):
        """SetStyle(self, int style)"""
        return _richtext.TextAttrBorder_SetStyle(*args, **kwargs)

    def GetStyle(*args, **kwargs):
        """GetStyle(self) -> int"""
        return _richtext.TextAttrBorder_GetStyle(*args, **kwargs)

    def SetColour(*args):
        """
        SetColour(self, unsigned long colour)
        SetColour(self, Colour colour)
        """
        return _richtext.TextAttrBorder_SetColour(*args)

    def GetColourLong(*args, **kwargs):
        """GetColourLong(self) -> unsigned long"""
        return _richtext.TextAttrBorder_GetColourLong(*args, **kwargs)

    def GetColour(*args, **kwargs):
        """GetColour(self) -> Colour"""
        return _richtext.TextAttrBorder_GetColour(*args, **kwargs)

    def GetWidth(*args):
        """
        GetWidth(self) -> TextAttrDimension
        GetWidth(self) -> TextAttrDimension
        """
        return _richtext.TextAttrBorder_GetWidth(*args)

    def SetWidth(*args):
        """
        SetWidth(self, TextAttrDimension width)
        SetWidth(self, int value, int units=TEXT_ATTR_UNITS_TENTHS_MM)
        """
        return _richtext.TextAttrBorder_SetWidth(*args)

    def HasStyle(*args, **kwargs):
        """HasStyle(self) -> bool"""
        return _richtext.TextAttrBorder_HasStyle(*args, **kwargs)

    def HasColour(*args, **kwargs):
        """HasColour(self) -> bool"""
        return _richtext.TextAttrBorder_HasColour(*args, **kwargs)

    def HasWidth(*args, **kwargs):
        """HasWidth(self) -> bool"""
        return _richtext.TextAttrBorder_HasWidth(*args, **kwargs)

    def IsValid(*args, **kwargs):
        """IsValid(self) -> bool"""
        return _richtext.TextAttrBorder_IsValid(*args, **kwargs)

    def MakeValid(*args, **kwargs):
        """MakeValid(self)"""
        return _richtext.TextAttrBorder_MakeValid(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """GetFlags(self) -> int"""
        return _richtext.TextAttrBorder_GetFlags(*args, **kwargs)

    def SetFlags(*args, **kwargs):
        """SetFlags(self, int flags)"""
        return _richtext.TextAttrBorder_SetFlags(*args, **kwargs)

    def AddFlag(*args, **kwargs):
        """AddFlag(self, int flag)"""
        return _richtext.TextAttrBorder_AddFlag(*args, **kwargs)

    def RemoveFlag(*args, **kwargs):
        """RemoveFlag(self, int flag)"""
        return _richtext.TextAttrBorder_RemoveFlag(*args, **kwargs)

    m_borderStyle = property(_richtext.TextAttrBorder_m_borderStyle_get, _richtext.TextAttrBorder_m_borderStyle_set)
    m_borderColour = property(_richtext.TextAttrBorder_m_borderColour_get, _richtext.TextAttrBorder_m_borderColour_set)
    m_borderWidth = property(_richtext.TextAttrBorder_m_borderWidth_get, _richtext.TextAttrBorder_m_borderWidth_set)
    m_flags = property(_richtext.TextAttrBorder_m_flags_get, _richtext.TextAttrBorder_m_flags_set)
_richtext.TextAttrBorder_swigregister(TextAttrBorder)

class TextAttrBorders(object):
    """Proxy of C++ TextAttrBorders class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> TextAttrBorders"""
        _richtext.TextAttrBorders_swiginit(self,_richtext.new_TextAttrBorders(*args, **kwargs))
    def __eq__(*args, **kwargs):
        """__eq__(self, TextAttrBorders borders) -> bool"""
        return _richtext.TextAttrBorders___eq__(*args, **kwargs)

    def SetStyle(*args, **kwargs):
        """SetStyle(self, int style)"""
        return _richtext.TextAttrBorders_SetStyle(*args, **kwargs)

    def SetColour(*args):
        """
        SetColour(self, unsigned long colour)
        SetColour(self, Colour colour)
        """
        return _richtext.TextAttrBorders_SetColour(*args)

    def SetWidth(*args):
        """
        SetWidth(self, TextAttrDimension width)
        SetWidth(self, int value, int units=TEXT_ATTR_UNITS_TENTHS_MM)
        """
        return _richtext.TextAttrBorders_SetWidth(*args)

    def Reset(*args, **kwargs):
        """Reset(self)"""
        return _richtext.TextAttrBorders_Reset(*args, **kwargs)

    def EqPartial(*args, **kwargs):
        """EqPartial(self, TextAttrBorders borders) -> bool"""
        return _richtext.TextAttrBorders_EqPartial(*args, **kwargs)

    def Apply(*args, **kwargs):
        """Apply(self, TextAttrBorders borders, TextAttrBorders compareWith=None) -> bool"""
        return _richtext.TextAttrBorders_Apply(*args, **kwargs)

    def RemoveStyle(*args, **kwargs):
        """RemoveStyle(self, TextAttrBorders attr) -> bool"""
        return _richtext.TextAttrBorders_RemoveStyle(*args, **kwargs)

    def CollectCommonAttributes(*args, **kwargs):
        """
        CollectCommonAttributes(self, TextAttrBorders attr, TextAttrBorders clashingAttr, 
            TextAttrBorders absentAttr)
        """
        return _richtext.TextAttrBorders_CollectCommonAttributes(*args, **kwargs)

    def IsValid(*args, **kwargs):
        """IsValid(self) -> bool"""
        return _richtext.TextAttrBorders_IsValid(*args, **kwargs)

    def GetLeft(*args):
        """
        GetLeft(self) -> TextAttrBorder
        GetLeft(self) -> TextAttrBorder
        """
        return _richtext.TextAttrBorders_GetLeft(*args)

    def GetRight(*args):
        """
        GetRight(self) -> TextAttrBorder
        GetRight(self) -> TextAttrBorder
        """
        return _richtext.TextAttrBorders_GetRight(*args)

    def GetTop(*args):
        """
        GetTop(self) -> TextAttrBorder
        GetTop(self) -> TextAttrBorder
        """
        return _richtext.TextAttrBorders_GetTop(*args)

    def GetBottom(*args):
        """
        GetBottom(self) -> TextAttrBorder
        GetBottom(self) -> TextAttrBorder
        """
        return _richtext.TextAttrBorders_GetBottom(*args)

    m_left = property(_richtext.TextAttrBorders_m_left_get, _richtext.TextAttrBorders_m_left_set)
    m_right = property(_richtext.TextAttrBorders_m_right_get, _richtext.TextAttrBorders_m_right_set)
    m_top = property(_richtext.TextAttrBorders_m_top_get, _richtext.TextAttrBorders_m_top_set)
    m_bottom = property(_richtext.TextAttrBorders_m_bottom_get, _richtext.TextAttrBorders_m_bottom_set)
_richtext.TextAttrBorders_swigregister(TextAttrBorders)

class TextBoxAttr(object):
    """Proxy of C++ TextBoxAttr class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> TextBoxAttr
        __init__(self, TextBoxAttr attr) -> TextBoxAttr
        """
        _richtext.TextBoxAttr_swiginit(self,_richtext.new_TextBoxAttr(*args))
    def Init(*args, **kwargs):
        """Init(self)"""
        return _richtext.TextBoxAttr_Init(*args, **kwargs)

    def Reset(*args, **kwargs):
        """Reset(self)"""
        return _richtext.TextBoxAttr_Reset(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """__eq__(self, TextBoxAttr attr) -> bool"""
        return _richtext.TextBoxAttr___eq__(*args, **kwargs)

    def EqPartial(*args, **kwargs):
        """EqPartial(self, TextBoxAttr attr) -> bool"""
        return _richtext.TextBoxAttr_EqPartial(*args, **kwargs)

    def Apply(*args, **kwargs):
        """Apply(self, TextBoxAttr style, TextBoxAttr compareWith=None) -> bool"""
        return _richtext.TextBoxAttr_Apply(*args, **kwargs)

    def CollectCommonAttributes(*args, **kwargs):
        """CollectCommonAttributes(self, TextBoxAttr attr, TextBoxAttr clashingAttr, TextBoxAttr absentAttr)"""
        return _richtext.TextBoxAttr_CollectCommonAttributes(*args, **kwargs)

    def RemoveStyle(*args, **kwargs):
        """RemoveStyle(self, TextBoxAttr attr) -> bool"""
        return _richtext.TextBoxAttr_RemoveStyle(*args, **kwargs)

    def SetFlags(*args, **kwargs):
        """SetFlags(self, int flags)"""
        return _richtext.TextBoxAttr_SetFlags(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """GetFlags(self) -> int"""
        return _richtext.TextBoxAttr_GetFlags(*args, **kwargs)

    def HasFlag(*args, **kwargs):
        """HasFlag(self, int flag) -> bool"""
        return _richtext.TextBoxAttr_HasFlag(*args, **kwargs)

    def RemoveFlag(*args, **kwargs):
        """RemoveFlag(self, int flag)"""
        return _richtext.TextBoxAttr_RemoveFlag(*args, **kwargs)

    def AddFlag(*args, **kwargs):
        """AddFlag(self, int flag)"""
        return _richtext.TextBoxAttr_AddFlag(*args, **kwargs)

    def GetFloatMode(*args, **kwargs):
        """GetFloatMode(self) -> int"""
        return _richtext.TextBoxAttr_GetFloatMode(*args, **kwargs)

    def SetFloatMode(*args, **kwargs):
        """SetFloatMode(self, int mode)"""
        return _richtext.TextBoxAttr_SetFloatMode(*args, **kwargs)

    def HasFloatMode(*args, **kwargs):
        """HasFloatMode(self) -> bool"""
        return _richtext.TextBoxAttr_HasFloatMode(*args, **kwargs)

    def IsFloating(*args, **kwargs):
        """IsFloating(self) -> bool"""
        return _richtext.TextBoxAttr_IsFloating(*args, **kwargs)

    def GetClearMode(*args, **kwargs):
        """GetClearMode(self) -> int"""
        return _richtext.TextBoxAttr_GetClearMode(*args, **kwargs)

    def SetClearMode(*args, **kwargs):
        """SetClearMode(self, int mode)"""
        return _richtext.TextBoxAttr_SetClearMode(*args, **kwargs)

    def HasClearMode(*args, **kwargs):
        """HasClearMode(self) -> bool"""
        return _richtext.TextBoxAttr_HasClearMode(*args, **kwargs)

    def GetCollapseBorders(*args, **kwargs):
        """GetCollapseBorders(self) -> int"""
        return _richtext.TextBoxAttr_GetCollapseBorders(*args, **kwargs)

    def SetCollapseBorders(*args, **kwargs):
        """SetCollapseBorders(self, int collapse)"""
        return _richtext.TextBoxAttr_SetCollapseBorders(*args, **kwargs)

    def HasCollapseBorders(*args, **kwargs):
        """HasCollapseBorders(self) -> bool"""
        return _richtext.TextBoxAttr_HasCollapseBorders(*args, **kwargs)

    def GetVerticalAlignment(*args, **kwargs):
        """GetVerticalAlignment(self) -> int"""
        return _richtext.TextBoxAttr_GetVerticalAlignment(*args, **kwargs)

    def SetVerticalAlignment(*args, **kwargs):
        """SetVerticalAlignment(self, int verticalAlignment)"""
        return _richtext.TextBoxAttr_SetVerticalAlignment(*args, **kwargs)

    def HasVerticalAlignment(*args, **kwargs):
        """HasVerticalAlignment(self) -> bool"""
        return _richtext.TextBoxAttr_HasVerticalAlignment(*args, **kwargs)

    def GetMargins(*args):
        """
        GetMargins(self) -> TextAttrDimensions
        GetMargins(self) -> TextAttrDimensions
        """
        return _richtext.TextBoxAttr_GetMargins(*args)

    def GetLeftMargin(*args):
        """
        GetLeftMargin(self) -> TextAttrDimension
        GetLeftMargin(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetLeftMargin(*args)

    def GetRightMargin(*args):
        """
        GetRightMargin(self) -> TextAttrDimension
        GetRightMargin(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetRightMargin(*args)

    def GetTopMargin(*args):
        """
        GetTopMargin(self) -> TextAttrDimension
        GetTopMargin(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetTopMargin(*args)

    def GetBottomMargin(*args):
        """
        GetBottomMargin(self) -> TextAttrDimension
        GetBottomMargin(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetBottomMargin(*args)

    def GetPosition(*args):
        """
        GetPosition(self) -> TextAttrDimensions
        GetPosition(self) -> TextAttrDimensions
        """
        return _richtext.TextBoxAttr_GetPosition(*args)

    def GetLeft(*args):
        """
        GetLeft(self) -> TextAttrDimension
        GetLeft(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetLeft(*args)

    def GetRight(*args):
        """
        GetRight(self) -> TextAttrDimension
        GetRight(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetRight(*args)

    def GetTop(*args):
        """
        GetTop(self) -> TextAttrDimension
        GetTop(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetTop(*args)

    def GetBottom(*args):
        """
        GetBottom(self) -> TextAttrDimension
        GetBottom(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetBottom(*args)

    def GetPadding(*args):
        """
        GetPadding(self) -> TextAttrDimensions
        GetPadding(self) -> TextAttrDimensions
        """
        return _richtext.TextBoxAttr_GetPadding(*args)

    def GetLeftPadding(*args):
        """
        GetLeftPadding(self) -> TextAttrDimension
        GetLeftPadding(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetLeftPadding(*args)

    def GetRightPadding(*args):
        """
        GetRightPadding(self) -> TextAttrDimension
        GetRightPadding(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetRightPadding(*args)

    def GetTopPadding(*args):
        """
        GetTopPadding(self) -> TextAttrDimension
        GetTopPadding(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetTopPadding(*args)

    def GetBottomPadding(*args):
        """
        GetBottomPadding(self) -> TextAttrDimension
        GetBottomPadding(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetBottomPadding(*args)

    def GetBorder(*args):
        """
        GetBorder(self) -> TextAttrBorders
        GetBorder(self) -> TextAttrBorders
        """
        return _richtext.TextBoxAttr_GetBorder(*args)

    def GetLeftBorder(*args):
        """
        GetLeftBorder(self) -> TextAttrBorder
        GetLeftBorder(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetLeftBorder(*args)

    def GetTopBorder(*args):
        """
        GetTopBorder(self) -> TextAttrBorder
        GetTopBorder(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetTopBorder(*args)

    def GetRightBorder(*args):
        """
        GetRightBorder(self) -> TextAttrBorder
        GetRightBorder(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetRightBorder(*args)

    def GetBottomBorder(*args):
        """
        GetBottomBorder(self) -> TextAttrBorder
        GetBottomBorder(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetBottomBorder(*args)

    def GetOutline(*args):
        """
        GetOutline(self) -> TextAttrBorders
        GetOutline(self) -> TextAttrBorders
        """
        return _richtext.TextBoxAttr_GetOutline(*args)

    def GetLeftOutline(*args):
        """
        GetLeftOutline(self) -> TextAttrBorder
        GetLeftOutline(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetLeftOutline(*args)

    def GetTopOutline(*args):
        """
        GetTopOutline(self) -> TextAttrBorder
        GetTopOutline(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetTopOutline(*args)

    def GetRightOutline(*args):
        """
        GetRightOutline(self) -> TextAttrBorder
        GetRightOutline(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetRightOutline(*args)

    def GetBottomOutline(*args):
        """
        GetBottomOutline(self) -> TextAttrBorder
        GetBottomOutline(self) -> TextAttrBorder
        """
        return _richtext.TextBoxAttr_GetBottomOutline(*args)

    def GetSize(*args):
        """
        GetSize(self) -> wxTextAttrSize
        GetSize(self) -> wxTextAttrSize
        """
        return _richtext.TextBoxAttr_GetSize(*args)

    def SetSize(*args, **kwargs):
        """SetSize(self, wxTextAttrSize sz)"""
        return _richtext.TextBoxAttr_SetSize(*args, **kwargs)

    def GetWidth(*args):
        """
        GetWidth(self) -> TextAttrDimension
        GetWidth(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetWidth(*args)

    def GetHeight(*args):
        """
        GetHeight(self) -> TextAttrDimension
        GetHeight(self) -> TextAttrDimension
        """
        return _richtext.TextBoxAttr_GetHeight(*args)

    def GetBoxStyleName(*args, **kwargs):
        """GetBoxStyleName(self) -> String"""
        return _richtext.TextBoxAttr_GetBoxStyleName(*args, **kwargs)

    def SetBoxStyleName(*args, **kwargs):
        """SetBoxStyleName(self, String name)"""
        return _richtext.TextBoxAttr_SetBoxStyleName(*args, **kwargs)

    def HasBoxStyleName(*args, **kwargs):
        """HasBoxStyleName(self) -> bool"""
        return _richtext.TextBoxAttr_HasBoxStyleName(*args, **kwargs)

    m_flags = property(_richtext.TextBoxAttr_m_flags_get, _richtext.TextBoxAttr_m_flags_set)
    m_margins = property(_richtext.TextBoxAttr_m_margins_get, _richtext.TextBoxAttr_m_margins_set)
    m_padding = property(_richtext.TextBoxAttr_m_padding_get, _richtext.TextBoxAttr_m_padding_set)
    m_position = property(_richtext.TextBoxAttr_m_position_get, _richtext.TextBoxAttr_m_position_set)
    m_size = property(_richtext.TextBoxAttr_m_size_get, _richtext.TextBoxAttr_m_size_set)
    m_border = property(_richtext.TextBoxAttr_m_border_get, _richtext.TextBoxAttr_m_border_set)
    m_outline = property(_richtext.TextBoxAttr_m_outline_get, _richtext.TextBoxAttr_m_outline_set)
    m_floatMode = property(_richtext.TextBoxAttr_m_floatMode_get, _richtext.TextBoxAttr_m_floatMode_set)
    m_clearMode = property(_richtext.TextBoxAttr_m_clearMode_get, _richtext.TextBoxAttr_m_clearMode_set)
    m_collapseMode = property(_richtext.TextBoxAttr_m_collapseMode_get, _richtext.TextBoxAttr_m_collapseMode_set)
    m_verticalAlignment = property(_richtext.TextBoxAttr_m_verticalAlignment_get, _richtext.TextBoxAttr_m_verticalAlignment_set)
    m_boxStyleName = property(_richtext.TextBoxAttr_m_boxStyleName_get, _richtext.TextBoxAttr_m_boxStyleName_set)
_richtext.TextBoxAttr_swigregister(TextBoxAttr)

#---------------------------------------------------------------------------

class RichTextAttr(_controls.TextAttr):
    """Proxy of C++ RichTextAttr class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, TextAttr attr) -> RichTextAttr
        __init__(self, RichTextAttr attr) -> RichTextAttr
        __init__(self) -> RichTextAttr
        """
        _richtext.RichTextAttr_swiginit(self,_richtext.new_RichTextAttr(*args))
    __swig_destroy__ = _richtext.delete_RichTextAttr
    __del__ = lambda self : None;
    def Copy(*args, **kwargs):
        """Copy(self, RichTextAttr attr)"""
        return _richtext.RichTextAttr_Copy(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """__eq__(self, RichTextAttr attr) -> bool"""
        return _richtext.RichTextAttr___eq__(*args, **kwargs)

    def EqPartial(*args, **kwargs):
        """EqPartial(self, RichTextAttr attr) -> bool"""
        return _richtext.RichTextAttr_EqPartial(*args, **kwargs)

    def Apply(*args, **kwargs):
        """Apply(self, RichTextAttr style, RichTextAttr compareWith=None) -> bool"""
        return _richtext.RichTextAttr_Apply(*args, **kwargs)

    def CollectCommonAttributes(*args, **kwargs):
        """CollectCommonAttributes(self, RichTextAttr attr, RichTextAttr clashingAttr, RichTextAttr absentAttr)"""
        return _richtext.RichTextAttr_CollectCommonAttributes(*args, **kwargs)

    def RemoveStyle(*args, **kwargs):
        """RemoveStyle(self, RichTextAttr attr) -> bool"""
        return _richtext.RichTextAttr_RemoveStyle(*args, **kwargs)

    def GetTextBoxAttr(*args):
        """
        GetTextBoxAttr(self) -> TextBoxAttr
        GetTextBoxAttr(self) -> TextBoxAttr
        """
        return _richtext.RichTextAttr_GetTextBoxAttr(*args)

    def SetTextBoxAttr(*args, **kwargs):
        """SetTextBoxAttr(self, TextBoxAttr attr)"""
        return _richtext.RichTextAttr_SetTextBoxAttr(*args, **kwargs)

    m_textBoxAttr = property(_richtext.RichTextAttr_m_textBoxAttr_get, _richtext.RichTextAttr_m_textBoxAttr_set)
_richtext.RichTextAttr_swigregister(RichTextAttr)

class RichTextFontTable(_core.Object):
    """Proxy of C++ RichTextFontTable class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> RichTextFontTable"""
        _richtext.RichTextFontTable_swiginit(self,_richtext.new_RichTextFontTable(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_RichTextFontTable
    __del__ = lambda self : None;
    def IsOk(*args, **kwargs):
        """IsOk(self) -> bool"""
        return _richtext.RichTextFontTable_IsOk(*args, **kwargs)

    def FindFont(*args, **kwargs):
        """FindFont(self, RichTextAttr fontSpec) -> Font"""
        return _richtext.RichTextFontTable_FindFont(*args, **kwargs)

    def Clear(*args, **kwargs):
        """Clear(self)"""
        return _richtext.RichTextFontTable_Clear(*args, **kwargs)

_richtext.RichTextFontTable_swigregister(RichTextFontTable)

class RichTextRange(object):
    """
    RichTextRange is a data structure that represents a range of text
    within a `RichTextCtrl`.  It simply contains integer ``start`` and
    ``end`` properties and a few operations useful for dealing with
    ranges.  In most places in wxPython where a RichTextRange is expected a
    2-tuple containing (start, end) can be used instead.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, long start=0, long end=0) -> RichTextRange

        Creates a new range object.
        """
        _richtext.RichTextRange_swiginit(self,_richtext.new_RichTextRange(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_RichTextRange
    __del__ = lambda self : None;
    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of RichTextRange objects.
        """
        return _richtext.RichTextRange___eq__(*args, **kwargs)

    def __sub__(*args, **kwargs):
        """__sub__(self, RichTextRange range) -> RichTextRange"""
        return _richtext.RichTextRange___sub__(*args, **kwargs)

    def __add__(*args, **kwargs):
        """__add__(self, RichTextRange range) -> RichTextRange"""
        return _richtext.RichTextRange___add__(*args, **kwargs)

    def SetRange(*args, **kwargs):
        """SetRange(self, long start, long end)"""
        return _richtext.RichTextRange_SetRange(*args, **kwargs)

    def SetStart(*args, **kwargs):
        """SetStart(self, long start)"""
        return _richtext.RichTextRange_SetStart(*args, **kwargs)

    def GetStart(*args, **kwargs):
        """GetStart(self) -> long"""
        return _richtext.RichTextRange_GetStart(*args, **kwargs)

    start = property(GetStart, SetStart) 
    def SetEnd(*args, **kwargs):
        """SetEnd(self, long end)"""
        return _richtext.RichTextRange_SetEnd(*args, **kwargs)

    def GetEnd(*args, **kwargs):
        """GetEnd(self) -> long"""
        return _richtext.RichTextRange_GetEnd(*args, **kwargs)

    end = property(GetEnd, SetEnd) 
    def IsOutside(*args, **kwargs):
        """
        IsOutside(self, RichTextRange range) -> bool

        Returns true if this range is completely outside 'range'
        """
        return _richtext.RichTextRange_IsOutside(*args, **kwargs)

    def IsWithin(*args, **kwargs):
        """
        IsWithin(self, RichTextRange range) -> bool

        Returns true if this range is completely within 'range'
        """
        return _richtext.RichTextRange_IsWithin(*args, **kwargs)

    def Contains(*args, **kwargs):
        """
        Contains(self, long pos) -> bool

        Returns true if the given position is within this range. Allow for the
        possibility of an empty range - assume the position is within this
        empty range.
        """
        return _richtext.RichTextRange_Contains(*args, **kwargs)

    def LimitTo(*args, **kwargs):
        """
        LimitTo(self, RichTextRange range) -> bool

        Limit this range to be within 'range'
        """
        return _richtext.RichTextRange_LimitTo(*args, **kwargs)

    def GetLength(*args, **kwargs):
        """
        GetLength(self) -> long

        Gets the length of the range
        """
        return _richtext.RichTextRange_GetLength(*args, **kwargs)

    def Swap(*args, **kwargs):
        """
        Swap(self)

        Swaps the start and end
        """
        return _richtext.RichTextRange_Swap(*args, **kwargs)

    def ToInternal(*args, **kwargs):
        """
        ToInternal(self) -> RichTextRange

        Convert to internal form: (n, n) is the range of a single character.
        """
        return _richtext.RichTextRange_ToInternal(*args, **kwargs)

    def FromInternal(*args, **kwargs):
        """
        FromInternal(self) -> RichTextRange

        Convert from internal to public API form: (n, n+1) is the range of a
        single character.
        """
        return _richtext.RichTextRange_FromInternal(*args, **kwargs)

    def Get(*args, **kwargs):
        """
        Get() -> (start,end)

        Returns the start and end properties as a tuple.
        """
        return _richtext.RichTextRange_Get(*args, **kwargs)

    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'RichTextRange'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.start = val
        elif index == 1: self.end = val
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0,0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (RichTextRange, self.Get())

    End = property(GetEnd,SetEnd,doc="See `GetEnd` and `SetEnd`") 
    Length = property(GetLength,doc="See `GetLength`") 
    Start = property(GetStart,SetStart,doc="See `GetStart` and `SetStart`") 
_richtext.RichTextRange_swigregister(RichTextRange)

class RichTextDrawingContext(_core.Object):
    """Proxy of C++ RichTextDrawingContext class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, RichTextBuffer buffer) -> RichTextDrawingContext"""
        _richtext.RichTextDrawingContext_swiginit(self,_richtext.new_RichTextDrawingContext(*args, **kwargs))
    def Init(*args, **kwargs):
        """Init(self)"""
        return _richtext.RichTextDrawingContext_Init(*args, **kwargs)

    def HasVirtualAttributes(*args, **kwargs):
        """HasVirtualAttributes(self, RichTextObject obj) -> bool"""
        return _richtext.RichTextDrawingContext_HasVirtualAttributes(*args, **kwargs)

    def GetVirtualAttributes(*args, **kwargs):
        """GetVirtualAttributes(self, RichTextObject obj) -> RichTextAttr"""
        return _richtext.RichTextDrawingContext_GetVirtualAttributes(*args, **kwargs)

    def ApplyVirtualAttributes(*args, **kwargs):
        """ApplyVirtualAttributes(self, RichTextAttr attr, RichTextObject obj) -> bool"""
        return _richtext.RichTextDrawingContext_ApplyVirtualAttributes(*args, **kwargs)

    m_buffer = property(_richtext.RichTextDrawingContext_m_buffer_get, _richtext.RichTextDrawingContext_m_buffer_set)
_richtext.RichTextDrawingContext_swigregister(RichTextDrawingContext)
cvar = _richtext.cvar
RICHTEXT_ALL = cvar.RICHTEXT_ALL
RICHTEXT_NONE = cvar.RICHTEXT_NONE

class RichTextObject(_core.Object):
    """
    This is the base class for all drawable objects in a `RichTextCtrl`.

    The data displayed in a `RichTextCtrl` is handled by `RichTextBuffer`,
    and a `RichTextCtrl` always has one such buffer.

    The content is represented by a hierarchy of objects, all derived from
    `RichTextObject`. An object might be an image, a fragment of text, a
    paragraph, or a whole buffer. Objects store a an attribute object
    containing style information; a paragraph object can contain both
    paragraph and character information, but content objects such as text
    can only store character information. The final style displayed in the
    control or in a printout is a combination of base style, paragraph
    style and content (character) style.

    The top of the hierarchy is the buffer, a kind of
    `RichTextParagraphLayoutBox`. containing further `RichTextParagraph`
    objects, each of which can include text, images and potentially other
    types of objects.

    Each object maintains a range (start and end position) measured from
    the start of the main parent object.

    When Layout is called on an object, it is given a size which the
    object must limit itself to, or one or more flexible directions
    (vertical or horizontal). So, for example, a centred paragraph is
    given the page width to play with (minus any margins), but can extend
    indefinitely in the vertical direction. The implementation of Layout
    caches the calculated size and position.

    When the buffer is modified, a range is invalidated (marked as
    requiring layout), so that only the minimum amount of layout is
    performed.

    A paragraph of pure text with the same style contains just one further
    object, a `RichTextPlainText` object. When styling is applied to part
    of this object, the object is decomposed into separate objects, one
    object for each different character style. So each object within a
    paragraph always has just one attribute object to denote its character
    style. Of course, this can lead to fragmentation after a lot of edit
    operations, potentially leading to several objects with the same style
    where just one would do. So a Defragment function is called when
    updating the control's display, to ensure that the minimum number of
    objects is used.

    To implement your own RichTextObjects in Python you must derive a
    class from `PyRichTextObject`, which has been instrumented to forward
    the virtual C++ method calls to the Python methods in the derived
    class. (This class hasn't been implemented yet!)
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextObject
    __del__ = lambda self : None;
    def Draw(*args, **kwargs):
        """
        Draw(self, DC dc, RichTextDrawingContext context, RichTextRange range, 
            wxRichTextSelection selection, Rect rect, 
            int descent, int style) -> bool
        """
        return _richtext.RichTextObject_Draw(*args, **kwargs)

    def Layout(*args, **kwargs):
        """
        Layout(self, DC dc, RichTextDrawingContext context, Rect rect, Rect parentRect, 
            int style) -> bool
        """
        return _richtext.RichTextObject_Layout(*args, **kwargs)

    def HitTest(*args, **kwargs):
        """
        HitTest(self, DC dc, RichTextDrawingContext context, Point pt, long OUTPUT, 
            RichTextObject obj, RichTextObject contextObj, 
            int flags=0) -> int
        """
        return _richtext.RichTextObject_HitTest(*args, **kwargs)

    def FindPosition(*args, **kwargs):
        """
        FindPosition(self, DC dc, RichTextDrawingContext context, long index, 
            Point OUTPUT, int OUTPUT, bool forceLineStart) -> bool
        """
        return _richtext.RichTextObject_FindPosition(*args, **kwargs)

    def GetBestSize(*args, **kwargs):
        """GetBestSize(self) -> Size"""
        return _richtext.RichTextObject_GetBestSize(*args, **kwargs)

    def GetRangeSize(*args, **kwargs):
        """
        GetRangeSize(self, RichTextRange range, Size OUTPUT, int OUTPUT, DC dc, 
            RichTextDrawingContext context, int flags, 
            Point position=wxPoint(0,0)) -> bool
        """
        return _richtext.RichTextObject_GetRangeSize(*args, **kwargs)

    def DoSplit(*args, **kwargs):
        """DoSplit(self, long pos) -> RichTextObject"""
        return _richtext.RichTextObject_DoSplit(*args, **kwargs)

    def CalculateRange(*args, **kwargs):
        """CalculateRange(self, long start, long OUTPUT)"""
        return _richtext.RichTextObject_CalculateRange(*args, **kwargs)

    def DeleteRange(*args, **kwargs):
        """DeleteRange(self, RichTextRange range) -> bool"""
        return _richtext.RichTextObject_DeleteRange(*args, **kwargs)

    def IsEmpty(*args, **kwargs):
        """IsEmpty(self) -> bool"""
        return _richtext.RichTextObject_IsEmpty(*args, **kwargs)

    def IsFloatable(*args, **kwargs):
        """IsFloatable(self) -> bool"""
        return _richtext.RichTextObject_IsFloatable(*args, **kwargs)

    def IsFloating(*args, **kwargs):
        """IsFloating(self) -> bool"""
        return _richtext.RichTextObject_IsFloating(*args, **kwargs)

    def GetFloatDirection(*args, **kwargs):
        """GetFloatDirection(self) -> int"""
        return _richtext.RichTextObject_GetFloatDirection(*args, **kwargs)

    def GetTextForRange(*args, **kwargs):
        """GetTextForRange(self, RichTextRange range) -> String"""
        return _richtext.RichTextObject_GetTextForRange(*args, **kwargs)

    def CanMerge(*args, **kwargs):
        """CanMerge(self, RichTextObject object) -> bool"""
        return _richtext.RichTextObject_CanMerge(*args, **kwargs)

    def Merge(self, obj):
        """Merge(self, RichTextObject object) -> bool"""
        val = _richtext.RichTextObject_Merge(self, obj)
        if val:
            obj.this.own(True)
        return val


    def Dump(*args, **kwargs):
        """Dump(self) -> String"""
        return _richtext.RichTextObject_Dump(*args, **kwargs)

    def CanEditProperties(*args, **kwargs):
        """CanEditProperties(self) -> bool"""
        return _richtext.RichTextObject_CanEditProperties(*args, **kwargs)

    def EditProperties(*args, **kwargs):
        """EditProperties(self, Window parent, RichTextBuffer buffer) -> bool"""
        return _richtext.RichTextObject_EditProperties(*args, **kwargs)

    def ImportFromXML(*args, **kwargs):
        """
        ImportFromXML(self, RichTextBuffer buffer, wxXmlNode node, RichTextXMLHandler handler, 
            bool recurse) -> bool
        """
        return _richtext.RichTextObject_ImportFromXML(*args, **kwargs)

    def ExportXML(*args):
        """
        ExportXML(self, wxOutputStream stream, int indent, RichTextXMLHandler handler) -> bool
        ExportXML(self, wxXmlNode parent, RichTextXMLHandler handler) -> bool
        """
        return _richtext.RichTextObject_ExportXML(*args)

    def UsesParagraphAttributes(*args, **kwargs):
        """UsesParagraphAttributes(self) -> bool"""
        return _richtext.RichTextObject_UsesParagraphAttributes(*args, **kwargs)

    def GetXMLNodeName(*args, **kwargs):
        """GetXMLNodeName(self) -> String"""
        return _richtext.RichTextObject_GetXMLNodeName(*args, **kwargs)

    def GetCachedSize(*args, **kwargs):
        """GetCachedSize(self) -> Size"""
        return _richtext.RichTextObject_GetCachedSize(*args, **kwargs)

    def SetCachedSize(*args, **kwargs):
        """SetCachedSize(self, Size sz)"""
        return _richtext.RichTextObject_SetCachedSize(*args, **kwargs)

    CachedSize = property(GetCachedSize,SetCachedSize) 
    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> Point"""
        return _richtext.RichTextObject_GetPosition(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, Point pos)"""
        return _richtext.RichTextObject_SetPosition(*args, **kwargs)

    Position = property(GetPosition,SetPosition) 
    def GetRect(*args, **kwargs):
        """GetRect(self) -> Rect"""
        return _richtext.RichTextObject_GetRect(*args, **kwargs)

    Rect = property(GetRect) 
    def SetRange(*args, **kwargs):
        """SetRange(self, RichTextRange range)"""
        return _richtext.RichTextObject_SetRange(*args, **kwargs)

    def GetRange(*args, **kwargs):
        """GetRange(self) -> RichTextRange"""
        return _richtext.RichTextObject_GetRange(*args, **kwargs)

    Range = property(GetRange,SetRange) 
    def IsComposite(*args, **kwargs):
        """IsComposite(self) -> bool"""
        return _richtext.RichTextObject_IsComposite(*args, **kwargs)

    def GetParent(*args, **kwargs):
        """GetParent(self) -> RichTextObject"""
        return _richtext.RichTextObject_GetParent(*args, **kwargs)

    def SetParent(*args, **kwargs):
        """SetParent(self, RichTextObject parent)"""
        return _richtext.RichTextObject_SetParent(*args, **kwargs)

    Parent = property(GetParent,SetParent) 
    def SetSameMargins(*args, **kwargs):
        """SetSameMargins(self, int margin)"""
        return _richtext.RichTextObject_SetSameMargins(*args, **kwargs)

    def SetMargins(*args, **kwargs):
        """SetMargins(self, int leftMargin, int rightMargin, int topMargin, int bottomMargin)"""
        return _richtext.RichTextObject_SetMargins(*args, **kwargs)

    def GetLeftMargin(*args, **kwargs):
        """GetLeftMargin(self) -> int"""
        return _richtext.RichTextObject_GetLeftMargin(*args, **kwargs)

    def GetRightMargin(*args, **kwargs):
        """GetRightMargin(self) -> int"""
        return _richtext.RichTextObject_GetRightMargin(*args, **kwargs)

    def GetTopMargin(*args, **kwargs):
        """GetTopMargin(self) -> int"""
        return _richtext.RichTextObject_GetTopMargin(*args, **kwargs)

    def GetBottomMargin(*args, **kwargs):
        """GetBottomMargin(self) -> int"""
        return _richtext.RichTextObject_GetBottomMargin(*args, **kwargs)

    def SetAttributes(*args, **kwargs):
        """SetAttributes(self, RichTextAttr attr)"""
        return _richtext.RichTextObject_SetAttributes(*args, **kwargs)

    def GetAttributes(*args, **kwargs):
        """GetAttributes(self) -> RichTextAttr"""
        return _richtext.RichTextObject_GetAttributes(*args, **kwargs)

    Attributes = property(GetAttributes,SetAttributes) 
    def SetDescent(*args, **kwargs):
        """SetDescent(self, int descent)"""
        return _richtext.RichTextObject_SetDescent(*args, **kwargs)

    def GetDescent(*args, **kwargs):
        """GetDescent(self) -> int"""
        return _richtext.RichTextObject_GetDescent(*args, **kwargs)

    Descent = property(GetDescent,SetDescent) 
    def GetBuffer(*args, **kwargs):
        """GetBuffer(self) -> RichTextBuffer"""
        return _richtext.RichTextObject_GetBuffer(*args, **kwargs)

    def Clone(*args, **kwargs):
        """Clone(self) -> RichTextObject"""
        return _richtext.RichTextObject_Clone(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextObject obj)"""
        return _richtext.RichTextObject_Copy(*args, **kwargs)

    def Reference(*args, **kwargs):
        """Reference(self)"""
        return _richtext.RichTextObject_Reference(*args, **kwargs)

    def Dereference(*args, **kwargs):
        """Dereference(self)"""
        return _richtext.RichTextObject_Dereference(*args, **kwargs)

    def ConvertTenthsMMToPixelsDC(*args, **kwargs):
        """ConvertTenthsMMToPixelsDC(self, DC dc, int units) -> int"""
        return _richtext.RichTextObject_ConvertTenthsMMToPixelsDC(*args, **kwargs)

    def ConvertTenthsMMToPixels(*args, **kwargs):
        """ConvertTenthsMMToPixels(int ppi, int units, double scale=1.0) -> int"""
        return _richtext.RichTextObject_ConvertTenthsMMToPixels(*args, **kwargs)

    ConvertTenthsMMToPixels = staticmethod(ConvertTenthsMMToPixels)
    def ConvertPixelsToTenthsMM(*args):
        """
        ConvertPixelsToTenthsMM(DC dc, int pixels) -> int
        ConvertPixelsToTenthsMM(int ppi, int pixels, double scale=1.0) -> int
        """
        return _richtext.RichTextObject_ConvertPixelsToTenthsMM(*args)

    ConvertPixelsToTenthsMM = staticmethod(ConvertPixelsToTenthsMM)
    def DrawBoxAttributes(*args, **kwargs):
        """
        DrawBoxAttributes(DC dc, RichTextBuffer buffer, RichTextAttr attr, Rect boxRect, 
            int flags=0) -> bool
        """
        return _richtext.RichTextObject_DrawBoxAttributes(*args, **kwargs)

    DrawBoxAttributes = staticmethod(DrawBoxAttributes)
    def DrawBorder(*args, **kwargs):
        """
        DrawBorder(DC dc, RichTextBuffer buffer, TextAttrBorders attr, 
            Rect rect, int flags=0) -> bool
        """
        return _richtext.RichTextObject_DrawBorder(*args, **kwargs)

    DrawBorder = staticmethod(DrawBorder)
    def GetBoxRects(*args, **kwargs):
        """
        GetBoxRects(DC dc, RichTextBuffer buffer, RichTextAttr attr, Rect marginRect, 
            Rect borderRect, Rect contentRect, 
            Rect paddingRect, Rect outlineRect) -> bool
        """
        return _richtext.RichTextObject_GetBoxRects(*args, **kwargs)

    GetBoxRects = staticmethod(GetBoxRects)
    def GetTotalMargin(*args, **kwargs):
        """
        GetTotalMargin(DC dc, RichTextBuffer buffer, RichTextAttr attr, int leftMargin, 
            int rightMargin, int topMargin, 
            int bottomMargin) -> bool
        """
        return _richtext.RichTextObject_GetTotalMargin(*args, **kwargs)

    GetTotalMargin = staticmethod(GetTotalMargin)
    def AdjustAvailableSpace(*args, **kwargs):
        """
        AdjustAvailableSpace(DC dc, RichTextBuffer buffer, RichTextAttr parentAttr, 
            RichTextAttr childAttr, Rect availableParentSpace, 
            Rect availableContainerSpace) -> Rect
        """
        return _richtext.RichTextObject_AdjustAvailableSpace(*args, **kwargs)

    AdjustAvailableSpace = staticmethod(AdjustAvailableSpace)
_richtext.RichTextObject_swigregister(RichTextObject)

def RichTextObject_ConvertTenthsMMToPixels(*args, **kwargs):
  """RichTextObject_ConvertTenthsMMToPixels(int ppi, int units, double scale=1.0) -> int"""
  return _richtext.RichTextObject_ConvertTenthsMMToPixels(*args, **kwargs)

def RichTextObject_ConvertPixelsToTenthsMM(*args):
  """
    ConvertPixelsToTenthsMM(DC dc, int pixels) -> int
    RichTextObject_ConvertPixelsToTenthsMM(int ppi, int pixels, double scale=1.0) -> int
    """
  return _richtext.RichTextObject_ConvertPixelsToTenthsMM(*args)

def RichTextObject_DrawBoxAttributes(*args, **kwargs):
  """
    RichTextObject_DrawBoxAttributes(DC dc, RichTextBuffer buffer, RichTextAttr attr, Rect boxRect, 
        int flags=0) -> bool
    """
  return _richtext.RichTextObject_DrawBoxAttributes(*args, **kwargs)

def RichTextObject_DrawBorder(*args, **kwargs):
  """
    RichTextObject_DrawBorder(DC dc, RichTextBuffer buffer, TextAttrBorders attr, 
        Rect rect, int flags=0) -> bool
    """
  return _richtext.RichTextObject_DrawBorder(*args, **kwargs)

def RichTextObject_GetBoxRects(*args, **kwargs):
  """
    RichTextObject_GetBoxRects(DC dc, RichTextBuffer buffer, RichTextAttr attr, Rect marginRect, 
        Rect borderRect, Rect contentRect, 
        Rect paddingRect, Rect outlineRect) -> bool
    """
  return _richtext.RichTextObject_GetBoxRects(*args, **kwargs)

def RichTextObject_GetTotalMargin(*args, **kwargs):
  """
    RichTextObject_GetTotalMargin(DC dc, RichTextBuffer buffer, RichTextAttr attr, int leftMargin, 
        int rightMargin, int topMargin, 
        int bottomMargin) -> bool
    """
  return _richtext.RichTextObject_GetTotalMargin(*args, **kwargs)

def RichTextObject_AdjustAvailableSpace(*args, **kwargs):
  """
    RichTextObject_AdjustAvailableSpace(DC dc, RichTextBuffer buffer, RichTextAttr parentAttr, 
        RichTextAttr childAttr, Rect availableParentSpace, 
        Rect availableContainerSpace) -> Rect
    """
  return _richtext.RichTextObject_AdjustAvailableSpace(*args, **kwargs)

class RichTextObjectList_iterator(object):
    """This class serves as an iterator for a wxRichTextObjectList object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextObjectList_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> RichTextObject"""
        return _richtext.RichTextObjectList_iterator_next(*args, **kwargs)

_richtext.RichTextObjectList_iterator_swigregister(RichTextObjectList_iterator)

class RichTextObjectList(object):
    """
    This class wraps a wxList-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextObjectList
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return _richtext.RichTextObjectList___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> RichTextObject"""
        return _richtext.RichTextObjectList___getitem__(*args, **kwargs)

    def __contains__(*args, **kwargs):
        """__contains__(self, RichTextObject obj) -> bool"""
        return _richtext.RichTextObjectList___contains__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> RichTextObjectList_iterator"""
        return _richtext.RichTextObjectList___iter__(*args, **kwargs)

    def index(*args, **kwargs):
        """index(self, RichTextObject obj) -> int"""
        return _richtext.RichTextObjectList_index(*args, **kwargs)

    def __repr__(self):
        return "wxRichTextObjectList: " + repr(list(self))

_richtext.RichTextObjectList_swigregister(RichTextObjectList)

class RichTextCompositeObject(RichTextObject):
    """Objects of this class can contain other rich text objects."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextCompositeObject
    __del__ = lambda self : None;
    def GetChildren(*args, **kwargs):
        """GetChildren(self) -> RichTextObjectList"""
        return _richtext.RichTextCompositeObject_GetChildren(*args, **kwargs)

    def GetChildCount(*args, **kwargs):
        """GetChildCount(self) -> size_t"""
        return _richtext.RichTextCompositeObject_GetChildCount(*args, **kwargs)

    def GetChild(*args, **kwargs):
        """GetChild(self, size_t n) -> RichTextObject"""
        return _richtext.RichTextCompositeObject_GetChild(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextCompositeObject obj)"""
        return _richtext.RichTextCompositeObject_Copy(*args, **kwargs)

    def AppendChild(*args, **kwargs):
        """AppendChild(self, RichTextObject child) -> size_t"""
        return _richtext.RichTextCompositeObject_AppendChild(*args, **kwargs)

    def InsertChild(*args, **kwargs):
        """InsertChild(self, RichTextObject child, RichTextObject inFrontOf) -> bool"""
        return _richtext.RichTextCompositeObject_InsertChild(*args, **kwargs)

    def RemoveChild(self, child, deleteChild=False):
        val = _richtext.RichTextCompositeObject_RemoveChild(self, child, deleteChild)
        self.this.own(not deleteChild)
        return val


    def DeleteChildren(*args, **kwargs):
        """DeleteChildren(self) -> bool"""
        return _richtext.RichTextCompositeObject_DeleteChildren(*args, **kwargs)

    def Defragment(*args, **kwargs):
        """Defragment(self, RichTextRange range=wxRICHTEXT_ALL) -> bool"""
        return _richtext.RichTextCompositeObject_Defragment(*args, **kwargs)

_richtext.RichTextCompositeObject_swigregister(RichTextCompositeObject)

class RichTextParagraphLayoutBox(RichTextCompositeObject):
    """This box knows how to lay out paragraphs."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, RichTextObject parent=None) -> RichTextParagraphLayoutBox
        __init__(self, RichTextParagraphLayoutBox obj) -> RichTextParagraphLayoutBox

        This box knows how to lay out paragraphs.
        """
        _richtext.RichTextParagraphLayoutBox_swiginit(self,_richtext.new_RichTextParagraphLayoutBox(*args))
    __swig_destroy__ = _richtext.delete_RichTextParagraphLayoutBox
    __del__ = lambda self : None;
    def SetRichTextCtrl(*args, **kwargs):
        """SetRichTextCtrl(self, RichTextCtrl ctrl)"""
        return _richtext.RichTextParagraphLayoutBox_SetRichTextCtrl(*args, **kwargs)

    def GetRichTextCtrl(*args, **kwargs):
        """GetRichTextCtrl(self) -> RichTextCtrl"""
        return _richtext.RichTextParagraphLayoutBox_GetRichTextCtrl(*args, **kwargs)

    def SetPartialParagraph(*args, **kwargs):
        """SetPartialParagraph(self, bool partialPara)"""
        return _richtext.RichTextParagraphLayoutBox_SetPartialParagraph(*args, **kwargs)

    def GetPartialParagraph(*args, **kwargs):
        """GetPartialParagraph(self) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_GetPartialParagraph(*args, **kwargs)

    def GetStyleSheet(*args, **kwargs):
        """GetStyleSheet(self) -> wxRichTextStyleSheet"""
        return _richtext.RichTextParagraphLayoutBox_GetStyleSheet(*args, **kwargs)

    def DrawFloats(*args, **kwargs):
        """
        DrawFloats(self, DC dc, RichTextDrawingContext context, RichTextRange range, 
            wxRichTextSelection selection, Rect rect, 
            int descent, int style)
        """
        return _richtext.RichTextParagraphLayoutBox_DrawFloats(*args, **kwargs)

    def MoveAnchoredObjectToParagraph(*args, **kwargs):
        """MoveAnchoredObjectToParagraph(self, RichTextParagraph from, RichTextParagraph to, RichTextObject obj)"""
        return _richtext.RichTextParagraphLayoutBox_MoveAnchoredObjectToParagraph(*args, **kwargs)

    def Init(*args, **kwargs):
        """Init(self)"""
        return _richtext.RichTextParagraphLayoutBox_Init(*args, **kwargs)

    def Clear(*args, **kwargs):
        """Clear(self)"""
        return _richtext.RichTextParagraphLayoutBox_Clear(*args, **kwargs)

    def Reset(*args, **kwargs):
        """Reset(self)"""
        return _richtext.RichTextParagraphLayoutBox_Reset(*args, **kwargs)

    def AddParagraph(*args, **kwargs):
        """AddParagraph(self, String text, RichTextAttr paraStyle=None) -> RichTextRange"""
        return _richtext.RichTextParagraphLayoutBox_AddParagraph(*args, **kwargs)

    def AddImage(*args, **kwargs):
        """AddImage(self, Image image, RichTextAttr paraStyle=None) -> RichTextRange"""
        return _richtext.RichTextParagraphLayoutBox_AddImage(*args, **kwargs)

    def AddParagraphs(*args, **kwargs):
        """AddParagraphs(self, String text, RichTextAttr paraStyle=None) -> RichTextRange"""
        return _richtext.RichTextParagraphLayoutBox_AddParagraphs(*args, **kwargs)

    def GetLineAtPosition(*args, **kwargs):
        """GetLineAtPosition(self, long pos, bool caretPosition=False) -> RichTextLine"""
        return _richtext.RichTextParagraphLayoutBox_GetLineAtPosition(*args, **kwargs)

    def GetLineAtYPosition(*args, **kwargs):
        """GetLineAtYPosition(self, int y) -> RichTextLine"""
        return _richtext.RichTextParagraphLayoutBox_GetLineAtYPosition(*args, **kwargs)

    def GetParagraphAtPosition(*args, **kwargs):
        """GetParagraphAtPosition(self, long pos, bool caretPosition=False) -> RichTextParagraph"""
        return _richtext.RichTextParagraphLayoutBox_GetParagraphAtPosition(*args, **kwargs)

    def GetLineSizeAtPosition(*args, **kwargs):
        """GetLineSizeAtPosition(self, long pos, bool caretPosition=False) -> Size"""
        return _richtext.RichTextParagraphLayoutBox_GetLineSizeAtPosition(*args, **kwargs)

    def GetVisibleLineNumber(*args, **kwargs):
        """GetVisibleLineNumber(self, long pos, bool caretPosition=False, bool startOfLine=False) -> long"""
        return _richtext.RichTextParagraphLayoutBox_GetVisibleLineNumber(*args, **kwargs)

    def GetLineForVisibleLineNumber(*args, **kwargs):
        """GetLineForVisibleLineNumber(self, long lineNumber) -> RichTextLine"""
        return _richtext.RichTextParagraphLayoutBox_GetLineForVisibleLineNumber(*args, **kwargs)

    def GetLeafObjectAtPosition(*args, **kwargs):
        """GetLeafObjectAtPosition(self, long position) -> RichTextObject"""
        return _richtext.RichTextParagraphLayoutBox_GetLeafObjectAtPosition(*args, **kwargs)

    def GetParagraphAtLine(*args, **kwargs):
        """GetParagraphAtLine(self, long paragraphNumber) -> RichTextParagraph"""
        return _richtext.RichTextParagraphLayoutBox_GetParagraphAtLine(*args, **kwargs)

    def GetParagraphForLine(*args, **kwargs):
        """GetParagraphForLine(self, RichTextLine line) -> RichTextParagraph"""
        return _richtext.RichTextParagraphLayoutBox_GetParagraphForLine(*args, **kwargs)

    def GetParagraphLength(*args, **kwargs):
        """GetParagraphLength(self, long paragraphNumber) -> int"""
        return _richtext.RichTextParagraphLayoutBox_GetParagraphLength(*args, **kwargs)

    def GetParagraphCount(*args, **kwargs):
        """GetParagraphCount(self) -> int"""
        return _richtext.RichTextParagraphLayoutBox_GetParagraphCount(*args, **kwargs)

    def GetLineCount(*args, **kwargs):
        """GetLineCount(self) -> int"""
        return _richtext.RichTextParagraphLayoutBox_GetLineCount(*args, **kwargs)

    def GetParagraphText(*args, **kwargs):
        """GetParagraphText(self, long paragraphNumber) -> String"""
        return _richtext.RichTextParagraphLayoutBox_GetParagraphText(*args, **kwargs)

    def XYToPosition(*args, **kwargs):
        """XYToPosition(self, long x, long y) -> long"""
        return _richtext.RichTextParagraphLayoutBox_XYToPosition(*args, **kwargs)

    def PositionToXY(*args, **kwargs):
        """PositionToXY(self, long pos, long x, long y) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_PositionToXY(*args, **kwargs)

    def SetStyle(*args, **kwargs):
        """SetStyle(self, RichTextRange range, RichTextAttr style, int flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_SetStyle(*args, **kwargs)

    def GetStyle(*args, **kwargs):
        """GetStyle(self, long position, RichTextAttr style) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_GetStyle(*args, **kwargs)

    def GetUncombinedStyle(*args, **kwargs):
        """GetUncombinedStyle(self, long position, RichTextAttr style) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_GetUncombinedStyle(*args, **kwargs)

    def DoGetStyle(*args, **kwargs):
        """DoGetStyle(self, long position, RichTextAttr style, bool combineStyles=True) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_DoGetStyle(*args, **kwargs)

    def GetStyleForRange(*args, **kwargs):
        """GetStyleForRange(self, RichTextRange range, RichTextAttr style) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_GetStyleForRange(*args, **kwargs)

    def CollectStyle(*args, **kwargs):
        """
        CollectStyle(self, RichTextAttr currentStyle, RichTextAttr style, RichTextAttr clashingAttr, 
            RichTextAttr absentAttr) -> bool
        """
        return _richtext.RichTextParagraphLayoutBox_CollectStyle(*args, **kwargs)

    def SetListStyle(*args):
        """
        SetListStyle(self, RichTextRange range, wxRichTextListStyleDefinition def, 
            int flags=RICHTEXT_SETSTYLE_WITH_UNDO, int startFrom=1, 
            int specifiedLevel=-1) -> bool
        SetListStyle(self, RichTextRange range, String defName, int flags=RICHTEXT_SETSTYLE_WITH_UNDO, 
            int startFrom=1, int specifiedLevel=-1) -> bool
        """
        return _richtext.RichTextParagraphLayoutBox_SetListStyle(*args)

    def ClearListStyle(*args, **kwargs):
        """ClearListStyle(self, RichTextRange range, int flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_ClearListStyle(*args, **kwargs)

    def NumberList(*args):
        """
        NumberList(self, RichTextRange range, wxRichTextListStyleDefinition def=None, 
            int flags=RICHTEXT_SETSTYLE_WITH_UNDO, 
            int startFrom=1, int specifiedLevel=-1) -> bool
        NumberList(self, RichTextRange range, String defName, int flags=RICHTEXT_SETSTYLE_WITH_UNDO, 
            int startFrom=1, int specifiedLevel=-1) -> bool
        """
        return _richtext.RichTextParagraphLayoutBox_NumberList(*args)

    def PromoteList(*args):
        """
        PromoteList(self, int promoteBy, RichTextRange range, wxRichTextListStyleDefinition def=None, 
            int flags=RICHTEXT_SETSTYLE_WITH_UNDO, 
            int specifiedLevel=-1) -> bool
        PromoteList(self, int promoteBy, RichTextRange range, String defName, 
            int flags=RICHTEXT_SETSTYLE_WITH_UNDO, int specifiedLevel=-1) -> bool
        """
        return _richtext.RichTextParagraphLayoutBox_PromoteList(*args)

    def DoNumberList(*args, **kwargs):
        """
        DoNumberList(self, RichTextRange range, RichTextRange promotionRange, 
            int promoteBy, wxRichTextListStyleDefinition def, 
            int flags=RICHTEXT_SETSTYLE_WITH_UNDO, int startFrom=1, 
            int specifiedLevel=-1) -> bool
        """
        return _richtext.RichTextParagraphLayoutBox_DoNumberList(*args, **kwargs)

    def FindNextParagraphNumber(*args, **kwargs):
        """FindNextParagraphNumber(self, RichTextParagraph previousParagraph, RichTextAttr attr) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_FindNextParagraphNumber(*args, **kwargs)

    def HasCharacterAttributes(*args, **kwargs):
        """HasCharacterAttributes(self, RichTextRange range, RichTextAttr style) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_HasCharacterAttributes(*args, **kwargs)

    def HasParagraphAttributes(*args, **kwargs):
        """HasParagraphAttributes(self, RichTextRange range, RichTextAttr style) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_HasParagraphAttributes(*args, **kwargs)

    def InsertFragment(*args, **kwargs):
        """InsertFragment(self, long position, RichTextParagraphLayoutBox fragment) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_InsertFragment(*args, **kwargs)

    def CopyFragment(*args, **kwargs):
        """CopyFragment(self, RichTextRange range, RichTextParagraphLayoutBox fragment) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_CopyFragment(*args, **kwargs)

    def ApplyStyleSheet(*args, **kwargs):
        """ApplyStyleSheet(self, wxRichTextStyleSheet styleSheet) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_ApplyStyleSheet(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextParagraphLayoutBox obj)"""
        return _richtext.RichTextParagraphLayoutBox_Copy(*args, **kwargs)

    def UpdateRanges(*args, **kwargs):
        """UpdateRanges(self)"""
        return _richtext.RichTextParagraphLayoutBox_UpdateRanges(*args, **kwargs)

    def GetText(*args, **kwargs):
        """GetText(self) -> String"""
        return _richtext.RichTextParagraphLayoutBox_GetText(*args, **kwargs)

    def SetDefaultStyle(*args, **kwargs):
        """SetDefaultStyle(self, RichTextAttr style) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_SetDefaultStyle(*args, **kwargs)

    def GetDefaultStyle(*args, **kwargs):
        """GetDefaultStyle(self) -> RichTextAttr"""
        return _richtext.RichTextParagraphLayoutBox_GetDefaultStyle(*args, **kwargs)

    def SetBasicStyle(*args, **kwargs):
        """SetBasicStyle(self, RichTextAttr style)"""
        return _richtext.RichTextParagraphLayoutBox_SetBasicStyle(*args, **kwargs)

    def GetBasicStyle(*args, **kwargs):
        """GetBasicStyle(self) -> RichTextAttr"""
        return _richtext.RichTextParagraphLayoutBox_GetBasicStyle(*args, **kwargs)

    def Invalidate(*args, **kwargs):
        """Invalidate(self, RichTextRange invalidRange=wxRICHTEXT_ALL)"""
        return _richtext.RichTextParagraphLayoutBox_Invalidate(*args, **kwargs)

    def UpdateFloatingObjects(*args, **kwargs):
        """UpdateFloatingObjects(self, Rect availableRect, RichTextObject untilObj=None) -> bool"""
        return _richtext.RichTextParagraphLayoutBox_UpdateFloatingObjects(*args, **kwargs)

    def GetInvalidRange(*args, **kwargs):
        """GetInvalidRange(self, bool wholeParagraphs=False) -> RichTextRange"""
        return _richtext.RichTextParagraphLayoutBox_GetInvalidRange(*args, **kwargs)

    def GetFloatCollector(*args, **kwargs):
        """GetFloatCollector(self) -> wxRichTextFloatCollector"""
        return _richtext.RichTextParagraphLayoutBox_GetFloatCollector(*args, **kwargs)

_richtext.RichTextParagraphLayoutBox_swigregister(RichTextParagraphLayoutBox)

class RichTextBox(RichTextCompositeObject):
    """Proxy of C++ RichTextBox class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, RichTextObject parent=None) -> RichTextBox
        __init__(self, RichTextBox obj) -> RichTextBox
        """
        _richtext.RichTextBox_swiginit(self,_richtext.new_RichTextBox(*args))
    def Copy(*args, **kwargs):
        """Copy(self, RichTextBox obj)"""
        return _richtext.RichTextBox_Copy(*args, **kwargs)

_richtext.RichTextBox_swigregister(RichTextBox)

class RichTextLine(object):
    """
    This object represents a line in a paragraph, and stores offsets from
    the start of the paragraph representing the start and end positions of
    the line.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, RichTextParagraph parent) -> RichTextLine

        This object represents a line in a paragraph, and stores offsets from
        the start of the paragraph representing the start and end positions of
        the line.
        """
        _richtext.RichTextLine_swiginit(self,_richtext.new_RichTextLine(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_RichTextLine
    __del__ = lambda self : None;
    def SetRange(*args, **kwargs):
        """SetRange(self, RichTextRange range)"""
        return _richtext.RichTextLine_SetRange(*args, **kwargs)

    def GetParent(*args, **kwargs):
        """GetParent(self) -> RichTextParagraph"""
        return _richtext.RichTextLine_GetParent(*args, **kwargs)

    def GetRange(*args, **kwargs):
        """GetRange(self) -> RichTextRange"""
        return _richtext.RichTextLine_GetRange(*args, **kwargs)

    def GetAbsoluteRange(*args, **kwargs):
        """GetAbsoluteRange(self) -> RichTextRange"""
        return _richtext.RichTextLine_GetAbsoluteRange(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """GetSize(self) -> Size"""
        return _richtext.RichTextLine_GetSize(*args, **kwargs)

    def SetSize(*args, **kwargs):
        """SetSize(self, Size sz)"""
        return _richtext.RichTextLine_SetSize(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> Point"""
        return _richtext.RichTextLine_GetPosition(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, Point pos)"""
        return _richtext.RichTextLine_SetPosition(*args, **kwargs)

    def GetAbsolutePosition(*args, **kwargs):
        """GetAbsolutePosition(self) -> Point"""
        return _richtext.RichTextLine_GetAbsolutePosition(*args, **kwargs)

    def GetRect(*args, **kwargs):
        """GetRect(self) -> Rect"""
        return _richtext.RichTextLine_GetRect(*args, **kwargs)

    def SetDescent(*args, **kwargs):
        """SetDescent(self, int descent)"""
        return _richtext.RichTextLine_SetDescent(*args, **kwargs)

    def GetDescent(*args, **kwargs):
        """GetDescent(self) -> int"""
        return _richtext.RichTextLine_GetDescent(*args, **kwargs)

    def Init(*args, **kwargs):
        """Init(self, RichTextParagraph parent)"""
        return _richtext.RichTextLine_Init(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextLine obj)"""
        return _richtext.RichTextLine_Copy(*args, **kwargs)

    def Clone(*args, **kwargs):
        """Clone(self) -> RichTextLine"""
        return _richtext.RichTextLine_Clone(*args, **kwargs)

_richtext.RichTextLine_swigregister(RichTextLine)

class RichTextParagraph(RichTextBox):
    """
    This object represents a single paragraph (or in a straight text
    editor, a line).
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String text, RichTextObject parent=None, RichTextAttr paraStyle=None, 
            RichTextAttr charStyle=None) -> RichTextParagraph

        This object represents a single paragraph (or in a straight text
        editor, a line).
        """
        _richtext.RichTextParagraph_swiginit(self,_richtext.new_RichTextParagraph(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_RichTextParagraph
    __del__ = lambda self : None;
    def GetLines(*args, **kwargs):
        """GetLines(self) -> wxRichTextLineList"""
        return _richtext.RichTextParagraph_GetLines(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextParagraph obj)"""
        return _richtext.RichTextParagraph_Copy(*args, **kwargs)

    def ClearLines(*args, **kwargs):
        """ClearLines(self)"""
        return _richtext.RichTextParagraph_ClearLines(*args, **kwargs)

    def ApplyParagraphStyle(*args, **kwargs):
        """ApplyParagraphStyle(self, RichTextLine line, RichTextAttr attr, Rect rect, DC dc)"""
        return _richtext.RichTextParagraph_ApplyParagraphStyle(*args, **kwargs)

    def InsertText(*args, **kwargs):
        """InsertText(self, long pos, String text) -> bool"""
        return _richtext.RichTextParagraph_InsertText(*args, **kwargs)

    def SplitAt(*args, **kwargs):
        """SplitAt(self, long pos, RichTextObject previousObject=None) -> RichTextObject"""
        return _richtext.RichTextParagraph_SplitAt(*args, **kwargs)

    def MoveToList(*args, **kwargs):
        """MoveToList(self, RichTextObject obj, wxList list)"""
        return _richtext.RichTextParagraph_MoveToList(*args, **kwargs)

    def MoveFromList(*args, **kwargs):
        """MoveFromList(self, wxList list)"""
        return _richtext.RichTextParagraph_MoveFromList(*args, **kwargs)

    def GetContiguousPlainText(*args, **kwargs):
        """GetContiguousPlainText(self, String text, RichTextRange range, bool fromStart=True) -> bool"""
        return _richtext.RichTextParagraph_GetContiguousPlainText(*args, **kwargs)

    def FindWrapPosition(*args, **kwargs):
        """
        FindWrapPosition(self, RichTextRange range, DC dc, RichTextDrawingContext context, 
            int availableSpace, long wrapPosition, 
            wxArrayInt partialExtents) -> bool
        """
        return _richtext.RichTextParagraph_FindWrapPosition(*args, **kwargs)

    def FindObjectAtPosition(*args, **kwargs):
        """FindObjectAtPosition(self, long position) -> RichTextObject"""
        return _richtext.RichTextParagraph_FindObjectAtPosition(*args, **kwargs)

    def GetBulletText(*args, **kwargs):
        """GetBulletText(self) -> String"""
        return _richtext.RichTextParagraph_GetBulletText(*args, **kwargs)

    def AllocateLine(*args, **kwargs):
        """AllocateLine(self, int pos) -> RichTextLine"""
        return _richtext.RichTextParagraph_AllocateLine(*args, **kwargs)

    def ClearUnusedLines(*args, **kwargs):
        """ClearUnusedLines(self, int lineCount) -> bool"""
        return _richtext.RichTextParagraph_ClearUnusedLines(*args, **kwargs)

    def GetCombinedAttributes(*args, **kwargs):
        """GetCombinedAttributes(self, RichTextAttr contentStyle=None) -> RichTextAttr"""
        return _richtext.RichTextParagraph_GetCombinedAttributes(*args, **kwargs)

    def GetFirstLineBreakPosition(*args, **kwargs):
        """GetFirstLineBreakPosition(self, long pos) -> long"""
        return _richtext.RichTextParagraph_GetFirstLineBreakPosition(*args, **kwargs)

    def InitDefaultTabs(*args, **kwargs):
        """InitDefaultTabs()"""
        return _richtext.RichTextParagraph_InitDefaultTabs(*args, **kwargs)

    InitDefaultTabs = staticmethod(InitDefaultTabs)
    def ClearDefaultTabs(*args, **kwargs):
        """ClearDefaultTabs()"""
        return _richtext.RichTextParagraph_ClearDefaultTabs(*args, **kwargs)

    ClearDefaultTabs = staticmethod(ClearDefaultTabs)
    def GetDefaultTabs(*args, **kwargs):
        """GetDefaultTabs() -> wxArrayInt"""
        return _richtext.RichTextParagraph_GetDefaultTabs(*args, **kwargs)

    GetDefaultTabs = staticmethod(GetDefaultTabs)
_richtext.RichTextParagraph_swigregister(RichTextParagraph)

def RichTextParagraph_InitDefaultTabs(*args):
  """RichTextParagraph_InitDefaultTabs()"""
  return _richtext.RichTextParagraph_InitDefaultTabs(*args)

def RichTextParagraph_ClearDefaultTabs(*args):
  """RichTextParagraph_ClearDefaultTabs()"""
  return _richtext.RichTextParagraph_ClearDefaultTabs(*args)

def RichTextParagraph_GetDefaultTabs(*args):
  """RichTextParagraph_GetDefaultTabs() -> wxArrayInt"""
  return _richtext.RichTextParagraph_GetDefaultTabs(*args)

class RichTextPlainText(RichTextObject):
    """This object represents a single piece of text."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String text=wxEmptyString, RichTextObject parent=None, 
            RichTextAttr style=None) -> RichTextPlainText

        This object represents a single piece of text.
        """
        _richtext.RichTextPlainText_swiginit(self,_richtext.new_RichTextPlainText(*args, **kwargs))
    def GetFirstLineBreakPosition(*args, **kwargs):
        """GetFirstLineBreakPosition(self, long pos) -> long"""
        return _richtext.RichTextPlainText_GetFirstLineBreakPosition(*args, **kwargs)

    def GetText(*args, **kwargs):
        """GetText(self) -> String"""
        return _richtext.RichTextPlainText_GetText(*args, **kwargs)

    def SetText(*args, **kwargs):
        """SetText(self, String text)"""
        return _richtext.RichTextPlainText_SetText(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextPlainText obj)"""
        return _richtext.RichTextPlainText_Copy(*args, **kwargs)

_richtext.RichTextPlainText_swigregister(RichTextPlainText)

class RichTextImage(RichTextObject):
    """This object represents an image."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, RichTextObject parent=None) -> RichTextImage
        __init__(self, Image image, RichTextObject parent=None, RichTextAttr charStyle=None) -> RichTextImage
        __init__(self, wxRichTextImageBlock imageBlock, RichTextObject parent=None, 
            RichTextAttr charStyle=None) -> RichTextImage
        __init__(self, RichTextImage obj) -> RichTextImage

        This object represents an image.
        """
        _richtext.RichTextImage_swiginit(self,_richtext.new_RichTextImage(*args))
    def GetImageCache(*args, **kwargs):
        """GetImageCache(self) -> Bitmap"""
        return _richtext.RichTextImage_GetImageCache(*args, **kwargs)

    def SetImageCache(*args, **kwargs):
        """SetImageCache(self, Bitmap bitmap)"""
        return _richtext.RichTextImage_SetImageCache(*args, **kwargs)

    def ResetImageCache(*args, **kwargs):
        """ResetImageCache(self)"""
        return _richtext.RichTextImage_ResetImageCache(*args, **kwargs)

    def GetImageBlock(*args, **kwargs):
        """GetImageBlock(self) -> wxRichTextImageBlock"""
        return _richtext.RichTextImage_GetImageBlock(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextImage obj)"""
        return _richtext.RichTextImage_Copy(*args, **kwargs)

    def LoadImageCache(*args, **kwargs):
        """LoadImageCache(self, DC dc, bool resetCache=False) -> bool"""
        return _richtext.RichTextImage_LoadImageCache(*args, **kwargs)

_richtext.RichTextImage_swigregister(RichTextImage)

class RichTextFileHandlerList_iterator(object):
    """This class serves as an iterator for a wxRichTextFileHandlerList object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextFileHandlerList_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> RichTextFileHandler"""
        return _richtext.RichTextFileHandlerList_iterator_next(*args, **kwargs)

_richtext.RichTextFileHandlerList_iterator_swigregister(RichTextFileHandlerList_iterator)

class RichTextFileHandlerList(object):
    """
    This class wraps a wxList-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextFileHandlerList
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return _richtext.RichTextFileHandlerList___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> RichTextFileHandler"""
        return _richtext.RichTextFileHandlerList___getitem__(*args, **kwargs)

    def __contains__(*args, **kwargs):
        """__contains__(self, RichTextFileHandler obj) -> bool"""
        return _richtext.RichTextFileHandlerList___contains__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> RichTextFileHandlerList_iterator"""
        return _richtext.RichTextFileHandlerList___iter__(*args, **kwargs)

    def __repr__(self):
        return "wxRichTextFileHandlerList: " + repr(list(self))

_richtext.RichTextFileHandlerList_swigregister(RichTextFileHandlerList)

class RichTextBuffer(RichTextParagraphLayoutBox):
    """This is a kind of box, used to represent the whole buffer."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> RichTextBuffer

        This is a kind of box, used to represent the whole buffer.
        """
        _richtext.RichTextBuffer_swiginit(self,_richtext.new_RichTextBuffer(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_RichTextBuffer
    __del__ = lambda self : None;
    def GetCommandProcessor(*args, **kwargs):
        """GetCommandProcessor(self) -> wxCommandProcessor"""
        return _richtext.RichTextBuffer_GetCommandProcessor(*args, **kwargs)

    def SetStyleSheet(*args, **kwargs):
        """SetStyleSheet(self, wxRichTextStyleSheet styleSheet)"""
        return _richtext.RichTextBuffer_SetStyleSheet(*args, **kwargs)

    def SetStyleSheetAndNotify(*args, **kwargs):
        """SetStyleSheetAndNotify(self, wxRichTextStyleSheet sheet) -> bool"""
        return _richtext.RichTextBuffer_SetStyleSheetAndNotify(*args, **kwargs)

    def PushStyleSheet(*args, **kwargs):
        """PushStyleSheet(self, wxRichTextStyleSheet styleSheet) -> bool"""
        return _richtext.RichTextBuffer_PushStyleSheet(*args, **kwargs)

    def PopStyleSheet(*args, **kwargs):
        """PopStyleSheet(self) -> wxRichTextStyleSheet"""
        return _richtext.RichTextBuffer_PopStyleSheet(*args, **kwargs)

    def GetFontTable(*args, **kwargs):
        """GetFontTable(self) -> RichTextFontTable"""
        return _richtext.RichTextBuffer_GetFontTable(*args, **kwargs)

    def SetFontTable(*args, **kwargs):
        """SetFontTable(self, RichTextFontTable table)"""
        return _richtext.RichTextBuffer_SetFontTable(*args, **kwargs)

    def Init(*args, **kwargs):
        """Init(self)"""
        return _richtext.RichTextBuffer_Init(*args, **kwargs)

    def ResetAndClearCommands(*args, **kwargs):
        """ResetAndClearCommands(self)"""
        return _richtext.RichTextBuffer_ResetAndClearCommands(*args, **kwargs)

    def LoadFile(*args, **kwargs):
        """LoadFile(self, String filename, int type=RICHTEXT_TYPE_ANY) -> bool"""
        return _richtext.RichTextBuffer_LoadFile(*args, **kwargs)

    def SaveFile(*args, **kwargs):
        """SaveFile(self, String filename, int type=RICHTEXT_TYPE_ANY) -> bool"""
        return _richtext.RichTextBuffer_SaveFile(*args, **kwargs)

    def LoadStream(*args, **kwargs):
        """LoadStream(self, InputStream stream, int type=RICHTEXT_TYPE_ANY) -> bool"""
        return _richtext.RichTextBuffer_LoadStream(*args, **kwargs)

    def SaveStream(*args, **kwargs):
        """SaveStream(self, wxOutputStream stream, int type=RICHTEXT_TYPE_ANY) -> bool"""
        return _richtext.RichTextBuffer_SaveStream(*args, **kwargs)

    def SetHandlerFlags(*args, **kwargs):
        """SetHandlerFlags(self, int flags)"""
        return _richtext.RichTextBuffer_SetHandlerFlags(*args, **kwargs)

    def GetHandlerFlags(*args, **kwargs):
        """GetHandlerFlags(self) -> int"""
        return _richtext.RichTextBuffer_GetHandlerFlags(*args, **kwargs)

    def BeginBatchUndo(*args, **kwargs):
        """BeginBatchUndo(self, String cmdName) -> bool"""
        return _richtext.RichTextBuffer_BeginBatchUndo(*args, **kwargs)

    def EndBatchUndo(*args, **kwargs):
        """EndBatchUndo(self) -> bool"""
        return _richtext.RichTextBuffer_EndBatchUndo(*args, **kwargs)

    def BatchingUndo(*args, **kwargs):
        """BatchingUndo(self) -> bool"""
        return _richtext.RichTextBuffer_BatchingUndo(*args, **kwargs)

    def SubmitAction(*args, **kwargs):
        """SubmitAction(self, RichTextAction action) -> bool"""
        return _richtext.RichTextBuffer_SubmitAction(*args, **kwargs)

    def GetBatchedCommand(*args, **kwargs):
        """GetBatchedCommand(self) -> RichTextCommand"""
        return _richtext.RichTextBuffer_GetBatchedCommand(*args, **kwargs)

    def BeginSuppressUndo(*args, **kwargs):
        """BeginSuppressUndo(self) -> bool"""
        return _richtext.RichTextBuffer_BeginSuppressUndo(*args, **kwargs)

    def EndSuppressUndo(*args, **kwargs):
        """EndSuppressUndo(self) -> bool"""
        return _richtext.RichTextBuffer_EndSuppressUndo(*args, **kwargs)

    def SuppressingUndo(*args, **kwargs):
        """SuppressingUndo(self) -> bool"""
        return _richtext.RichTextBuffer_SuppressingUndo(*args, **kwargs)

    def CopyToClipboard(*args, **kwargs):
        """CopyToClipboard(self, RichTextRange range) -> bool"""
        return _richtext.RichTextBuffer_CopyToClipboard(*args, **kwargs)

    def PasteFromClipboard(*args, **kwargs):
        """PasteFromClipboard(self, long position) -> bool"""
        return _richtext.RichTextBuffer_PasteFromClipboard(*args, **kwargs)

    def CanPasteFromClipboard(*args, **kwargs):
        """CanPasteFromClipboard(self) -> bool"""
        return _richtext.RichTextBuffer_CanPasteFromClipboard(*args, **kwargs)

    def BeginStyle(*args, **kwargs):
        """BeginStyle(self, RichTextAttr style) -> bool"""
        return _richtext.RichTextBuffer_BeginStyle(*args, **kwargs)

    def EndStyle(*args, **kwargs):
        """EndStyle(self) -> bool"""
        return _richtext.RichTextBuffer_EndStyle(*args, **kwargs)

    def EndAllStyles(*args, **kwargs):
        """EndAllStyles(self) -> bool"""
        return _richtext.RichTextBuffer_EndAllStyles(*args, **kwargs)

    def ClearStyleStack(*args, **kwargs):
        """ClearStyleStack(self)"""
        return _richtext.RichTextBuffer_ClearStyleStack(*args, **kwargs)

    def GetStyleStackSize(*args, **kwargs):
        """GetStyleStackSize(self) -> size_t"""
        return _richtext.RichTextBuffer_GetStyleStackSize(*args, **kwargs)

    def BeginBold(*args, **kwargs):
        """BeginBold(self) -> bool"""
        return _richtext.RichTextBuffer_BeginBold(*args, **kwargs)

    def EndBold(*args, **kwargs):
        """EndBold(self) -> bool"""
        return _richtext.RichTextBuffer_EndBold(*args, **kwargs)

    def BeginItalic(*args, **kwargs):
        """BeginItalic(self) -> bool"""
        return _richtext.RichTextBuffer_BeginItalic(*args, **kwargs)

    def EndItalic(*args, **kwargs):
        """EndItalic(self) -> bool"""
        return _richtext.RichTextBuffer_EndItalic(*args, **kwargs)

    def BeginUnderline(*args, **kwargs):
        """BeginUnderline(self) -> bool"""
        return _richtext.RichTextBuffer_BeginUnderline(*args, **kwargs)

    def EndUnderline(*args, **kwargs):
        """EndUnderline(self) -> bool"""
        return _richtext.RichTextBuffer_EndUnderline(*args, **kwargs)

    def BeginFontSize(*args, **kwargs):
        """BeginFontSize(self, int pointSize) -> bool"""
        return _richtext.RichTextBuffer_BeginFontSize(*args, **kwargs)

    def EndFontSize(*args, **kwargs):
        """EndFontSize(self) -> bool"""
        return _richtext.RichTextBuffer_EndFontSize(*args, **kwargs)

    def BeginFont(*args, **kwargs):
        """BeginFont(self, Font font) -> bool"""
        return _richtext.RichTextBuffer_BeginFont(*args, **kwargs)

    def EndFont(*args, **kwargs):
        """EndFont(self) -> bool"""
        return _richtext.RichTextBuffer_EndFont(*args, **kwargs)

    def BeginTextColour(*args, **kwargs):
        """BeginTextColour(self, Colour colour) -> bool"""
        return _richtext.RichTextBuffer_BeginTextColour(*args, **kwargs)

    def EndTextColour(*args, **kwargs):
        """EndTextColour(self) -> bool"""
        return _richtext.RichTextBuffer_EndTextColour(*args, **kwargs)

    def BeginAlignment(*args, **kwargs):
        """BeginAlignment(self, int alignment) -> bool"""
        return _richtext.RichTextBuffer_BeginAlignment(*args, **kwargs)

    def EndAlignment(*args, **kwargs):
        """EndAlignment(self) -> bool"""
        return _richtext.RichTextBuffer_EndAlignment(*args, **kwargs)

    def BeginLeftIndent(*args, **kwargs):
        """BeginLeftIndent(self, int leftIndent, int leftSubIndent=0) -> bool"""
        return _richtext.RichTextBuffer_BeginLeftIndent(*args, **kwargs)

    def EndLeftIndent(*args, **kwargs):
        """EndLeftIndent(self) -> bool"""
        return _richtext.RichTextBuffer_EndLeftIndent(*args, **kwargs)

    def BeginRightIndent(*args, **kwargs):
        """BeginRightIndent(self, int rightIndent) -> bool"""
        return _richtext.RichTextBuffer_BeginRightIndent(*args, **kwargs)

    def EndRightIndent(*args, **kwargs):
        """EndRightIndent(self) -> bool"""
        return _richtext.RichTextBuffer_EndRightIndent(*args, **kwargs)

    def BeginParagraphSpacing(*args, **kwargs):
        """BeginParagraphSpacing(self, int before, int after) -> bool"""
        return _richtext.RichTextBuffer_BeginParagraphSpacing(*args, **kwargs)

    def EndParagraphSpacing(*args, **kwargs):
        """EndParagraphSpacing(self) -> bool"""
        return _richtext.RichTextBuffer_EndParagraphSpacing(*args, **kwargs)

    def BeginLineSpacing(*args, **kwargs):
        """BeginLineSpacing(self, int lineSpacing) -> bool"""
        return _richtext.RichTextBuffer_BeginLineSpacing(*args, **kwargs)

    def EndLineSpacing(*args, **kwargs):
        """EndLineSpacing(self) -> bool"""
        return _richtext.RichTextBuffer_EndLineSpacing(*args, **kwargs)

    def BeginNumberedBullet(*args, **kwargs):
        """
        BeginNumberedBullet(self, int bulletNumber, int leftIndent, int leftSubIndent, 
            int bulletStyle=wxTEXT_ATTR_BULLET_STYLE_ARABIC|wxTEXT_ATTR_BULLET_STYLE_PERIOD) -> bool
        """
        return _richtext.RichTextBuffer_BeginNumberedBullet(*args, **kwargs)

    def EndNumberedBullet(*args, **kwargs):
        """EndNumberedBullet(self) -> bool"""
        return _richtext.RichTextBuffer_EndNumberedBullet(*args, **kwargs)

    def BeginSymbolBullet(*args, **kwargs):
        """BeginSymbolBullet(self, String symbol, int leftIndent, int leftSubIndent, int bulletStyle=TEXT_ATTR_BULLET_STYLE_SYMBOL) -> bool"""
        return _richtext.RichTextBuffer_BeginSymbolBullet(*args, **kwargs)

    def EndSymbolBullet(*args, **kwargs):
        """EndSymbolBullet(self) -> bool"""
        return _richtext.RichTextBuffer_EndSymbolBullet(*args, **kwargs)

    def BeginStandardBullet(*args, **kwargs):
        """
        BeginStandardBullet(self, String bulletName, int leftIndent, int leftSubIndent, 
            int bulletStyle=TEXT_ATTR_BULLET_STYLE_STANDARD) -> bool
        """
        return _richtext.RichTextBuffer_BeginStandardBullet(*args, **kwargs)

    def EndStandardBullet(*args, **kwargs):
        """EndStandardBullet(self) -> bool"""
        return _richtext.RichTextBuffer_EndStandardBullet(*args, **kwargs)

    def BeginCharacterStyle(*args, **kwargs):
        """BeginCharacterStyle(self, String characterStyle) -> bool"""
        return _richtext.RichTextBuffer_BeginCharacterStyle(*args, **kwargs)

    def EndCharacterStyle(*args, **kwargs):
        """EndCharacterStyle(self) -> bool"""
        return _richtext.RichTextBuffer_EndCharacterStyle(*args, **kwargs)

    def BeginParagraphStyle(*args, **kwargs):
        """BeginParagraphStyle(self, String paragraphStyle) -> bool"""
        return _richtext.RichTextBuffer_BeginParagraphStyle(*args, **kwargs)

    def EndParagraphStyle(*args, **kwargs):
        """EndParagraphStyle(self) -> bool"""
        return _richtext.RichTextBuffer_EndParagraphStyle(*args, **kwargs)

    def BeginListStyle(*args, **kwargs):
        """BeginListStyle(self, String listStyle, int level=1, int number=1) -> bool"""
        return _richtext.RichTextBuffer_BeginListStyle(*args, **kwargs)

    def EndListStyle(*args, **kwargs):
        """EndListStyle(self) -> bool"""
        return _richtext.RichTextBuffer_EndListStyle(*args, **kwargs)

    def BeginURL(*args, **kwargs):
        """BeginURL(self, String url, String characterStyle=wxEmptyString) -> bool"""
        return _richtext.RichTextBuffer_BeginURL(*args, **kwargs)

    def EndURL(*args, **kwargs):
        """EndURL(self) -> bool"""
        return _richtext.RichTextBuffer_EndURL(*args, **kwargs)

    def AddEventHandler(*args, **kwargs):
        """AddEventHandler(self, EvtHandler handler) -> bool"""
        return _richtext.RichTextBuffer_AddEventHandler(*args, **kwargs)

    def RemoveEventHandler(*args, **kwargs):
        """RemoveEventHandler(self, EvtHandler handler, bool deleteHandler=False) -> bool"""
        return _richtext.RichTextBuffer_RemoveEventHandler(*args, **kwargs)

    def ClearEventHandlers(*args, **kwargs):
        """ClearEventHandlers(self)"""
        return _richtext.RichTextBuffer_ClearEventHandlers(*args, **kwargs)

    def SendEvent(*args, **kwargs):
        """SendEvent(self, Event event, bool sendToAll=True) -> bool"""
        return _richtext.RichTextBuffer_SendEvent(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self, RichTextBuffer obj)"""
        return _richtext.RichTextBuffer_Copy(*args, **kwargs)

    def InsertParagraphsWithUndo(*args, **kwargs):
        """
        InsertParagraphsWithUndo(self, long pos, RichTextParagraphLayoutBox paragraphs, RichTextCtrl ctrl, 
            int flags=0) -> bool
        """
        return _richtext.RichTextBuffer_InsertParagraphsWithUndo(*args, **kwargs)

    def InsertTextWithUndo(*args, **kwargs):
        """InsertTextWithUndo(self, long pos, String text, RichTextCtrl ctrl, int flags=0) -> bool"""
        return _richtext.RichTextBuffer_InsertTextWithUndo(*args, **kwargs)

    def InsertNewlineWithUndo(*args, **kwargs):
        """InsertNewlineWithUndo(self, long pos, RichTextCtrl ctrl, int flags=0) -> bool"""
        return _richtext.RichTextBuffer_InsertNewlineWithUndo(*args, **kwargs)

    def InsertImageWithUndo(*args, **kwargs):
        """
        InsertImageWithUndo(self, long pos, wxRichTextImageBlock imageBlock, RichTextCtrl ctrl, 
            int flags=0) -> bool
        """
        return _richtext.RichTextBuffer_InsertImageWithUndo(*args, **kwargs)

    def DeleteRangeWithUndo(*args, **kwargs):
        """DeleteRangeWithUndo(self, RichTextRange range, RichTextCtrl ctrl) -> bool"""
        return _richtext.RichTextBuffer_DeleteRangeWithUndo(*args, **kwargs)

    def Modify(*args, **kwargs):
        """Modify(self, bool modify=True)"""
        return _richtext.RichTextBuffer_Modify(*args, **kwargs)

    def IsModified(*args, **kwargs):
        """IsModified(self) -> bool"""
        return _richtext.RichTextBuffer_IsModified(*args, **kwargs)

    def GetStyleForNewParagraph(*args, **kwargs):
        """
        GetStyleForNewParagraph(self, RichTextBuffer buffer, long pos, bool caretPosition=False, 
            bool lookUpNewParaStyle=False) -> RichTextAttr
        """
        return _richtext.RichTextBuffer_GetStyleForNewParagraph(*args, **kwargs)

    def GetHandlers(*args, **kwargs):
        """GetHandlers() -> wxRichTextFileHandlerList_t"""
        return _richtext.RichTextBuffer_GetHandlers(*args, **kwargs)

    GetHandlers = staticmethod(GetHandlers)
    def AddHandler(*args, **kwargs):
        """AddHandler(RichTextFileHandler handler)"""
        return _richtext.RichTextBuffer_AddHandler(*args, **kwargs)

    AddHandler = staticmethod(AddHandler)
    def InsertHandler(*args, **kwargs):
        """InsertHandler(RichTextFileHandler handler)"""
        return _richtext.RichTextBuffer_InsertHandler(*args, **kwargs)

    InsertHandler = staticmethod(InsertHandler)
    def RemoveHandler(*args, **kwargs):
        """RemoveHandler(String name) -> bool"""
        return _richtext.RichTextBuffer_RemoveHandler(*args, **kwargs)

    RemoveHandler = staticmethod(RemoveHandler)
    def FindHandlerByName(*args, **kwargs):
        """FindHandlerByName(String name) -> RichTextFileHandler"""
        return _richtext.RichTextBuffer_FindHandlerByName(*args, **kwargs)

    FindHandlerByName = staticmethod(FindHandlerByName)
    def FindHandlerByExtension(*args, **kwargs):
        """FindHandlerByExtension(String extension, int imageType) -> RichTextFileHandler"""
        return _richtext.RichTextBuffer_FindHandlerByExtension(*args, **kwargs)

    FindHandlerByExtension = staticmethod(FindHandlerByExtension)
    def FindHandlerByFilename(*args, **kwargs):
        """FindHandlerByFilename(String filename, int imageType) -> RichTextFileHandler"""
        return _richtext.RichTextBuffer_FindHandlerByFilename(*args, **kwargs)

    FindHandlerByFilename = staticmethod(FindHandlerByFilename)
    def FindHandlerByType(*args, **kwargs):
        """FindHandlerByType(int imageType) -> RichTextFileHandler"""
        return _richtext.RichTextBuffer_FindHandlerByType(*args, **kwargs)

    FindHandlerByType = staticmethod(FindHandlerByType)
    def GetExtWildcard(*args, **kwargs):
        """
        GetExtWildcard(self, bool combine=False, bool save=False) --> (wildcards, types)

        Gets a wildcard string for the file dialog based on all the currently
        loaded richtext file handlers, and a list that can be used to map
        those filter types to the file handler type.
        """
        return _richtext.RichTextBuffer_GetExtWildcard(*args, **kwargs)

    GetExtWildcard = staticmethod(GetExtWildcard)
    def CleanUpHandlers(*args, **kwargs):
        """CleanUpHandlers()"""
        return _richtext.RichTextBuffer_CleanUpHandlers(*args, **kwargs)

    CleanUpHandlers = staticmethod(CleanUpHandlers)
    def InitStandardHandlers(*args, **kwargs):
        """InitStandardHandlers()"""
        return _richtext.RichTextBuffer_InitStandardHandlers(*args, **kwargs)

    InitStandardHandlers = staticmethod(InitStandardHandlers)
    def GetRenderer(*args, **kwargs):
        """GetRenderer() -> RichTextRenderer"""
        return _richtext.RichTextBuffer_GetRenderer(*args, **kwargs)

    GetRenderer = staticmethod(GetRenderer)
    def SetRenderer(*args, **kwargs):
        """SetRenderer(RichTextRenderer renderer)"""
        return _richtext.RichTextBuffer_SetRenderer(*args, **kwargs)

    SetRenderer = staticmethod(SetRenderer)
    def GetBulletRightMargin(*args, **kwargs):
        """GetBulletRightMargin() -> int"""
        return _richtext.RichTextBuffer_GetBulletRightMargin(*args, **kwargs)

    GetBulletRightMargin = staticmethod(GetBulletRightMargin)
    def SetBulletRightMargin(*args, **kwargs):
        """SetBulletRightMargin(int margin)"""
        return _richtext.RichTextBuffer_SetBulletRightMargin(*args, **kwargs)

    SetBulletRightMargin = staticmethod(SetBulletRightMargin)
    def GetBulletProportion(*args, **kwargs):
        """GetBulletProportion() -> float"""
        return _richtext.RichTextBuffer_GetBulletProportion(*args, **kwargs)

    GetBulletProportion = staticmethod(GetBulletProportion)
    def SetBulletProportion(*args, **kwargs):
        """SetBulletProportion(float prop)"""
        return _richtext.RichTextBuffer_SetBulletProportion(*args, **kwargs)

    SetBulletProportion = staticmethod(SetBulletProportion)
    def GetScale(*args, **kwargs):
        """GetScale(self) -> double"""
        return _richtext.RichTextBuffer_GetScale(*args, **kwargs)

    def SetScale(*args, **kwargs):
        """SetScale(self, double scale)"""
        return _richtext.RichTextBuffer_SetScale(*args, **kwargs)

_richtext.RichTextBuffer_swigregister(RichTextBuffer)

def RichTextBuffer_GetHandlers(*args):
  """RichTextBuffer_GetHandlers() -> wxRichTextFileHandlerList_t"""
  return _richtext.RichTextBuffer_GetHandlers(*args)

def RichTextBuffer_AddHandler(*args, **kwargs):
  """RichTextBuffer_AddHandler(RichTextFileHandler handler)"""
  return _richtext.RichTextBuffer_AddHandler(*args, **kwargs)

def RichTextBuffer_InsertHandler(*args, **kwargs):
  """RichTextBuffer_InsertHandler(RichTextFileHandler handler)"""
  return _richtext.RichTextBuffer_InsertHandler(*args, **kwargs)

def RichTextBuffer_RemoveHandler(*args, **kwargs):
  """RichTextBuffer_RemoveHandler(String name) -> bool"""
  return _richtext.RichTextBuffer_RemoveHandler(*args, **kwargs)

def RichTextBuffer_FindHandlerByName(*args, **kwargs):
  """RichTextBuffer_FindHandlerByName(String name) -> RichTextFileHandler"""
  return _richtext.RichTextBuffer_FindHandlerByName(*args, **kwargs)

def RichTextBuffer_FindHandlerByExtension(*args, **kwargs):
  """RichTextBuffer_FindHandlerByExtension(String extension, int imageType) -> RichTextFileHandler"""
  return _richtext.RichTextBuffer_FindHandlerByExtension(*args, **kwargs)

def RichTextBuffer_FindHandlerByFilename(*args, **kwargs):
  """RichTextBuffer_FindHandlerByFilename(String filename, int imageType) -> RichTextFileHandler"""
  return _richtext.RichTextBuffer_FindHandlerByFilename(*args, **kwargs)

def RichTextBuffer_FindHandlerByType(*args, **kwargs):
  """RichTextBuffer_FindHandlerByType(int imageType) -> RichTextFileHandler"""
  return _richtext.RichTextBuffer_FindHandlerByType(*args, **kwargs)

def RichTextBuffer_GetExtWildcard(*args, **kwargs):
  """
    GetExtWildcard(self, bool combine=False, bool save=False) --> (wildcards, types)

    Gets a wildcard string for the file dialog based on all the currently
    loaded richtext file handlers, and a list that can be used to map
    those filter types to the file handler type.
    """
  return _richtext.RichTextBuffer_GetExtWildcard(*args, **kwargs)

def RichTextBuffer_CleanUpHandlers(*args):
  """RichTextBuffer_CleanUpHandlers()"""
  return _richtext.RichTextBuffer_CleanUpHandlers(*args)

def RichTextBuffer_InitStandardHandlers(*args):
  """RichTextBuffer_InitStandardHandlers()"""
  return _richtext.RichTextBuffer_InitStandardHandlers(*args)

def RichTextBuffer_GetRenderer(*args):
  """RichTextBuffer_GetRenderer() -> RichTextRenderer"""
  return _richtext.RichTextBuffer_GetRenderer(*args)

def RichTextBuffer_SetRenderer(*args, **kwargs):
  """RichTextBuffer_SetRenderer(RichTextRenderer renderer)"""
  return _richtext.RichTextBuffer_SetRenderer(*args, **kwargs)

def RichTextBuffer_GetBulletRightMargin(*args):
  """RichTextBuffer_GetBulletRightMargin() -> int"""
  return _richtext.RichTextBuffer_GetBulletRightMargin(*args)

def RichTextBuffer_SetBulletRightMargin(*args, **kwargs):
  """RichTextBuffer_SetBulletRightMargin(int margin)"""
  return _richtext.RichTextBuffer_SetBulletRightMargin(*args, **kwargs)

def RichTextBuffer_GetBulletProportion(*args):
  """RichTextBuffer_GetBulletProportion() -> float"""
  return _richtext.RichTextBuffer_GetBulletProportion(*args)

def RichTextBuffer_SetBulletProportion(*args, **kwargs):
  """RichTextBuffer_SetBulletProportion(float prop)"""
  return _richtext.RichTextBuffer_SetBulletProportion(*args, **kwargs)

#---------------------------------------------------------------------------

RICHTEXT_HANDLER_INCLUDE_STYLESHEET = _richtext.RICHTEXT_HANDLER_INCLUDE_STYLESHEET
RICHTEXT_HANDLER_SAVE_IMAGES_TO_MEMORY = _richtext.RICHTEXT_HANDLER_SAVE_IMAGES_TO_MEMORY
RICHTEXT_HANDLER_SAVE_IMAGES_TO_FILES = _richtext.RICHTEXT_HANDLER_SAVE_IMAGES_TO_FILES
RICHTEXT_HANDLER_SAVE_IMAGES_TO_BASE64 = _richtext.RICHTEXT_HANDLER_SAVE_IMAGES_TO_BASE64
RICHTEXT_HANDLER_NO_HEADER_FOOTER = _richtext.RICHTEXT_HANDLER_NO_HEADER_FOOTER
RICHTEXT_HANDLER_CONVERT_FACENAMES = _richtext.RICHTEXT_HANDLER_CONVERT_FACENAMES
class RichTextFileHandler(_core.Object):
    """Base class for file handlers"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextFileHandler
    __del__ = lambda self : None;
    def LoadStream(*args, **kwargs):
        """LoadStream(self, RichTextBuffer buffer, InputStream stream) -> bool"""
        return _richtext.RichTextFileHandler_LoadStream(*args, **kwargs)

    def SaveStream(*args, **kwargs):
        """SaveStream(self, RichTextBuffer buffer, wxOutputStream stream) -> bool"""
        return _richtext.RichTextFileHandler_SaveStream(*args, **kwargs)

    def LoadFile(*args, **kwargs):
        """LoadFile(self, RichTextBuffer buffer, String filename) -> bool"""
        return _richtext.RichTextFileHandler_LoadFile(*args, **kwargs)

    def SaveFile(*args, **kwargs):
        """SaveFile(self, RichTextBuffer buffer, String filename) -> bool"""
        return _richtext.RichTextFileHandler_SaveFile(*args, **kwargs)

    def CanHandle(*args, **kwargs):
        """CanHandle(self, String filename) -> bool"""
        return _richtext.RichTextFileHandler_CanHandle(*args, **kwargs)

    def CanSave(*args, **kwargs):
        """CanSave(self) -> bool"""
        return _richtext.RichTextFileHandler_CanSave(*args, **kwargs)

    def CanLoad(*args, **kwargs):
        """CanLoad(self) -> bool"""
        return _richtext.RichTextFileHandler_CanLoad(*args, **kwargs)

    def IsVisible(*args, **kwargs):
        """IsVisible(self) -> bool"""
        return _richtext.RichTextFileHandler_IsVisible(*args, **kwargs)

    def SetVisible(*args, **kwargs):
        """SetVisible(self, bool visible)"""
        return _richtext.RichTextFileHandler_SetVisible(*args, **kwargs)

    def SetName(*args, **kwargs):
        """SetName(self, String name)"""
        return _richtext.RichTextFileHandler_SetName(*args, **kwargs)

    def GetName(*args, **kwargs):
        """GetName(self) -> String"""
        return _richtext.RichTextFileHandler_GetName(*args, **kwargs)

    Name = property(GetName,SetName) 
    def SetExtension(*args, **kwargs):
        """SetExtension(self, String ext)"""
        return _richtext.RichTextFileHandler_SetExtension(*args, **kwargs)

    def GetExtension(*args, **kwargs):
        """GetExtension(self) -> String"""
        return _richtext.RichTextFileHandler_GetExtension(*args, **kwargs)

    Extension = property(GetExtension,SetExtension) 
    def SetType(*args, **kwargs):
        """SetType(self, int type)"""
        return _richtext.RichTextFileHandler_SetType(*args, **kwargs)

    def GetType(*args, **kwargs):
        """GetType(self) -> int"""
        return _richtext.RichTextFileHandler_GetType(*args, **kwargs)

    Type = property(GetType,SetType) 
    def SetFlags(*args, **kwargs):
        """SetFlags(self, int flags)"""
        return _richtext.RichTextFileHandler_SetFlags(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """GetFlags(self) -> int"""
        return _richtext.RichTextFileHandler_GetFlags(*args, **kwargs)

    Flags = property(GetFlags,SetFlags) 
    def SetEncoding(*args, **kwargs):
        """SetEncoding(self, String encoding)"""
        return _richtext.RichTextFileHandler_SetEncoding(*args, **kwargs)

    def GetEncoding(*args, **kwargs):
        """GetEncoding(self) -> String"""
        return _richtext.RichTextFileHandler_GetEncoding(*args, **kwargs)

    Encoding = property(GetEncoding,SetEncoding) 
_richtext.RichTextFileHandler_swigregister(RichTextFileHandler)

class RichTextPlainTextHandler(RichTextFileHandler):
    """Proxy of C++ RichTextPlainTextHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String name=TextName, String ext=TextExt, int type=RICHTEXT_TYPE_TEXT) -> RichTextPlainTextHandler"""
        _richtext.RichTextPlainTextHandler_swiginit(self,_richtext.new_RichTextPlainTextHandler(*args, **kwargs))
_richtext.RichTextPlainTextHandler_swigregister(RichTextPlainTextHandler)
TextName = cvar.TextName
TextExt = cvar.TextExt

#---------------------------------------------------------------------------

class RichTextRenderer(_core.Object):
    """Proxy of C++ RichTextRenderer class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _richtext.delete_RichTextRenderer
    __del__ = lambda self : None;
    def DrawStandardBullet(*args, **kwargs):
        """
        DrawStandardBullet(self, RichTextParagraph paragraph, DC dc, RichTextAttr attr, 
            Rect rect) -> bool
        """
        return _richtext.RichTextRenderer_DrawStandardBullet(*args, **kwargs)

    def DrawTextBullet(*args, **kwargs):
        """
        DrawTextBullet(self, RichTextParagraph paragraph, DC dc, RichTextAttr attr, 
            Rect rect, String text) -> bool
        """
        return _richtext.RichTextRenderer_DrawTextBullet(*args, **kwargs)

    def DrawBitmapBullet(*args, **kwargs):
        """
        DrawBitmapBullet(self, RichTextParagraph paragraph, DC dc, RichTextAttr attr, 
            Rect rect) -> bool
        """
        return _richtext.RichTextRenderer_DrawBitmapBullet(*args, **kwargs)

    def EnumerateStandardBulletNames(*args, **kwargs):
        """EnumerateStandardBulletNames(self, wxArrayString bulletNames) -> bool"""
        return _richtext.RichTextRenderer_EnumerateStandardBulletNames(*args, **kwargs)

_richtext.RichTextRenderer_swigregister(RichTextRenderer)

class RichTextStdRenderer(RichTextRenderer):
    """Proxy of C++ RichTextStdRenderer class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> RichTextStdRenderer"""
        _richtext.RichTextStdRenderer_swiginit(self,_richtext.new_RichTextStdRenderer(*args, **kwargs))
_richtext.RichTextStdRenderer_swigregister(RichTextStdRenderer)

#---------------------------------------------------------------------------

RE_READONLY = _richtext.RE_READONLY
RE_MULTILINE = _richtext.RE_MULTILINE
RE_CENTER_CARET = _richtext.RE_CENTER_CARET
RE_CENTRE_CARET = _richtext.RE_CENTRE_CARET
RICHTEXT_SHIFT_DOWN = _richtext.RICHTEXT_SHIFT_DOWN
RICHTEXT_CTRL_DOWN = _richtext.RICHTEXT_CTRL_DOWN
RICHTEXT_ALT_DOWN = _richtext.RICHTEXT_ALT_DOWN
class RichTextCtrl(_core.Control,_core.TextCtrlIface,_windows.ScrollHelper):
    """Proxy of C++ RichTextCtrl class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=-1, String value=EmptyString, 
            Point pos=DefaultPosition, Size size=DefaultSize, 
            long style=RE_MULTILINE, Validator validator=DefaultValidator, 
            String name=RichTextCtrlNameStr) -> RichTextCtrl
        """
        _richtext.RichTextCtrl_swiginit(self,_richtext.new_RichTextCtrl(*args, **kwargs))
        self._setOORInfo(self)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=-1, String value=EmptyString, 
            Point pos=DefaultPosition, Size size=DefaultSize, 
            long style=RE_MULTILINE, Validator validator=DefaultValidator, 
            String name=RichTextCtrlNameStr) -> bool
        """
        return _richtext.RichTextCtrl_Create(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> String"""
        return _richtext.RichTextCtrl_GetValue(*args, **kwargs)

    def IsSingleLine(*args, **kwargs):
        """IsSingleLine(self) -> bool"""
        return _richtext.RichTextCtrl_IsSingleLine(*args, **kwargs)

    def IsMultiLine(*args, **kwargs):
        """IsMultiLine(self) -> bool"""
        return _richtext.RichTextCtrl_IsMultiLine(*args, **kwargs)

    def GetFilename(*args, **kwargs):
        """GetFilename(self) -> String"""
        return _richtext.RichTextCtrl_GetFilename(*args, **kwargs)

    def SetFilename(*args, **kwargs):
        """SetFilename(self, String filename)"""
        return _richtext.RichTextCtrl_SetFilename(*args, **kwargs)

    def SetDelayedLayoutThreshold(*args, **kwargs):
        """
        SetDelayedLayoutThreshold(self, long threshold)

        Set the threshold in character positions for doing layout optimization
        during sizing.
        """
        return _richtext.RichTextCtrl_SetDelayedLayoutThreshold(*args, **kwargs)

    def GetDelayedLayoutThreshold(*args, **kwargs):
        """
        GetDelayedLayoutThreshold(self) -> long

        Get the threshold in character positions for doing layout optimization
        during sizing.
        """
        return _richtext.RichTextCtrl_GetDelayedLayoutThreshold(*args, **kwargs)

    def GetFullLayoutRequired(*args, **kwargs):
        """GetFullLayoutRequired(self) -> bool"""
        return _richtext.RichTextCtrl_GetFullLayoutRequired(*args, **kwargs)

    def SetFullLayoutRequired(*args, **kwargs):
        """SetFullLayoutRequired(self, bool b)"""
        return _richtext.RichTextCtrl_SetFullLayoutRequired(*args, **kwargs)

    def GetFullLayoutTime(*args, **kwargs):
        """GetFullLayoutTime(self) -> wxLongLong"""
        return _richtext.RichTextCtrl_GetFullLayoutTime(*args, **kwargs)

    def SetFullLayoutTime(*args, **kwargs):
        """SetFullLayoutTime(self, wxLongLong t)"""
        return _richtext.RichTextCtrl_SetFullLayoutTime(*args, **kwargs)

    def GetFullLayoutSavedPosition(*args, **kwargs):
        """GetFullLayoutSavedPosition(self) -> long"""
        return _richtext.RichTextCtrl_GetFullLayoutSavedPosition(*args, **kwargs)

    def SetFullLayoutSavedPosition(*args, **kwargs):
        """SetFullLayoutSavedPosition(self, long p)"""
        return _richtext.RichTextCtrl_SetFullLayoutSavedPosition(*args, **kwargs)

    def ForceDelayedLayout(*args, **kwargs):
        """ForceDelayedLayout(self)"""
        return _richtext.RichTextCtrl_ForceDelayedLayout(*args, **kwargs)

    def SetTextCursor(*args, **kwargs):
        """
        SetTextCursor(self, Cursor cursor)

        Set text cursor
        """
        return _richtext.RichTextCtrl_SetTextCursor(*args, **kwargs)

    def GetTextCursor(*args, **kwargs):
        """
        GetTextCursor(self) -> Cursor

        Get text cursor
        """
        return _richtext.RichTextCtrl_GetTextCursor(*args, **kwargs)

    def SetURLCursor(*args, **kwargs):
        """
        SetURLCursor(self, Cursor cursor)

        Set URL cursor
        """
        return _richtext.RichTextCtrl_SetURLCursor(*args, **kwargs)

    def GetURLCursor(*args, **kwargs):
        """
        GetURLCursor(self) -> Cursor

        Get URL cursor
        """
        return _richtext.RichTextCtrl_GetURLCursor(*args, **kwargs)

    def GetCaretAtLineStart(*args, **kwargs):
        """GetCaretAtLineStart(self) -> bool"""
        return _richtext.RichTextCtrl_GetCaretAtLineStart(*args, **kwargs)

    def SetCaretAtLineStart(*args, **kwargs):
        """SetCaretAtLineStart(self, bool atStart)"""
        return _richtext.RichTextCtrl_SetCaretAtLineStart(*args, **kwargs)

    def GetDragging(*args, **kwargs):
        """GetDragging(self) -> bool"""
        return _richtext.RichTextCtrl_GetDragging(*args, **kwargs)

    def SetDragging(*args, **kwargs):
        """SetDragging(self, bool dragging)"""
        return _richtext.RichTextCtrl_SetDragging(*args, **kwargs)

    def GetPreDrag(*args, **kwargs):
        """GetPreDrag(self) -> bool"""
        return _richtext.RichTextCtrl_GetPreDrag(*args, **kwargs)

    def SetPreDrag(*args, **kwargs):
        """SetPreDrag(self, bool pd)"""
        return _richtext.RichTextCtrl_SetPreDrag(*args, **kwargs)

    def GetDragStartPoint(*args, **kwargs):
        """GetDragStartPoint(self) -> Point"""
        return _richtext.RichTextCtrl_GetDragStartPoint(*args, **kwargs)

    def SetDragStartPoint(*args, **kwargs):
        """SetDragStartPoint(self, Point sp)"""
        return _richtext.RichTextCtrl_SetDragStartPoint(*args, **kwargs)

    def GetDragStartTime(*args, **kwargs):
        """GetDragStartTime(self) -> DateTime"""
        return _richtext.RichTextCtrl_GetDragStartTime(*args, **kwargs)

    def SetDragStartTime(*args, **kwargs):
        """SetDragStartTime(self, DateTime st)"""
        return _richtext.RichTextCtrl_SetDragStartTime(*args, **kwargs)

    def GetBufferBitmap(*args, **kwargs):
        """GetBufferBitmap(self) -> Bitmap"""
        return _richtext.RichTextCtrl_GetBufferBitmap(*args, **kwargs)

    def GetContextMenu(*args, **kwargs):
        """GetContextMenu(self) -> Menu"""
        return _richtext.RichTextCtrl_GetContextMenu(*args, **kwargs)

    def SetContextMenu(*args, **kwargs):
        """SetContextMenu(self, Menu menu)"""
        return _richtext.RichTextCtrl_SetContextMenu(*args, **kwargs)

    def GetSelectionAnchor(*args, **kwargs):
        """GetSelectionAnchor(self) -> long"""
        return _richtext.RichTextCtrl_GetSelectionAnchor(*args, **kwargs)

    def SetSelectionAnchor(*args, **kwargs):
        """SetSelectionAnchor(self, long anchor)"""
        return _richtext.RichTextCtrl_SetSelectionAnchor(*args, **kwargs)

    def LoadFile(*args, **kwargs):
        """
        LoadFile(self, String file, int type=RICHTEXT_TYPE_ANY) -> bool

        Load the contents of the document from the given filename.
        """
        return _richtext.RichTextCtrl_LoadFile(*args, **kwargs)

    def SaveFile(*args, **kwargs):
        """
        SaveFile(self, String file=EmptyString, int type=RICHTEXT_TYPE_ANY) -> bool

        Save the contents of the document to the given filename, or if the
        empty string is passed then to the filename set with `SetFilename`.
        """
        return _richtext.RichTextCtrl_SaveFile(*args, **kwargs)

    def SetHandlerFlags(*args, **kwargs):
        """
        SetHandlerFlags(self, int flags)

        Set the handler flags, controlling loading and saving.
        """
        return _richtext.RichTextCtrl_SetHandlerFlags(*args, **kwargs)

    def GetHandlerFlags(*args, **kwargs):
        """
        GetHandlerFlags(self) -> int

        Get the handler flags, controlling loading and saving.
        """
        return _richtext.RichTextCtrl_GetHandlerFlags(*args, **kwargs)

    def SetMaxLength(*args, **kwargs):
        """
        SetMaxLength(self, unsigned long len)

        Set the max number of characters which may be entered in a single line
        text control.
        """
        return _richtext.RichTextCtrl_SetMaxLength(*args, **kwargs)

    def SetStyle(*args, **kwargs):
        """
        SetStyle(self, RichTextRange range, RichTextAttr style) -> bool

        Set the style for the text in ``range`` to ``style``
        """
        return _richtext.RichTextCtrl_SetStyle(*args, **kwargs)

    def GetStyle(*args, **kwargs):
        """
        GetStyle(self, long position, RichTextAttr style) -> bool

        Retrieve the style used at the given position.  Copies the style
        values at ``position`` into the ``style`` parameter and returns ``True``
        if successful.  Returns ``False`` otherwise.
        """
        return _richtext.RichTextCtrl_GetStyle(*args, **kwargs)

    def GetStyleForRange(*args, **kwargs):
        """
        GetStyleForRange(self, RichTextRange range, RichTextAttr style) -> bool

        Get the common set of styles for the range
        """
        return _richtext.RichTextCtrl_GetStyleForRange(*args, **kwargs)

    def SetStyleEx(*args, **kwargs):
        """
        SetStyleEx(self, RichTextRange range, RichTextAttr style, int flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool

        Extended style setting operation with flags including:
        RICHTEXT_SETSTYLE_WITH_UNDO, RICHTEXT_SETSTYLE_OPTIMIZE,
        RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY, RICHTEXT_SETSTYLE_CHARACTERS_ONLY
        """
        return _richtext.RichTextCtrl_SetStyleEx(*args, **kwargs)

    def GetUncombinedStyle(*args, **kwargs):
        """
        GetUncombinedStyle(self, long position, RichTextAttr style) -> bool

        Get the content (uncombined) attributes for this position.  Copies the
        style values at ``position`` into the ``style`` parameter and returns
        ``True`` if successful.  Returns ``False`` otherwise.
        """
        return _richtext.RichTextCtrl_GetUncombinedStyle(*args, **kwargs)

    def SetDefaultStyle(*args, **kwargs):
        """
        SetDefaultStyle(self, RichTextAttr style) -> bool

        Set the style used by default for the rich text document.
        """
        return _richtext.RichTextCtrl_SetDefaultStyle(*args, **kwargs)

    def GetDefaultStyle(*args, **kwargs):
        """
        GetDefaultStyle(self) -> RichTextAttr

        Retrieves a copy of the default style object.
        """
        return _richtext.RichTextCtrl_GetDefaultStyle(*args, **kwargs)

    def SetListStyle(*args, **kwargs):
        """
        SetListStyle(self, RichTextRange range, String defName, int flags=RICHTEXT_SETSTYLE_WITH_UNDO, 
            int startFrom=1, int specifiedLevel=-1) -> bool
        """
        return _richtext.RichTextCtrl_SetListStyle(*args, **kwargs)

    def ClearListStyle(*args, **kwargs):
        """ClearListStyle(self, RichTextRange range, int flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool"""
        return _richtext.RichTextCtrl_ClearListStyle(*args, **kwargs)

    def NumberList(*args, **kwargs):
        """
        NumberList(self, RichTextRange range, String defName, int flags=RICHTEXT_SETSTYLE_WITH_UNDO, 
            int startFrom=1, int specifiedLevel=-1) -> bool
        """
        return _richtext.RichTextCtrl_NumberList(*args, **kwargs)

    def PromoteList(*args, **kwargs):
        """
        PromoteList(self, int promoteBy, RichTextRange range, String defName, 
            int flags=RICHTEXT_SETSTYLE_WITH_UNDO, int specifiedLevel=-1) -> bool
        """
        return _richtext.RichTextCtrl_PromoteList(*args, **kwargs)

    def Delete(*args, **kwargs):
        """Delete(self, RichTextRange range) -> bool"""
        return _richtext.RichTextCtrl_Delete(*args, **kwargs)

    def HitTestXY(*args, **kwargs):
        """
        HitTestRC(self, Point pt) --> (result, col, row)

        Returns the column and row of the given point in pixels.  Note that
        ``pt`` should be given in device coordinates, and not be adjusted for
        the client area origin nor for scrolling.  The return value is a tuple
        of the hit test result and the column and row values.
        """
        return _richtext.RichTextCtrl_HitTestXY(*args, **kwargs)

    def FindContainerAtPoint(*args, **kwargs):
        """
        FindContainerAtPoint(self, Point pt, long position, int hit, RichTextObject hitObj, 
            int flags=0) -> RichTextParagraphLayoutBox
        """
        return _richtext.RichTextCtrl_FindContainerAtPoint(*args, **kwargs)

    def DeleteSelection(*args, **kwargs):
        """
        DeleteSelection(self)

        Remove the current selection.
        """
        return _richtext.RichTextCtrl_DeleteSelection(*args, **kwargs)

    def CanDeleteSelection(*args, **kwargs):
        """
        CanDeleteSelection(self) -> bool

        Returns ``True`` if the selection can be removed from the document.
        """
        return _richtext.RichTextCtrl_CanDeleteSelection(*args, **kwargs)

    def HasSelection(*args, **kwargs):
        """HasSelection(self) -> bool"""
        return _richtext.RichTextCtrl_HasSelection(*args, **kwargs)

    def WriteImage(*args, **kwargs):
        """
        WriteImage(self, Image image, int bitmapType=BITMAP_TYPE_PNG) -> bool

        Write an image at the current insertion point. Supply optional type to
        use for internal and file storage of the raw data.

        """
        return _richtext.RichTextCtrl_WriteImage(*args, **kwargs)

    def WriteBitmap(*args, **kwargs):
        """
        WriteBitmap(self, Bitmap bitmap, int bitmapType=BITMAP_TYPE_PNG) -> bool

        Write a bitmap at the current insertion point. Supply optional type to
        use for internal and file storage of the raw data.
        """
        return _richtext.RichTextCtrl_WriteBitmap(*args, **kwargs)

    def WriteImageFile(*args, **kwargs):
        """
        WriteImageFile(self, String filename, int bitmapType) -> bool

        Load an image from file and write at the current insertion point.
        """
        return _richtext.RichTextCtrl_WriteImageFile(*args, **kwargs)

    def WriteImageBlock(*args, **kwargs):
        """
        WriteImageBlock(self, wxRichTextImageBlock imageBlock) -> bool

        Write an image block at the current insertion point.
        """
        return _richtext.RichTextCtrl_WriteImageBlock(*args, **kwargs)

    def Newline(*args, **kwargs):
        """
        Newline(self) -> bool

        Insert a newline (actually paragraph) at the current insertion point.
        """
        return _richtext.RichTextCtrl_Newline(*args, **kwargs)

    def LineBreak(*args, **kwargs):
        """
        LineBreak(self) -> bool

        Insert a line break at the current insertion point.
        """
        return _richtext.RichTextCtrl_LineBreak(*args, **kwargs)

    def SetBasicStyle(*args, **kwargs):
        """SetBasicStyle(self, RichTextAttr style)"""
        return _richtext.RichTextCtrl_SetBasicStyle(*args, **kwargs)

    def GetBasicStyle(*args, **kwargs):
        """
        GetBasicStyle(self) -> RichTextAttr

        Get basic (overall) style
        """
        return _richtext.RichTextCtrl_GetBasicStyle(*args, **kwargs)

    def BeginStyle(*args, **kwargs):
        """
        BeginStyle(self, RichTextAttr style) -> bool

        Begin using a style
        """
        return _richtext.RichTextCtrl_BeginStyle(*args, **kwargs)

    def EndStyle(*args, **kwargs):
        """
        EndStyle(self) -> bool

        End the style
        """
        return _richtext.RichTextCtrl_EndStyle(*args, **kwargs)

    def EndAllStyles(*args, **kwargs):
        """
        EndAllStyles(self) -> bool

        End all styles
        """
        return _richtext.RichTextCtrl_EndAllStyles(*args, **kwargs)

    def BeginBold(*args, **kwargs):
        """
        BeginBold(self) -> bool

        Begin using bold
        """
        return _richtext.RichTextCtrl_BeginBold(*args, **kwargs)

    def EndBold(*args, **kwargs):
        """
        EndBold(self) -> bool

        End using bold
        """
        return _richtext.RichTextCtrl_EndBold(*args, **kwargs)

    def BeginItalic(*args, **kwargs):
        """
        BeginItalic(self) -> bool

        Begin using italic
        """
        return _richtext.RichTextCtrl_BeginItalic(*args, **kwargs)

    def EndItalic(*args, **kwargs):
        """
        EndItalic(self) -> bool

        End using italic
        """
        return _richtext.RichTextCtrl_EndItalic(*args, **kwargs)

    def BeginUnderline(*args, **kwargs):
        """
        BeginUnderline(self) -> bool

        Begin using underline
        """
        return _richtext.RichTextCtrl_BeginUnderline(*args, **kwargs)

    def EndUnderline(*args, **kwargs):
        """
        EndUnderline(self) -> bool

        End using underline
        """
        return _richtext.RichTextCtrl_EndUnderline(*args, **kwargs)

    def BeginFontSize(*args, **kwargs):
        """
        BeginFontSize(self, int pointSize) -> bool

        Begin using point size
        """
        return _richtext.RichTextCtrl_BeginFontSize(*args, **kwargs)

    def EndFontSize(*args, **kwargs):
        """
        EndFontSize(self) -> bool

        End using point size
        """
        return _richtext.RichTextCtrl_EndFontSize(*args, **kwargs)

    def BeginFont(*args, **kwargs):
        """
        BeginFont(self, Font font) -> bool

        Begin using this font
        """
        return _richtext.RichTextCtrl_BeginFont(*args, **kwargs)

    def EndFont(*args, **kwargs):
        """
        EndFont(self) -> bool

        End using a font
        """
        return _richtext.RichTextCtrl_EndFont(*args, **kwargs)

    def BeginTextColour(*args, **kwargs):
        """
        BeginTextColour(self, Colour colour) -> bool

        Begin using this colour
        """
        return _richtext.RichTextCtrl_BeginTextColour(*args, **kwargs)

    def EndTextColour(*args, **kwargs):
        """
        EndTextColour(self) -> bool

        End using a colour
        """
        return _richtext.RichTextCtrl_EndTextColour(*args, **kwargs)

    def BeginAlignment(*args, **kwargs):
        """
        BeginAlignment(self, int alignment) -> bool

        Begin using alignment
        """
        return _richtext.RichTextCtrl_BeginAlignment(*args, **kwargs)

    def EndAlignment(*args, **kwargs):
        """
        EndAlignment(self) -> bool

        End alignment
        """
        return _richtext.RichTextCtrl_EndAlignment(*args, **kwargs)

    def BeginLeftIndent(*args, **kwargs):
        """
        BeginLeftIndent(self, int leftIndent, int leftSubIndent=0) -> bool

        Begin left indent
        """
        return _richtext.RichTextCtrl_BeginLeftIndent(*args, **kwargs)

    def EndLeftIndent(*args, **kwargs):
        """
        EndLeftIndent(self) -> bool

        End left indent
        """
        return _richtext.RichTextCtrl_EndLeftIndent(*args, **kwargs)

    def BeginRightIndent(*args, **kwargs):
        """
        BeginRightIndent(self, int rightIndent) -> bool

        Begin right indent
        """
        return _richtext.RichTextCtrl_BeginRightIndent(*args, **kwargs)

    def EndRightIndent(*args, **kwargs):
        """
        EndRightIndent(self) -> bool

        End right indent
        """
        return _richtext.RichTextCtrl_EndRightIndent(*args, **kwargs)

    def BeginParagraphSpacing(*args, **kwargs):
        """
        BeginParagraphSpacing(self, int before, int after) -> bool

        Begin paragraph spacing
        """
        return _richtext.RichTextCtrl_BeginParagraphSpacing(*args, **kwargs)

    def EndParagraphSpacing(*args, **kwargs):
        """
        EndParagraphSpacing(self) -> bool

        End paragraph spacing
        """
        return _richtext.RichTextCtrl_EndParagraphSpacing(*args, **kwargs)

    def BeginLineSpacing(*args, **kwargs):
        """
        BeginLineSpacing(self, int lineSpacing) -> bool

        Begin line spacing
        """
        return _richtext.RichTextCtrl_BeginLineSpacing(*args, **kwargs)

    def EndLineSpacing(*args, **kwargs):
        """
        EndLineSpacing(self) -> bool

        End line spacing
        """
        return _richtext.RichTextCtrl_EndLineSpacing(*args, **kwargs)

    def BeginNumberedBullet(*args, **kwargs):
        """
        BeginNumberedBullet(self, int bulletNumber, int leftIndent, int leftSubIndent, 
            int bulletStyle=wxTEXT_ATTR_BULLET_STYLE_ARABIC|wxTEXT_ATTR_BULLET_STYLE_PERIOD) -> bool

        Begin numbered bullet
        """
        return _richtext.RichTextCtrl_BeginNumberedBullet(*args, **kwargs)

    def EndNumberedBullet(*args, **kwargs):
        """
        EndNumberedBullet(self) -> bool

        End numbered bullet
        """
        return _richtext.RichTextCtrl_EndNumberedBullet(*args, **kwargs)

    def BeginSymbolBullet(*args, **kwargs):
        """
        BeginSymbolBullet(self, String symbol, int leftIndent, int leftSubIndent, int bulletStyle=TEXT_ATTR_BULLET_STYLE_SYMBOL) -> bool

        Begin symbol bullet
        """
        return _richtext.RichTextCtrl_BeginSymbolBullet(*args, **kwargs)

    def EndSymbolBullet(*args, **kwargs):
        """
        EndSymbolBullet(self) -> bool

        End symbol bullet
        """
        return _richtext.RichTextCtrl_EndSymbolBullet(*args, **kwargs)

    def BeginStandardBullet(*args, **kwargs):
        """
        BeginStandardBullet(self, String bulletName, int leftIndent, int leftSubIndent, 
            int bulletStyle=TEXT_ATTR_BULLET_STYLE_STANDARD) -> bool

        Begin standard bullet
        """
        return _richtext.RichTextCtrl_BeginStandardBullet(*args, **kwargs)

    def EndStandardBullet(*args, **kwargs):
        """
        EndStandardBullet(self) -> bool

        End standard bullet
        """
        return _richtext.RichTextCtrl_EndStandardBullet(*args, **kwargs)

    def BeginCharacterStyle(*args, **kwargs):
        """
        BeginCharacterStyle(self, String characterStyle) -> bool

        Begin named character style
        """
        return _richtext.RichTextCtrl_BeginCharacterStyle(*args, **kwargs)

    def EndCharacterStyle(*args, **kwargs):
        """
        EndCharacterStyle(self) -> bool

        End named character style
        """
        return _richtext.RichTextCtrl_EndCharacterStyle(*args, **kwargs)

    def BeginParagraphStyle(*args, **kwargs):
        """
        BeginParagraphStyle(self, String paragraphStyle) -> bool

        Begin named paragraph style
        """
        return _richtext.RichTextCtrl_BeginParagraphStyle(*args, **kwargs)

    def EndParagraphStyle(*args, **kwargs):
        """
        EndParagraphStyle(self) -> bool

        End named character style
        """
        return _richtext.RichTextCtrl_EndParagraphStyle(*args, **kwargs)

    def BeginListStyle(*args, **kwargs):
        """
        BeginListStyle(self, String listStyle, int level=1, int number=1) -> bool

        Begin named list style.
        """
        return _richtext.RichTextCtrl_BeginListStyle(*args, **kwargs)

    def EndListStyle(*args, **kwargs):
        """
        EndListStyle(self) -> bool

        End named list style.
        """
        return _richtext.RichTextCtrl_EndListStyle(*args, **kwargs)

    def BeginURL(*args, **kwargs):
        """
        BeginURL(self, String url, String characterStyle=wxEmptyString) -> bool

        Begin URL.
        """
        return _richtext.RichTextCtrl_BeginURL(*args, **kwargs)

    def EndURL(*args, **kwargs):
        """
        EndURL(self) -> bool

        End URL.
        """
        return _richtext.RichTextCtrl_EndURL(*args, **kwargs)

    def SetDefaultStyleToCursorStyle(*args, **kwargs):
        """
        SetDefaultStyleToCursorStyle(self) -> bool

        Sets the default style to the style under the cursor
        """
        return _richtext.RichTextCtrl_SetDefaultStyleToCursorStyle(*args, **kwargs)

    def SelectNone(*args, **kwargs):
        """
        SelectNone(self)

        Clear the selection
        """
        return _richtext.RichTextCtrl_SelectNone(*args, **kwargs)

    def SelectWord(*args, **kwargs):
        """
        SelectWord(self, long position) -> bool

        Select the word at the given character position
        """
        return _richtext.RichTextCtrl_SelectWord(*args, **kwargs)

    def GetSelectionRange(*args, **kwargs):
        """
        GetSelectionRange(self) -> RichTextRange

        Get the selection range in character positions.
        """
        return _richtext.RichTextCtrl_GetSelectionRange(*args, **kwargs)

    def SetSelectionRange(*args, **kwargs):
        """
        SetSelectionRange(self, RichTextRange range)

        Set the selection range in character positions. The end point of range
        is specified as the last character position of the span of text, plus
        one. So, for example, to set the selection for a character at position
        5, use the range (5,6).
        """
        return _richtext.RichTextCtrl_SetSelectionRange(*args, **kwargs)

    def GetInternalSelectionRange(*args, **kwargs):
        """
        GetInternalSelectionRange(self) -> RichTextRange

        Get the selection range in character positions. The range is in
        internal format, i.e. a single character selection is denoted by (n,n).

        """
        return _richtext.RichTextCtrl_GetInternalSelectionRange(*args, **kwargs)

    def SetInternalSelectionRange(*args, **kwargs):
        """
        SetInternalSelectionRange(self, RichTextRange range)

        Set the selection range in character positions. The range is in
        internal format, i.e. a single character selection is denoted by (n,n).
        """
        return _richtext.RichTextCtrl_SetInternalSelectionRange(*args, **kwargs)

    def AddParagraph(*args, **kwargs):
        """
        AddParagraph(self, String text) -> RichTextRange

        Add a new paragraph of text to the end of the buffer
        """
        return _richtext.RichTextCtrl_AddParagraph(*args, **kwargs)

    def AddImage(*args, **kwargs):
        """
        AddImage(self, Image image) -> RichTextRange

        Add an image
        """
        return _richtext.RichTextCtrl_AddImage(*args, **kwargs)

    def LayoutContent(*args, **kwargs):
        """
        LayoutContent(self, bool onlyVisibleRect=False) -> bool

        Layout the buffer: which we must do before certain operations, such as
        setting the caret position.
        """
        return _richtext.RichTextCtrl_LayoutContent(*args, **kwargs)

    def MoveCaret(*args, **kwargs):
        """
        MoveCaret(self, long pos, bool showAtLineStart=False) -> bool

        Move the caret to the given character position
        """
        return _richtext.RichTextCtrl_MoveCaret(*args, **kwargs)

    def MoveRight(*args, **kwargs):
        """
        MoveRight(self, int noPositions=1, int flags=0) -> bool

        Move right
        """
        return _richtext.RichTextCtrl_MoveRight(*args, **kwargs)

    def MoveLeft(*args, **kwargs):
        """
        MoveLeft(self, int noPositions=1, int flags=0) -> bool

        Move left
        """
        return _richtext.RichTextCtrl_MoveLeft(*args, **kwargs)

    def MoveUp(*args, **kwargs):
        """
        MoveUp(self, int noLines=1, int flags=0) -> bool

        Move up
        """
        return _richtext.RichTextCtrl_MoveUp(*args, **kwargs)

    def MoveDown(*args, **kwargs):
        """
        MoveDown(self, int noLines=1, int flags=0) -> bool

        Move down
        """
        return _richtext.RichTextCtrl_MoveDown(*args, **kwargs)

    def MoveToLineEnd(*args, **kwargs):
        """
        MoveToLineEnd(self, int flags=0) -> bool

        Move to the end of the line
        """
        return _richtext.RichTextCtrl_MoveToLineEnd(*args, **kwargs)

    def MoveToLineStart(*args, **kwargs):
        """
        MoveToLineStart(self, int flags=0) -> bool

        Move to the start of the line
        """
        return _richtext.RichTextCtrl_MoveToLineStart(*args, **kwargs)

    def MoveToParagraphEnd(*args, **kwargs):
        """
        MoveToParagraphEnd(self, int flags=0) -> bool

        Move to the end of the paragraph
        """
        return _richtext.RichTextCtrl_MoveToParagraphEnd(*args, **kwargs)

    def MoveToParagraphStart(*args, **kwargs):
        """
        MoveToParagraphStart(self, int flags=0) -> bool

        Move to the start of the paragraph
        """
        return _richtext.RichTextCtrl_MoveToParagraphStart(*args, **kwargs)

    def MoveHome(*args, **kwargs):
        """
        MoveHome(self, int flags=0) -> bool

        Move to the start of the buffer
        """
        return _richtext.RichTextCtrl_MoveHome(*args, **kwargs)

    def MoveEnd(*args, **kwargs):
        """
        MoveEnd(self, int flags=0) -> bool

        Move to the end of the buffer
        """
        return _richtext.RichTextCtrl_MoveEnd(*args, **kwargs)

    def PageUp(*args, **kwargs):
        """
        PageUp(self, int noPages=1, int flags=0) -> bool

        Move n pages up
        """
        return _richtext.RichTextCtrl_PageUp(*args, **kwargs)

    def PageDown(*args, **kwargs):
        """
        PageDown(self, int noPages=1, int flags=0) -> bool

        Move n pages down
        """
        return _richtext.RichTextCtrl_PageDown(*args, **kwargs)

    def WordLeft(*args, **kwargs):
        """
        WordLeft(self, int noPages=1, int flags=0) -> bool

        Move n words left
        """
        return _richtext.RichTextCtrl_WordLeft(*args, **kwargs)

    def WordRight(*args, **kwargs):
        """
        WordRight(self, int noPages=1, int flags=0) -> bool

        Move n words right
        """
        return _richtext.RichTextCtrl_WordRight(*args, **kwargs)

    def GetBuffer(*args, **kwargs):
        """
        GetBuffer(self) -> RichTextBuffer

        Returns the buffer associated with the control.

        """
        return _richtext.RichTextCtrl_GetBuffer(*args, **kwargs)

    def BeginBatchUndo(*args, **kwargs):
        """
        BeginBatchUndo(self, String cmdName) -> bool

        Start batching undo history for commands
        """
        return _richtext.RichTextCtrl_BeginBatchUndo(*args, **kwargs)

    def EndBatchUndo(*args, **kwargs):
        """
        EndBatchUndo(self) -> bool

        End batching undo history for commands.
        """
        return _richtext.RichTextCtrl_EndBatchUndo(*args, **kwargs)

    def BatchingUndo(*args, **kwargs):
        """
        BatchingUndo(self) -> bool

        Are we batching undo history for commands?
        """
        return _richtext.RichTextCtrl_BatchingUndo(*args, **kwargs)

    def BeginSuppressUndo(*args, **kwargs):
        """
        BeginSuppressUndo(self) -> bool

        Start suppressing undo history for commands.
        """
        return _richtext.RichTextCtrl_BeginSuppressUndo(*args, **kwargs)

    def EndSuppressUndo(*args, **kwargs):
        """
        EndSuppressUndo(self) -> bool

        End suppressing undo history for commands.
        """
        return _richtext.RichTextCtrl_EndSuppressUndo(*args, **kwargs)

    def SuppressingUndo(*args, **kwargs):
        """
        SuppressingUndo(self) -> bool

        Are we suppressing undo history for commands?
        """
        return _richtext.RichTextCtrl_SuppressingUndo(*args, **kwargs)

    def HasCharacterAttributes(*args, **kwargs):
        """
        HasCharacterAttributes(self, RichTextRange range, RichTextAttr style) -> bool

        Test if this whole range has character attributes of the specified
        kind. If any of the attributes are different within the range, the
        test fails. You can use this to implement, for example, bold button
        updating. ``style`` must have flags indicating which attributes are of
        interest.

        """
        return _richtext.RichTextCtrl_HasCharacterAttributes(*args, **kwargs)

    def HasParagraphAttributes(*args, **kwargs):
        """
        HasParagraphAttributes(self, RichTextRange range, RichTextAttr style) -> bool

        Test if this whole range has paragraph attributes of the specified
        kind. If any of the attributes are different within the range, the
        test fails. You can use this to implement, for example, centering
        button updating. style must have flags indicating which attributes are
        of interest.

        """
        return _richtext.RichTextCtrl_HasParagraphAttributes(*args, **kwargs)

    def IsSelectionBold(*args, **kwargs):
        """
        IsSelectionBold(self) -> bool

        Is all of the selection bold?
        """
        return _richtext.RichTextCtrl_IsSelectionBold(*args, **kwargs)

    def IsSelectionItalics(*args, **kwargs):
        """
        IsSelectionItalics(self) -> bool

        Is all of the selection italics?
        """
        return _richtext.RichTextCtrl_IsSelectionItalics(*args, **kwargs)

    def IsSelectionUnderlined(*args, **kwargs):
        """
        IsSelectionUnderlined(self) -> bool

        Is all of the selection underlined?
        """
        return _richtext.RichTextCtrl_IsSelectionUnderlined(*args, **kwargs)

    def DoesSelectionHaveTextEffectFlag(*args, **kwargs):
        """DoesSelectionHaveTextEffectFlag(self, int flag) -> bool"""
        return _richtext.RichTextCtrl_DoesSelectionHaveTextEffectFlag(*args, **kwargs)

    def IsSelectionAligned(*args, **kwargs):
        """
        IsSelectionAligned(self, int alignment) -> bool

        Is all of the selection aligned according to the specified flag?
        """
        return _richtext.RichTextCtrl_IsSelectionAligned(*args, **kwargs)

    def ApplyBoldToSelection(*args, **kwargs):
        """
        ApplyBoldToSelection(self) -> bool

        Apply bold to the selection
        """
        return _richtext.RichTextCtrl_ApplyBoldToSelection(*args, **kwargs)

    def ApplyItalicToSelection(*args, **kwargs):
        """
        ApplyItalicToSelection(self) -> bool

        Apply italic to the selection
        """
        return _richtext.RichTextCtrl_ApplyItalicToSelection(*args, **kwargs)

    def ApplyUnderlineToSelection(*args, **kwargs):
        """
        ApplyUnderlineToSelection(self) -> bool

        Apply underline to the selection
        """
        return _richtext.RichTextCtrl_ApplyUnderlineToSelection(*args, **kwargs)

    def ApplyTextEffectToSelection(*args, **kwargs):
        """ApplyTextEffectToSelection(self, int flags) -> bool"""
        return _richtext.RichTextCtrl_ApplyTextEffectToSelection(*args, **kwargs)

    def ApplyAlignmentToSelection(*args, **kwargs):
        """
        ApplyAlignmentToSelection(self, int alignment) -> bool

        Apply alignment to the selection
        """
        return _richtext.RichTextCtrl_ApplyAlignmentToSelection(*args, **kwargs)

    def ApplyStyle(*args, **kwargs):
        """
        ApplyStyle(self, wxRichTextStyleDefinition def) -> bool

        Apply a named style to the selection
        """
        return _richtext.RichTextCtrl_ApplyStyle(*args, **kwargs)

    def SetStyleSheet(*args, **kwargs):
        """
        SetStyleSheet(self, wxRichTextStyleSheet styleSheet)

        Set style sheet, if any.
        """
        return _richtext.RichTextCtrl_SetStyleSheet(*args, **kwargs)

    def GetStyleSheet(*args, **kwargs):
        """GetStyleSheet(self) -> wxRichTextStyleSheet"""
        return _richtext.RichTextCtrl_GetStyleSheet(*args, **kwargs)

    def PushStyleSheet(*args, **kwargs):
        """
        PushStyleSheet(self, wxRichTextStyleSheet styleSheet) -> bool

        Push style sheet to top of stack
        """
        return _richtext.RichTextCtrl_PushStyleSheet(*args, **kwargs)

    def PopStyleSheet(*args, **kwargs):
        """
        PopStyleSheet(self) -> wxRichTextStyleSheet

        Pop style sheet from top of stack
        """
        return _richtext.RichTextCtrl_PopStyleSheet(*args, **kwargs)

    def ApplyStyleSheet(*args, **kwargs):
        """
        ApplyStyleSheet(self, wxRichTextStyleSheet styleSheet=None) -> bool

        Apply the style sheet to the buffer, for example if the styles have
        changed.
        """
        return _richtext.RichTextCtrl_ApplyStyleSheet(*args, **kwargs)

    def ShowContextMenu(*args, **kwargs):
        """ShowContextMenu(self, Menu menu, Point pt, bool addPropertyCommands=True) -> bool"""
        return _richtext.RichTextCtrl_ShowContextMenu(*args, **kwargs)

    def PrepareContextMenu(*args, **kwargs):
        """PrepareContextMenu(self, Menu menu, Point pt, bool addPropertyCommands=True) -> int"""
        return _richtext.RichTextCtrl_PrepareContextMenu(*args, **kwargs)

    Buffer = property(GetBuffer) 
    DelayedLayoutThreshold = property(GetDelayedLayoutThreshold,SetDelayedLayoutThreshold) 
    Filename = property(GetFilename,SetFilename) 
    InternalSelectionRange = property(GetInternalSelectionRange,SetInternalSelectionRange) 
    SelectionRange = property(GetSelectionRange,SetSelectionRange) 
    StyleSheet = property(GetStyleSheet,SetStyleSheet) 
    TextCursor = property(GetTextCursor,SetTextCursor) 
    URLCursor = property(GetURLCursor,SetURLCursor) 
    def SetupScrollbars(*args, **kwargs):
        """SetupScrollbars(self, bool atTop=False)"""
        return _richtext.RichTextCtrl_SetupScrollbars(*args, **kwargs)

    def KeyboardNavigate(*args, **kwargs):
        """KeyboardNavigate(self, int keyCode, int flags) -> bool"""
        return _richtext.RichTextCtrl_KeyboardNavigate(*args, **kwargs)

    def PositionCaret(*args, **kwargs):
        """PositionCaret(self)"""
        return _richtext.RichTextCtrl_PositionCaret(*args, **kwargs)

    def ExtendSelection(*args, **kwargs):
        """ExtendSelection(self, long oldPosition, long newPosition, int flags) -> bool"""
        return _richtext.RichTextCtrl_ExtendSelection(*args, **kwargs)

    def ScrollIntoView(*args, **kwargs):
        """ScrollIntoView(self, long position, int keyCode) -> bool"""
        return _richtext.RichTextCtrl_ScrollIntoView(*args, **kwargs)

    def SetCaretPosition(*args, **kwargs):
        """SetCaretPosition(self, long position, bool showAtLineStart=False)"""
        return _richtext.RichTextCtrl_SetCaretPosition(*args, **kwargs)

    def GetCaretPosition(*args, **kwargs):
        """GetCaretPosition(self) -> long"""
        return _richtext.RichTextCtrl_GetCaretPosition(*args, **kwargs)

    def GetAdjustedCaretPosition(*args, **kwargs):
        """GetAdjustedCaretPosition(self, long caretPos) -> long"""
        return _richtext.RichTextCtrl_GetAdjustedCaretPosition(*args, **kwargs)

    def MoveCaretForward(*args, **kwargs):
        """MoveCaretForward(self, long oldPosition)"""
        return _richtext.RichTextCtrl_MoveCaretForward(*args, **kwargs)

    def MoveCaretBack(*args, **kwargs):
        """MoveCaretBack(self, long oldPosition)"""
        return _richtext.RichTextCtrl_MoveCaretBack(*args, **kwargs)

    def GetCaretPositionForIndex(*args, **kwargs):
        """GetCaretPositionForIndex(self, long position, Rect rect) -> bool"""
        return _richtext.RichTextCtrl_GetCaretPositionForIndex(*args, **kwargs)

    def GetVisibleLineForCaretPosition(*args, **kwargs):
        """GetVisibleLineForCaretPosition(self, long caretPosition) -> RichTextLine"""
        return _richtext.RichTextCtrl_GetVisibleLineForCaretPosition(*args, **kwargs)

    def GetCommandProcessor(*args, **kwargs):
        """GetCommandProcessor(self) -> wxCommandProcessor"""
        return _richtext.RichTextCtrl_GetCommandProcessor(*args, **kwargs)

    def DeleteSelectedContent(*args, **kwargs):
        """DeleteSelectedContent(self, long OUTPUT) -> bool"""
        return _richtext.RichTextCtrl_DeleteSelectedContent(*args, **kwargs)

    def GetPhysicalPoint(*args, **kwargs):
        """GetPhysicalPoint(self, Point ptLogical) -> Point"""
        return _richtext.RichTextCtrl_GetPhysicalPoint(*args, **kwargs)

    def GetLogicalPoint(*args, **kwargs):
        """GetLogicalPoint(self, Point ptPhysical) -> Point"""
        return _richtext.RichTextCtrl_GetLogicalPoint(*args, **kwargs)

    def FindNextWordPosition(*args, **kwargs):
        """FindNextWordPosition(self, int direction=1) -> long"""
        return _richtext.RichTextCtrl_FindNextWordPosition(*args, **kwargs)

    def IsPositionVisible(*args, **kwargs):
        """IsPositionVisible(self, long pos) -> bool"""
        return _richtext.RichTextCtrl_IsPositionVisible(*args, **kwargs)

    def GetFirstVisiblePosition(*args, **kwargs):
        """GetFirstVisiblePosition(self) -> long"""
        return _richtext.RichTextCtrl_GetFirstVisiblePosition(*args, **kwargs)

    def GetCaretPositionForDefaultStyle(*args, **kwargs):
        """GetCaretPositionForDefaultStyle(self) -> long"""
        return _richtext.RichTextCtrl_GetCaretPositionForDefaultStyle(*args, **kwargs)

    def SetCaretPositionForDefaultStyle(*args, **kwargs):
        """SetCaretPositionForDefaultStyle(self, long pos)"""
        return _richtext.RichTextCtrl_SetCaretPositionForDefaultStyle(*args, **kwargs)

    def IsDefaultStyleShowing(*args, **kwargs):
        """IsDefaultStyleShowing(self) -> bool"""
        return _richtext.RichTextCtrl_IsDefaultStyleShowing(*args, **kwargs)

    def SetAndShowDefaultStyle(*args, **kwargs):
        """SetAndShowDefaultStyle(self, RichTextAttr attr)"""
        return _richtext.RichTextCtrl_SetAndShowDefaultStyle(*args, **kwargs)

    def GetFirstVisiblePoint(*args, **kwargs):
        """GetFirstVisiblePoint(self) -> Point"""
        return _richtext.RichTextCtrl_GetFirstVisiblePoint(*args, **kwargs)

    def GetScrollPageSize(*args, **kwargs):
        """GetScrollPageSize(self, int orient) -> int"""
        return _richtext.RichTextCtrl_GetScrollPageSize(*args, **kwargs)

    def SetScrollPageSize(*args, **kwargs):
        """SetScrollPageSize(self, int orient, int pageSize)"""
        return _richtext.RichTextCtrl_SetScrollPageSize(*args, **kwargs)

    def SetScrollRate(*args, **kwargs):
        """SetScrollRate(self, int xstep, int ystep)"""
        return _richtext.RichTextCtrl_SetScrollRate(*args, **kwargs)

    def GetViewStart(*args, **kwargs):
        """
        GetViewStart() -> (x,y)

        Get the view start
        """
        return _richtext.RichTextCtrl_GetViewStart(*args, **kwargs)

    def SetScale(*args, **kwargs):
        """SetScale(self, double xs, double ys)"""
        return _richtext.RichTextCtrl_SetScale(*args, **kwargs)

    def GetScaleX(*args, **kwargs):
        """GetScaleX(self) -> double"""
        return _richtext.RichTextCtrl_GetScaleX(*args, **kwargs)

    def GetScaleY(*args, **kwargs):
        """GetScaleY(self) -> double"""
        return _richtext.RichTextCtrl_GetScaleY(*args, **kwargs)

    def CalcScrolledPosition(*args):
        """
        CalcScrolledPosition(self, Point pt) -> Point
        CalcScrolledPosition(int x, int y) -> (sx, sy)

        Translate between scrolled and unscrolled coordinates.
        """
        return _richtext.RichTextCtrl_CalcScrolledPosition(*args)

    def CalcUnscrolledPosition(*args):
        """
        CalcUnscrolledPosition(self, Point pt) -> Point
        CalcUnscrolledPosition(int x, int y) -> (ux, uy)

        Translate between scrolled and unscrolled coordinates.
        """
        return _richtext.RichTextCtrl_CalcUnscrolledPosition(*args)

    def SetTargetRect(*args, **kwargs):
        """SetTargetRect(self, Rect rect)"""
        return _richtext.RichTextCtrl_SetTargetRect(*args, **kwargs)

    def GetTargetRect(*args, **kwargs):
        """GetTargetRect(self) -> Rect"""
        return _richtext.RichTextCtrl_GetTargetRect(*args, **kwargs)

    def IsEmpty(*args, **kwargs):
        """
        IsEmpty(self) -> bool

        Returns True if the value in the text field is empty.
        """
        return _richtext.RichTextCtrl_IsEmpty(*args, **kwargs)

    def SetModified(*args, **kwargs):
        """SetModified(self, bool modified)"""
        return _richtext.RichTextCtrl_SetModified(*args, **kwargs)

_richtext.RichTextCtrl_swigregister(RichTextCtrl)
RichTextCtrlNameStr = cvar.RichTextCtrlNameStr

def PreRichTextCtrl(*args, **kwargs):
    """PreRichTextCtrl() -> RichTextCtrl"""
    val = _richtext.new_PreRichTextCtrl(*args, **kwargs)
    return val

#---------------------------------------------------------------------------

wxEVT_COMMAND_RICHTEXT_LEFT_CLICK = _richtext.wxEVT_COMMAND_RICHTEXT_LEFT_CLICK
wxEVT_COMMAND_RICHTEXT_RIGHT_CLICK = _richtext.wxEVT_COMMAND_RICHTEXT_RIGHT_CLICK
wxEVT_COMMAND_RICHTEXT_MIDDLE_CLICK = _richtext.wxEVT_COMMAND_RICHTEXT_MIDDLE_CLICK
wxEVT_COMMAND_RICHTEXT_LEFT_DCLICK = _richtext.wxEVT_COMMAND_RICHTEXT_LEFT_DCLICK
wxEVT_COMMAND_RICHTEXT_RETURN = _richtext.wxEVT_COMMAND_RICHTEXT_RETURN
wxEVT_COMMAND_RICHTEXT_CHARACTER = _richtext.wxEVT_COMMAND_RICHTEXT_CHARACTER
wxEVT_COMMAND_RICHTEXT_DELETE = _richtext.wxEVT_COMMAND_RICHTEXT_DELETE
wxEVT_COMMAND_RICHTEXT_STYLESHEET_CHANGING = _richtext.wxEVT_COMMAND_RICHTEXT_STYLESHEET_CHANGING
wxEVT_COMMAND_RICHTEXT_STYLESHEET_CHANGED = _richtext.wxEVT_COMMAND_RICHTEXT_STYLESHEET_CHANGED
wxEVT_COMMAND_RICHTEXT_STYLESHEET_REPLACING = _richtext.wxEVT_COMMAND_RICHTEXT_STYLESHEET_REPLACING
wxEVT_COMMAND_RICHTEXT_STYLESHEET_REPLACED = _richtext.wxEVT_COMMAND_RICHTEXT_STYLESHEET_REPLACED
wxEVT_COMMAND_RICHTEXT_CONTENT_INSERTED = _richtext.wxEVT_COMMAND_RICHTEXT_CONTENT_INSERTED
wxEVT_COMMAND_RICHTEXT_CONTENT_DELETED = _richtext.wxEVT_COMMAND_RICHTEXT_CONTENT_DELETED
wxEVT_COMMAND_RICHTEXT_STYLE_CHANGED = _richtext.wxEVT_COMMAND_RICHTEXT_STYLE_CHANGED
wxEVT_COMMAND_RICHTEXT_SELECTION_CHANGED = _richtext.wxEVT_COMMAND_RICHTEXT_SELECTION_CHANGED
wxEVT_COMMAND_RICHTEXT_BUFFER_RESET = _richtext.wxEVT_COMMAND_RICHTEXT_BUFFER_RESET
EVT_RICHTEXT_LEFT_CLICK = wx.PyEventBinder(wxEVT_COMMAND_RICHTEXT_LEFT_CLICK, 1)
EVT_RICHTEXT_RIGHT_CLICK = wx.PyEventBinder(wxEVT_COMMAND_RICHTEXT_RIGHT_CLICK, 1)
EVT_RICHTEXT_MIDDLE_CLICK = wx.PyEventBinder(wxEVT_COMMAND_RICHTEXT_MIDDLE_CLICK, 1)
EVT_RICHTEXT_LEFT_DCLICK = wx.PyEventBinder(wxEVT_COMMAND_RICHTEXT_LEFT_DCLICK, 1)
EVT_RICHTEXT_RETURN = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_RETURN, 1)
EVT_RICHTEXT_CHARACTER = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_CHARACTER, 1)
EVT_RICHTEXT_DELETE = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_DELETE, 1)

EVT_RICHTEXT_STYLESHEET_CHANGING = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_STYLESHEET_CHANGING, 1)
EVT_RICHTEXT_STYLESHEET_CHANGED = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_STYLESHEET_CHANGED, 1)
EVT_RICHTEXT_STYLESHEET_REPLACING = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_STYLESHEET_REPLACING, 1)
EVT_RICHTEXT_STYLESHEET_REPLACED = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_STYLESHEET_REPLACED, 1)

EVT_RICHTEXT_CONTENT_INSERTED = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_CONTENT_INSERTED, 1)
EVT_RICHTEXT_CONTENT_DELETED = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_CONTENT_DELETED, 1)
EVT_RICHTEXT_STYLE_CHANGED = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_STYLE_CHANGED, 1)
EVT_RICHTEXT_SELECTION_CHANGED = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_SELECTION_CHANGED, 1)    
EVT_RICHTEXT_BUFFER_RESET = wx.PyEventBinder( wxEVT_COMMAND_RICHTEXT_BUFFER_RESET, 1)

class RichTextEvent(_core.NotifyEvent):
    """Proxy of C++ RichTextEvent class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, EventType commandType=wxEVT_NULL, int winid=0) -> RichTextEvent"""
        _richtext.RichTextEvent_swiginit(self,_richtext.new_RichTextEvent(*args, **kwargs))
    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> int"""
        return _richtext.RichTextEvent_GetPosition(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, int n)"""
        return _richtext.RichTextEvent_SetPosition(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """GetFlags(self) -> int"""
        return _richtext.RichTextEvent_GetFlags(*args, **kwargs)

    def SetFlags(*args, **kwargs):
        """SetFlags(self, int flags)"""
        return _richtext.RichTextEvent_SetFlags(*args, **kwargs)

    def GetOldStyleSheet(*args, **kwargs):
        """GetOldStyleSheet(self) -> wxRichTextStyleSheet"""
        return _richtext.RichTextEvent_GetOldStyleSheet(*args, **kwargs)

    def SetOldStyleSheet(*args, **kwargs):
        """SetOldStyleSheet(self, wxRichTextStyleSheet sheet)"""
        return _richtext.RichTextEvent_SetOldStyleSheet(*args, **kwargs)

    def GetNewStyleSheet(*args, **kwargs):
        """GetNewStyleSheet(self) -> wxRichTextStyleSheet"""
        return _richtext.RichTextEvent_GetNewStyleSheet(*args, **kwargs)

    def SetNewStyleSheet(*args, **kwargs):
        """SetNewStyleSheet(self, wxRichTextStyleSheet sheet)"""
        return _richtext.RichTextEvent_SetNewStyleSheet(*args, **kwargs)

    def GetRange(*args, **kwargs):
        """GetRange(self) -> RichTextRange"""
        return _richtext.RichTextEvent_GetRange(*args, **kwargs)

    def SetRange(*args, **kwargs):
        """SetRange(self, RichTextRange range)"""
        return _richtext.RichTextEvent_SetRange(*args, **kwargs)

    def GetCharacter(*args, **kwargs):
        """GetCharacter(self) -> wxChar"""
        return _richtext.RichTextEvent_GetCharacter(*args, **kwargs)

    def SetCharacter(*args, **kwargs):
        """SetCharacter(self, wxChar ch)"""
        return _richtext.RichTextEvent_SetCharacter(*args, **kwargs)

    Flags = property(GetFlags,SetFlags) 
    Index = property(GetPosition,SetPosition) 
    OldStyleSheet = property(GetOldStyleSheet,SetOldStyleSheet) 
    NewStyleSheet = property(GetNewStyleSheet,SetNewStyleSheet) 
    Range = property(GetRange,SetRange) 
    Character = property(GetCharacter,SetCharacter) 
_richtext.RichTextEvent_swigregister(RichTextEvent)

#---------------------------------------------------------------------------

class RichTextHTMLHandler(RichTextFileHandler):
    """Proxy of C++ RichTextHTMLHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String name=HtmlName, String ext=HtmlExt, int type=RICHTEXT_TYPE_HTML) -> RichTextHTMLHandler"""
        _richtext.RichTextHTMLHandler_swiginit(self,_richtext.new_RichTextHTMLHandler(*args, **kwargs))
    def SetTemporaryImageLocations(*args, **kwargs):
        """
        SetTemporaryImageLocations(self, wxArrayString locations)

        Set the list of image locations generated by the last operation
        """
        return _richtext.RichTextHTMLHandler_SetTemporaryImageLocations(*args, **kwargs)

    def GetTemporaryImageLocations(*args, **kwargs):
        """
        GetTemporaryImageLocations(self) -> wxArrayString

        Get the list of image locations generated by the last operation
        """
        return _richtext.RichTextHTMLHandler_GetTemporaryImageLocations(*args, **kwargs)

    TemporaryImageLocations = property(GetTemporaryImageLocations,SetTemporaryImageLocations) 
    def ClearTemporaryImageLocations(*args, **kwargs):
        """
        ClearTemporaryImageLocations(self)

        Clear the image locations generated by the last operation
        """
        return _richtext.RichTextHTMLHandler_ClearTemporaryImageLocations(*args, **kwargs)

    def DeleteTemporaryImages(*args, **kwargs):
        """
        DeleteTemporaryImages(self) -> bool

        Delete the in-memory or temporary files generated by the last operation
        """
        return _richtext.RichTextHTMLHandler_DeleteTemporaryImages(*args, **kwargs)

    def SetFileCounter(*args, **kwargs):
        """
        SetFileCounter(int counter)

        Reset the file counter, in case, for example, the same names are required each
        time
        """
        return _richtext.RichTextHTMLHandler_SetFileCounter(*args, **kwargs)

    SetFileCounter = staticmethod(SetFileCounter)
    def SetTempDir(*args, **kwargs):
        """
        SetTempDir(self, String tempDir)

        Set the directory for storing temporary files. If empty, the system temporary
        directory will be used.
        """
        return _richtext.RichTextHTMLHandler_SetTempDir(*args, **kwargs)

    def GetTempDir(*args, **kwargs):
        """
        GetTempDir(self) -> String

        Get the directory for storing temporary files. If empty, the system temporary
        directory will be used.
        """
        return _richtext.RichTextHTMLHandler_GetTempDir(*args, **kwargs)

    TempDir = property(GetTempDir,SetTempDir) 
    def SetFontSizeMapping(*args, **kwargs):
        """
        SetFontSizeMapping(self, wxArrayInt fontSizeMapping)

        Set mapping from point size to HTML font size. There should be 7 elements, one
        for each HTML font size, each element specifying the maximum point size for
        that HTML font size. E.g. 8, 10, 13, 17, 22, 29, 100

        """
        return _richtext.RichTextHTMLHandler_SetFontSizeMapping(*args, **kwargs)

    def GetFontSizeMapping(*args, **kwargs):
        """
        GetFontSizeMapping(self) -> wxArrayInt

        Get mapping deom point size to HTML font size.
        """
        return _richtext.RichTextHTMLHandler_GetFontSizeMapping(*args, **kwargs)

    FontSizeMapping = property(GetFontSizeMapping,SetFontSizeMapping) 
_richtext.RichTextHTMLHandler_swigregister(RichTextHTMLHandler)
HtmlName = cvar.HtmlName
HtmlExt = cvar.HtmlExt

def RichTextHTMLHandler_SetFileCounter(*args, **kwargs):
  """
    RichTextHTMLHandler_SetFileCounter(int counter)

    Reset the file counter, in case, for example, the same names are required each
    time
    """
  return _richtext.RichTextHTMLHandler_SetFileCounter(*args, **kwargs)

#---------------------------------------------------------------------------

class RichTextXMLHandler(RichTextFileHandler):
    """Proxy of C++ RichTextXMLHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String name=XmlName, String ext=XmlExt, int type=RICHTEXT_TYPE_XML) -> RichTextXMLHandler"""
        _richtext.RichTextXMLHandler_swiginit(self,_richtext.new_RichTextXMLHandler(*args, **kwargs))
_richtext.RichTextXMLHandler_swigregister(RichTextXMLHandler)
XmlName = cvar.XmlName
XmlExt = cvar.XmlExt

#---------------------------------------------------------------------------

RICHTEXT_PRINT_MAX_PAGES = _richtext.RICHTEXT_PRINT_MAX_PAGES
RICHTEXT_PAGE_ODD = _richtext.RICHTEXT_PAGE_ODD
RICHTEXT_PAGE_EVEN = _richtext.RICHTEXT_PAGE_EVEN
RICHTEXT_PAGE_ALL = _richtext.RICHTEXT_PAGE_ALL
RICHTEXT_PAGE_LEFT = _richtext.RICHTEXT_PAGE_LEFT
RICHTEXT_PAGE_CENTRE = _richtext.RICHTEXT_PAGE_CENTRE
RICHTEXT_PAGE_RIGHT = _richtext.RICHTEXT_PAGE_RIGHT
class RichTextPrintout(_windows.Printout):
    """Proxy of C++ RichTextPrintout class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String title=wxT("Printout")) -> RichTextPrintout"""
        _richtext.RichTextPrintout_swiginit(self,_richtext.new_RichTextPrintout(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_RichTextPrintout
    __del__ = lambda self : None;
    def SetRichTextBuffer(*args, **kwargs):
        """SetRichTextBuffer(self, RichTextBuffer buffer)"""
        return _richtext.RichTextPrintout_SetRichTextBuffer(*args, **kwargs)

    def GetRichTextBuffer(*args, **kwargs):
        """GetRichTextBuffer(self) -> RichTextBuffer"""
        return _richtext.RichTextPrintout_GetRichTextBuffer(*args, **kwargs)

    def SetHeaderFooterData(*args, **kwargs):
        """SetHeaderFooterData(self, wxRichTextHeaderFooterData data)"""
        return _richtext.RichTextPrintout_SetHeaderFooterData(*args, **kwargs)

    def GetHeaderFooterData(*args, **kwargs):
        """GetHeaderFooterData(self) -> wxRichTextHeaderFooterData"""
        return _richtext.RichTextPrintout_GetHeaderFooterData(*args, **kwargs)

    def SetMargins(*args, **kwargs):
        """SetMargins(self, int top=254, int bottom=254, int left=254, int right=254)"""
        return _richtext.RichTextPrintout_SetMargins(*args, **kwargs)

    def CalculateScaling(*args, **kwargs):
        """CalculateScaling(self, DC dc, Rect textRect, Rect headerRect, Rect footerRect)"""
        return _richtext.RichTextPrintout_CalculateScaling(*args, **kwargs)

_richtext.RichTextPrintout_swigregister(RichTextPrintout)

class RichTextPrinting(_core.Object):
    """Proxy of C++ RichTextPrinting class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String name=wxT("Printing"), Window parentWindow=None) -> RichTextPrinting"""
        _richtext.RichTextPrinting_swiginit(self,_richtext.new_RichTextPrinting(*args, **kwargs))
    __swig_destroy__ = _richtext.delete_RichTextPrinting
    __del__ = lambda self : None;
    def PreviewFile(*args, **kwargs):
        """PreviewFile(self, String richTextFile) -> bool"""
        return _richtext.RichTextPrinting_PreviewFile(*args, **kwargs)

    def PreviewBuffer(*args, **kwargs):
        """PreviewBuffer(self, RichTextBuffer buffer) -> bool"""
        return _richtext.RichTextPrinting_PreviewBuffer(*args, **kwargs)

    def PrintFile(*args, **kwargs):
        """PrintFile(self, String richTextFile) -> bool"""
        return _richtext.RichTextPrinting_PrintFile(*args, **kwargs)

    def PrintBuffer(*args, **kwargs):
        """PrintBuffer(self, RichTextBuffer buffer) -> bool"""
        return _richtext.RichTextPrinting_PrintBuffer(*args, **kwargs)

    def PageSetup(*args, **kwargs):
        """PageSetup(self)"""
        return _richtext.RichTextPrinting_PageSetup(*args, **kwargs)

    def SetHeaderFooterData(*args, **kwargs):
        """SetHeaderFooterData(self, wxRichTextHeaderFooterData data)"""
        return _richtext.RichTextPrinting_SetHeaderFooterData(*args, **kwargs)

    def GetHeaderFooterData(*args, **kwargs):
        """GetHeaderFooterData(self) -> wxRichTextHeaderFooterData"""
        return _richtext.RichTextPrinting_GetHeaderFooterData(*args, **kwargs)

    def SetHeaderText(*args, **kwargs):
        """SetHeaderText(self, String text, int page=RICHTEXT_PAGE_ALL, int location=RICHTEXT_PAGE_CENTRE)"""
        return _richtext.RichTextPrinting_SetHeaderText(*args, **kwargs)

    def GetHeaderText(*args, **kwargs):
        """GetHeaderText(self, int page=RICHTEXT_PAGE_EVEN, int location=RICHTEXT_PAGE_CENTRE) -> String"""
        return _richtext.RichTextPrinting_GetHeaderText(*args, **kwargs)

    def SetFooterText(*args, **kwargs):
        """SetFooterText(self, String text, int page=RICHTEXT_PAGE_ALL, int location=RICHTEXT_PAGE_CENTRE)"""
        return _richtext.RichTextPrinting_SetFooterText(*args, **kwargs)

    def GetFooterText(*args, **kwargs):
        """GetFooterText(self, int page=RICHTEXT_PAGE_EVEN, int location=RICHTEXT_PAGE_CENTRE) -> String"""
        return _richtext.RichTextPrinting_GetFooterText(*args, **kwargs)

    def SetShowOnFirstPage(*args, **kwargs):
        """SetShowOnFirstPage(self, bool show)"""
        return _richtext.RichTextPrinting_SetShowOnFirstPage(*args, **kwargs)

    def SetHeaderFooterFont(*args, **kwargs):
        """SetHeaderFooterFont(self, Font font)"""
        return _richtext.RichTextPrinting_SetHeaderFooterFont(*args, **kwargs)

    def SetHeaderFooterTextColour(*args, **kwargs):
        """SetHeaderFooterTextColour(self, Colour font)"""
        return _richtext.RichTextPrinting_SetHeaderFooterTextColour(*args, **kwargs)

    def GetPrintData(*args, **kwargs):
        """GetPrintData(self) -> PrintData"""
        return _richtext.RichTextPrinting_GetPrintData(*args, **kwargs)

    def GetPageSetupData(*args, **kwargs):
        """GetPageSetupData(self) -> PageSetupDialogData"""
        return _richtext.RichTextPrinting_GetPageSetupData(*args, **kwargs)

    def SetPrintData(*args, **kwargs):
        """SetPrintData(self, PrintData printData)"""
        return _richtext.RichTextPrinting_SetPrintData(*args, **kwargs)

    def SetPageSetupData(*args, **kwargs):
        """SetPageSetupData(self, wxPageSetupData pageSetupData)"""
        return _richtext.RichTextPrinting_SetPageSetupData(*args, **kwargs)

    def SetRichTextBufferPreview(*args, **kwargs):
        """SetRichTextBufferPreview(self, RichTextBuffer buf)"""
        return _richtext.RichTextPrinting_SetRichTextBufferPreview(*args, **kwargs)

    def GetRichTextBufferPreview(*args, **kwargs):
        """GetRichTextBufferPreview(self) -> RichTextBuffer"""
        return _richtext.RichTextPrinting_GetRichTextBufferPreview(*args, **kwargs)

    def SetRichTextBufferPrinting(*args, **kwargs):
        """SetRichTextBufferPrinting(self, RichTextBuffer buf)"""
        return _richtext.RichTextPrinting_SetRichTextBufferPrinting(*args, **kwargs)

    def GetRichTextBufferPrinting(*args, **kwargs):
        """GetRichTextBufferPrinting(self) -> RichTextBuffer"""
        return _richtext.RichTextPrinting_GetRichTextBufferPrinting(*args, **kwargs)

    def SetParentWindow(*args, **kwargs):
        """SetParentWindow(self, Window parent)"""
        return _richtext.RichTextPrinting_SetParentWindow(*args, **kwargs)

    def GetParentWindow(*args, **kwargs):
        """GetParentWindow(self) -> Window"""
        return _richtext.RichTextPrinting_GetParentWindow(*args, **kwargs)

    def SetTitle(*args, **kwargs):
        """SetTitle(self, String title)"""
        return _richtext.RichTextPrinting_SetTitle(*args, **kwargs)

    def GetTitle(*args, **kwargs):
        """GetTitle(self) -> String"""
        return _richtext.RichTextPrinting_GetTitle(*args, **kwargs)

    def SetPreviewRect(*args, **kwargs):
        """SetPreviewRect(self, Rect rect)"""
        return _richtext.RichTextPrinting_SetPreviewRect(*args, **kwargs)

    def GetPreviewRect(*args, **kwargs):
        """GetPreviewRect(self) -> Rect"""
        return _richtext.RichTextPrinting_GetPreviewRect(*args, **kwargs)

_richtext.RichTextPrinting_swigregister(RichTextPrinting)



