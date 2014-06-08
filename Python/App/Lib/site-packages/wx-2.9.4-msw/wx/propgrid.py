# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

"""
The `PropertyGrid` provides a specialized grid for editing
properties such as strings, numbers, colours, and string lists.
"""

import _propgrid
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


import _core
import _windows
wx = _core 
__docfilter__ = wx.__DocFilter(globals()) 
PG_XBEFORETEXT = _propgrid.PG_XBEFORETEXT
PG_XBEFOREWIDGET = _propgrid.PG_XBEFOREWIDGET
PG_ICON_WIDTH = _propgrid.PG_ICON_WIDTH
PG_USE_RENDERER_NATIVE = _propgrid.PG_USE_RENDERER_NATIVE
PG_SUPPORT_TOOLTIPS = _propgrid.PG_SUPPORT_TOOLTIPS
PG_CUSTOM_IMAGE_WIDTH = _propgrid.PG_CUSTOM_IMAGE_WIDTH
PG_NO_CHILD_EVT_MOTION = _propgrid.PG_NO_CHILD_EVT_MOTION
PG_NAT_BUTTON_BORDER_ANY = _propgrid.PG_NAT_BUTTON_BORDER_ANY
PG_NAT_BUTTON_BORDER_X = _propgrid.PG_NAT_BUTTON_BORDER_X
PG_NAT_BUTTON_BORDER_Y = _propgrid.PG_NAT_BUTTON_BORDER_Y
PG_REFRESH_CONTROLS = _propgrid.PG_REFRESH_CONTROLS
PG_CONTROL_MARGIN = _propgrid.PG_CONTROL_MARGIN
CC_CUSTOM_IMAGE_MARGIN1 = _propgrid.CC_CUSTOM_IMAGE_MARGIN1
CC_CUSTOM_IMAGE_MARGIN2 = _propgrid.CC_CUSTOM_IMAGE_MARGIN2
DEFAULT_IMAGE_OFFSET_INCREMENT = _propgrid.DEFAULT_IMAGE_OFFSET_INCREMENT
PG_DRAG_MARGIN = _propgrid.PG_DRAG_MARGIN
PG_SPLITTERX_DETECTMARGIN1 = _propgrid.PG_SPLITTERX_DETECTMARGIN1
PG_SPLITTERX_DETECTMARGIN2 = _propgrid.PG_SPLITTERX_DETECTMARGIN2
PG_SMALL_SCREEN = _propgrid.PG_SMALL_SCREEN
PG_COMPATIBILITY_1_4 = _propgrid.PG_COMPATIBILITY_1_4
PG_INCLUDE_ADVPROPS = _propgrid.PG_INCLUDE_ADVPROPS
PG_INCLUDE_CHECKBOX = _propgrid.PG_INCLUDE_CHECKBOX
PG_KEEP_STRUCTURE = _propgrid.PG_KEEP_STRUCTURE
PG_RECURSE = _propgrid.PG_RECURSE
PG_INC_ATTRIBUTES = _propgrid.PG_INC_ATTRIBUTES
PG_RECURSE_STARTS = _propgrid.PG_RECURSE_STARTS
PG_FORCE = _propgrid.PG_FORCE
PG_SORT_TOP_LEVEL_ONLY = _propgrid.PG_SORT_TOP_LEVEL_ONLY
PG_DONT_RECURSE = _propgrid.PG_DONT_RECURSE
PG_FULL_VALUE = _propgrid.PG_FULL_VALUE
PG_REPORT_ERROR = _propgrid.PG_REPORT_ERROR
PG_PROPERTY_SPECIFIC = _propgrid.PG_PROPERTY_SPECIFIC
PG_EDITABLE_VALUE = _propgrid.PG_EDITABLE_VALUE
PG_COMPOSITE_FRAGMENT = _propgrid.PG_COMPOSITE_FRAGMENT
PG_UNEDITABLE_COMPOSITE_FRAGMENT = _propgrid.PG_UNEDITABLE_COMPOSITE_FRAGMENT
PG_VALUE_IS_CURRENT = _propgrid.PG_VALUE_IS_CURRENT
PG_PROGRAMMATIC_VALUE = _propgrid.PG_PROGRAMMATIC_VALUE
PG_SETVAL_REFRESH_EDITOR = _propgrid.PG_SETVAL_REFRESH_EDITOR
PG_SETVAL_AGGREGATED = _propgrid.PG_SETVAL_AGGREGATED
PG_SETVAL_FROM_PARENT = _propgrid.PG_SETVAL_FROM_PARENT
PG_SETVAL_BY_USER = _propgrid.PG_SETVAL_BY_USER
class PGPaintData(object):
    """Proxy of C++ PGPaintData class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    m_parent = property(_propgrid.PGPaintData_m_parent_get, _propgrid.PGPaintData_m_parent_set)
    m_choiceItem = property(_propgrid.PGPaintData_m_choiceItem_get, _propgrid.PGPaintData_m_choiceItem_set)
    m_drawnWidth = property(_propgrid.PGPaintData_m_drawnWidth_get, _propgrid.PGPaintData_m_drawnWidth_set)
    m_drawnHeight = property(_propgrid.PGPaintData_m_drawnHeight_get, _propgrid.PGPaintData_m_drawnHeight_set)
_propgrid.PGPaintData_swigregister(PGPaintData)

PG_CUSTOM_IMAGE_SPACINGY = _propgrid.PG_CUSTOM_IMAGE_SPACINGY
PG_CAPRECTXMARGIN = _propgrid.PG_CAPRECTXMARGIN
PG_CAPRECTYMARGIN = _propgrid.PG_CAPRECTYMARGIN
class PGCell(_core.Object):
    """Proxy of C++ PGCell class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PGCell
        __init__(self, PGCell other) -> PGCell
        __init__(self, String text, Bitmap bitmap=wxNullBitmap, Colour fgCol=wxNullColour, 
            Colour bgCol=wxNullColour) -> PGCell
        """
        _propgrid.PGCell_swiginit(self,_propgrid.new_PGCell(*args))
    __swig_destroy__ = _propgrid.delete_PGCell
    __del__ = lambda self : None;
    def GetData(*args):
        """
        GetData(self)
        GetData(self)
        """
        return _propgrid.PGCell_GetData(*args)

    def HasText(*args, **kwargs):
        """HasText(self) -> bool"""
        return _propgrid.PGCell_HasText(*args, **kwargs)

    def SetEmptyData(*args, **kwargs):
        """SetEmptyData(self)"""
        return _propgrid.PGCell_SetEmptyData(*args, **kwargs)

    def MergeFrom(*args, **kwargs):
        """MergeFrom(self, PGCell srcCell)"""
        return _propgrid.PGCell_MergeFrom(*args, **kwargs)

    def SetText(*args, **kwargs):
        """SetText(self, String text)"""
        return _propgrid.PGCell_SetText(*args, **kwargs)

    def SetBitmap(*args, **kwargs):
        """SetBitmap(self, Bitmap bitmap)"""
        return _propgrid.PGCell_SetBitmap(*args, **kwargs)

    def SetFgCol(*args, **kwargs):
        """SetFgCol(self, Colour col)"""
        return _propgrid.PGCell_SetFgCol(*args, **kwargs)

    def SetFont(*args, **kwargs):
        """SetFont(self, Font font)"""
        return _propgrid.PGCell_SetFont(*args, **kwargs)

    def SetBgCol(*args, **kwargs):
        """SetBgCol(self, Colour col)"""
        return _propgrid.PGCell_SetBgCol(*args, **kwargs)

    def GetText(*args, **kwargs):
        """GetText(self) -> String"""
        return _propgrid.PGCell_GetText(*args, **kwargs)

    def GetBitmap(*args, **kwargs):
        """GetBitmap(self) -> Bitmap"""
        return _propgrid.PGCell_GetBitmap(*args, **kwargs)

    def GetFgCol(*args, **kwargs):
        """GetFgCol(self) -> Colour"""
        return _propgrid.PGCell_GetFgCol(*args, **kwargs)

    def GetFont(*args, **kwargs):
        """GetFont(self) -> Font"""
        return _propgrid.PGCell_GetFont(*args, **kwargs)

    def GetBgCol(*args, **kwargs):
        """GetBgCol(self) -> Colour"""
        return _propgrid.PGCell_GetBgCol(*args, **kwargs)

    def IsInvalid(*args, **kwargs):
        """IsInvalid(self) -> bool"""
        return _propgrid.PGCell_IsInvalid(*args, **kwargs)

_propgrid.PGCell_swigregister(PGCell)

PG_PROP_MODIFIED = _propgrid.PG_PROP_MODIFIED
PG_PROP_DISABLED = _propgrid.PG_PROP_DISABLED
PG_PROP_HIDDEN = _propgrid.PG_PROP_HIDDEN
PG_PROP_CUSTOMIMAGE = _propgrid.PG_PROP_CUSTOMIMAGE
PG_PROP_NOEDITOR = _propgrid.PG_PROP_NOEDITOR
PG_PROP_COLLAPSED = _propgrid.PG_PROP_COLLAPSED
PG_PROP_INVALID_VALUE = _propgrid.PG_PROP_INVALID_VALUE
PG_PROP_WAS_MODIFIED = _propgrid.PG_PROP_WAS_MODIFIED
PG_PROP_AGGREGATE = _propgrid.PG_PROP_AGGREGATE
PG_PROP_CHILDREN_ARE_COPIES = _propgrid.PG_PROP_CHILDREN_ARE_COPIES
PG_PROP_PROPERTY = _propgrid.PG_PROP_PROPERTY
PG_PROP_CATEGORY = _propgrid.PG_PROP_CATEGORY
PG_PROP_MISC_PARENT = _propgrid.PG_PROP_MISC_PARENT
PG_PROP_READONLY = _propgrid.PG_PROP_READONLY
PG_PROP_COMPOSED_VALUE = _propgrid.PG_PROP_COMPOSED_VALUE
PG_PROP_USES_COMMON_VALUE = _propgrid.PG_PROP_USES_COMMON_VALUE
PG_PROP_AUTO_UNSPECIFIED = _propgrid.PG_PROP_AUTO_UNSPECIFIED
PG_PROP_CLASS_SPECIFIC_1 = _propgrid.PG_PROP_CLASS_SPECIFIC_1
PG_PROP_CLASS_SPECIFIC_2 = _propgrid.PG_PROP_CLASS_SPECIFIC_2
PG_PROP_BEING_DELETED = _propgrid.PG_PROP_BEING_DELETED
class PGChoices(object):
    """Proxy of C++ PGChoices class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PGChoices
        __init__(self, PGChoices a) -> PGChoices
        __init__(self, wxChar labels, long values=None) -> PGChoices
        __init__(self, wxArrayString labels, wxArrayInt values=wxArrayInt()) -> PGChoices
        __init__(self,  data) -> PGChoices
        """
        _propgrid.PGChoices_swiginit(self,_propgrid.new_PGChoices(*args))
    __swig_destroy__ = _propgrid.delete_PGChoices
    __del__ = lambda self : None;
    def Add(*args):
        """
        Add(self, wxChar labels, ValArrItem values=None)
        Add(self, wxArrayString arr, wxArrayInt arrint=wxArrayInt())
        Add(self, String label, int value=INT_MAX)
        Add(self, String label, Bitmap bitmap, int value=INT_MAX)
        Add(self,  entry)
        """
        return _propgrid.PGChoices_Add(*args)

    def AddAsSorted(*args, **kwargs):
        """AddAsSorted(self, String label, int value=INT_MAX)"""
        return _propgrid.PGChoices_AddAsSorted(*args, **kwargs)

    def Assign(*args, **kwargs):
        """Assign(self, PGChoices a)"""
        return _propgrid.PGChoices_Assign(*args, **kwargs)

    def AssignData(*args, **kwargs):
        """AssignData(self,  data)"""
        return _propgrid.PGChoices_AssignData(*args, **kwargs)

    def Clear(*args, **kwargs):
        """Clear(self)"""
        return _propgrid.PGChoices_Clear(*args, **kwargs)

    def Copy(*args, **kwargs):
        """Copy(self) -> PGChoices"""
        return _propgrid.PGChoices_Copy(*args, **kwargs)

    def EnsureData(*args, **kwargs):
        """EnsureData(self)"""
        return _propgrid.PGChoices_EnsureData(*args, **kwargs)

    def GetId(*args, **kwargs):
        """GetId(self) -> PGChoicesId"""
        return _propgrid.PGChoices_GetId(*args, **kwargs)

    def GetLabel(*args, **kwargs):
        """GetLabel(self, int ind) -> String"""
        return _propgrid.PGChoices_GetLabel(*args, **kwargs)

    def GetCount(*args, **kwargs):
        """GetCount(self) -> int"""
        return _propgrid.PGChoices_GetCount(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self, int ind) -> int"""
        return _propgrid.PGChoices_GetValue(*args, **kwargs)

    def GetValuesForStrings(*args, **kwargs):
        """GetValuesForStrings(self, wxArrayString strings) -> wxArrayInt"""
        return _propgrid.PGChoices_GetValuesForStrings(*args, **kwargs)

    def GetIndicesForStrings(*args, **kwargs):
        """GetIndicesForStrings(self, wxArrayString strings, wxArrayString unmatched=None) -> wxArrayInt"""
        return _propgrid.PGChoices_GetIndicesForStrings(*args, **kwargs)

    def Index(*args):
        """
        Index(self, String str) -> int
        Index(self, int val) -> int
        """
        return _propgrid.PGChoices_Index(*args)

    def Insert(*args):
        """
        Insert(self, String label, int index, int value=INT_MAX)
        Insert(self,  entry, int index)
        """
        return _propgrid.PGChoices_Insert(*args)

    def IsOk(*args, **kwargs):
        """IsOk(self) -> bool"""
        return _propgrid.PGChoices_IsOk(*args, **kwargs)

    def Item(*args):
        """
        Item(self, int i)
        Item(self, int i)
        """
        return _propgrid.PGChoices_Item(*args)

    def RemoveAt(*args, **kwargs):
        """RemoveAt(self, size_t nIndex, size_t count=1)"""
        return _propgrid.PGChoices_RemoveAt(*args, **kwargs)

    def Set(*args):
        """
        Set(self, wxChar labels, long values=None)
        Set(self, wxArrayString labels, wxArrayInt values=wxArrayInt())
        """
        return _propgrid.PGChoices_Set(*args)

    def AllocExclusive(*args, **kwargs):
        """AllocExclusive(self)"""
        return _propgrid.PGChoices_AllocExclusive(*args, **kwargs)

    def GetData(*args, **kwargs):
        """GetData(self)"""
        return _propgrid.PGChoices_GetData(*args, **kwargs)

    def GetDataPtr(*args, **kwargs):
        """GetDataPtr(self)"""
        return _propgrid.PGChoices_GetDataPtr(*args, **kwargs)

    def ExtractData(*args, **kwargs):
        """ExtractData(self)"""
        return _propgrid.PGChoices_ExtractData(*args, **kwargs)

    def GetLabels(*args, **kwargs):
        """GetLabels(self) -> wxArrayString"""
        return _propgrid.PGChoices_GetLabels(*args, **kwargs)

_propgrid.PGChoices_swigregister(PGChoices)

class PGProperty(_core.Object):
    """Proxy of C++ PGProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PGProperty
        __init__(self, String label, String name) -> PGProperty
        """
        _propgrid.PGProperty_swiginit(self,_propgrid.new_PGProperty(*args))
    __swig_destroy__ = _propgrid.delete_PGProperty
    __del__ = lambda self : None;
    def OnSetValue(*args, **kwargs):
        """OnSetValue(self)"""
        return _propgrid.PGProperty_OnSetValue(*args, **kwargs)

    def DoGetValue(*args, **kwargs):
        """DoGetValue(self) -> wxVariant"""
        return _propgrid.PGProperty_DoGetValue(*args, **kwargs)

    def ValueToString(*args, **kwargs):
        """ValueToString(self, wxVariant value, int argFlags=0) -> String"""
        return _propgrid.PGProperty_ValueToString(*args, **kwargs)

    def SetValueFromString(*args, **kwargs):
        """SetValueFromString(self, String text, int flags=PG_PROGRAMMATIC_VALUE) -> bool"""
        return _propgrid.PGProperty_SetValueFromString(*args, **kwargs)

    def SetValueFromInt(*args, **kwargs):
        """SetValueFromInt(self, long value, int flags=0) -> bool"""
        return _propgrid.PGProperty_SetValueFromInt(*args, **kwargs)

    def OnMeasureImage(*args, **kwargs):
        """OnMeasureImage(self, int item=-1) -> Size"""
        return _propgrid.PGProperty_OnMeasureImage(*args, **kwargs)

    def OnEvent(*args, **kwargs):
        """OnEvent(self, PropertyGrid propgrid, Window wnd_primary, Event event) -> bool"""
        return _propgrid.PGProperty_OnEvent(*args, **kwargs)

    def ChildChanged(*args, **kwargs):
        """ChildChanged(self, wxVariant thisValue, int childIndex, wxVariant childValue) -> wxVariant"""
        return _propgrid.PGProperty_ChildChanged(*args, **kwargs)

    def DoGetEditorClass(*args, **kwargs):
        """DoGetEditorClass(self) -> PGEditor"""
        return _propgrid.PGProperty_DoGetEditorClass(*args, **kwargs)

    def DoGetValidator(*args, **kwargs):
        """DoGetValidator(self) -> Validator"""
        return _propgrid.PGProperty_DoGetValidator(*args, **kwargs)

    def OnCustomPaint(*args, **kwargs):
        """OnCustomPaint(self, DC dc, Rect rect, PGPaintData paintdata)"""
        return _propgrid.PGProperty_OnCustomPaint(*args, **kwargs)

    def GetCellRenderer(*args, **kwargs):
        """GetCellRenderer(self, int column)"""
        return _propgrid.PGProperty_GetCellRenderer(*args, **kwargs)

    def GetChoiceSelection(*args, **kwargs):
        """GetChoiceSelection(self) -> int"""
        return _propgrid.PGProperty_GetChoiceSelection(*args, **kwargs)

    def RefreshChildren(*args, **kwargs):
        """RefreshChildren(self)"""
        return _propgrid.PGProperty_RefreshChildren(*args, **kwargs)

    def DoSetAttribute(*args, **kwargs):
        """DoSetAttribute(self, String name, wxVariant value) -> bool"""
        return _propgrid.PGProperty_DoSetAttribute(*args, **kwargs)

    def DoGetAttribute(*args, **kwargs):
        """DoGetAttribute(self, String name) -> wxVariant"""
        return _propgrid.PGProperty_DoGetAttribute(*args, **kwargs)

    def GetEditorDialog(*args, **kwargs):
        """GetEditorDialog(self) -> PGEditorDialogAdapter"""
        return _propgrid.PGProperty_GetEditorDialog(*args, **kwargs)

    def OnValidationFailure(*args, **kwargs):
        """OnValidationFailure(self, wxVariant pendingValue)"""
        return _propgrid.PGProperty_OnValidationFailure(*args, **kwargs)

    def AddChoice(*args, **kwargs):
        """AddChoice(self, String label, int value=INT_MAX) -> int"""
        return _propgrid.PGProperty_AddChoice(*args, **kwargs)

    def AreChildrenComponents(*args, **kwargs):
        """AreChildrenComponents(self) -> bool"""
        return _propgrid.PGProperty_AreChildrenComponents(*args, **kwargs)

    def DeleteChildren(*args, **kwargs):
        """DeleteChildren(self)"""
        return _propgrid.PGProperty_DeleteChildren(*args, **kwargs)

    def DeleteChoice(*args, **kwargs):
        """DeleteChoice(self, int index)"""
        return _propgrid.PGProperty_DeleteChoice(*args, **kwargs)

    def Enable(*args, **kwargs):
        """Enable(self, bool enable=True)"""
        return _propgrid.PGProperty_Enable(*args, **kwargs)

    def EnableCommonValue(*args, **kwargs):
        """EnableCommonValue(self, bool enable=True)"""
        return _propgrid.PGProperty_EnableCommonValue(*args, **kwargs)

    def GenerateComposedValue(*args, **kwargs):
        """GenerateComposedValue(self) -> String"""
        return _propgrid.PGProperty_GenerateComposedValue(*args, **kwargs)

    def GetLabel(*args, **kwargs):
        """GetLabel(self) -> String"""
        return _propgrid.PGProperty_GetLabel(*args, **kwargs)

    def GetName(*args, **kwargs):
        """GetName(self) -> String"""
        return _propgrid.PGProperty_GetName(*args, **kwargs)

    def GetBaseName(*args, **kwargs):
        """GetBaseName(self) -> String"""
        return _propgrid.PGProperty_GetBaseName(*args, **kwargs)

    def GetChoices(*args, **kwargs):
        """GetChoices(self) -> PGChoices"""
        return _propgrid.PGProperty_GetChoices(*args, **kwargs)

    def GetY(*args, **kwargs):
        """GetY(self) -> int"""
        return _propgrid.PGProperty_GetY(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> wxVariant"""
        return _propgrid.PGProperty_GetValue(*args, **kwargs)

    def GetValuePlain(*args, **kwargs):
        """GetValuePlain(self) -> wxVariant"""
        return _propgrid.PGProperty_GetValuePlain(*args, **kwargs)

    def GetValueAsString(*args, **kwargs):
        """GetValueAsString(self, int argFlags=0) -> String"""
        return _propgrid.PGProperty_GetValueAsString(*args, **kwargs)

    def GetCell(*args):
        """
        GetCell(self, int column) -> PGCell
        GetCell(self, int column) -> PGCell
        """
        return _propgrid.PGProperty_GetCell(*args)

    def GetOrCreateCell(*args, **kwargs):
        """GetOrCreateCell(self, int column) -> PGCell"""
        return _propgrid.PGProperty_GetOrCreateCell(*args, **kwargs)

    def GetDisplayedCommonValueCount(*args, **kwargs):
        """GetDisplayedCommonValueCount(self) -> int"""
        return _propgrid.PGProperty_GetDisplayedCommonValueCount(*args, **kwargs)

    def GetDisplayedString(*args, **kwargs):
        """GetDisplayedString(self) -> String"""
        return _propgrid.PGProperty_GetDisplayedString(*args, **kwargs)

    def GetHintText(*args, **kwargs):
        """GetHintText(self) -> String"""
        return _propgrid.PGProperty_GetHintText(*args, **kwargs)

    def GetGrid(*args, **kwargs):
        """GetGrid(self) -> PropertyGrid"""
        return _propgrid.PGProperty_GetGrid(*args, **kwargs)

    def GetGridIfDisplayed(*args, **kwargs):
        """GetGridIfDisplayed(self) -> PropertyGrid"""
        return _propgrid.PGProperty_GetGridIfDisplayed(*args, **kwargs)

    def GetMainParent(*args, **kwargs):
        """GetMainParent(self) -> PGProperty"""
        return _propgrid.PGProperty_GetMainParent(*args, **kwargs)

    def GetParent(*args, **kwargs):
        """GetParent(self) -> PGProperty"""
        return _propgrid.PGProperty_GetParent(*args, **kwargs)

    def IsTextEditable(*args, **kwargs):
        """IsTextEditable(self) -> bool"""
        return _propgrid.PGProperty_IsTextEditable(*args, **kwargs)

    def IsValueUnspecified(*args, **kwargs):
        """IsValueUnspecified(self) -> bool"""
        return _propgrid.PGProperty_IsValueUnspecified(*args, **kwargs)

    def HasFlag(*args, **kwargs):
        """HasFlag(self, int flag) -> FlagType"""
        return _propgrid.PGProperty_HasFlag(*args, **kwargs)

    def GetAttributes(*args, **kwargs):
        """GetAttributes(self)"""
        return _propgrid.PGProperty_GetAttributes(*args, **kwargs)

    def GetAttributesAsList(*args, **kwargs):
        """GetAttributesAsList(self) -> wxVariant"""
        return _propgrid.PGProperty_GetAttributesAsList(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """GetFlags(self) -> FlagType"""
        return _propgrid.PGProperty_GetFlags(*args, **kwargs)

    def GetEditorClass(*args, **kwargs):
        """GetEditorClass(self) -> PGEditor"""
        return _propgrid.PGProperty_GetEditorClass(*args, **kwargs)

    def GetValueType(*args, **kwargs):
        """GetValueType(self) -> String"""
        return _propgrid.PGProperty_GetValueType(*args, **kwargs)

    def GetColumnEditor(*args, **kwargs):
        """GetColumnEditor(self, int column) -> PGEditor"""
        return _propgrid.PGProperty_GetColumnEditor(*args, **kwargs)

    def GetCommonValue(*args, **kwargs):
        """GetCommonValue(self) -> int"""
        return _propgrid.PGProperty_GetCommonValue(*args, **kwargs)

    def HasVisibleChildren(*args, **kwargs):
        """HasVisibleChildren(self) -> bool"""
        return _propgrid.PGProperty_HasVisibleChildren(*args, **kwargs)

    def InsertChild(*args, **kwargs):
        """InsertChild(self, int index, PGProperty childProperty) -> PGProperty"""
        return _propgrid.PGProperty_InsertChild(*args, **kwargs)

    def InsertChoice(*args, **kwargs):
        """InsertChoice(self, String label, int index, int value=INT_MAX) -> int"""
        return _propgrid.PGProperty_InsertChoice(*args, **kwargs)

    def IsCategory(*args, **kwargs):
        """IsCategory(self) -> bool"""
        return _propgrid.PGProperty_IsCategory(*args, **kwargs)

    def IsRoot(*args, **kwargs):
        """IsRoot(self) -> bool"""
        return _propgrid.PGProperty_IsRoot(*args, **kwargs)

    def IsSubProperty(*args, **kwargs):
        """IsSubProperty(self) -> bool"""
        return _propgrid.PGProperty_IsSubProperty(*args, **kwargs)

    def GetLastVisibleSubItem(*args, **kwargs):
        """GetLastVisibleSubItem(self) -> PGProperty"""
        return _propgrid.PGProperty_GetLastVisibleSubItem(*args, **kwargs)

    def GetDefaultValue(*args, **kwargs):
        """GetDefaultValue(self) -> wxVariant"""
        return _propgrid.PGProperty_GetDefaultValue(*args, **kwargs)

    def GetMaxLength(*args, **kwargs):
        """GetMaxLength(self) -> int"""
        return _propgrid.PGProperty_GetMaxLength(*args, **kwargs)

    def AreAllChildrenSpecified(*args, **kwargs):
        """AreAllChildrenSpecified(self, wxVariant pendingList=None) -> bool"""
        return _propgrid.PGProperty_AreAllChildrenSpecified(*args, **kwargs)

    def UpdateParentValues(*args, **kwargs):
        """UpdateParentValues(self) -> PGProperty"""
        return _propgrid.PGProperty_UpdateParentValues(*args, **kwargs)

    def UsesAutoUnspecified(*args, **kwargs):
        """UsesAutoUnspecified(self) -> bool"""
        return _propgrid.PGProperty_UsesAutoUnspecified(*args, **kwargs)

    def GetValueImage(*args, **kwargs):
        """GetValueImage(self) -> Bitmap"""
        return _propgrid.PGProperty_GetValueImage(*args, **kwargs)

    def GetAttribute(*args):
        """
        GetAttribute(self, String name) -> wxVariant
        GetAttribute(self, String name, String defVal) -> String
        """
        return _propgrid.PGProperty_GetAttribute(*args)

    def GetAttributeAsLong(*args, **kwargs):
        """GetAttributeAsLong(self, String name, long defVal) -> long"""
        return _propgrid.PGProperty_GetAttributeAsLong(*args, **kwargs)

    def GetAttributeAsDouble(*args, **kwargs):
        """GetAttributeAsDouble(self, String name, double defVal) -> double"""
        return _propgrid.PGProperty_GetAttributeAsDouble(*args, **kwargs)

    def GetDepth(*args, **kwargs):
        """GetDepth(self) -> int"""
        return _propgrid.PGProperty_GetDepth(*args, **kwargs)

    def GetFlagsAsString(*args, **kwargs):
        """GetFlagsAsString(self, FlagType flagsMask) -> String"""
        return _propgrid.PGProperty_GetFlagsAsString(*args, **kwargs)

    def GetIndexInParent(*args, **kwargs):
        """GetIndexInParent(self) -> int"""
        return _propgrid.PGProperty_GetIndexInParent(*args, **kwargs)

    def Hide(*args, **kwargs):
        """Hide(self, bool hide, int flags=PG_RECURSE) -> bool"""
        return _propgrid.PGProperty_Hide(*args, **kwargs)

    def IsExpanded(*args, **kwargs):
        """IsExpanded(self) -> bool"""
        return _propgrid.PGProperty_IsExpanded(*args, **kwargs)

    def IsVisible(*args, **kwargs):
        """IsVisible(self) -> bool"""
        return _propgrid.PGProperty_IsVisible(*args, **kwargs)

    def IsEnabled(*args, **kwargs):
        """IsEnabled(self) -> bool"""
        return _propgrid.PGProperty_IsEnabled(*args, **kwargs)

    def RecreateEditor(*args, **kwargs):
        """RecreateEditor(self) -> bool"""
        return _propgrid.PGProperty_RecreateEditor(*args, **kwargs)

    def RefreshEditor(*args, **kwargs):
        """RefreshEditor(self)"""
        return _propgrid.PGProperty_RefreshEditor(*args, **kwargs)

    def SetAttribute(*args, **kwargs):
        """SetAttribute(self, String name, wxVariant value)"""
        return _propgrid.PGProperty_SetAttribute(*args, **kwargs)

    def SetAttributes(*args, **kwargs):
        """SetAttributes(self,  attributes)"""
        return _propgrid.PGProperty_SetAttributes(*args, **kwargs)

    def SetAutoUnspecified(*args, **kwargs):
        """SetAutoUnspecified(self, bool enable=True)"""
        return _propgrid.PGProperty_SetAutoUnspecified(*args, **kwargs)

    def SetBackgroundColour(*args, **kwargs):
        """SetBackgroundColour(self, Colour colour, int flags=PG_RECURSE)"""
        return _propgrid.PGProperty_SetBackgroundColour(*args, **kwargs)

    def SetTextColour(*args, **kwargs):
        """SetTextColour(self, Colour colour, int flags=PG_RECURSE)"""
        return _propgrid.PGProperty_SetTextColour(*args, **kwargs)

    def SetDefaultValue(*args, **kwargs):
        """SetDefaultValue(self, wxVariant value)"""
        return _propgrid.PGProperty_SetDefaultValue(*args, **kwargs)

    def SetEditor(*args, **kwargs):
        """SetEditor(self, String editorName)"""
        return _propgrid.PGProperty_SetEditor(*args, **kwargs)

    def SetCell(*args, **kwargs):
        """SetCell(self, int column, PGCell cell)"""
        return _propgrid.PGProperty_SetCell(*args, **kwargs)

    def SetCommonValue(*args, **kwargs):
        """SetCommonValue(self, int commonValue)"""
        return _propgrid.PGProperty_SetCommonValue(*args, **kwargs)

    def SetFlagsFromString(*args, **kwargs):
        """SetFlagsFromString(self, String str)"""
        return _propgrid.PGProperty_SetFlagsFromString(*args, **kwargs)

    def SetModifiedStatus(*args, **kwargs):
        """SetModifiedStatus(self, bool modified)"""
        return _propgrid.PGProperty_SetModifiedStatus(*args, **kwargs)

    def SetValueInEvent(*args, **kwargs):
        """SetValueInEvent(self, wxVariant value)"""
        return _propgrid.PGProperty_SetValueInEvent(*args, **kwargs)

    def SetValue(*args, **kwargs):
        """SetValue(self, wxVariant value, wxVariant pList=None, int flags=PG_SETVAL_REFRESH_EDITOR)"""
        return _propgrid.PGProperty_SetValue(*args, **kwargs)

    def SetValueImage(*args, **kwargs):
        """SetValueImage(self, Bitmap bmp)"""
        return _propgrid.PGProperty_SetValueImage(*args, **kwargs)

    def SetChoiceSelection(*args, **kwargs):
        """SetChoiceSelection(self, int newValue)"""
        return _propgrid.PGProperty_SetChoiceSelection(*args, **kwargs)

    def SetExpanded(*args, **kwargs):
        """SetExpanded(self, bool expanded)"""
        return _propgrid.PGProperty_SetExpanded(*args, **kwargs)

    def ChangeFlag(*args, **kwargs):
        """ChangeFlag(self, int flag, bool set)"""
        return _propgrid.PGProperty_ChangeFlag(*args, **kwargs)

    def SetFlagRecursively(*args, **kwargs):
        """SetFlagRecursively(self, int flag, bool set)"""
        return _propgrid.PGProperty_SetFlagRecursively(*args, **kwargs)

    def SetHelpString(*args, **kwargs):
        """SetHelpString(self, String helpString)"""
        return _propgrid.PGProperty_SetHelpString(*args, **kwargs)

    def SetLabel(*args, **kwargs):
        """SetLabel(self, String label)"""
        return _propgrid.PGProperty_SetLabel(*args, **kwargs)

    def SetName(*args, **kwargs):
        """SetName(self, String newName)"""
        return _propgrid.PGProperty_SetName(*args, **kwargs)

    def SetParentalType(*args, **kwargs):
        """SetParentalType(self, int flag)"""
        return _propgrid.PGProperty_SetParentalType(*args, **kwargs)

    def SetValueToUnspecified(*args, **kwargs):
        """SetValueToUnspecified(self)"""
        return _propgrid.PGProperty_SetValueToUnspecified(*args, **kwargs)

    def SetValuePlain(*args, **kwargs):
        """SetValuePlain(self, wxVariant value)"""
        return _propgrid.PGProperty_SetValuePlain(*args, **kwargs)

    def SetValidator(*args, **kwargs):
        """SetValidator(self, Validator validator)"""
        return _propgrid.PGProperty_SetValidator(*args, **kwargs)

    def GetValidator(*args, **kwargs):
        """GetValidator(self) -> Validator"""
        return _propgrid.PGProperty_GetValidator(*args, **kwargs)

    def SetMaxLength(*args, **kwargs):
        """SetMaxLength(self, int maxLen) -> bool"""
        return _propgrid.PGProperty_SetMaxLength(*args, **kwargs)

    def SetWasModified(*args, **kwargs):
        """SetWasModified(self, bool set=True)"""
        return _propgrid.PGProperty_SetWasModified(*args, **kwargs)

    def GetHelpString(*args, **kwargs):
        """GetHelpString(self) -> String"""
        return _propgrid.PGProperty_GetHelpString(*args, **kwargs)

    def IsSomeParent(*args, **kwargs):
        """IsSomeParent(self, PGProperty candidate_parent) -> bool"""
        return _propgrid.PGProperty_IsSomeParent(*args, **kwargs)

    def AdaptListToValue(*args, **kwargs):
        """AdaptListToValue(self, wxVariant list, wxVariant value)"""
        return _propgrid.PGProperty_AdaptListToValue(*args, **kwargs)

    def AddPrivateChild(*args, **kwargs):
        """AddPrivateChild(self, PGProperty prop)"""
        return _propgrid.PGProperty_AddPrivateChild(*args, **kwargs)

    def AppendChild(*args, **kwargs):
        """AppendChild(self, PGProperty prop) -> PGProperty"""
        return _propgrid.PGProperty_AppendChild(*args, **kwargs)

    def GetChildrenHeight(*args, **kwargs):
        """GetChildrenHeight(self, int lh, int iMax=-1) -> int"""
        return _propgrid.PGProperty_GetChildrenHeight(*args, **kwargs)

    def GetChildCount(*args, **kwargs):
        """GetChildCount(self) -> int"""
        return _propgrid.PGProperty_GetChildCount(*args, **kwargs)

    def Item(*args, **kwargs):
        """Item(self, int i) -> PGProperty"""
        return _propgrid.PGProperty_Item(*args, **kwargs)

    def Last(*args, **kwargs):
        """Last(self) -> PGProperty"""
        return _propgrid.PGProperty_Last(*args, **kwargs)

    def Index(*args, **kwargs):
        """Index(self, PGProperty p) -> int"""
        return _propgrid.PGProperty_Index(*args, **kwargs)

    def FixIndicesOfChildren(*args, **kwargs):
        """FixIndicesOfChildren(self, int starthere=0)"""
        return _propgrid.PGProperty_FixIndicesOfChildren(*args, **kwargs)

    def GetImageOffset(*args, **kwargs):
        """GetImageOffset(self, int imageWidth) -> int"""
        return _propgrid.PGProperty_GetImageOffset(*args, **kwargs)

    def GetItemAtY(*args, **kwargs):
        """GetItemAtY(self, int y) -> PGProperty"""
        return _propgrid.PGProperty_GetItemAtY(*args, **kwargs)

    def GetPropertyByName(*args, **kwargs):
        """GetPropertyByName(self, String name) -> PGProperty"""
        return _propgrid.PGProperty_GetPropertyByName(*args, **kwargs)

    def SetPyChoices(*args):
        """
        SetPyChoices(self, PGChoices chs) -> bool
        SetPyChoices(self, wxArrayString labels, wxArrayInt values=wxArrayInt()) -> bool
        """
        return _propgrid.PGProperty_SetPyChoices(*args)

    def PyBase_StringToValue(*args, **kwargs):
        """PyBase_StringToValue(self, String text, int argFlags=0) -> wxPGVariantAndBool"""
        return _propgrid.PGProperty_PyBase_StringToValue(*args, **kwargs)

    def PyBase_IntToValue(*args, **kwargs):
        """PyBase_IntToValue(self, wxVariant value, int number, int argFlags=0) -> wxPGVariantAndBool"""
        return _propgrid.PGProperty_PyBase_IntToValue(*args, **kwargs)

    m_value = property(GetValuePlain,SetValuePlain) 
    def GetPyClientData(*args, **kwargs):
        """
        GetPyClientData(self) -> PyObject

        Returns the client data object for a property
        """
        return _propgrid.PGProperty_GetPyClientData(*args, **kwargs)

    def SetPyClientData(*args, **kwargs):
        """
        SetPyClientData(self, PyObject clientData)

        Associate the given client data.
        """
        return _propgrid.PGProperty_SetPyClientData(*args, **kwargs)

    SetChoices = SetPyChoices
    StringToValue = PyBase_StringToValue
    IntToValue = PyBase_IntToValue
    GetClientObject = GetPyClientData
    SetClientObject = SetPyClientData
    GetClientData = GetPyClientData
    SetClientData = SetPyClientData

_propgrid.PGProperty_swigregister(PGProperty)

class PropertyGridHitTestResult(object):
    """Proxy of C++ PropertyGridHitTestResult class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PropertyGridHitTestResult"""
        _propgrid.PropertyGridHitTestResult_swiginit(self,_propgrid.new_PropertyGridHitTestResult(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PropertyGridHitTestResult
    __del__ = lambda self : None;
    def GetColumn(*args, **kwargs):
        """GetColumn(self) -> int"""
        return _propgrid.PropertyGridHitTestResult_GetColumn(*args, **kwargs)

    def GetProperty(*args, **kwargs):
        """GetProperty(self) -> PGProperty"""
        return _propgrid.PropertyGridHitTestResult_GetProperty(*args, **kwargs)

    def GetSplitter(*args, **kwargs):
        """GetSplitter(self) -> int"""
        return _propgrid.PropertyGridHitTestResult_GetSplitter(*args, **kwargs)

    def GetSplitterHitOffset(*args, **kwargs):
        """GetSplitterHitOffset(self) -> int"""
        return _propgrid.PropertyGridHitTestResult_GetSplitterHitOffset(*args, **kwargs)

_propgrid.PropertyGridHitTestResult_swigregister(PropertyGridHitTestResult)

PG_ITERATE_PROPERTIES = _propgrid.PG_ITERATE_PROPERTIES
PG_ITERATE_HIDDEN = _propgrid.PG_ITERATE_HIDDEN
PG_ITERATE_FIXED_CHILDREN = _propgrid.PG_ITERATE_FIXED_CHILDREN
PG_ITERATE_CATEGORIES = _propgrid.PG_ITERATE_CATEGORIES
PG_ITERATE_ALL_PARENTS = _propgrid.PG_ITERATE_ALL_PARENTS
PG_ITERATE_ALL_PARENTS_RECURSIVELY = _propgrid.PG_ITERATE_ALL_PARENTS_RECURSIVELY
PG_ITERATOR_FLAGS_ALL = _propgrid.PG_ITERATOR_FLAGS_ALL
PG_ITERATOR_MASK_OP_ITEM = _propgrid.PG_ITERATOR_MASK_OP_ITEM
PG_ITERATOR_MASK_OP_PARENT = _propgrid.PG_ITERATOR_MASK_OP_PARENT
PG_ITERATE_VISIBLE = _propgrid.PG_ITERATE_VISIBLE
PG_ITERATE_ALL = _propgrid.PG_ITERATE_ALL
PG_ITERATE_NORMAL = _propgrid.PG_ITERATE_NORMAL
PG_ITERATE_DEFAULT = _propgrid.PG_ITERATE_DEFAULT
class PropertyGridIteratorBase(object):
    """Proxy of C++ PropertyGridIteratorBase class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PropertyGridIteratorBase"""
        _propgrid.PropertyGridIteratorBase_swiginit(self,_propgrid.new_PropertyGridIteratorBase(*args, **kwargs))
    def Assign(*args, **kwargs):
        """Assign(self, PropertyGridIteratorBase it)"""
        return _propgrid.PropertyGridIteratorBase_Assign(*args, **kwargs)

    def AtEnd(*args, **kwargs):
        """AtEnd(self) -> bool"""
        return _propgrid.PropertyGridIteratorBase_AtEnd(*args, **kwargs)

    def GetProperty(*args, **kwargs):
        """GetProperty(self) -> PGProperty"""
        return _propgrid.PropertyGridIteratorBase_GetProperty(*args, **kwargs)

    def Init(*args):
        """
        Init(self,  state, int flags, PGProperty property, int dir=1)
        Init(self,  state, int flags, int startPos=TOP, int dir=0)
        """
        return _propgrid.PropertyGridIteratorBase_Init(*args)

    def Next(*args, **kwargs):
        """Next(self, bool iterateChildren=True)"""
        return _propgrid.PropertyGridIteratorBase_Next(*args, **kwargs)

    def Prev(*args, **kwargs):
        """Prev(self)"""
        return _propgrid.PropertyGridIteratorBase_Prev(*args, **kwargs)

    def SetBaseParent(*args, **kwargs):
        """SetBaseParent(self, PGProperty baseParent)"""
        return _propgrid.PropertyGridIteratorBase_SetBaseParent(*args, **kwargs)

_propgrid.PropertyGridIteratorBase_swigregister(PropertyGridIteratorBase)

class PropertyGridIterator(PropertyGridIteratorBase):
    """Proxy of C++ PropertyGridIterator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self,  state, int flags=PG_ITERATE_DEFAULT, PGProperty property=None, 
            int dir=1) -> PropertyGridIterator
        __init__(self,  state, int flags, int startPos, int dir=0) -> PropertyGridIterator
        __init__(self) -> PropertyGridIterator
        __init__(self, PropertyGridIterator it) -> PropertyGridIterator
        """
        _propgrid.PropertyGridIterator_swiginit(self,_propgrid.new_PropertyGridIterator(*args))
    __swig_destroy__ = _propgrid.delete_PropertyGridIterator
    __del__ = lambda self : None;
    def __ref__(*args, **kwargs):
        """__ref__(self) -> PGProperty"""
        return _propgrid.PropertyGridIterator___ref__(*args, **kwargs)

    def OneStep(*args, **kwargs):
        """
        OneStep( state, int flags=PG_ITERATE_DEFAULT, PGProperty property=None, 
            int dir=1) -> PGProperty
        """
        return _propgrid.PropertyGridIterator_OneStep(*args, **kwargs)

    OneStep = staticmethod(OneStep)
_propgrid.PropertyGridIterator_swigregister(PropertyGridIterator)

def PropertyGridIterator_OneStep(*args, **kwargs):
  """
    PropertyGridIterator_OneStep( state, int flags=PG_ITERATE_DEFAULT, PGProperty property=None, 
        int dir=1) -> PGProperty
    """
  return _propgrid.PropertyGridIterator_OneStep(*args, **kwargs)

class PropertyGridConstIterator(PropertyGridIteratorBase):
    """Proxy of C++ PropertyGridConstIterator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_PropertyGridConstIterator
    __del__ = lambda self : None;
    def __ref__(*args, **kwargs):
        """__ref__(self) -> PGProperty"""
        return _propgrid.PropertyGridConstIterator___ref__(*args, **kwargs)

    def OneStep(*args, **kwargs):
        """
        OneStep( state, int flags=PG_ITERATE_DEFAULT, PGProperty property=None, 
            int dir=1) -> PGProperty
        """
        return _propgrid.PropertyGridConstIterator_OneStep(*args, **kwargs)

    OneStep = staticmethod(OneStep)
    def __init__(self, *args): 
        """
        __init__(self,  state, int flags=PG_ITERATE_DEFAULT, PGProperty property=None, 
            int dir=1) -> PropertyGridConstIterator
        __init__(self,  state, int flags, int startPos, int dir=0) -> PropertyGridConstIterator
        __init__(self) -> PropertyGridConstIterator
        __init__(self, PropertyGridConstIterator it) -> PropertyGridConstIterator
        __init__(self, PropertyGridIterator other) -> PropertyGridConstIterator
        """
        _propgrid.PropertyGridConstIterator_swiginit(self,_propgrid.new_PropertyGridConstIterator(*args))
_propgrid.PropertyGridConstIterator_swigregister(PropertyGridConstIterator)

def PropertyGridConstIterator_OneStep(*args, **kwargs):
  """
    PropertyGridConstIterator_OneStep( state, int flags=PG_ITERATE_DEFAULT, PGProperty property=None, 
        int dir=1) -> PGProperty
    """
  return _propgrid.PropertyGridConstIterator_OneStep(*args, **kwargs)

class PGVIteratorBase(_core.RefCounter):
    """Proxy of C++ PGVIteratorBase class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def Next(*args, **kwargs):
        """Next(self)"""
        return _propgrid.PGVIteratorBase_Next(*args, **kwargs)

_propgrid.PGVIteratorBase_swigregister(PGVIteratorBase)

class PGVIterator(object):
    """Proxy of C++ PGVIterator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_PGVIterator
    __del__ = lambda self : None;
    def UnRef(*args, **kwargs):
        """UnRef(self)"""
        return _propgrid.PGVIterator_UnRef(*args, **kwargs)

    def __init__(self, *args): 
        """
        __init__(self) -> PGVIterator
        __init__(self, PGVIteratorBase obj) -> PGVIterator
        __init__(self, PGVIterator it) -> PGVIterator
        """
        _propgrid.PGVIterator_swiginit(self,_propgrid.new_PGVIterator(*args))
    def Next(*args, **kwargs):
        """Next(self)"""
        return _propgrid.PGVIterator_Next(*args, **kwargs)

    def AtEnd(*args, **kwargs):
        """AtEnd(self) -> bool"""
        return _propgrid.PGVIterator_AtEnd(*args, **kwargs)

    def GetProperty(*args, **kwargs):
        """GetProperty(self) -> PGProperty"""
        return _propgrid.PGVIterator_GetProperty(*args, **kwargs)

_propgrid.PGVIterator_swigregister(PGVIterator)


def PGTypeOperationFailed(*args, **kwargs):
  """PGTypeOperationFailed(PGProperty p, String typestr, String op)"""
  return _propgrid.PGTypeOperationFailed(*args, **kwargs)

def PGGetFailed(*args, **kwargs):
  """PGGetFailed(PGProperty p, String typestr)"""
  return _propgrid.PGGetFailed(*args, **kwargs)
class PropertyGridInterface(object):
    """Proxy of C++ PropertyGridInterface class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_PropertyGridInterface
    __del__ = lambda self : None;
    def Append(*args, **kwargs):
        """Append(self, PGProperty property) -> PGProperty"""
        return _propgrid.PropertyGridInterface_Append(*args, **kwargs)

    def AppendIn(*args, **kwargs):
        """AppendIn(self, PGPropArg id, PGProperty newproperty) -> PGProperty"""
        return _propgrid.PropertyGridInterface_AppendIn(*args, **kwargs)

    def BeginAddChildren(*args, **kwargs):
        """BeginAddChildren(self, PGPropArg id)"""
        return _propgrid.PropertyGridInterface_BeginAddChildren(*args, **kwargs)

    def Clear(*args, **kwargs):
        """Clear(self)"""
        return _propgrid.PropertyGridInterface_Clear(*args, **kwargs)

    def ClearSelection(*args, **kwargs):
        """ClearSelection(self, bool validation=False) -> bool"""
        return _propgrid.PropertyGridInterface_ClearSelection(*args, **kwargs)

    def ClearModifiedStatus(*args, **kwargs):
        """ClearModifiedStatus(self)"""
        return _propgrid.PropertyGridInterface_ClearModifiedStatus(*args, **kwargs)

    def Collapse(*args, **kwargs):
        """Collapse(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_Collapse(*args, **kwargs)

    def CollapseAll(*args, **kwargs):
        """CollapseAll(self) -> bool"""
        return _propgrid.PropertyGridInterface_CollapseAll(*args, **kwargs)

    def ChangePropertyValue(*args, **kwargs):
        """ChangePropertyValue(self, PGPropArg id, wxVariant newValue) -> bool"""
        return _propgrid.PropertyGridInterface_ChangePropertyValue(*args, **kwargs)

    def DeleteProperty(*args, **kwargs):
        """DeleteProperty(self, PGPropArg id)"""
        return _propgrid.PropertyGridInterface_DeleteProperty(*args, **kwargs)

    def RemoveProperty(*args, **kwargs):
        """RemoveProperty(self, PGPropArg id) -> PGProperty"""
        return _propgrid.PropertyGridInterface_RemoveProperty(*args, **kwargs)

    def DisableProperty(*args, **kwargs):
        """DisableProperty(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_DisableProperty(*args, **kwargs)

    def EditorValidate(*args, **kwargs):
        """EditorValidate(self) -> bool"""
        return _propgrid.PropertyGridInterface_EditorValidate(*args, **kwargs)

    def EnableProperty(*args, **kwargs):
        """EnableProperty(self, PGPropArg id, bool enable=True) -> bool"""
        return _propgrid.PropertyGridInterface_EnableProperty(*args, **kwargs)

    def EndAddChildren(*args, **kwargs):
        """EndAddChildren(self, PGPropArg id)"""
        return _propgrid.PropertyGridInterface_EndAddChildren(*args, **kwargs)

    def Expand(*args, **kwargs):
        """Expand(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_Expand(*args, **kwargs)

    def ExpandAll(*args, **kwargs):
        """ExpandAll(self, bool expand=True) -> bool"""
        return _propgrid.PropertyGridInterface_ExpandAll(*args, **kwargs)

    def GetFirstChild(*args, **kwargs):
        """GetFirstChild(self, PGPropArg id) -> PGProperty"""
        return _propgrid.PropertyGridInterface_GetFirstChild(*args, **kwargs)

    def GetIterator(*args):
        """
        GetIterator(self, int flags=PG_ITERATE_DEFAULT, PGProperty firstProp=None) -> PropertyGridIterator
        GetIterator(self, int flags=PG_ITERATE_DEFAULT, PGProperty firstProp=None) -> PropertyGridConstIterator
        GetIterator(self, int flags, int startPos) -> PropertyGridIterator
        GetIterator(self, int flags, int startPos) -> PropertyGridConstIterator
        """
        return _propgrid.PropertyGridInterface_GetIterator(*args)

    def GetFirst(*args):
        """
        GetFirst(self, int flags=PG_ITERATE_ALL) -> PGProperty
        GetFirst(self, int flags=PG_ITERATE_ALL) -> PGProperty
        """
        return _propgrid.PropertyGridInterface_GetFirst(*args)

    def GetProperty(*args, **kwargs):
        """GetProperty(self, String name) -> PGProperty"""
        return _propgrid.PropertyGridInterface_GetProperty(*args, **kwargs)

    def GetPropertyAttributes(*args, **kwargs):
        """GetPropertyAttributes(self, PGPropArg id)"""
        return _propgrid.PropertyGridInterface_GetPropertyAttributes(*args, **kwargs)

    def GetPropertiesWithFlag(*args, **kwargs):
        """
        GetPropertiesWithFlag(self, wxArrayPGProperty targetArr, FlagType flags, bool inverse=False, 
            int iterFlags=wxPG_ITERATE_PROPERTIES|wxPG_ITERATE_HIDDEN|wxPG_ITERATE_CATEGORIES)
        """
        return _propgrid.PropertyGridInterface_GetPropertiesWithFlag(*args, **kwargs)

    def GetPropertyAttribute(*args, **kwargs):
        """GetPropertyAttribute(self, PGPropArg id, String attrName) -> wxVariant"""
        return _propgrid.PropertyGridInterface_GetPropertyAttribute(*args, **kwargs)

    def GetPropertyCategory(*args, **kwargs):
        """GetPropertyCategory(self, PGPropArg id)"""
        return _propgrid.PropertyGridInterface_GetPropertyCategory(*args, **kwargs)

    def GetPropertyByLabel(*args, **kwargs):
        """GetPropertyByLabel(self, String label) -> PGProperty"""
        return _propgrid.PropertyGridInterface_GetPropertyByLabel(*args, **kwargs)

    def GetPropertyByName(*args):
        """
        GetPropertyByName(self, String name) -> PGProperty
        GetPropertyByName(self, String name, String subname) -> PGProperty
        """
        return _propgrid.PropertyGridInterface_GetPropertyByName(*args)

    def GetPropertyEditor(*args, **kwargs):
        """GetPropertyEditor(self, PGPropArg id) -> PGEditor"""
        return _propgrid.PropertyGridInterface_GetPropertyEditor(*args, **kwargs)

    def GetPropertyHelpString(*args, **kwargs):
        """GetPropertyHelpString(self, PGPropArg id) -> String"""
        return _propgrid.PropertyGridInterface_GetPropertyHelpString(*args, **kwargs)

    def GetPropertyImage(*args, **kwargs):
        """GetPropertyImage(self, PGPropArg id) -> Bitmap"""
        return _propgrid.PropertyGridInterface_GetPropertyImage(*args, **kwargs)

    def GetPropertyLabel(*args, **kwargs):
        """GetPropertyLabel(self, PGPropArg id) -> String"""
        return _propgrid.PropertyGridInterface_GetPropertyLabel(*args, **kwargs)

    def GetPropertyName(*args, **kwargs):
        """GetPropertyName(self, PGProperty property) -> String"""
        return _propgrid.PropertyGridInterface_GetPropertyName(*args, **kwargs)

    def GetPropertyParent(*args, **kwargs):
        """GetPropertyParent(self, PGPropArg id) -> PGProperty"""
        return _propgrid.PropertyGridInterface_GetPropertyParent(*args, **kwargs)

    def GetPropertyValidator(*args, **kwargs):
        """GetPropertyValidator(self, PGPropArg id) -> Validator"""
        return _propgrid.PropertyGridInterface_GetPropertyValidator(*args, **kwargs)

    def GetPropertyValue(*args, **kwargs):
        """GetPropertyValue(self, PGPropArg id) -> wxVariant"""
        return _propgrid.PropertyGridInterface_GetPropertyValue(*args, **kwargs)

    def GetPropertyValueAsString(*args, **kwargs):
        """GetPropertyValueAsString(self, PGPropArg id) -> String"""
        return _propgrid.PropertyGridInterface_GetPropertyValueAsString(*args, **kwargs)

    def GetPropertyValueAsLong(*args, **kwargs):
        """GetPropertyValueAsLong(self, PGPropArg id) -> long"""
        return _propgrid.PropertyGridInterface_GetPropertyValueAsLong(*args, **kwargs)

    def GetPropertyValueAsULong(*args, **kwargs):
        """GetPropertyValueAsULong(self, PGPropArg id) -> long"""
        return _propgrid.PropertyGridInterface_GetPropertyValueAsULong(*args, **kwargs)

    def GetPropertyValueAsBool(*args, **kwargs):
        """GetPropertyValueAsBool(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_GetPropertyValueAsBool(*args, **kwargs)

    def GetPropertyValueAsDouble(*args, **kwargs):
        """GetPropertyValueAsDouble(self, PGPropArg id) -> double"""
        return _propgrid.PropertyGridInterface_GetPropertyValueAsDouble(*args, **kwargs)

    def GetPropertyValueAsArrayString(*args, **kwargs):
        """GetPropertyValueAsArrayString(self, PGPropArg id) -> wxArrayString"""
        return _propgrid.PropertyGridInterface_GetPropertyValueAsArrayString(*args, **kwargs)

    def GetPropertyValueAsArrayInt(*args, **kwargs):
        """GetPropertyValueAsArrayInt(self, PGPropArg id) -> wxArrayInt"""
        return _propgrid.PropertyGridInterface_GetPropertyValueAsArrayInt(*args, **kwargs)

    def GetSelection(*args, **kwargs):
        """GetSelection(self) -> PGProperty"""
        return _propgrid.PropertyGridInterface_GetSelection(*args, **kwargs)

    def GetSelectedProperties(*args, **kwargs):
        """GetSelectedProperties(self) -> wxArrayPGProperty"""
        return _propgrid.PropertyGridInterface_GetSelectedProperties(*args, **kwargs)

    def GetVIterator(*args, **kwargs):
        """GetVIterator(self, int flags) -> PGVIterator"""
        return _propgrid.PropertyGridInterface_GetVIterator(*args, **kwargs)

    def HideProperty(*args, **kwargs):
        """HideProperty(self, PGPropArg id, bool hide=True, int flags=PG_RECURSE) -> bool"""
        return _propgrid.PropertyGridInterface_HideProperty(*args, **kwargs)

    def InitAllTypeHandlers(*args, **kwargs):
        """InitAllTypeHandlers()"""
        return _propgrid.PropertyGridInterface_InitAllTypeHandlers(*args, **kwargs)

    InitAllTypeHandlers = staticmethod(InitAllTypeHandlers)
    def Insert(*args):
        """
        Insert(self, PGPropArg priorThis, PGProperty newproperty) -> PGProperty
        Insert(self, PGPropArg parent, int index, PGProperty newproperty) -> PGProperty
        """
        return _propgrid.PropertyGridInterface_Insert(*args)

    def IsPropertyCategory(*args, **kwargs):
        """IsPropertyCategory(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_IsPropertyCategory(*args, **kwargs)

    def IsPropertyEnabled(*args, **kwargs):
        """IsPropertyEnabled(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_IsPropertyEnabled(*args, **kwargs)

    def IsPropertyExpanded(*args, **kwargs):
        """IsPropertyExpanded(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_IsPropertyExpanded(*args, **kwargs)

    def IsPropertyModified(*args, **kwargs):
        """IsPropertyModified(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_IsPropertyModified(*args, **kwargs)

    def IsPropertySelected(*args, **kwargs):
        """IsPropertySelected(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_IsPropertySelected(*args, **kwargs)

    def IsPropertyShown(*args, **kwargs):
        """IsPropertyShown(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_IsPropertyShown(*args, **kwargs)

    def IsPropertyValueUnspecified(*args, **kwargs):
        """IsPropertyValueUnspecified(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridInterface_IsPropertyValueUnspecified(*args, **kwargs)

    def LimitPropertyEditing(*args, **kwargs):
        """LimitPropertyEditing(self, PGPropArg id, bool limit=True)"""
        return _propgrid.PropertyGridInterface_LimitPropertyEditing(*args, **kwargs)

    def RefreshGrid(*args, **kwargs):
        """RefreshGrid(self,  state=None)"""
        return _propgrid.PropertyGridInterface_RefreshGrid(*args, **kwargs)

    def RegisterAdditionalEditors(*args, **kwargs):
        """RegisterAdditionalEditors()"""
        return _propgrid.PropertyGridInterface_RegisterAdditionalEditors(*args, **kwargs)

    RegisterAdditionalEditors = staticmethod(RegisterAdditionalEditors)
    def ReplaceProperty(*args, **kwargs):
        """ReplaceProperty(self, PGPropArg id, PGProperty property) -> PGProperty"""
        return _propgrid.PropertyGridInterface_ReplaceProperty(*args, **kwargs)

    SelectionState = _propgrid.PropertyGridInterface_SelectionState
    ExpandedState = _propgrid.PropertyGridInterface_ExpandedState
    ScrollPosState = _propgrid.PropertyGridInterface_ScrollPosState
    PageState = _propgrid.PropertyGridInterface_PageState
    SplitterPosState = _propgrid.PropertyGridInterface_SplitterPosState
    DescBoxState = _propgrid.PropertyGridInterface_DescBoxState
    AllStates = _propgrid.PropertyGridInterface_AllStates
    def RestoreEditableState(*args, **kwargs):
        """RestoreEditableState(self, String src, int restoreStates=AllStates) -> bool"""
        return _propgrid.PropertyGridInterface_RestoreEditableState(*args, **kwargs)

    def SaveEditableState(*args, **kwargs):
        """SaveEditableState(self, int includedStates=AllStates) -> String"""
        return _propgrid.PropertyGridInterface_SaveEditableState(*args, **kwargs)

    def SetBoolChoices(*args, **kwargs):
        """SetBoolChoices(String trueChoice, String falseChoice)"""
        return _propgrid.PropertyGridInterface_SetBoolChoices(*args, **kwargs)

    SetBoolChoices = staticmethod(SetBoolChoices)
    def SetColumnProportion(*args, **kwargs):
        """SetColumnProportion(self, int column, int proportion) -> bool"""
        return _propgrid.PropertyGridInterface_SetColumnProportion(*args, **kwargs)

    def GetColumnProportion(*args, **kwargs):
        """GetColumnProportion(self, int column) -> int"""
        return _propgrid.PropertyGridInterface_GetColumnProportion(*args, **kwargs)

    def SetPropertyAttribute(*args, **kwargs):
        """SetPropertyAttribute(self, PGPropArg id, String attrName, wxVariant value, long argFlags=0)"""
        return _propgrid.PropertyGridInterface_SetPropertyAttribute(*args, **kwargs)

    def SetPropertyAttributeAll(*args, **kwargs):
        """SetPropertyAttributeAll(self, String attrName, wxVariant value)"""
        return _propgrid.PropertyGridInterface_SetPropertyAttributeAll(*args, **kwargs)

    def SetPropertyBackgroundColour(*args, **kwargs):
        """SetPropertyBackgroundColour(self, PGPropArg id, Colour colour, int flags=PG_RECURSE)"""
        return _propgrid.PropertyGridInterface_SetPropertyBackgroundColour(*args, **kwargs)

    def SetPropertyColoursToDefault(*args, **kwargs):
        """SetPropertyColoursToDefault(self, PGPropArg id)"""
        return _propgrid.PropertyGridInterface_SetPropertyColoursToDefault(*args, **kwargs)

    def SetPropertyTextColour(*args, **kwargs):
        """SetPropertyTextColour(self, PGPropArg id, Colour col, int flags=PG_RECURSE)"""
        return _propgrid.PropertyGridInterface_SetPropertyTextColour(*args, **kwargs)

    def GetPropertyBackgroundColour(*args, **kwargs):
        """GetPropertyBackgroundColour(self, PGPropArg id) -> Colour"""
        return _propgrid.PropertyGridInterface_GetPropertyBackgroundColour(*args, **kwargs)

    def GetPropertyTextColour(*args, **kwargs):
        """GetPropertyTextColour(self, PGPropArg id) -> Colour"""
        return _propgrid.PropertyGridInterface_GetPropertyTextColour(*args, **kwargs)

    def SetPropertyCell(*args, **kwargs):
        """
        SetPropertyCell(self, PGPropArg id, int column, String text=wxEmptyString, 
            Bitmap bitmap=wxNullBitmap, Colour fgCol=wxNullColour, 
            Colour bgCol=wxNullColour)
        """
        return _propgrid.PropertyGridInterface_SetPropertyCell(*args, **kwargs)

    def SetPropertyEditor(*args, **kwargs):
        """SetPropertyEditor(self, PGPropArg id, String editorName)"""
        return _propgrid.PropertyGridInterface_SetPropertyEditor(*args, **kwargs)

    def SetPropertyLabel(*args, **kwargs):
        """SetPropertyLabel(self, PGPropArg id, String newproplabel)"""
        return _propgrid.PropertyGridInterface_SetPropertyLabel(*args, **kwargs)

    def SetPropertyName(*args, **kwargs):
        """SetPropertyName(self, PGPropArg id, String newName)"""
        return _propgrid.PropertyGridInterface_SetPropertyName(*args, **kwargs)

    def SetPropertyReadOnly(*args, **kwargs):
        """SetPropertyReadOnly(self, PGPropArg id, bool set=True, int flags=PG_RECURSE)"""
        return _propgrid.PropertyGridInterface_SetPropertyReadOnly(*args, **kwargs)

    def SetPropertyValueUnspecified(*args, **kwargs):
        """SetPropertyValueUnspecified(self, PGPropArg id)"""
        return _propgrid.PropertyGridInterface_SetPropertyValueUnspecified(*args, **kwargs)

    def SetPropertyHelpString(*args, **kwargs):
        """SetPropertyHelpString(self, PGPropArg id, String helpString)"""
        return _propgrid.PropertyGridInterface_SetPropertyHelpString(*args, **kwargs)

    def SetPropertyImage(*args, **kwargs):
        """SetPropertyImage(self, PGPropArg id, Bitmap bmp)"""
        return _propgrid.PropertyGridInterface_SetPropertyImage(*args, **kwargs)

    def SetPropertyMaxLength(*args, **kwargs):
        """SetPropertyMaxLength(self, PGPropArg id, int maxLen) -> bool"""
        return _propgrid.PropertyGridInterface_SetPropertyMaxLength(*args, **kwargs)

    def SetPropertyValidator(*args, **kwargs):
        """SetPropertyValidator(self, PGPropArg id, Validator validator)"""
        return _propgrid.PropertyGridInterface_SetPropertyValidator(*args, **kwargs)

    def SetPropertyValueString(*args, **kwargs):
        """SetPropertyValueString(self, PGPropArg id, String value)"""
        return _propgrid.PropertyGridInterface_SetPropertyValueString(*args, **kwargs)

    def SetPropertyValue(*args, **kwargs):
        """SetPropertyValue(self, PGPropArg id, wxVariant value)"""
        return _propgrid.PropertyGridInterface_SetPropertyValue(*args, **kwargs)

    def SetValidationFailureBehavior(*args, **kwargs):
        """SetValidationFailureBehavior(self, int vfbFlags)"""
        return _propgrid.PropertyGridInterface_SetValidationFailureBehavior(*args, **kwargs)

    def Sort(*args, **kwargs):
        """Sort(self, int flags=0)"""
        return _propgrid.PropertyGridInterface_Sort(*args, **kwargs)

    def SortChildren(*args, **kwargs):
        """SortChildren(self, PGPropArg id, int flags=0)"""
        return _propgrid.PropertyGridInterface_SortChildren(*args, **kwargs)

    def GetPropertyByNameA(*args, **kwargs):
        """GetPropertyByNameA(self, String name) -> PGProperty"""
        return _propgrid.PropertyGridInterface_GetPropertyByNameA(*args, **kwargs)

    def GetEditorByName(*args, **kwargs):
        """GetEditorByName(String editorName) -> PGEditor"""
        return _propgrid.PropertyGridInterface_GetEditorByName(*args, **kwargs)

    GetEditorByName = staticmethod(GetEditorByName)
    def RefreshProperty(*args, **kwargs):
        """RefreshProperty(self, PGProperty p)"""
        return _propgrid.PropertyGridInterface_RefreshProperty(*args, **kwargs)

    def MapType(class_,factory):
        "Registers Python type/class to property mapping.\n\nfactory: "
        "Property builder function/class."
        global _type2property
        try:
            mappings = _type2property
        except NameError:
            raise AssertionError("call only after a propertygrid or "
                                 "manager instance constructed")

        mappings[class_] = factory


    def DoDefaultTypeMappings(self):
        "Map built-in properties."
        global _type2property
        try:
            mappings = _type2property

            return
        except NameError:
            mappings = {}
            _type2property = mappings

        mappings[str] = StringProperty
        mappings[unicode] = StringProperty
        mappings[int] = IntProperty
        mappings[float] = FloatProperty
        mappings[bool] = BoolProperty
        mappings[list] = ArrayStringProperty
        mappings[tuple] = ArrayStringProperty
        mappings[wx.Font] = FontProperty
        mappings[wx.Colour] = ColourProperty
        "mappings[wx.Size] = SizeProperty"
        "mappings[wx.Point] = PointProperty"
        "mappings[wx.FontData] = FontDataProperty"

    def DoDefaultValueTypeMappings(self):
        "Map pg value type ids to getter methods."
        global _vt2getter
        try:
            vt2getter = _vt2getter

            return
        except NameError:
            vt2getter = {}
            _vt2getter = vt2getter

    def GetPropertyValues(self,dict_=None, as_strings=False,
                          inc_attributes=False):
        "Returns values in the grid."
        ""
        "dict_: if not given, then a new one is created. dict_ can be"
        "  object as well, in which case it's __dict__ is used."
        "as_strings: if True, then string representations of values"
        "  are fetched instead of native types. Useful for config and "
        "such."
        "inc_attributes: if True, then property attributes are added"
        "  as @<propname>@<attr>."
        ""
        "Return value: dictionary with values. It is always a dictionary,"
        "so if dict_ was object with __dict__ attribute, then that "
        "attribute is returned."

        if dict_ is None:
            dict_ = {}
        elif hasattr(dict_,'__dict__'):
            dict_ = dict_.__dict__

        if not as_strings:
            getter = self.GetPropertyValue
        else:
            getter = self.GetPropertyValueAsString

        it = self.GetVIterator(PG_ITERATE_PROPERTIES)
        while not it.AtEnd():
            p = it.GetProperty()
            name = p.GetName()

            dict_[name] = getter(p)

            if inc_attributes:
                attrs = p.GetAttributes()
                if attrs and len(attrs):
                    dict_['@%s@attr'%name] = attrs

            it.Next()

        return dict_

    GetValues = GetPropertyValues


    def SetPropertyValues(self,dict_):
        "Sets property values from dict_, which can be either\ndictionary "
        "or an object with __dict__ attribute."
        ""
        "autofill: If true, keys with not relevant properties"
        "  are auto-created. For more info, see AutoFill."
        ""
        "Notes:"
        "  * Keys starting with underscore are ignored."
        "  * Attributes can be set with entries named @<propname>@<attr>."
        ""

        autofill = False

        if dict_ is None:
            dict_ = {}
        elif hasattr(dict_,'__dict__'):
            dict_ = dict_.__dict__

        attr_dicts = []

        def set_sub_obj(k0,dict_):
            for k,v in dict_.iteritems():
                if k[0] != '_':
                    if k.endswith('@attr'):
                        attr_dicts.append((k[1:-5],v))
                    else:
                        try:
                            self.SetPropertyValue(k,v)
                        except:
                            try:
                                if autofill:
                                    self._AutoFillOne(k0,k,v)
                                    continue
                            except:
                                if isinstance(v,dict):
                                    set_sub_obj(k,v)
                                elif hasattr(v,'__dict__'):
                                    set_sub_obj(k,v.__dict__)


        for k,v in attr_dicts:
            p = GetPropertyByName(k)
            if not p:
                raise AssertionError("No such property: '%s'"%k)
            for an,av in v.iteritems():
                p.SetAttribute(an, av)


        cur_page = False
        is_manager = isinstance(self,PropertyGridManager)

        try:
            set_sub_obj(self.GetGrid().GetRoot(),dict_)
        except:
            import traceback
            traceback.print_exc()

        self.Refresh()

    SetValues = SetPropertyValues

    def _AutoFillMany(self,cat,dict_):
        for k,v in dict_.iteritems():
            self._AutoFillOne(cat,k,v)


    def _AutoFillOne(self,cat,k,v):
        global _type2property

        factory = _type2property.get(v.__class__,None)

        if factory:
            self.AppendIn( cat, factory(k,k,v) )
        elif hasattr(v,'__dict__'):
            cat2 = self.AppendIn( cat, PropertyCategory(k) )
            self._AutoFillMany(cat2,v.__dict__)
        elif isinstance(v,dict):
            cat2 = self.AppendIn( cat, PropertyCategory(k) )
            self._AutoFillMany(cat2,v)
        elif not k.startswith('_'):
            raise AssertionError("member '%s' is of unregisted type/"
                                 "class '%s'"%(k,v.__class__))


    def AutoFill(self,obj,parent=None):
        "Clears properties and re-fills to match members and\nvalues of "
        "given object or dictionary obj."

        self.edited_objects[parent] = obj

        cur_page = False
        is_manager = isinstance(self,PropertyGridManager)

        if not parent:
            if is_manager:
                page = self.GetCurrentPage()
                page.Clear()
                parent = page.GetRoot()
            else:
                self.Clear()
                parent = self.GetGrid().GetRoot()
        else:
            it = self.GetIterator(PG_ITERATE_PROPERTIES, parent)
            it.Next()  # Skip the parent
            while not it.AtEnd():
                p = it.GetProperty()
                if not p.IsSomeParent(parent):
                    break

                self.DeleteProperty(p)

                name = p.GetName()
                it.Next()

        if not is_manager or page == self.GetCurrentPage():
            self.Freeze()
            cur_page = True

        try:
            self._AutoFillMany(parent,obj.__dict__)
        except:
            import traceback
            traceback.print_exc()

        if cur_page:
            self.Thaw()

    def RegisterEditor(self, editor, editorName=None):
        "Transform class into instance, if necessary."
        if not isinstance(editor, PGEditor):
            editor = editor()
        if not editorName:
            editorName = editor.__class__.__name__
        try:
            self._editor_instances.append(editor)
        except:
            self._editor_instances = [editor]
        RegisterEditor(editor, editorName)

    def GetPropertyClientData(self, p):
        if isinstance(p, basestring):
            p = self.GetPropertyByName(p)
        return p.GetClientData()

    def SetPropertyClientData(self, p, data):
        if isinstance(p, basestring):
            p = self.GetPropertyByName(p)
        return p.SetClientData(data)

    def GetPyIterator(self, flags=PG_ITERATE_DEFAULT,
                      firstProperty=None):
        """
        Returns a pythonic property iterator for a single `PropertyGrid`
        or page in `PropertyGridManager`. Arguments are same as for
        `GetIterator`. Following example demonstrates iterating absolutely
        all items in a single grid::

            iterator = propGrid.GetPyIterator(wx.propgrid.PG_ITERATE_ALL)
            for prop in iterator:
                print(prop)

        :see: `wx.propgrid.PropertyGridInterface.Properties`
              `wx.propgrid.PropertyGridInterface.Items`
        """
        it = self.GetIterator(flags, firstProperty)
        while not it.AtEnd():
            yield it.GetProperty()
            it.Next()

    def GetPyVIterator(self, flags=PG_ITERATE_DEFAULT):
        """
        Returns a pythonic property iterator for a single `PropertyGrid`
        or entire `PropertyGridManager`. Arguments are same as for
        `GetIterator`. Following example demonstrates iterating absolutely
        all items in an entire `PropertyGridManager`::

            iterator = propGridManager.GetPyVIterator(wx.propgrid.PG_ITERATE_ALL)
            for prop in iterator:
                print(prop)

        :see: `wx.propgrid.PropertyGridInterface.Properties`
              `wx.propgrid.PropertyGridInterface.Items`
        """
        it = self.GetVIterator(flags)
        while not it.AtEnd():
            yield it.GetProperty()
            it.Next()

    @property
    def Properties(self):
        """
        This attribute is a pythonic iterator over all properties in
        this `PropertyGrid` property container. It will only skip
        categories and private child properties. Usage is simple::

            for prop in propGrid.Properties:
                print(prop)

        :see: `wx.propgrid.PropertyGridInterface.Items`
              `wx.propgrid.PropertyGridInterface.GetPyIterator`
        """
        it = self.GetVIterator(PG_ITERATE_NORMAL)
        while not it.AtEnd():
            yield it.GetProperty()
            it.Next()

    @property
    def Items(self):
        """
        This attribute is a pythonic iterator over all items in this
        `PropertyGrid` property container, excluding only private child
        properties. Usage is simple::

            for prop in propGrid.Items:
                print(prop)

        :see: `wx.propgrid.PropertyGridInterface.Properties`
              `wx.propgrid.PropertyGridInterface.GetPyIterator`
        """
        it = self.GetVIterator(PG_ITERATE_NORMAL | PG_ITERATE_CATEGORIES)
        while not it.AtEnd():
            yield it.GetProperty()
            it.Next()

_propgrid.PropertyGridInterface_swigregister(PropertyGridInterface)

def PropertyGridInterface_InitAllTypeHandlers(*args):
  """PropertyGridInterface_InitAllTypeHandlers()"""
  return _propgrid.PropertyGridInterface_InitAllTypeHandlers(*args)

def PropertyGridInterface_RegisterAdditionalEditors(*args):
  """PropertyGridInterface_RegisterAdditionalEditors()"""
  return _propgrid.PropertyGridInterface_RegisterAdditionalEditors(*args)

def PropertyGridInterface_SetBoolChoices(*args, **kwargs):
  """PropertyGridInterface_SetBoolChoices(String trueChoice, String falseChoice)"""
  return _propgrid.PropertyGridInterface_SetBoolChoices(*args, **kwargs)

def PropertyGridInterface_GetEditorByName(*args, **kwargs):
  """PropertyGridInterface_GetEditorByName(String editorName) -> PGEditor"""
  return _propgrid.PropertyGridInterface_GetEditorByName(*args, **kwargs)

PG_AUTO_SORT = _propgrid.PG_AUTO_SORT
PG_HIDE_CATEGORIES = _propgrid.PG_HIDE_CATEGORIES
PG_ALPHABETIC_MODE = _propgrid.PG_ALPHABETIC_MODE
PG_BOLD_MODIFIED = _propgrid.PG_BOLD_MODIFIED
PG_SPLITTER_AUTO_CENTER = _propgrid.PG_SPLITTER_AUTO_CENTER
PG_TOOLTIPS = _propgrid.PG_TOOLTIPS
PG_HIDE_MARGIN = _propgrid.PG_HIDE_MARGIN
PG_STATIC_SPLITTER = _propgrid.PG_STATIC_SPLITTER
PG_STATIC_LAYOUT = _propgrid.PG_STATIC_LAYOUT
PG_LIMITED_EDITING = _propgrid.PG_LIMITED_EDITING
PG_TOOLBAR = _propgrid.PG_TOOLBAR
PG_DESCRIPTION = _propgrid.PG_DESCRIPTION
PG_NO_INTERNAL_BORDER = _propgrid.PG_NO_INTERNAL_BORDER
PG_EX_INIT_NOCAT = _propgrid.PG_EX_INIT_NOCAT
PG_EX_NO_FLAT_TOOLBAR = _propgrid.PG_EX_NO_FLAT_TOOLBAR
PG_EX_MODE_BUTTONS = _propgrid.PG_EX_MODE_BUTTONS
PG_EX_HELP_AS_TOOLTIPS = _propgrid.PG_EX_HELP_AS_TOOLTIPS
PG_EX_NATIVE_DOUBLE_BUFFERING = _propgrid.PG_EX_NATIVE_DOUBLE_BUFFERING
PG_EX_AUTO_UNSPECIFIED_VALUES = _propgrid.PG_EX_AUTO_UNSPECIFIED_VALUES
PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES = _propgrid.PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES
PG_EX_HIDE_PAGE_BUTTONS = _propgrid.PG_EX_HIDE_PAGE_BUTTONS
PG_EX_MULTIPLE_SELECTION = _propgrid.PG_EX_MULTIPLE_SELECTION
PG_EX_ENABLE_TLP_TRACKING = _propgrid.PG_EX_ENABLE_TLP_TRACKING
PG_EX_NO_TOOLBAR_DIVIDER = _propgrid.PG_EX_NO_TOOLBAR_DIVIDER
PG_EX_TOOLBAR_SEPARATOR = _propgrid.PG_EX_TOOLBAR_SEPARATOR
PG_DEFAULT_STYLE = _propgrid.PG_DEFAULT_STYLE
PGMAN_DEFAULT_STYLE = _propgrid.PGMAN_DEFAULT_STYLE
PG_SUBID1 = _propgrid.PG_SUBID1
PG_SUBID2 = _propgrid.PG_SUBID2
PG_SUBID_TEMP1 = _propgrid.PG_SUBID_TEMP1
class PGCommonValue(object):
    """Proxy of C++ PGCommonValue class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String label,  renderer) -> PGCommonValue"""
        _propgrid.PGCommonValue_swiginit(self,_propgrid.new_PGCommonValue(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PGCommonValue
    __del__ = lambda self : None;
    def GetEditableText(*args, **kwargs):
        """GetEditableText(self) -> String"""
        return _propgrid.PGCommonValue_GetEditableText(*args, **kwargs)

    def GetLabel(*args, **kwargs):
        """GetLabel(self) -> String"""
        return _propgrid.PGCommonValue_GetLabel(*args, **kwargs)

    def GetRenderer(*args, **kwargs):
        """GetRenderer(self)"""
        return _propgrid.PGCommonValue_GetRenderer(*args, **kwargs)

_propgrid.PGCommonValue_swigregister(PGCommonValue)

PG_VFB_STAY_IN_PROPERTY = _propgrid.PG_VFB_STAY_IN_PROPERTY
PG_VFB_BEEP = _propgrid.PG_VFB_BEEP
PG_VFB_MARK_CELL = _propgrid.PG_VFB_MARK_CELL
PG_VFB_SHOW_MESSAGE = _propgrid.PG_VFB_SHOW_MESSAGE
PG_VFB_SHOW_MESSAGEBOX = _propgrid.PG_VFB_SHOW_MESSAGEBOX
PG_VFB_SHOW_MESSAGE_ON_STATUSBAR = _propgrid.PG_VFB_SHOW_MESSAGE_ON_STATUSBAR
PG_VFB_DEFAULT = _propgrid.PG_VFB_DEFAULT
PG_VFB_UNDEFINED = _propgrid.PG_VFB_UNDEFINED
class PGValidationInfo(object):
    """Proxy of C++ PGValidationInfo class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PGValidationInfo"""
        _propgrid.PGValidationInfo_swiginit(self,_propgrid.new_PGValidationInfo(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PGValidationInfo
    __del__ = lambda self : None;
    def GetFailureBehavior(*args, **kwargs):
        """GetFailureBehavior(self) -> char"""
        return _propgrid.PGValidationInfo_GetFailureBehavior(*args, **kwargs)

    def GetFailureMessage(*args, **kwargs):
        """GetFailureMessage(self) -> String"""
        return _propgrid.PGValidationInfo_GetFailureMessage(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> wxVariant"""
        return _propgrid.PGValidationInfo_GetValue(*args, **kwargs)

    def SetFailureBehavior(*args, **kwargs):
        """SetFailureBehavior(self, char failureBehavior)"""
        return _propgrid.PGValidationInfo_SetFailureBehavior(*args, **kwargs)

    def SetFailureMessage(*args, **kwargs):
        """SetFailureMessage(self, String message)"""
        return _propgrid.PGValidationInfo_SetFailureMessage(*args, **kwargs)

_propgrid.PGValidationInfo_swigregister(PGValidationInfo)

PG_ACTION_INVALID = _propgrid.PG_ACTION_INVALID
PG_ACTION_NEXT_PROPERTY = _propgrid.PG_ACTION_NEXT_PROPERTY
PG_ACTION_PREV_PROPERTY = _propgrid.PG_ACTION_PREV_PROPERTY
PG_ACTION_EXPAND_PROPERTY = _propgrid.PG_ACTION_EXPAND_PROPERTY
PG_ACTION_COLLAPSE_PROPERTY = _propgrid.PG_ACTION_COLLAPSE_PROPERTY
PG_ACTION_CANCEL_EDIT = _propgrid.PG_ACTION_CANCEL_EDIT
PG_ACTION_EDIT = _propgrid.PG_ACTION_EDIT
PG_ACTION_PRESS_BUTTON = _propgrid.PG_ACTION_PRESS_BUTTON
PG_ACTION_MAX = _propgrid.PG_ACTION_MAX
PG_SEL_FOCUS = _propgrid.PG_SEL_FOCUS
PG_SEL_FORCE = _propgrid.PG_SEL_FORCE
PG_SEL_NONVISIBLE = _propgrid.PG_SEL_NONVISIBLE
PG_SEL_NOVALIDATE = _propgrid.PG_SEL_NOVALIDATE
PG_SEL_DELETING = _propgrid.PG_SEL_DELETING
PG_SEL_SETUNSPEC = _propgrid.PG_SEL_SETUNSPEC
PG_SEL_DIALOGVAL = _propgrid.PG_SEL_DIALOGVAL
PG_SEL_DONT_SEND_EVENT = _propgrid.PG_SEL_DONT_SEND_EVENT
PG_SEL_NO_REFRESH = _propgrid.PG_SEL_NO_REFRESH
PG_SPLITTER_REFRESH = _propgrid.PG_SPLITTER_REFRESH
PG_SPLITTER_ALL_PAGES = _propgrid.PG_SPLITTER_ALL_PAGES
PG_SPLITTER_FROM_EVENT = _propgrid.PG_SPLITTER_FROM_EVENT
PG_SPLITTER_FROM_AUTO_CENTER = _propgrid.PG_SPLITTER_FROM_AUTO_CENTER
PG_FL_INITIALIZED = _propgrid.PG_FL_INITIALIZED
PG_FL_ACTIVATION_BY_CLICK = _propgrid.PG_FL_ACTIVATION_BY_CLICK
PG_FL_DONT_CENTER_SPLITTER = _propgrid.PG_FL_DONT_CENTER_SPLITTER
PG_FL_FOCUSED = _propgrid.PG_FL_FOCUSED
PG_FL_MOUSE_CAPTURED = _propgrid.PG_FL_MOUSE_CAPTURED
PG_FL_MOUSE_INSIDE = _propgrid.PG_FL_MOUSE_INSIDE
PG_FL_VALUE_MODIFIED = _propgrid.PG_FL_VALUE_MODIFIED
PG_FL_PRIMARY_FILLS_ENTIRE = _propgrid.PG_FL_PRIMARY_FILLS_ENTIRE
PG_FL_CUR_USES_CUSTOM_IMAGE = _propgrid.PG_FL_CUR_USES_CUSTOM_IMAGE
PG_FL_CELL_OVERRIDES_SEL = _propgrid.PG_FL_CELL_OVERRIDES_SEL
PG_FL_SCROLLED = _propgrid.PG_FL_SCROLLED
PG_FL_ADDING_HIDEABLES = _propgrid.PG_FL_ADDING_HIDEABLES
PG_FL_NOSTATUSBARHELP = _propgrid.PG_FL_NOSTATUSBARHELP
PG_FL_CREATEDSTATE = _propgrid.PG_FL_CREATEDSTATE
PG_FL_SCROLLBAR_DETECTED = _propgrid.PG_FL_SCROLLBAR_DETECTED
PG_FL_DESC_REFRESH_REQUIRED = _propgrid.PG_FL_DESC_REFRESH_REQUIRED
PG_FL_IN_MANAGER = _propgrid.PG_FL_IN_MANAGER
PG_FL_GOOD_SIZE_SET = _propgrid.PG_FL_GOOD_SIZE_SET
PG_FL_IN_SELECT_PROPERTY = _propgrid.PG_FL_IN_SELECT_PROPERTY
PG_FL_STRING_IN_STATUSBAR = _propgrid.PG_FL_STRING_IN_STATUSBAR
PG_FL_CATMODE_AUTO_SORT = _propgrid.PG_FL_CATMODE_AUTO_SORT
PG_MAN_FL_PAGE_INSERTED = _propgrid.PG_MAN_FL_PAGE_INSERTED
PG_FL_ABNORMAL_EDITOR = _propgrid.PG_FL_ABNORMAL_EDITOR
PG_FL_IN_HANDLECUSTOMEDITOREVENT = _propgrid.PG_FL_IN_HANDLECUSTOMEDITOREVENT
PG_FL_VALUE_CHANGE_IN_EVENT = _propgrid.PG_FL_VALUE_CHANGE_IN_EVENT
PG_FL_FIXED_WIDTH_EDITOR = _propgrid.PG_FL_FIXED_WIDTH_EDITOR
PG_FL_HAS_VIRTUAL_WIDTH = _propgrid.PG_FL_HAS_VIRTUAL_WIDTH
PG_FL_RECALCULATING_VIRTUAL_SIZE = _propgrid.PG_FL_RECALCULATING_VIRTUAL_SIZE
class PropertyGrid(_core.Control,_windows.ScrollHelper,PropertyGridInterface):
    """Proxy of C++ PropertyGrid class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=ID_ANY, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=(0), 
            String name=wxPropertyGridNameStr) -> PropertyGrid
        """
        _propgrid.PropertyGrid_swiginit(self,_propgrid.new_PropertyGrid(*args, **kwargs))
        
        self._setOORInfo(self)
        self.DoDefaultTypeMappings()
        self.edited_objects = {}
        self.DoDefaultValueTypeMappings()
        if not hasattr(self.__class__,'_vt2setter'):
            self.__class__._vt2setter = {}
    

    __swig_destroy__ = _propgrid.delete_PropertyGrid
    __del__ = lambda self : None;
    def AddActionTrigger(*args, **kwargs):
        """AddActionTrigger(self, int action, int keycode, int modifiers=0)"""
        return _propgrid.PropertyGrid_AddActionTrigger(*args, **kwargs)

    def DedicateKey(*args, **kwargs):
        """DedicateKey(self, int keycode)"""
        return _propgrid.PropertyGrid_DedicateKey(*args, **kwargs)

    def AutoGetTranslation(*args, **kwargs):
        """AutoGetTranslation(bool enable)"""
        return _propgrid.PropertyGrid_AutoGetTranslation(*args, **kwargs)

    AutoGetTranslation = staticmethod(AutoGetTranslation)
    def ChangePropertyValue(*args, **kwargs):
        """ChangePropertyValue(self, PGPropArg id, wxVariant newValue) -> bool"""
        return _propgrid.PropertyGrid_ChangePropertyValue(*args, **kwargs)

    def CenterSplitter(*args, **kwargs):
        """CenterSplitter(self, bool enableAutoResizing=False)"""
        return _propgrid.PropertyGrid_CenterSplitter(*args, **kwargs)

    def ClearActionTriggers(*args, **kwargs):
        """ClearActionTriggers(self, int action)"""
        return _propgrid.PropertyGrid_ClearActionTriggers(*args, **kwargs)

    def CommitChangesFromEditor(*args, **kwargs):
        """CommitChangesFromEditor(self, int flags=0) -> bool"""
        return _propgrid.PropertyGrid_CommitChangesFromEditor(*args, **kwargs)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=ID_ANY, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=(0), 
            String name=wxPropertyGridNameStr) -> bool
        """
        return _propgrid.PropertyGrid_Create(*args, **kwargs)

    def EditorsValueWasModified(*args, **kwargs):
        """EditorsValueWasModified(self)"""
        return _propgrid.PropertyGrid_EditorsValueWasModified(*args, **kwargs)

    def EditorsValueWasNotModified(*args, **kwargs):
        """EditorsValueWasNotModified(self)"""
        return _propgrid.PropertyGrid_EditorsValueWasNotModified(*args, **kwargs)

    def EnableCategories(*args, **kwargs):
        """EnableCategories(self, bool enable) -> bool"""
        return _propgrid.PropertyGrid_EnableCategories(*args, **kwargs)

    def EnsureVisible(*args, **kwargs):
        """EnsureVisible(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGrid_EnsureVisible(*args, **kwargs)

    def FitColumns(*args, **kwargs):
        """FitColumns(self) -> Size"""
        return _propgrid.PropertyGrid_FitColumns(*args, **kwargs)

    def GetPanel(*args, **kwargs):
        """GetPanel(self) -> Window"""
        return _propgrid.PropertyGrid_GetPanel(*args, **kwargs)

    def GetCaptionBackgroundColour(*args, **kwargs):
        """GetCaptionBackgroundColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetCaptionBackgroundColour(*args, **kwargs)

    def GetCaptionFont(*args):
        """
        GetCaptionFont(self) -> Font
        GetCaptionFont(self) -> Font
        """
        return _propgrid.PropertyGrid_GetCaptionFont(*args)

    def GetCaptionForegroundColour(*args, **kwargs):
        """GetCaptionForegroundColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetCaptionForegroundColour(*args, **kwargs)

    def GetCellBackgroundColour(*args, **kwargs):
        """GetCellBackgroundColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetCellBackgroundColour(*args, **kwargs)

    def GetCellDisabledTextColour(*args, **kwargs):
        """GetCellDisabledTextColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetCellDisabledTextColour(*args, **kwargs)

    def GetCellTextColour(*args, **kwargs):
        """GetCellTextColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetCellTextColour(*args, **kwargs)

    def GetColumnCount(*args, **kwargs):
        """GetColumnCount(self) -> int"""
        return _propgrid.PropertyGrid_GetColumnCount(*args, **kwargs)

    def GetEmptySpaceColour(*args, **kwargs):
        """GetEmptySpaceColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetEmptySpaceColour(*args, **kwargs)

    def GetFontHeight(*args, **kwargs):
        """GetFontHeight(self) -> int"""
        return _propgrid.PropertyGrid_GetFontHeight(*args, **kwargs)

    def GetGrid(*args, **kwargs):
        """GetGrid(self) -> PropertyGrid"""
        return _propgrid.PropertyGrid_GetGrid(*args, **kwargs)

    def GetImageRect(*args, **kwargs):
        """GetImageRect(self, PGProperty p, int item) -> Rect"""
        return _propgrid.PropertyGrid_GetImageRect(*args, **kwargs)

    def GetImageSize(*args, **kwargs):
        """GetImageSize(self, PGProperty p=None, int item=-1) -> Size"""
        return _propgrid.PropertyGrid_GetImageSize(*args, **kwargs)

    def GetLastItem(*args):
        """
        GetLastItem(self, int flags=PG_ITERATE_DEFAULT) -> PGProperty
        GetLastItem(self, int flags=PG_ITERATE_DEFAULT) -> PGProperty
        """
        return _propgrid.PropertyGrid_GetLastItem(*args)

    def GetLineColour(*args, **kwargs):
        """GetLineColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetLineColour(*args, **kwargs)

    def GetMarginColour(*args, **kwargs):
        """GetMarginColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetMarginColour(*args, **kwargs)

    def GetMarginWidth(*args, **kwargs):
        """GetMarginWidth(self) -> int"""
        return _propgrid.PropertyGrid_GetMarginWidth(*args, **kwargs)

    def GetUncommittedPropertyValue(*args, **kwargs):
        """GetUncommittedPropertyValue(self) -> wxVariant"""
        return _propgrid.PropertyGrid_GetUncommittedPropertyValue(*args, **kwargs)

    def GetRoot(*args, **kwargs):
        """GetRoot(self) -> PGProperty"""
        return _propgrid.PropertyGrid_GetRoot(*args, **kwargs)

    def GetRowHeight(*args, **kwargs):
        """GetRowHeight(self) -> int"""
        return _propgrid.PropertyGrid_GetRowHeight(*args, **kwargs)

    def GetSelectedProperty(*args, **kwargs):
        """GetSelectedProperty(self) -> PGProperty"""
        return _propgrid.PropertyGrid_GetSelectedProperty(*args, **kwargs)

    def GetSelectionBackgroundColour(*args, **kwargs):
        """GetSelectionBackgroundColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetSelectionBackgroundColour(*args, **kwargs)

    def GetSelectionForegroundColour(*args, **kwargs):
        """GetSelectionForegroundColour(self) -> Colour"""
        return _propgrid.PropertyGrid_GetSelectionForegroundColour(*args, **kwargs)

    def GetSplitterPosition(*args, **kwargs):
        """GetSplitterPosition(self, int splitterIndex=0) -> int"""
        return _propgrid.PropertyGrid_GetSplitterPosition(*args, **kwargs)

    def GetEditorTextCtrl(*args, **kwargs):
        """GetEditorTextCtrl(self) -> wxTextCtrl"""
        return _propgrid.PropertyGrid_GetEditorTextCtrl(*args, **kwargs)

    def GetValidationInfo(*args, **kwargs):
        """GetValidationInfo(self) -> PGValidationInfo"""
        return _propgrid.PropertyGrid_GetValidationInfo(*args, **kwargs)

    def GetVerticalSpacing(*args, **kwargs):
        """GetVerticalSpacing(self) -> int"""
        return _propgrid.PropertyGrid_GetVerticalSpacing(*args, **kwargs)

    def IsEditorFocused(*args, **kwargs):
        """IsEditorFocused(self) -> bool"""
        return _propgrid.PropertyGrid_IsEditorFocused(*args, **kwargs)

    def IsEditorsValueModified(*args, **kwargs):
        """IsEditorsValueModified(self) -> bool"""
        return _propgrid.PropertyGrid_IsEditorsValueModified(*args, **kwargs)

    def HitTest(*args, **kwargs):
        """
        HitTest(self, Point pt) -> PropertyGridHitTestResult

        Test where the given (in client coords) point lies
        """
        return _propgrid.PropertyGrid_HitTest(*args, **kwargs)

    def IsAnyModified(*args, **kwargs):
        """IsAnyModified(self) -> bool"""
        return _propgrid.PropertyGrid_IsAnyModified(*args, **kwargs)

    def IsFrozen(*args, **kwargs):
        """
        IsFrozen(self) -> bool

        Returns ``True`` if the window has been frozen and not thawed yet.

        :see: `Freeze` and `Thaw`
        """
        return _propgrid.PropertyGrid_IsFrozen(*args, **kwargs)

    def OnTLPChanging(*args, **kwargs):
        """OnTLPChanging(self, Window newTLP)"""
        return _propgrid.PropertyGrid_OnTLPChanging(*args, **kwargs)

    def ResetColours(*args, **kwargs):
        """ResetColours(self)"""
        return _propgrid.PropertyGrid_ResetColours(*args, **kwargs)

    def ResetColumnSizes(*args, **kwargs):
        """ResetColumnSizes(self, bool enableAutoResizing=False)"""
        return _propgrid.PropertyGrid_ResetColumnSizes(*args, **kwargs)

    def SelectProperty(*args, **kwargs):
        """SelectProperty(self, PGPropArg id, bool focus=False) -> bool"""
        return _propgrid.PropertyGrid_SelectProperty(*args, **kwargs)

    def SetSelection(*args, **kwargs):
        """SetSelection(self, wxArrayPGProperty newSelection)"""
        return _propgrid.PropertyGrid_SetSelection(*args, **kwargs)

    def AddToSelection(*args, **kwargs):
        """AddToSelection(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGrid_AddToSelection(*args, **kwargs)

    def RemoveFromSelection(*args, **kwargs):
        """RemoveFromSelection(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGrid_RemoveFromSelection(*args, **kwargs)

    def MakeColumnEditable(*args, **kwargs):
        """MakeColumnEditable(self, int column, bool editable=True)"""
        return _propgrid.PropertyGrid_MakeColumnEditable(*args, **kwargs)

    def BeginLabelEdit(*args, **kwargs):
        """BeginLabelEdit(self, int column=0)"""
        return _propgrid.PropertyGrid_BeginLabelEdit(*args, **kwargs)

    def EndLabelEdit(*args, **kwargs):
        """EndLabelEdit(self, bool commit=True)"""
        return _propgrid.PropertyGrid_EndLabelEdit(*args, **kwargs)

    def GetLabelEditor(*args, **kwargs):
        """GetLabelEditor(self) -> wxTextCtrl"""
        return _propgrid.PropertyGrid_GetLabelEditor(*args, **kwargs)

    def SetCaptionBackgroundColour(*args, **kwargs):
        """SetCaptionBackgroundColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetCaptionBackgroundColour(*args, **kwargs)

    def SetCaptionTextColour(*args, **kwargs):
        """SetCaptionTextColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetCaptionTextColour(*args, **kwargs)

    def SetCellBackgroundColour(*args, **kwargs):
        """SetCellBackgroundColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetCellBackgroundColour(*args, **kwargs)

    def SetCellDisabledTextColour(*args, **kwargs):
        """SetCellDisabledTextColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetCellDisabledTextColour(*args, **kwargs)

    def SetCellTextColour(*args, **kwargs):
        """SetCellTextColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetCellTextColour(*args, **kwargs)

    def SetColumnCount(*args, **kwargs):
        """SetColumnCount(self, int colCount)"""
        return _propgrid.PropertyGrid_SetColumnCount(*args, **kwargs)

    def SetCurrentCategory(*args, **kwargs):
        """SetCurrentCategory(self, PGPropArg id)"""
        return _propgrid.PropertyGrid_SetCurrentCategory(*args, **kwargs)

    def SetEmptySpaceColour(*args, **kwargs):
        """SetEmptySpaceColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetEmptySpaceColour(*args, **kwargs)

    def SetLineColour(*args, **kwargs):
        """SetLineColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetLineColour(*args, **kwargs)

    def SetMarginColour(*args, **kwargs):
        """SetMarginColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetMarginColour(*args, **kwargs)

    def SetSelectionBackgroundColour(*args, **kwargs):
        """SetSelectionBackgroundColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetSelectionBackgroundColour(*args, **kwargs)

    def SetSelectionTextColour(*args, **kwargs):
        """SetSelectionTextColour(self, Colour col)"""
        return _propgrid.PropertyGrid_SetSelectionTextColour(*args, **kwargs)

    def SetSplitterPosition(*args, **kwargs):
        """SetSplitterPosition(self, int newXPos, int col=0)"""
        return _propgrid.PropertyGrid_SetSplitterPosition(*args, **kwargs)

    def SetSortFunction(*args, **kwargs):
        """SetSortFunction(self, PGSortCallback sortFunction)"""
        return _propgrid.PropertyGrid_SetSortFunction(*args, **kwargs)

    def GetSortFunction(*args, **kwargs):
        """GetSortFunction(self) -> PGSortCallback"""
        return _propgrid.PropertyGrid_GetSortFunction(*args, **kwargs)

    def SetUnspecifiedValueAppearance(*args, **kwargs):
        """SetUnspecifiedValueAppearance(self, PGCell cell)"""
        return _propgrid.PropertyGrid_SetUnspecifiedValueAppearance(*args, **kwargs)

    def GetUnspecifiedValueAppearance(*args, **kwargs):
        """GetUnspecifiedValueAppearance(self) -> PGCell"""
        return _propgrid.PropertyGrid_GetUnspecifiedValueAppearance(*args, **kwargs)

    def GetUnspecifiedValueText(*args, **kwargs):
        """GetUnspecifiedValueText(self, int argFlags=0) -> String"""
        return _propgrid.PropertyGrid_GetUnspecifiedValueText(*args, **kwargs)

    def SetVirtualWidth(*args, **kwargs):
        """SetVirtualWidth(self, int width)"""
        return _propgrid.PropertyGrid_SetVirtualWidth(*args, **kwargs)

    def SetSplitterLeft(*args, **kwargs):
        """SetSplitterLeft(self, bool privateChildrenToo=False)"""
        return _propgrid.PropertyGrid_SetSplitterLeft(*args, **kwargs)

    def SetVerticalSpacing(*args, **kwargs):
        """SetVerticalSpacing(self, int vspacing)"""
        return _propgrid.PropertyGrid_SetVerticalSpacing(*args, **kwargs)

    def ShowPropertyError(*args, **kwargs):
        """ShowPropertyError(self, PGPropArg id, String msg)"""
        return _propgrid.PropertyGrid_ShowPropertyError(*args, **kwargs)

    def HasVirtualWidth(*args, **kwargs):
        """HasVirtualWidth(self) -> bool"""
        return _propgrid.PropertyGrid_HasVirtualWidth(*args, **kwargs)

    def GetCommonValue(*args, **kwargs):
        """GetCommonValue(self, int i) -> PGCommonValue"""
        return _propgrid.PropertyGrid_GetCommonValue(*args, **kwargs)

    def GetCommonValueCount(*args, **kwargs):
        """GetCommonValueCount(self) -> int"""
        return _propgrid.PropertyGrid_GetCommonValueCount(*args, **kwargs)

    def GetCommonValueLabel(*args, **kwargs):
        """GetCommonValueLabel(self, int i) -> String"""
        return _propgrid.PropertyGrid_GetCommonValueLabel(*args, **kwargs)

    def GetUnspecifiedCommonValue(*args, **kwargs):
        """GetUnspecifiedCommonValue(self) -> int"""
        return _propgrid.PropertyGrid_GetUnspecifiedCommonValue(*args, **kwargs)

    def SetUnspecifiedCommonValue(*args, **kwargs):
        """SetUnspecifiedCommonValue(self, int index)"""
        return _propgrid.PropertyGrid_SetUnspecifiedCommonValue(*args, **kwargs)

    def GenerateEditorButton(*args, **kwargs):
        """GenerateEditorButton(self, Point pos, Size sz) -> Window"""
        return _propgrid.PropertyGrid_GenerateEditorButton(*args, **kwargs)

    def FixPosForTextCtrl(*args, **kwargs):
        """FixPosForTextCtrl(self, Window ctrl, int forColumn=1, Point offset=wxPoint(0, 0))"""
        return _propgrid.PropertyGrid_FixPosForTextCtrl(*args, **kwargs)

    def GenerateEditorTextCtrl(*args, **kwargs):
        """
        GenerateEditorTextCtrl(self, Point pos, Size sz, String value, Window secondary, 
            int extraStyle=0, int maxLen=0, int forColumn=1) -> Window
        """
        return _propgrid.PropertyGrid_GenerateEditorTextCtrl(*args, **kwargs)

    def GenerateEditorTextCtrlAndButton(*args, **kwargs):
        """
        GenerateEditorTextCtrlAndButton(self, Point pos, Size sz, Window psecondary, int limited_editing, 
            PGProperty property) -> Window
        """
        return _propgrid.PropertyGrid_GenerateEditorTextCtrlAndButton(*args, **kwargs)

    def GetGoodEditorDialogPosition(*args, **kwargs):
        """GetGoodEditorDialogPosition(self, PGProperty p, Size sz) -> Point"""
        return _propgrid.PropertyGrid_GetGoodEditorDialogPosition(*args, **kwargs)

    def ExpandEscapeSequences(*args, **kwargs):
        """ExpandEscapeSequences(String dst_str, String src_str) -> String"""
        return _propgrid.PropertyGrid_ExpandEscapeSequences(*args, **kwargs)

    ExpandEscapeSequences = staticmethod(ExpandEscapeSequences)
    def CreateEscapeSequences(*args, **kwargs):
        """CreateEscapeSequences(String dst_str, String src_str) -> String"""
        return _propgrid.PropertyGrid_CreateEscapeSequences(*args, **kwargs)

    CreateEscapeSequences = staticmethod(CreateEscapeSequences)
    def GetPropertyRect(*args, **kwargs):
        """GetPropertyRect(self, PGProperty p1, PGProperty p2) -> Rect"""
        return _propgrid.PropertyGrid_GetPropertyRect(*args, **kwargs)

    def GetEditorControl(*args, **kwargs):
        """GetEditorControl(self) -> Window"""
        return _propgrid.PropertyGrid_GetEditorControl(*args, **kwargs)

    def GetPrimaryEditor(*args, **kwargs):
        """GetPrimaryEditor(self) -> Window"""
        return _propgrid.PropertyGrid_GetPrimaryEditor(*args, **kwargs)

    def GetEditorControlSecondary(*args, **kwargs):
        """GetEditorControlSecondary(self) -> Window"""
        return _propgrid.PropertyGrid_GetEditorControlSecondary(*args, **kwargs)

    def RefreshEditor(*args, **kwargs):
        """RefreshEditor(self)"""
        return _propgrid.PropertyGrid_RefreshEditor(*args, **kwargs)

    def HandleCustomEditorEvent(*args, **kwargs):
        """HandleCustomEditorEvent(self, Event event) -> bool"""
        return _propgrid.PropertyGrid_HandleCustomEditorEvent(*args, **kwargs)

    def GetInternalFlags(*args, **kwargs):
        """GetInternalFlags(self) -> long"""
        return _propgrid.PropertyGrid_GetInternalFlags(*args, **kwargs)

    def HasInternalFlag(*args, **kwargs):
        """HasInternalFlag(self, long flag) -> bool"""
        return _propgrid.PropertyGrid_HasInternalFlag(*args, **kwargs)

    def SetInternalFlag(*args, **kwargs):
        """SetInternalFlag(self, long flag)"""
        return _propgrid.PropertyGrid_SetInternalFlag(*args, **kwargs)

    def ClearInternalFlag(*args, **kwargs):
        """ClearInternalFlag(self, long flag)"""
        return _propgrid.PropertyGrid_ClearInternalFlag(*args, **kwargs)

    def DoubleToString(*args, **kwargs):
        """
        DoubleToString(String target, double value, int precision, bool removeZeroes, 
            String precTemplate=None) -> String
        """
        return _propgrid.PropertyGrid_DoubleToString(*args, **kwargs)

    DoubleToString = staticmethod(DoubleToString)
    def ValueChangeInEvent(*args, **kwargs):
        """ValueChangeInEvent(self, wxVariant variant)"""
        return _propgrid.PropertyGrid_ValueChangeInEvent(*args, **kwargs)

    def WasValueChangedInEvent(*args, **kwargs):
        """WasValueChangedInEvent(self) -> bool"""
        return _propgrid.PropertyGrid_WasValueChangedInEvent(*args, **kwargs)

    def IsMainButtonEvent(*args, **kwargs):
        """IsMainButtonEvent(self, Event event) -> bool"""
        return _propgrid.PropertyGrid_IsMainButtonEvent(*args, **kwargs)

    def DoHidePropertyError(*args, **kwargs):
        """DoHidePropertyError(self, PGProperty property)"""
        return _propgrid.PropertyGrid_DoHidePropertyError(*args, **kwargs)

    def GetSpacingY(*args, **kwargs):
        """GetSpacingY(self) -> int"""
        return _propgrid.PropertyGrid_GetSpacingY(*args, **kwargs)

    def SetupTextCtrlValue(*args, **kwargs):
        """SetupTextCtrlValue(self, String text)"""
        return _propgrid.PropertyGrid_SetupTextCtrlValue(*args, **kwargs)

    def UnfocusEditor(*args, **kwargs):
        """UnfocusEditor(self) -> bool"""
        return _propgrid.PropertyGrid_UnfocusEditor(*args, **kwargs)

    def GetPropertyDefaultCell(*args, **kwargs):
        """GetPropertyDefaultCell(self) -> PGCell"""
        return _propgrid.PropertyGrid_GetPropertyDefaultCell(*args, **kwargs)

    def GetCategoryDefaultCell(*args, **kwargs):
        """GetCategoryDefaultCell(self) -> PGCell"""
        return _propgrid.PropertyGrid_GetCategoryDefaultCell(*args, **kwargs)

    def GetItemAtY(*args, **kwargs):
        """GetItemAtY(self, int y) -> PGProperty"""
        return _propgrid.PropertyGrid_GetItemAtY(*args, **kwargs)

_propgrid.PropertyGrid_swigregister(PropertyGrid)

def PropertyGrid_AutoGetTranslation(*args, **kwargs):
  """PropertyGrid_AutoGetTranslation(bool enable)"""
  return _propgrid.PropertyGrid_AutoGetTranslation(*args, **kwargs)

def PropertyGrid_ExpandEscapeSequences(*args, **kwargs):
  """PropertyGrid_ExpandEscapeSequences(String dst_str, String src_str) -> String"""
  return _propgrid.PropertyGrid_ExpandEscapeSequences(*args, **kwargs)

def PropertyGrid_CreateEscapeSequences(*args, **kwargs):
  """PropertyGrid_CreateEscapeSequences(String dst_str, String src_str) -> String"""
  return _propgrid.PropertyGrid_CreateEscapeSequences(*args, **kwargs)

def PropertyGrid_DoubleToString(*args, **kwargs):
  """
    PropertyGrid_DoubleToString(String target, double value, int precision, bool removeZeroes, 
        String precTemplate=None) -> String
    """
  return _propgrid.PropertyGrid_DoubleToString(*args, **kwargs)

PG_BASE_EVT_PRE_ID = _propgrid.PG_BASE_EVT_PRE_ID
wxEVT_PG_SELECTED = _propgrid.wxEVT_PG_SELECTED
wxEVT_PG_CHANGING = _propgrid.wxEVT_PG_CHANGING
wxEVT_PG_CHANGED = _propgrid.wxEVT_PG_CHANGED
wxEVT_PG_HIGHLIGHTED = _propgrid.wxEVT_PG_HIGHLIGHTED
wxEVT_PG_RIGHT_CLICK = _propgrid.wxEVT_PG_RIGHT_CLICK
wxEVT_PG_PAGE_CHANGED = _propgrid.wxEVT_PG_PAGE_CHANGED
wxEVT_PG_ITEM_COLLAPSED = _propgrid.wxEVT_PG_ITEM_COLLAPSED
wxEVT_PG_ITEM_EXPANDED = _propgrid.wxEVT_PG_ITEM_EXPANDED
wxEVT_PG_DOUBLE_CLICK = _propgrid.wxEVT_PG_DOUBLE_CLICK
wxEVT_PG_LABEL_EDIT_BEGIN = _propgrid.wxEVT_PG_LABEL_EDIT_BEGIN
wxEVT_PG_LABEL_EDIT_ENDING = _propgrid.wxEVT_PG_LABEL_EDIT_ENDING
wxEVT_PG_COL_BEGIN_DRAG = _propgrid.wxEVT_PG_COL_BEGIN_DRAG
wxEVT_PG_COL_DRAGGING = _propgrid.wxEVT_PG_COL_DRAGGING
wxEVT_PG_COL_END_DRAG = _propgrid.wxEVT_PG_COL_END_DRAG
class PropertyGridEvent(_core.CommandEvent):
    """Proxy of C++ PropertyGridEvent class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, EventType commandType=0, int id=0) -> PropertyGridEvent"""
        _propgrid.PropertyGridEvent_swiginit(self,_propgrid.new_PropertyGridEvent(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PropertyGridEvent
    __del__ = lambda self : None;
    def GetColumn(*args, **kwargs):
        """GetColumn(self) -> int"""
        return _propgrid.PropertyGridEvent_GetColumn(*args, **kwargs)

    def GetMainParent(*args, **kwargs):
        """GetMainParent(self) -> PGProperty"""
        return _propgrid.PropertyGridEvent_GetMainParent(*args, **kwargs)

    def GetProperty(*args, **kwargs):
        """GetProperty(self) -> PGProperty"""
        return _propgrid.PropertyGridEvent_GetProperty(*args, **kwargs)

    def GetValidationInfo(*args, **kwargs):
        """GetValidationInfo(self) -> PGValidationInfo"""
        return _propgrid.PropertyGridEvent_GetValidationInfo(*args, **kwargs)

    def CanVeto(*args, **kwargs):
        """CanVeto(self) -> bool"""
        return _propgrid.PropertyGridEvent_CanVeto(*args, **kwargs)

    def Veto(*args, **kwargs):
        """Veto(self, bool veto=True)"""
        return _propgrid.PropertyGridEvent_Veto(*args, **kwargs)

    def GetPropertyName(*args, **kwargs):
        """GetPropertyName(self) -> String"""
        return _propgrid.PropertyGridEvent_GetPropertyName(*args, **kwargs)

    def GetPropertyValue(*args, **kwargs):
        """GetPropertyValue(self) -> wxVariant"""
        return _propgrid.PropertyGridEvent_GetPropertyValue(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> wxVariant"""
        return _propgrid.PropertyGridEvent_GetValue(*args, **kwargs)

    def SetValidationFailureBehavior(*args, **kwargs):
        """SetValidationFailureBehavior(self, char flags)"""
        return _propgrid.PropertyGridEvent_SetValidationFailureBehavior(*args, **kwargs)

    def SetValidationFailureMessage(*args, **kwargs):
        """SetValidationFailureMessage(self, String message)"""
        return _propgrid.PropertyGridEvent_SetValidationFailureMessage(*args, **kwargs)

    def SetColumn(*args, **kwargs):
        """SetColumn(self, int column)"""
        return _propgrid.PropertyGridEvent_SetColumn(*args, **kwargs)

    def SetCanVeto(*args, **kwargs):
        """SetCanVeto(self, bool canVeto)"""
        return _propgrid.PropertyGridEvent_SetCanVeto(*args, **kwargs)

    def WasVetoed(*args, **kwargs):
        """WasVetoed(self) -> bool"""
        return _propgrid.PropertyGridEvent_WasVetoed(*args, **kwargs)

    def SetProperty(*args, **kwargs):
        """SetProperty(self, PGProperty p)"""
        return _propgrid.PropertyGridEvent_SetProperty(*args, **kwargs)

_propgrid.PropertyGridEvent_swigregister(PropertyGridEvent)

class PropertyGridPopulator(object):
    """Proxy of C++ PropertyGridPopulator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_PropertyGridPopulator
    __del__ = lambda self : None;
    def SetState(*args, **kwargs):
        """SetState(self,  state)"""
        return _propgrid.PropertyGridPopulator_SetState(*args, **kwargs)

    def SetGrid(*args, **kwargs):
        """SetGrid(self, PropertyGrid pg)"""
        return _propgrid.PropertyGridPopulator_SetGrid(*args, **kwargs)

    def Add(*args, **kwargs):
        """
        Add(self, String propClass, String propLabel, String propName, 
            String propValue, PGChoices pChoices=None) -> PGProperty
        """
        return _propgrid.PropertyGridPopulator_Add(*args, **kwargs)

    def AddChildren(*args, **kwargs):
        """AddChildren(self, PGProperty property)"""
        return _propgrid.PropertyGridPopulator_AddChildren(*args, **kwargs)

    def AddAttribute(*args, **kwargs):
        """AddAttribute(self, String name, String type, String value) -> bool"""
        return _propgrid.PropertyGridPopulator_AddAttribute(*args, **kwargs)

    def DoScanForChildren(*args, **kwargs):
        """DoScanForChildren(self)"""
        return _propgrid.PropertyGridPopulator_DoScanForChildren(*args, **kwargs)

    def GetCurParent(*args, **kwargs):
        """GetCurParent(self) -> PGProperty"""
        return _propgrid.PropertyGridPopulator_GetCurParent(*args, **kwargs)

    def GetState(*args):
        """
        GetState(self)
        GetState(self)
        """
        return _propgrid.PropertyGridPopulator_GetState(*args)

    def ToLongPCT(*args, **kwargs):
        """ToLongPCT(String s, long pval, long max) -> bool"""
        return _propgrid.PropertyGridPopulator_ToLongPCT(*args, **kwargs)

    ToLongPCT = staticmethod(ToLongPCT)
    def ParseChoices(*args, **kwargs):
        """ParseChoices(self, String choicesString, String idString) -> PGChoices"""
        return _propgrid.PropertyGridPopulator_ParseChoices(*args, **kwargs)

    def ProcessError(*args, **kwargs):
        """ProcessError(self, String msg)"""
        return _propgrid.PropertyGridPopulator_ProcessError(*args, **kwargs)

_propgrid.PropertyGridPopulator_swigregister(PropertyGridPopulator)

def PropertyGridPopulator_ToLongPCT(*args, **kwargs):
  """PropertyGridPopulator_ToLongPCT(String s, long pval, long max) -> bool"""
  return _propgrid.PropertyGridPopulator_ToLongPCT(*args, **kwargs)

class PGWindowList(object):
    """Proxy of C++ PGWindowList class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PGWindowList"""
        _propgrid.PGWindowList_swiginit(self,_propgrid.new_PGWindowList(*args, **kwargs))
    def SetSecondary(*args, **kwargs):
        """SetSecondary(self, Window secondary)"""
        return _propgrid.PGWindowList_SetSecondary(*args, **kwargs)

    m_primary = property(_propgrid.PGWindowList_m_primary_get, _propgrid.PGWindowList_m_primary_set)
    m_secondary = property(_propgrid.PGWindowList_m_secondary_get, _propgrid.PGWindowList_m_secondary_set)
_propgrid.PGWindowList_swigregister(PGWindowList)

class PGEditor(_core.Object):
    """Proxy of C++ PGEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_PGEditor
    __del__ = lambda self : None;
    def GetName(*args, **kwargs):
        """GetName(self) -> String"""
        return _propgrid.PGEditor_GetName(*args, **kwargs)

    def CreateControls(*args, **kwargs):
        """
        CreateControls(self, PropertyGrid propgrid, PGProperty property, Point pos, 
            Size size) -> PGWindowList
        """
        return _propgrid.PGEditor_CreateControls(*args, **kwargs)

    def UpdateControl(*args, **kwargs):
        """UpdateControl(self, PGProperty property, Window ctrl)"""
        return _propgrid.PGEditor_UpdateControl(*args, **kwargs)

    def DrawValue(*args, **kwargs):
        """DrawValue(self, DC dc, Rect rect, PGProperty property, String text)"""
        return _propgrid.PGEditor_DrawValue(*args, **kwargs)

    def OnEvent(*args, **kwargs):
        """
        OnEvent(self, PropertyGrid propgrid, PGProperty property, Window wnd_primary, 
            Event event) -> bool
        """
        return _propgrid.PGEditor_OnEvent(*args, **kwargs)

    def SetControlAppearance(*args, **kwargs):
        """
        SetControlAppearance(self, PropertyGrid pg, PGProperty property, Window ctrl, 
            PGCell appearance, PGCell oldAppearance, bool unspecified)
        """
        return _propgrid.PGEditor_SetControlAppearance(*args, **kwargs)

    def SetValueToUnspecified(*args, **kwargs):
        """SetValueToUnspecified(self, PGProperty property, Window ctrl)"""
        return _propgrid.PGEditor_SetValueToUnspecified(*args, **kwargs)

    def SetControlStringValue(*args, **kwargs):
        """SetControlStringValue(self, PGProperty property, Window ctrl, String txt)"""
        return _propgrid.PGEditor_SetControlStringValue(*args, **kwargs)

    def SetControlIntValue(*args, **kwargs):
        """SetControlIntValue(self, PGProperty property, Window ctrl, int value)"""
        return _propgrid.PGEditor_SetControlIntValue(*args, **kwargs)

    def InsertItem(*args, **kwargs):
        """InsertItem(self, Window ctrl, String label, int index) -> int"""
        return _propgrid.PGEditor_InsertItem(*args, **kwargs)

    def DeleteItem(*args, **kwargs):
        """DeleteItem(self, Window ctrl, int index)"""
        return _propgrid.PGEditor_DeleteItem(*args, **kwargs)

    def OnFocus(*args, **kwargs):
        """OnFocus(self, PGProperty property, Window wnd)"""
        return _propgrid.PGEditor_OnFocus(*args, **kwargs)

    def CanContainCustomImage(*args, **kwargs):
        """CanContainCustomImage(self) -> bool"""
        return _propgrid.PGEditor_CanContainCustomImage(*args, **kwargs)

    m_clientData = property(_propgrid.PGEditor_m_clientData_get, _propgrid.PGEditor_m_clientData_set)
_propgrid.PGEditor_swigregister(PGEditor)

class PGTextCtrlEditor(PGEditor):
    """Proxy of C++ PGTextCtrlEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PGTextCtrlEditor"""
        _propgrid.PGTextCtrlEditor_swiginit(self,_propgrid.new_PGTextCtrlEditor(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PGTextCtrlEditor
    __del__ = lambda self : None;
    def OnTextCtrlEvent(*args, **kwargs):
        """
        OnTextCtrlEvent(PropertyGrid propgrid, PGProperty property, Window ctrl, 
            Event event) -> bool
        """
        return _propgrid.PGTextCtrlEditor_OnTextCtrlEvent(*args, **kwargs)

    OnTextCtrlEvent = staticmethod(OnTextCtrlEvent)
    def GetTextCtrlValueFromControl(*args, **kwargs):
        """GetTextCtrlValueFromControl(wxVariant variant, PGProperty property, Window ctrl) -> bool"""
        return _propgrid.PGTextCtrlEditor_GetTextCtrlValueFromControl(*args, **kwargs)

    GetTextCtrlValueFromControl = staticmethod(GetTextCtrlValueFromControl)
_propgrid.PGTextCtrlEditor_swigregister(PGTextCtrlEditor)

def PGTextCtrlEditor_OnTextCtrlEvent(*args, **kwargs):
  """
    PGTextCtrlEditor_OnTextCtrlEvent(PropertyGrid propgrid, PGProperty property, Window ctrl, 
        Event event) -> bool
    """
  return _propgrid.PGTextCtrlEditor_OnTextCtrlEvent(*args, **kwargs)

def PGTextCtrlEditor_GetTextCtrlValueFromControl(*args, **kwargs):
  """PGTextCtrlEditor_GetTextCtrlValueFromControl(wxVariant variant, PGProperty property, Window ctrl) -> bool"""
  return _propgrid.PGTextCtrlEditor_GetTextCtrlValueFromControl(*args, **kwargs)

class PGChoiceEditor(PGEditor):
    """Proxy of C++ PGChoiceEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PGChoiceEditor"""
        _propgrid.PGChoiceEditor_swiginit(self,_propgrid.new_PGChoiceEditor(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PGChoiceEditor
    __del__ = lambda self : None;
    def CreateControlsBase(*args, **kwargs):
        """
        CreateControlsBase(self, PropertyGrid propgrid, PGProperty property, Point pos, 
            Size sz, long extraStyle) -> Window
        """
        return _propgrid.PGChoiceEditor_CreateControlsBase(*args, **kwargs)

_propgrid.PGChoiceEditor_swigregister(PGChoiceEditor)

class PGComboBoxEditor(PGChoiceEditor):
    """Proxy of C++ PGComboBoxEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PGComboBoxEditor"""
        _propgrid.PGComboBoxEditor_swiginit(self,_propgrid.new_PGComboBoxEditor(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PGComboBoxEditor
    __del__ = lambda self : None;
_propgrid.PGComboBoxEditor_swigregister(PGComboBoxEditor)

class PGEditorDialogAdapter(_core.Object):
    """Proxy of C++ PGEditorDialogAdapter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_PGEditorDialogAdapter
    __del__ = lambda self : None;
    def ShowDialog(*args, **kwargs):
        """ShowDialog(self, PropertyGrid propGrid, PGProperty property) -> bool"""
        return _propgrid.PGEditorDialogAdapter_ShowDialog(*args, **kwargs)

    def DoShowDialog(*args, **kwargs):
        """DoShowDialog(self, PropertyGrid propGrid, PGProperty property) -> bool"""
        return _propgrid.PGEditorDialogAdapter_DoShowDialog(*args, **kwargs)

    def SetValue(*args, **kwargs):
        """SetValue(self, wxVariant value)"""
        return _propgrid.PGEditorDialogAdapter_SetValue(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> wxVariant"""
        return _propgrid.PGEditorDialogAdapter_GetValue(*args, **kwargs)

    m_clientData = property(_propgrid.PGEditorDialogAdapter_m_clientData_get, _propgrid.PGEditorDialogAdapter_m_clientData_set)
_propgrid.PGEditorDialogAdapter_swigregister(PGEditorDialogAdapter)

class PGMultiButton(_core.Window):
    """Proxy of C++ PGMultiButton class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, PropertyGrid pg, Size sz) -> PGMultiButton"""
        _propgrid.PGMultiButton_swiginit(self,_propgrid.new_PGMultiButton(*args, **kwargs))
        
        self._setOORInfo(self)
    

    __swig_destroy__ = _propgrid.delete_PGMultiButton
    __del__ = lambda self : None;
    def GetButton(*args):
        """
        GetButton(self, int i) -> Window
        GetButton(self, int i) -> Window
        """
        return _propgrid.PGMultiButton_GetButton(*args)

    def GetButtonId(*args, **kwargs):
        """GetButtonId(self, int i) -> int"""
        return _propgrid.PGMultiButton_GetButtonId(*args, **kwargs)

    def GetCount(*args, **kwargs):
        """GetCount(self) -> int"""
        return _propgrid.PGMultiButton_GetCount(*args, **kwargs)

    def Add(*args, **kwargs):
        """Add(self, String label, int id=-2)"""
        return _propgrid.PGMultiButton_Add(*args, **kwargs)

    def GetPrimarySize(*args, **kwargs):
        """GetPrimarySize(self) -> Size"""
        return _propgrid.PGMultiButton_GetPrimarySize(*args, **kwargs)

    def Finalize(*args, **kwargs):
        """Finalize(self, PropertyGrid propGrid, Point pos)"""
        return _propgrid.PGMultiButton_Finalize(*args, **kwargs)

    def AddBitmapButton(*args, **kwargs):
        """AddBitmapButton(self, Bitmap bitmap, int id=-2)"""
        return _propgrid.PGMultiButton_AddBitmapButton(*args, **kwargs)

    def AddButton(self, *args, **kwargs):
        return self.Add(*args, **kwargs)

_propgrid.PGMultiButton_swigregister(PGMultiButton)

class StringProperty(PGProperty):
    """Proxy of C++ StringProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            String value=wxEmptyString) -> StringProperty
        """
        _propgrid.StringProperty_swiginit(self,_propgrid.new_StringProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_StringProperty
    __del__ = lambda self : None;
_propgrid.StringProperty_swigregister(StringProperty)

PG_PROPERTY_VALIDATION_ERROR_MESSAGE = _propgrid.PG_PROPERTY_VALIDATION_ERROR_MESSAGE
PG_PROPERTY_VALIDATION_SATURATE = _propgrid.PG_PROPERTY_VALIDATION_SATURATE
PG_PROPERTY_VALIDATION_WRAP = _propgrid.PG_PROPERTY_VALIDATION_WRAP
class NumericPropertyValidator(object):
    """Proxy of C++ NumericPropertyValidator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    Signed = _propgrid.NumericPropertyValidator_Signed
    Unsigned = _propgrid.NumericPropertyValidator_Unsigned
    Float = _propgrid.NumericPropertyValidator_Float
    def __init__(self, *args, **kwargs): 
        """__init__(self, int numericType, int base=10) -> NumericPropertyValidator"""
        _propgrid.NumericPropertyValidator_swiginit(self,_propgrid.new_NumericPropertyValidator(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_NumericPropertyValidator
    __del__ = lambda self : None;
    def Validate(*args, **kwargs):
        """Validate(self, Window parent) -> bool"""
        return _propgrid.NumericPropertyValidator_Validate(*args, **kwargs)

_propgrid.NumericPropertyValidator_swigregister(NumericPropertyValidator)

class IntProperty(PGProperty):
    """Proxy of C++ IntProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_IntProperty
    __del__ = lambda self : None;
    def __init__(self, *args): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            long value=0) -> IntProperty
        __init__(self, String label, String name, wxLongLong value) -> IntProperty
        """
        _propgrid.IntProperty_swiginit(self,_propgrid.new_IntProperty(*args))
    def GetClassValidator(*args, **kwargs):
        """GetClassValidator() -> Validator"""
        return _propgrid.IntProperty_GetClassValidator(*args, **kwargs)

    GetClassValidator = staticmethod(GetClassValidator)
    def DoValidation(*args, **kwargs):
        """
        DoValidation(PGProperty property, wxLongLong_t value, PGValidationInfo pValidationInfo, 
            int mode=PG_PROPERTY_VALIDATION_ERROR_MESSAGE) -> bool
        """
        return _propgrid.IntProperty_DoValidation(*args, **kwargs)

    DoValidation = staticmethod(DoValidation)
_propgrid.IntProperty_swigregister(IntProperty)

def IntProperty_GetClassValidator(*args):
  """IntProperty_GetClassValidator() -> Validator"""
  return _propgrid.IntProperty_GetClassValidator(*args)

def IntProperty_DoValidation(*args, **kwargs):
  """
    IntProperty_DoValidation(PGProperty property, wxLongLong_t value, PGValidationInfo pValidationInfo, 
        int mode=PG_PROPERTY_VALIDATION_ERROR_MESSAGE) -> bool
    """
  return _propgrid.IntProperty_DoValidation(*args, **kwargs)

class UIntProperty(PGProperty):
    """Proxy of C++ UIntProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_UIntProperty
    __del__ = lambda self : None;
    def __init__(self, *args): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            long value=0) -> UIntProperty
        __init__(self, String label, String name, wxULongLong value) -> UIntProperty
        """
        _propgrid.UIntProperty_swiginit(self,_propgrid.new_UIntProperty(*args))
_propgrid.UIntProperty_swigregister(UIntProperty)

class FloatProperty(PGProperty):
    """Proxy of C++ FloatProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            double value=0.0) -> FloatProperty
        """
        _propgrid.FloatProperty_swiginit(self,_propgrid.new_FloatProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_FloatProperty
    __del__ = lambda self : None;
    def DoValidation(*args, **kwargs):
        """
        DoValidation(PGProperty property, double value, PGValidationInfo pValidationInfo, 
            int mode=PG_PROPERTY_VALIDATION_ERROR_MESSAGE) -> bool
        """
        return _propgrid.FloatProperty_DoValidation(*args, **kwargs)

    DoValidation = staticmethod(DoValidation)
    def GetClassValidator(*args, **kwargs):
        """GetClassValidator() -> Validator"""
        return _propgrid.FloatProperty_GetClassValidator(*args, **kwargs)

    GetClassValidator = staticmethod(GetClassValidator)
_propgrid.FloatProperty_swigregister(FloatProperty)

def FloatProperty_DoValidation(*args, **kwargs):
  """
    FloatProperty_DoValidation(PGProperty property, double value, PGValidationInfo pValidationInfo, 
        int mode=PG_PROPERTY_VALIDATION_ERROR_MESSAGE) -> bool
    """
  return _propgrid.FloatProperty_DoValidation(*args, **kwargs)

def FloatProperty_GetClassValidator(*args):
  """FloatProperty_GetClassValidator() -> Validator"""
  return _propgrid.FloatProperty_GetClassValidator(*args)

class EnumProperty(PGProperty):
    """Proxy of C++ EnumProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString labels=wxArrayString(), 
            wxArrayInt values=wxArrayInt(), 
            int value=0) -> EnumProperty
        """
        _propgrid.EnumProperty_swiginit(self,_propgrid.new_EnumProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_EnumProperty
    __del__ = lambda self : None;
    def GetItemCount(*args, **kwargs):
        """GetItemCount(self) -> size_t"""
        return _propgrid.EnumProperty_GetItemCount(*args, **kwargs)

    def GetIndexForValue(*args, **kwargs):
        """GetIndexForValue(self, int value) -> int"""
        return _propgrid.EnumProperty_GetIndexForValue(*args, **kwargs)

_propgrid.EnumProperty_swigregister(EnumProperty)

class EditEnumProperty(EnumProperty):
    """Proxy of C++ EditEnumProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, String label, String name, wxChar labels, long values, 
            String value) -> EditEnumProperty
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString labels=wxArrayString(), 
            wxArrayInt values=wxArrayInt(), 
            String value=wxEmptyString) -> EditEnumProperty
        __init__(self, String label, String name, PGChoices choices, String value=wxEmptyString) -> EditEnumProperty
        __init__(self, String label, String name, wxChar labels, long values, 
            PGChoices choicesCache, String value) -> EditEnumProperty
        """
        _propgrid.EditEnumProperty_swiginit(self,_propgrid.new_EditEnumProperty(*args))
    __swig_destroy__ = _propgrid.delete_EditEnumProperty
    __del__ = lambda self : None;
_propgrid.EditEnumProperty_swigregister(EditEnumProperty)

class FlagsProperty(PGProperty):
    """Proxy of C++ FlagsProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString labels=wxArrayString(), 
            wxArrayInt values=wxArrayInt(), 
            int value=0) -> FlagsProperty
        """
        _propgrid.FlagsProperty_swiginit(self,_propgrid.new_FlagsProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_FlagsProperty
    __del__ = lambda self : None;
    def GetItemCount(*args, **kwargs):
        """GetItemCount(self) -> size_t"""
        return _propgrid.FlagsProperty_GetItemCount(*args, **kwargs)

    def GetLabel(*args, **kwargs):
        """GetLabel(self, size_t ind) -> String"""
        return _propgrid.FlagsProperty_GetLabel(*args, **kwargs)

_propgrid.FlagsProperty_swigregister(FlagsProperty)

class PGFileDialogAdapter(PGEditorDialogAdapter):
    """Proxy of C++ PGFileDialogAdapter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
_propgrid.PGFileDialogAdapter_swigregister(PGFileDialogAdapter)

class FileProperty(PGProperty):
    """Proxy of C++ FileProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            String value=wxEmptyString) -> FileProperty
        """
        _propgrid.FileProperty_swiginit(self,_propgrid.new_FileProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_FileProperty
    __del__ = lambda self : None;
    def GetClassValidator(*args, **kwargs):
        """GetClassValidator() -> Validator"""
        return _propgrid.FileProperty_GetClassValidator(*args, **kwargs)

    GetClassValidator = staticmethod(GetClassValidator)
    def GetFileName(*args, **kwargs):
        """GetFileName(self) -> wxFileName"""
        return _propgrid.FileProperty_GetFileName(*args, **kwargs)

_propgrid.FileProperty_swigregister(FileProperty)

def FileProperty_GetClassValidator(*args):
  """FileProperty_GetClassValidator() -> Validator"""
  return _propgrid.FileProperty_GetClassValidator(*args)

class PGLongStringDialogAdapter(PGEditorDialogAdapter):
    """Proxy of C++ PGLongStringDialogAdapter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
_propgrid.PGLongStringDialogAdapter_swigregister(PGLongStringDialogAdapter)

class LongStringProperty(PGProperty):
    """Proxy of C++ LongStringProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            String value=wxEmptyString) -> LongStringProperty
        """
        _propgrid.LongStringProperty_swiginit(self,_propgrid.new_LongStringProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_LongStringProperty
    __del__ = lambda self : None;
    def OnButtonClick(*args, **kwargs):
        """OnButtonClick(self, PropertyGrid propgrid, String value) -> bool"""
        return _propgrid.LongStringProperty_OnButtonClick(*args, **kwargs)

    def DisplayEditorDialog(*args, **kwargs):
        """DisplayEditorDialog(PGProperty prop, PropertyGrid propGrid, String value) -> bool"""
        return _propgrid.LongStringProperty_DisplayEditorDialog(*args, **kwargs)

    DisplayEditorDialog = staticmethod(DisplayEditorDialog)
_propgrid.LongStringProperty_swigregister(LongStringProperty)

def LongStringProperty_DisplayEditorDialog(*args, **kwargs):
  """LongStringProperty_DisplayEditorDialog(PGProperty prop, PropertyGrid propGrid, String value) -> bool"""
  return _propgrid.LongStringProperty_DisplayEditorDialog(*args, **kwargs)

class ArrayStringProperty(PGProperty):
    """Proxy of C++ ArrayStringProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString value=wxArrayString()) -> ArrayStringProperty
        """
        _propgrid.ArrayStringProperty_swiginit(self,_propgrid.new_ArrayStringProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_ArrayStringProperty
    __del__ = lambda self : None;
    def ConvertArrayToString(*args, **kwargs):
        """ConvertArrayToString(self, wxArrayString arr, String pString, wxUniChar delimiter)"""
        return _propgrid.ArrayStringProperty_ConvertArrayToString(*args, **kwargs)

    def OnCustomStringEdit(*args, **kwargs):
        """OnCustomStringEdit(self, Window parent, String value) -> bool"""
        return _propgrid.ArrayStringProperty_OnCustomStringEdit(*args, **kwargs)

    def OnButtonClick(*args, **kwargs):
        """OnButtonClick(self, PropertyGrid propgrid, Window primary, wxChar cbt) -> bool"""
        return _propgrid.ArrayStringProperty_OnButtonClick(*args, **kwargs)

    Escape = _propgrid.ArrayStringProperty_Escape
    QuoteStrings = _propgrid.ArrayStringProperty_QuoteStrings
    def ArrayStringToString(*args, **kwargs):
        """
        ArrayStringToString(String dst, wxArrayString src, wxUniChar delimiter, 
            int flags)
        """
        return _propgrid.ArrayStringProperty_ArrayStringToString(*args, **kwargs)

    ArrayStringToString = staticmethod(ArrayStringToString)
_propgrid.ArrayStringProperty_swigregister(ArrayStringProperty)

def ArrayStringProperty_ArrayStringToString(*args, **kwargs):
  """
    ArrayStringProperty_ArrayStringToString(String dst, wxArrayString src, wxUniChar delimiter, 
        int flags)
    """
  return _propgrid.ArrayStringProperty_ArrayStringToString(*args, **kwargs)

class PGArrayEditorDialog(_windows.Dialog):
    """Proxy of C++ PGArrayEditorDialog class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _propgrid.delete_PGArrayEditorDialog
    __del__ = lambda self : None;
    def Init(*args, **kwargs):
        """Init(self)"""
        return _propgrid.PGArrayEditorDialog_Init(*args, **kwargs)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, String message, String caption, long style=(wxDEFAULT_DIALOG_STYLE|wxRESIZE_BORDER|wxOK|wxCANCEL|wxCENTRE), 
            Point pos=DefaultPosition, 
            Size sz=DefaultSize) -> bool
        """
        return _propgrid.PGArrayEditorDialog_Create(*args, **kwargs)

    def EnableCustomNewAction(*args, **kwargs):
        """EnableCustomNewAction(self)"""
        return _propgrid.PGArrayEditorDialog_EnableCustomNewAction(*args, **kwargs)

    def SetDialogValue(*args, **kwargs):
        """SetDialogValue(self, wxVariant value)"""
        return _propgrid.PGArrayEditorDialog_SetDialogValue(*args, **kwargs)

    def GetDialogValue(*args, **kwargs):
        """GetDialogValue(self) -> wxVariant"""
        return _propgrid.PGArrayEditorDialog_GetDialogValue(*args, **kwargs)

    def GetTextCtrlValidator(*args, **kwargs):
        """GetTextCtrlValidator(self) -> Validator"""
        return _propgrid.PGArrayEditorDialog_GetTextCtrlValidator(*args, **kwargs)

    def IsModified(*args, **kwargs):
        """IsModified(self) -> bool"""
        return _propgrid.PGArrayEditorDialog_IsModified(*args, **kwargs)

    def GetSelection(*args, **kwargs):
        """GetSelection(self) -> int"""
        return _propgrid.PGArrayEditorDialog_GetSelection(*args, **kwargs)

    def OnAddClick(*args, **kwargs):
        """OnAddClick(self, CommandEvent event)"""
        return _propgrid.PGArrayEditorDialog_OnAddClick(*args, **kwargs)

    def OnDeleteClick(*args, **kwargs):
        """OnDeleteClick(self, CommandEvent event)"""
        return _propgrid.PGArrayEditorDialog_OnDeleteClick(*args, **kwargs)

    def OnUpClick(*args, **kwargs):
        """OnUpClick(self, CommandEvent event)"""
        return _propgrid.PGArrayEditorDialog_OnUpClick(*args, **kwargs)

    def OnDownClick(*args, **kwargs):
        """OnDownClick(self, CommandEvent event)"""
        return _propgrid.PGArrayEditorDialog_OnDownClick(*args, **kwargs)

    def OnEndLabelEdit(*args, **kwargs):
        """OnEndLabelEdit(self, ListEvent event)"""
        return _propgrid.PGArrayEditorDialog_OnEndLabelEdit(*args, **kwargs)

    def OnIdle(*args, **kwargs):
        """OnIdle(self, IdleEvent event)"""
        return _propgrid.PGArrayEditorDialog_OnIdle(*args, **kwargs)

_propgrid.PGArrayEditorDialog_swigregister(PGArrayEditorDialog)

class PGArrayStringEditorDialog(PGArrayEditorDialog):
    """Proxy of C++ PGArrayStringEditorDialog class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PGArrayStringEditorDialog"""
        _propgrid.PGArrayStringEditorDialog_swiginit(self,_propgrid.new_PGArrayStringEditorDialog(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PGArrayStringEditorDialog
    __del__ = lambda self : None;
    def Init(*args, **kwargs):
        """Init(self)"""
        return _propgrid.PGArrayStringEditorDialog_Init(*args, **kwargs)

    def SetCustomButton(*args, **kwargs):
        """SetCustomButton(self, String custBtText, ArrayStringProperty pcc)"""
        return _propgrid.PGArrayStringEditorDialog_SetCustomButton(*args, **kwargs)

    def OnCustomNewAction(*args, **kwargs):
        """OnCustomNewAction(self, String resString) -> bool"""
        return _propgrid.PGArrayStringEditorDialog_OnCustomNewAction(*args, **kwargs)

_propgrid.PGArrayStringEditorDialog_swigregister(PGArrayStringEditorDialog)

PG_COLOUR_WEB_BASE = _propgrid.PG_COLOUR_WEB_BASE
PG_COLOUR_CUSTOM = _propgrid.PG_COLOUR_CUSTOM
PG_COLOUR_UNSPECIFIED = _propgrid.PG_COLOUR_UNSPECIFIED
class ColourPropertyValue(_core.Object):
    """Proxy of C++ ColourPropertyValue class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_type = property(_propgrid.ColourPropertyValue_m_type_get, _propgrid.ColourPropertyValue_m_type_set)
    m_colour = property(_propgrid.ColourPropertyValue_m_colour_get, _propgrid.ColourPropertyValue_m_colour_set)
    __swig_destroy__ = _propgrid.delete_ColourPropertyValue
    __del__ = lambda self : None;
    def Init(*args, **kwargs):
        """Init(self, int type, Colour colour)"""
        return _propgrid.ColourPropertyValue_Init(*args, **kwargs)

    def __init__(self, *args): 
        """
        __init__(self) -> ColourPropertyValue
        __init__(self, ColourPropertyValue v) -> ColourPropertyValue
        __init__(self, Colour colour) -> ColourPropertyValue
        __init__(self, int type) -> ColourPropertyValue
        __init__(self, int type, Colour colour) -> ColourPropertyValue
        """
        _propgrid.ColourPropertyValue_swiginit(self,_propgrid.new_ColourPropertyValue(*args))
_propgrid.ColourPropertyValue_swigregister(ColourPropertyValue)

class FontProperty(PGProperty):
    """Proxy of C++ FontProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            Font value=wxFont()) -> FontProperty
        """
        _propgrid.FontProperty_swiginit(self,_propgrid.new_FontProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_FontProperty
    __del__ = lambda self : None;
_propgrid.FontProperty_swigregister(FontProperty)

class SystemColourProperty(EnumProperty):
    """Proxy of C++ SystemColourProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            ColourPropertyValue value=wxColourPropertyValue()) -> SystemColourProperty
        """
        _propgrid.SystemColourProperty_swiginit(self,_propgrid.new_SystemColourProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_SystemColourProperty
    __del__ = lambda self : None;
    def ColourToString(*args, **kwargs):
        """ColourToString(self, Colour col, int index, int argFlags=0) -> String"""
        return _propgrid.SystemColourProperty_ColourToString(*args, **kwargs)

    def GetCustomColourIndex(*args, **kwargs):
        """GetCustomColourIndex(self) -> int"""
        return _propgrid.SystemColourProperty_GetCustomColourIndex(*args, **kwargs)

    def QueryColourFromUser(*args, **kwargs):
        """QueryColourFromUser(self, wxVariant variant) -> bool"""
        return _propgrid.SystemColourProperty_QueryColourFromUser(*args, **kwargs)

    def GetColour(*args, **kwargs):
        """GetColour(self, int index) -> Colour"""
        return _propgrid.SystemColourProperty_GetColour(*args, **kwargs)

    def GetVal(*args, **kwargs):
        """GetVal(self, wxVariant pVariant=None) -> ColourPropertyValue"""
        return _propgrid.SystemColourProperty_GetVal(*args, **kwargs)

_propgrid.SystemColourProperty_swigregister(SystemColourProperty)

class ColourProperty(SystemColourProperty):
    """Proxy of C++ ColourProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            Colour value=*wxWHITE) -> ColourProperty
        """
        _propgrid.ColourProperty_swiginit(self,_propgrid.new_ColourProperty(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_ColourProperty
    __del__ = lambda self : None;
_propgrid.ColourProperty_swigregister(ColourProperty)

class PropertyGridPage(_core.EvtHandler,PropertyGridInterface,):
    """Proxy of C++ PropertyGridPage class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PropertyGridPage"""
        _propgrid.PropertyGridPage_swiginit(self,_propgrid.new_PropertyGridPage(*args, **kwargs))
    __swig_destroy__ = _propgrid.delete_PropertyGridPage
    __del__ = lambda self : None;
    def FitColumns(*args, **kwargs):
        """FitColumns(self) -> Size"""
        return _propgrid.PropertyGridPage_FitColumns(*args, **kwargs)

    def GetIndex(*args, **kwargs):
        """GetIndex(self) -> int"""
        return _propgrid.PropertyGridPage_GetIndex(*args, **kwargs)

    def GetSplitterPosition(*args, **kwargs):
        """GetSplitterPosition(self, int col=0) -> int"""
        return _propgrid.PropertyGridPage_GetSplitterPosition(*args, **kwargs)

    def GetRoot(*args, **kwargs):
        """GetRoot(self) -> PGProperty"""
        return _propgrid.PropertyGridPage_GetRoot(*args, **kwargs)

    def GetStatePtr(*args):
        """
        GetStatePtr(self)
        GetStatePtr(self)
        """
        return _propgrid.PropertyGridPage_GetStatePtr(*args)

    def GetToolId(*args, **kwargs):
        """GetToolId(self) -> int"""
        return _propgrid.PropertyGridPage_GetToolId(*args, **kwargs)

    def Init(*args, **kwargs):
        """Init(self)"""
        return _propgrid.PropertyGridPage_Init(*args, **kwargs)

    def IsHandlingAllEvents(*args, **kwargs):
        """IsHandlingAllEvents(self) -> bool"""
        return _propgrid.PropertyGridPage_IsHandlingAllEvents(*args, **kwargs)

    def OnShow(*args, **kwargs):
        """OnShow(self)"""
        return _propgrid.PropertyGridPage_OnShow(*args, **kwargs)

    def SetSplitterPosition(*args, **kwargs):
        """SetSplitterPosition(self, int splitterPos, int col=0)"""
        return _propgrid.PropertyGridPage_SetSplitterPosition(*args, **kwargs)

_propgrid.PropertyGridPage_swigregister(PropertyGridPage)

class PropertyGridManager(_windows.Panel,PropertyGridInterface):
    """Proxy of C++ PropertyGridManager class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=ID_ANY, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=(0), 
            String name=wxPropertyGridManagerNameStr) -> PropertyGridManager
        """
        _propgrid.PropertyGridManager_swiginit(self,_propgrid.new_PropertyGridManager(*args, **kwargs))
        
        self._setOORInfo(self)
        self.DoDefaultTypeMappings()
        self.edited_objects = {}
        self.DoDefaultValueTypeMappings()
        if not hasattr(self.__class__,'_vt2setter'):
            self.__class__._vt2setter = {}
    

    __swig_destroy__ = _propgrid.delete_PropertyGridManager
    __del__ = lambda self : None;
    def AddPage(*args, **kwargs):
        """
        AddPage(self, String label=wxEmptyString, Bitmap bmp=wxNullBitmap, 
            PropertyGridPage pageObj=None) -> PropertyGridPage
        """
        return _propgrid.PropertyGridManager_AddPage(*args, **kwargs)

    def ClearPage(*args, **kwargs):
        """ClearPage(self, int page)"""
        return _propgrid.PropertyGridManager_ClearPage(*args, **kwargs)

    def CommitChangesFromEditor(*args, **kwargs):
        """CommitChangesFromEditor(self, int flags=0) -> bool"""
        return _propgrid.PropertyGridManager_CommitChangesFromEditor(*args, **kwargs)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=ID_ANY, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=(0), 
            String name=wxPropertyGridManagerNameStr) -> bool
        """
        return _propgrid.PropertyGridManager_Create(*args, **kwargs)

    def EnableCategories(*args, **kwargs):
        """EnableCategories(self, bool enable) -> bool"""
        return _propgrid.PropertyGridManager_EnableCategories(*args, **kwargs)

    def EnsureVisible(*args, **kwargs):
        """EnsureVisible(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridManager_EnsureVisible(*args, **kwargs)

    def GetColumnCount(*args, **kwargs):
        """GetColumnCount(self, int page=-1) -> int"""
        return _propgrid.PropertyGridManager_GetColumnCount(*args, **kwargs)

    def GetDescBoxHeight(*args, **kwargs):
        """GetDescBoxHeight(self) -> int"""
        return _propgrid.PropertyGridManager_GetDescBoxHeight(*args, **kwargs)

    def GetGrid(*args):
        """
        GetGrid(self) -> PropertyGrid
        GetGrid(self) -> PropertyGrid
        """
        return _propgrid.PropertyGridManager_GetGrid(*args)

    def GetIterator(*args):
        """
        GetIterator(self, int flags=PG_ITERATE_DEFAULT, PGProperty firstProp=None) -> PropertyGridIterator
        GetIterator(self, int flags=PG_ITERATE_DEFAULT, PGProperty firstProp=None) -> PropertyGridConstIterator
        GetIterator(self, int flags, int startPos) -> PropertyGridIterator
        GetIterator(self, int flags, int startPos) -> PropertyGridConstIterator
        """
        return _propgrid.PropertyGridManager_GetIterator(*args)

    def GetCurrentPage(*args, **kwargs):
        """GetCurrentPage(self) -> PropertyGridPage"""
        return _propgrid.PropertyGridManager_GetCurrentPage(*args, **kwargs)

    def GetPage(*args):
        """
        GetPage(self, int ind) -> PropertyGridPage
        GetPage(self, String name) -> PropertyGridPage
        """
        return _propgrid.PropertyGridManager_GetPage(*args)

    def GetPageByName(*args, **kwargs):
        """GetPageByName(self, String name) -> int"""
        return _propgrid.PropertyGridManager_GetPageByName(*args, **kwargs)

    def GetPageByState(*args, **kwargs):
        """GetPageByState(self,  pstate) -> int"""
        return _propgrid.PropertyGridManager_GetPageByState(*args, **kwargs)

    def GetPageCount(*args, **kwargs):
        """GetPageCount(self) -> size_t"""
        return _propgrid.PropertyGridManager_GetPageCount(*args, **kwargs)

    def GetPageName(*args, **kwargs):
        """GetPageName(self, int index) -> String"""
        return _propgrid.PropertyGridManager_GetPageName(*args, **kwargs)

    def GetPageRoot(*args, **kwargs):
        """GetPageRoot(self, int index) -> PGProperty"""
        return _propgrid.PropertyGridManager_GetPageRoot(*args, **kwargs)

    def GetSelectedPage(*args, **kwargs):
        """GetSelectedPage(self) -> int"""
        return _propgrid.PropertyGridManager_GetSelectedPage(*args, **kwargs)

    def GetSelectedProperty(*args, **kwargs):
        """GetSelectedProperty(self) -> PGProperty"""
        return _propgrid.PropertyGridManager_GetSelectedProperty(*args, **kwargs)

    def GetSelection(*args, **kwargs):
        """GetSelection(self) -> PGProperty"""
        return _propgrid.PropertyGridManager_GetSelection(*args, **kwargs)

    def GetToolBar(*args, **kwargs):
        """GetToolBar(self) -> wxToolBar"""
        return _propgrid.PropertyGridManager_GetToolBar(*args, **kwargs)

    def InsertPage(*args, **kwargs):
        """InsertPage(self, int index, String label, Bitmap bmp=wxNullBitmap, PropertyGridPage pageObj=None) -> PropertyGridPage"""
        return _propgrid.PropertyGridManager_InsertPage(*args, **kwargs)

    def IsAnyModified(*args, **kwargs):
        """IsAnyModified(self) -> bool"""
        return _propgrid.PropertyGridManager_IsAnyModified(*args, **kwargs)

    def IsFrozen(*args, **kwargs):
        """
        IsFrozen(self) -> bool

        Returns ``True`` if the window has been frozen and not thawed yet.

        :see: `Freeze` and `Thaw`
        """
        return _propgrid.PropertyGridManager_IsFrozen(*args, **kwargs)

    def IsPageModified(*args, **kwargs):
        """IsPageModified(self, size_t index) -> bool"""
        return _propgrid.PropertyGridManager_IsPageModified(*args, **kwargs)

    def IsPropertySelected(*args, **kwargs):
        """IsPropertySelected(self, PGPropArg id) -> bool"""
        return _propgrid.PropertyGridManager_IsPropertySelected(*args, **kwargs)

    def RemovePage(*args, **kwargs):
        """RemovePage(self, int page) -> bool"""
        return _propgrid.PropertyGridManager_RemovePage(*args, **kwargs)

    def SelectPage(*args):
        """
        SelectPage(self, int index)
        SelectPage(self, String label)
        SelectPage(self, PropertyGridPage ptr)
        """
        return _propgrid.PropertyGridManager_SelectPage(*args)

    def SelectProperty(*args, **kwargs):
        """SelectProperty(self, PGPropArg id, bool focus=False) -> bool"""
        return _propgrid.PropertyGridManager_SelectProperty(*args, **kwargs)

    def SetColumnTitle(*args, **kwargs):
        """SetColumnTitle(self, int idx, String title)"""
        return _propgrid.PropertyGridManager_SetColumnTitle(*args, **kwargs)

    def SetColumnCount(*args, **kwargs):
        """SetColumnCount(self, int colCount, int page=-1)"""
        return _propgrid.PropertyGridManager_SetColumnCount(*args, **kwargs)

    def SetDescription(*args, **kwargs):
        """SetDescription(self, String label, String content)"""
        return _propgrid.PropertyGridManager_SetDescription(*args, **kwargs)

    def SetDescBoxHeight(*args, **kwargs):
        """SetDescBoxHeight(self, int ht, bool refresh=True)"""
        return _propgrid.PropertyGridManager_SetDescBoxHeight(*args, **kwargs)

    def SetSplitterLeft(*args, **kwargs):
        """SetSplitterLeft(self, bool subProps=False, bool allPages=True)"""
        return _propgrid.PropertyGridManager_SetSplitterLeft(*args, **kwargs)

    def SetPageSplitterLeft(*args, **kwargs):
        """SetPageSplitterLeft(self, int page, bool subProps=False)"""
        return _propgrid.PropertyGridManager_SetPageSplitterLeft(*args, **kwargs)

    def SetPageSplitterPosition(*args, **kwargs):
        """SetPageSplitterPosition(self, int page, int pos, int column=0)"""
        return _propgrid.PropertyGridManager_SetPageSplitterPosition(*args, **kwargs)

    def SetSplitterPosition(*args, **kwargs):
        """SetSplitterPosition(self, int pos, int column=0)"""
        return _propgrid.PropertyGridManager_SetSplitterPosition(*args, **kwargs)

    def SetId(*args, **kwargs):
        """
        SetId(self, int winid)

        Sets the identifier of the window.  Each window has an integer
        identifier. If the application has not provided one, an identifier
        will be generated. Normally, the identifier should be provided on
        creation and should not be modified subsequently.
        """
        return _propgrid.PropertyGridManager_SetId(*args, **kwargs)

    def Freeze(*args, **kwargs):
        """
        Freeze(self)

        Freezes the window or, in other words, prevents any updates from
        taking place on screen, the window is not redrawn at all. Thaw must be
        called to reenable window redrawing.  Calls to Freeze/Thaw may be
        nested, with the actual Thaw being delayed until all the nesting has
        been undone.

        This method is useful for visual appearance optimization (for example,
        it is a good idea to use it before inserting large amount of text into
        a wxTextCtrl under wxGTK) but is not implemented on all platforms nor
        for all controls so it is mostly just a hint to wxWindows and not a
        mandatory directive.
        """
        return _propgrid.PropertyGridManager_Freeze(*args, **kwargs)

    def Thaw(*args, **kwargs):
        """
        Thaw(self)

        Reenables window updating after a previous call to Freeze.  Calls to
        Freeze/Thaw may be nested, so Thaw must be called the same number of
        times that Freeze was before the window will be updated.
        """
        return _propgrid.PropertyGridManager_Thaw(*args, **kwargs)

    def Reparent(*args, **kwargs):
        """Reparent(self, wxWindowBase newParent) -> bool"""
        return _propgrid.PropertyGridManager_Reparent(*args, **kwargs)

    def GetValuesFromPage(self,
                          page,
                          dict_=None,
                          as_strings=False,
                          inc_attributes=False):
        "Same as GetValues, but returns values from specific page only."
        "For argument descriptions, see GetValues."
        return page.GetPropertyValues(dict_, as_strings, inc_attributes)

_propgrid.PropertyGridManager_swigregister(PropertyGridManager)


def NewPropertyCategory(*args, **kwargs):
  """NewPropertyCategory(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL)) -> PGProperty"""
  return _propgrid.NewPropertyCategory(*args, **kwargs)

def NewStringProperty(*args, **kwargs):
  """
    NewStringProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        String value=wxEmptyString) -> PGProperty
    """
  return _propgrid.NewStringProperty(*args, **kwargs)

def NewUIntProperty(*args, **kwargs):
  """
    NewUIntProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        long value=0) -> PGProperty
    """
  return _propgrid.NewUIntProperty(*args, **kwargs)

def NewIntProperty(*args, **kwargs):
  """
    NewIntProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        long value=0) -> PGProperty
    """
  return _propgrid.NewIntProperty(*args, **kwargs)

def NewFloatProperty(*args, **kwargs):
  """
    NewFloatProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        double value=0.0) -> PGProperty
    """
  return _propgrid.NewFloatProperty(*args, **kwargs)

def NewBoolProperty(*args, **kwargs):
  """
    NewBoolProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        bool value=False) -> PGProperty
    """
  return _propgrid.NewBoolProperty(*args, **kwargs)

def NewEnumProperty(*args, **kwargs):
  """
    NewEnumProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        wxArrayString labels=wxArrayString(), 
        wxArrayInt values=wxArrayInt(), 
        int value=0) -> PGProperty
    """
  return _propgrid.NewEnumProperty(*args, **kwargs)

def NewEditEnumProperty(*args, **kwargs):
  """
    NewEditEnumProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        wxArrayString labels=wxArrayString(), 
        wxArrayInt values=wxArrayInt(), 
        String value=wxEmptyString) -> PGProperty
    """
  return _propgrid.NewEditEnumProperty(*args, **kwargs)

def NewFlagsProperty(*args, **kwargs):
  """
    NewFlagsProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        wxArrayString labels=wxArrayString(), 
        wxArrayInt values=wxArrayInt(), 
        int value=0) -> PGProperty
    """
  return _propgrid.NewFlagsProperty(*args, **kwargs)

def NewLongStringProperty(*args, **kwargs):
  """
    NewLongStringProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        String value=wxEmptyString) -> PGProperty
    """
  return _propgrid.NewLongStringProperty(*args, **kwargs)

def NewFileProperty(*args, **kwargs):
  """
    NewFileProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        String value=wxEmptyString) -> PGProperty
    """
  return _propgrid.NewFileProperty(*args, **kwargs)

def NewDirProperty(*args, **kwargs):
  """
    NewDirProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        String value=wxEmptyString) -> PGProperty
    """
  return _propgrid.NewDirProperty(*args, **kwargs)

def NewArrayStringProperty(*args, **kwargs):
  """
    NewArrayStringProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        wxArrayString value=wxArrayString()) -> PGProperty
    """
  return _propgrid.NewArrayStringProperty(*args, **kwargs)

def NewFontProperty(*args, **kwargs):
  """
    NewFontProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        Font value=wxFont()) -> PGProperty
    """
  return _propgrid.NewFontProperty(*args, **kwargs)

def NewSystemColourProperty(*args, **kwargs):
  """
    NewSystemColourProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        ColourPropertyValue value=wxColourPropertyValue()) -> PGProperty
    """
  return _propgrid.NewSystemColourProperty(*args, **kwargs)

def NewColourProperty(*args, **kwargs):
  """
    NewColourProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        Colour value=wxColour()) -> PGProperty
    """
  return _propgrid.NewColourProperty(*args, **kwargs)

def NewCursorProperty(*args, **kwargs):
  """
    NewCursorProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        int value=0) -> PGProperty
    """
  return _propgrid.NewCursorProperty(*args, **kwargs)

def NewImageFileProperty(*args, **kwargs):
  """
    NewImageFileProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        String value=wxEmptyString) -> PGProperty
    """
  return _propgrid.NewImageFileProperty(*args, **kwargs)

def NewMultiChoiceProperty(*args, **kwargs):
  """
    NewMultiChoiceProperty(String label, String name=(*wxPGProperty::sm_wxPG_LABEL), 
        wxArrayString choices=wxArrayString(), 
        wxArrayString value=wxArrayString()) -> PGProperty
    """
  return _propgrid.NewMultiChoiceProperty(*args, **kwargs)

def NewDateProperty(*args, **kwargs):
  """
    NewDateProperty(String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
        DateTime value=wxDateTime()) -> PGProperty
    """
  return _propgrid.NewDateProperty(*args, **kwargs)
class PyFloatProperty(FloatProperty):
    """Proxy of C++ PyFloatProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            double value=0.0) -> PyFloatProperty
        """
        _propgrid.PyFloatProperty_swiginit(self,_propgrid.new_PyFloatProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyFloatProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyFloatProperty__SetSelf(*args, **kwargs)

_propgrid.PyFloatProperty_swigregister(PyFloatProperty)

class PyEditorDialogAdapter(PGEditorDialogAdapter):
    """Proxy of C++ PyEditorDialogAdapter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyEditorDialogAdapter"""
        _propgrid.PyEditorDialogAdapter_swiginit(self,_propgrid.new_PyEditorDialogAdapter(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyEditorDialogAdapter, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyEditorDialogAdapter__SetSelf(*args, **kwargs)

_propgrid.PyEditorDialogAdapter_swigregister(PyEditorDialogAdapter)

class PyEnumProperty(EnumProperty):
    """Proxy of C++ PyEnumProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString labels=wxArrayString(), 
            wxArrayInt values=wxArrayInt(), 
            int value=0) -> PyEnumProperty
        """
        _propgrid.PyEnumProperty_swiginit(self,_propgrid.new_PyEnumProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyEnumProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyEnumProperty__SetSelf(*args, **kwargs)

_propgrid.PyEnumProperty_swigregister(PyEnumProperty)

class PyArrayStringProperty(ArrayStringProperty):
    """Proxy of C++ PyArrayStringProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString value=wxArrayString()) -> PyArrayStringProperty
        """
        _propgrid.PyArrayStringProperty_swiginit(self,_propgrid.new_PyArrayStringProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyArrayStringProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyArrayStringProperty__SetSelf(*args, **kwargs)

_propgrid.PyArrayStringProperty_swigregister(PyArrayStringProperty)

class PyComboBoxEditor(PGComboBoxEditor):
    """Proxy of C++ PyComboBoxEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyComboBoxEditor"""
        _propgrid.PyComboBoxEditor_swiginit(self,_propgrid.new_PyComboBoxEditor(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyComboBoxEditor, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyComboBoxEditor__SetSelf(*args, **kwargs)

_propgrid.PyComboBoxEditor_swigregister(PyComboBoxEditor)

class PyFileDialogAdapter(PGFileDialogAdapter):
    """Proxy of C++ PyFileDialogAdapter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyFileDialogAdapter"""
        _propgrid.PyFileDialogAdapter_swiginit(self,_propgrid.new_PyFileDialogAdapter(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyFileDialogAdapter, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyFileDialogAdapter__SetSelf(*args, **kwargs)

_propgrid.PyFileDialogAdapter_swigregister(PyFileDialogAdapter)

class PyStringProperty(StringProperty):
    """Proxy of C++ PyStringProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            String value=wxEmptyString) -> PyStringProperty
        """
        _propgrid.PyStringProperty_swiginit(self,_propgrid.new_PyStringProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyStringProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyStringProperty__SetSelf(*args, **kwargs)

_propgrid.PyStringProperty_swigregister(PyStringProperty)

class PyLongStringDialogAdapter(PGLongStringDialogAdapter):
    """Proxy of C++ PyLongStringDialogAdapter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyLongStringDialogAdapter"""
        _propgrid.PyLongStringDialogAdapter_swiginit(self,_propgrid.new_PyLongStringDialogAdapter(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyLongStringDialogAdapter, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyLongStringDialogAdapter__SetSelf(*args, **kwargs)

_propgrid.PyLongStringDialogAdapter_swigregister(PyLongStringDialogAdapter)

class PyEditEnumProperty(EditEnumProperty):
    """Proxy of C++ PyEditEnumProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, String label, String name, wxChar labels, long values, 
            String value) -> PyEditEnumProperty
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString labels=wxArrayString(), 
            wxArrayInt values=wxArrayInt(), 
            String value=wxEmptyString) -> PyEditEnumProperty
        __init__(self, String label, String name, PGChoices choices, String value=wxEmptyString) -> PyEditEnumProperty
        __init__(self, String label, String name, wxChar labels, long values, 
            PGChoices choicesCache, String value) -> PyEditEnumProperty
        """
        _propgrid.PyEditEnumProperty_swiginit(self,_propgrid.new_PyEditEnumProperty(*args))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyEditEnumProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyEditEnumProperty__SetSelf(*args, **kwargs)

_propgrid.PyEditEnumProperty_swigregister(PyEditEnumProperty)

class PyTextCtrlEditor(PGTextCtrlEditor):
    """Proxy of C++ PyTextCtrlEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyTextCtrlEditor"""
        _propgrid.PyTextCtrlEditor_swiginit(self,_propgrid.new_PyTextCtrlEditor(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyTextCtrlEditor, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyTextCtrlEditor__SetSelf(*args, **kwargs)

_propgrid.PyTextCtrlEditor_swigregister(PyTextCtrlEditor)

class PySystemColourProperty(SystemColourProperty):
    """Proxy of C++ PySystemColourProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            ColourPropertyValue value=wxColourPropertyValue()) -> PySystemColourProperty
        __init__(self, String label, String name, wxChar labels, long values, 
            PGChoices choicesCache, ColourPropertyValue value) -> PySystemColourProperty
        __init__(self, String label, String name, wxChar labels, long values, 
            PGChoices choicesCache, Colour value) -> PySystemColourProperty
        """
        _propgrid.PySystemColourProperty_swiginit(self,_propgrid.new_PySystemColourProperty(*args))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PySystemColourProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PySystemColourProperty__SetSelf(*args, **kwargs)

_propgrid.PySystemColourProperty_swigregister(PySystemColourProperty)

class PyFlagsProperty(FlagsProperty):
    """Proxy of C++ PyFlagsProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            wxArrayString labels=wxArrayString(), 
            wxArrayInt values=wxArrayInt(), 
            int value=0) -> PyFlagsProperty
        """
        _propgrid.PyFlagsProperty_swiginit(self,_propgrid.new_PyFlagsProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyFlagsProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyFlagsProperty__SetSelf(*args, **kwargs)

_propgrid.PyFlagsProperty_swigregister(PyFlagsProperty)

class PyFontProperty(FontProperty):
    """Proxy of C++ PyFontProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            Font value=wxFont()) -> PyFontProperty
        """
        _propgrid.PyFontProperty_swiginit(self,_propgrid.new_PyFontProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyFontProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyFontProperty__SetSelf(*args, **kwargs)

_propgrid.PyFontProperty_swigregister(PyFontProperty)

class PyColourProperty(ColourProperty):
    """Proxy of C++ PyColourProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            Colour value=*wxWHITE) -> PyColourProperty
        """
        _propgrid.PyColourProperty_swiginit(self,_propgrid.new_PyColourProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyColourProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyColourProperty__SetSelf(*args, **kwargs)

_propgrid.PyColourProperty_swigregister(PyColourProperty)

class PyFileProperty(FileProperty):
    """Proxy of C++ PyFileProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            String value=wxEmptyString) -> PyFileProperty
        """
        _propgrid.PyFileProperty_swiginit(self,_propgrid.new_PyFileProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyFileProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyFileProperty__SetSelf(*args, **kwargs)

_propgrid.PyFileProperty_swigregister(PyFileProperty)

class PyIntProperty(IntProperty):
    """Proxy of C++ PyIntProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            long value=0) -> PyIntProperty
        __init__(self, String label, String name, wxLongLong value) -> PyIntProperty
        """
        _propgrid.PyIntProperty_swiginit(self,_propgrid.new_PyIntProperty(*args))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyIntProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyIntProperty__SetSelf(*args, **kwargs)

_propgrid.PyIntProperty_swigregister(PyIntProperty)

class PyEditor(PGEditor):
    """Proxy of C++ PyEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyEditor"""
        _propgrid.PyEditor_swiginit(self,_propgrid.new_PyEditor(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyEditor, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyEditor__SetSelf(*args, **kwargs)

_propgrid.PyEditor_swigregister(PyEditor)

class PyChoiceEditor(PGChoiceEditor):
    """Proxy of C++ PyChoiceEditor class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyChoiceEditor"""
        _propgrid.PyChoiceEditor_swiginit(self,_propgrid.new_PyChoiceEditor(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyChoiceEditor, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyChoiceEditor__SetSelf(*args, **kwargs)

_propgrid.PyChoiceEditor_swigregister(PyChoiceEditor)

class PyProperty(PGProperty):
    """Proxy of C++ PyProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PyProperty
        __init__(self, String label, String name) -> PyProperty
        """
        _propgrid.PyProperty_swiginit(self,_propgrid.new_PyProperty(*args))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyProperty__SetSelf(*args, **kwargs)

_propgrid.PyProperty_swigregister(PyProperty)

class PyUIntProperty(UIntProperty):
    """Proxy of C++ PyUIntProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            long value=0) -> PyUIntProperty
        __init__(self, String label, String name, wxULongLong value) -> PyUIntProperty
        """
        _propgrid.PyUIntProperty_swiginit(self,_propgrid.new_PyUIntProperty(*args))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyUIntProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyUIntProperty__SetSelf(*args, **kwargs)

_propgrid.PyUIntProperty_swigregister(PyUIntProperty)

class PyLongStringProperty(LongStringProperty):
    """Proxy of C++ PyLongStringProperty class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=(*wxPGProperty::sm_wxPG_LABEL), String name=(*wxPGProperty::sm_wxPG_LABEL), 
            String value=wxEmptyString) -> PyLongStringProperty
        """
        _propgrid.PyLongStringProperty_swiginit(self,_propgrid.new_PyLongStringProperty(*args, **kwargs))
        self._SetSelf(self); self._RegisterMethods()

    def CallSuperMethod(self, *args, **kwargs):
        funcname = args[0]
        args2 = list(args)
        args2[0] = self
        self._super_call = True
        try:
            res = getattr(PyLongStringProperty, funcname)(*args2, **kwargs)
        finally:
            del self._super_call
        return res

    def _RegisterMethods(self):
        cls = self.__class__
        if not hasattr(cls,'_pyswig_methods_registered'):
            cls._pyswig_methods_registered = True
            ls = [ab for ab in cls.__dict__.iteritems()]
            for a, b in ls:
                if not a.startswith('_'):
                    setattr(cls, '%s_t_'%a, b)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return _propgrid.PyLongStringProperty__SetSelf(*args, **kwargs)

_propgrid.PyLongStringProperty_swigregister(PyLongStringProperty)


def RegisterEditor(*args, **kwargs):
  """RegisterEditor(PGEditor editor, String editorName)"""
  return _propgrid.RegisterEditor(*args, **kwargs)
EVT_PG_CHANGED = wx.PyEventBinder( wxEVT_PG_CHANGED, 1 )
EVT_PG_CHANGING = wx.PyEventBinder( wxEVT_PG_CHANGING, 1 )
EVT_PG_SELECTED = wx.PyEventBinder( wxEVT_PG_SELECTED, 1 )
EVT_PG_HIGHLIGHTED = wx.PyEventBinder( wxEVT_PG_HIGHLIGHTED, 1 )
EVT_PG_RIGHT_CLICK = wx.PyEventBinder( wxEVT_PG_RIGHT_CLICK, 1 )
EVT_PG_PAGE_CHANGED = wx.PyEventBinder( wxEVT_PG_PAGE_CHANGED, 1 )
EVT_PG_ITEM_COLLAPSED = wx.PyEventBinder( wxEVT_PG_ITEM_COLLAPSED, 1 )
EVT_PG_ITEM_EXPANDED = wx.PyEventBinder( wxEVT_PG_ITEM_EXPANDED, 1 )
EVT_PG_DOUBLE_CLICK = wx.PyEventBinder( wxEVT_PG_DOUBLE_CLICK, 1 )
EVT_PG_LABEL_EDIT_BEGIN = wx.PyEventBinder( wxEVT_PG_LABEL_EDIT_BEGIN, 1 )
EVT_PG_LABEL_EDIT_ENDING = wx.PyEventBinder( wxEVT_PG_LABEL_EDIT_ENDING, 1 )
EVT_PG_COL_BEGIN_DRAG = wx.PyEventBinder( wxEVT_PG_COL_BEGIN_DRAG, 1 )
EVT_PG_COL_DRAGGING = wx.PyEventBinder( wxEVT_PG_COL_DRAGGING, 1 )
EVT_PG_COL_END_DRAG = wx.PyEventBinder( wxEVT_PG_COL_END_DRAG, 1 )

LABEL_AS_NAME = "@!"
DEFAULT_IMAGE_SIZE = (-1,-1)
NO_IMAGE_SIZE = (0,0)

PG_BOOL_USE_CHECKBOX = "UseCheckbox"
PG_BOOL_USE_DOUBLE_CLICK_CYCLING = "UseDClickCycling"
PG_FLOAT_PRECISION = "Precision"
PG_STRING_PASSWORD = "Password"
PG_UINT_BASE = "Base"
PG_UINT_PREFIX = "Prefix"
PG_FILE_WILDCARD = "Wildcard"
PG_FILE_SHOW_FULL_PATH = "ShowFullPath"
PG_FILE_SHOW_RELATIVE_PATH = "ShowRelativePath"
PG_FILE_INITIAL_PATH = "InitialPath"
PG_FILE_DIALOG_TITLE = "DialogTitle"
PG_DIR_DIALOG_MESSAGE = "DialogMessage"
PG_DATE_FORMAT = "DateFormat"
PG_DATE_PICKER_STYLE = "PickerStyle"


PropertyCategory = NewPropertyCategory
StringProperty = NewStringProperty
IntProperty = NewIntProperty
UIntProperty = NewUIntProperty
FloatProperty = NewFloatProperty
BoolProperty = NewBoolProperty
EnumProperty = NewEnumProperty
EditEnumProperty = NewEditEnumProperty
FlagsProperty = NewFlagsProperty
LongStringProperty = NewLongStringProperty
FileProperty = NewFileProperty
DirProperty = NewDirProperty
ArrayStringProperty = NewArrayStringProperty
FontProperty = NewFontProperty
SystemColourProperty = NewSystemColourProperty
ColourProperty = NewColourProperty
CursorProperty = NewCursorProperty
ImageFileProperty = NewImageFileProperty
MultiChoiceProperty = NewMultiChoiceProperty
DateProperty = NewDateProperty









