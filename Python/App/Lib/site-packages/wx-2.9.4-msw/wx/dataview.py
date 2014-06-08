# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

"""
The `DataViewCtrl` class can display data in either a tree-like
fashion, in a tabular form, or in a combination of the two.  It is a
native widget on the platforms that provide such a control, (currently
OS X and GTK) and generic elsewhere.
"""

import _dataview
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
wx = _core 
__docfilter__ = wx.__DocFilter(globals()) 
DVC_DEFAULT_RENDERER_SIZE = _dataview.DVC_DEFAULT_RENDERER_SIZE
DVC_DEFAULT_WIDTH = _dataview.DVC_DEFAULT_WIDTH
DVC_TOGGLE_DEFAULT_WIDTH = _dataview.DVC_TOGGLE_DEFAULT_WIDTH
DVC_DEFAULT_MINWIDTH = _dataview.DVC_DEFAULT_MINWIDTH
DVR_DEFAULT_ALIGNMENT = _dataview.DVR_DEFAULT_ALIGNMENT
#---------------------------------------------------------------------------

class DataViewItem(object):
    """
    wxDataViewItem is a small opaque class that represents an item in a
    `DataViewCtrl` in a persistent way, i.e. indepent of the position of
    the item in the control or changes to its contents.  It contains a C
    void pointer which is used as the internal ID value for the item.  If
    the ID is NULL then the DataViewItem is considered invalid and the
    `IsOk` method will return False, which is used in many places in the
    API to indicate that no item was found.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, PyLong ID=0) -> DataViewItem

        wxDataViewItem is a small opaque class that represents an item in a
        `DataViewCtrl` in a persistent way, i.e. indepent of the position of
        the item in the control or changes to its contents.  It contains a C
        void pointer which is used as the internal ID value for the item.  If
        the ID is NULL then the DataViewItem is considered invalid and the
        `IsOk` method will return False, which is used in many places in the
        API to indicate that no item was found.
        """
        _dataview.DataViewItem_swiginit(self,_dataview.new_DataViewItem(*args, **kwargs))
    __swig_destroy__ = _dataview.delete_DataViewItem
    __del__ = lambda self : None;
    def IsOk(*args, **kwargs):
        """
        IsOk(self) -> bool

        Returns ``True`` if the object refers to an actual item in the data
        view control.
        """
        return _dataview.DataViewItem_IsOk(*args, **kwargs)

    def __nonzero__(self): return self.IsOk() 
    def GetID(*args, **kwargs):
        """GetID(self) -> PyLong"""
        return _dataview.DataViewItem_GetID(*args, **kwargs)

    ID = property(GetID) 
    def __hash__(*args, **kwargs):
        """__hash__(self) -> long"""
        return _dataview.DataViewItem___hash__(*args, **kwargs)

    def __cmp__(*args, **kwargs):
        """__cmp__(self, DataViewItem other) -> int"""
        return _dataview.DataViewItem___cmp__(*args, **kwargs)

_dataview.DataViewItem_swigregister(DataViewItem)
cvar = _dataview.cvar
DataViewCtrlNameStr = cvar.DataViewCtrlNameStr

class DataViewItemArray_iterator(object):
    """This class serves as an iterator for a wxDataViewItemArray object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewItemArray_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> DataViewItem"""
        return _dataview.DataViewItemArray_iterator_next(*args, **kwargs)

_dataview.DataViewItemArray_iterator_swigregister(DataViewItemArray_iterator)

class DataViewItemArray(object):
    """
    This class wraps a wxArray-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewItemArray
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return _dataview.DataViewItemArray___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> DataViewItem"""
        return _dataview.DataViewItemArray___getitem__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> DataViewItemArray_iterator"""
        return _dataview.DataViewItemArray___iter__(*args, **kwargs)

    def append(*args, **kwargs):
        """append(self, DataViewItem object)"""
        return _dataview.DataViewItemArray_append(*args, **kwargs)

    def insert(*args, **kwargs):
        """insert(self, size_t index, DataViewItem object)"""
        return _dataview.DataViewItemArray_insert(*args, **kwargs)

    def __repr__(self):
        return "wxDataViewItemArray: " + repr(list(self))

_dataview.DataViewItemArray_swigregister(DataViewItemArray)

NullDataViewItem = DataViewItem() 
#---------------------------------------------------------------------------

class DataViewModelNotifier(object):
    """
    This class allows multiple entities to be notified when a change
    happens in a `DataViewModel` instance, and it mirrors the notification
    interface in that class.  To add your own notifier object to a model,
    derive a new class from `PyDataViewModelNotifier`, override the
    methods you are interested in, and assign an instance of it to the
    model with `DataViewModel.AddNotifier`.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewModelNotifier
    __del__ = lambda self : None;
    def ItemAdded(*args, **kwargs):
        """
        ItemAdded(self, DataViewItem parent, DataViewItem item) -> bool

        Override this to be informed that an item has been added to the data
        model.
        """
        return _dataview.DataViewModelNotifier_ItemAdded(*args, **kwargs)

    def ItemDeleted(*args, **kwargs):
        """
        ItemDeleted(self, DataViewItem parent, DataViewItem item) -> bool

        Override this to be informed that an item has been deleted.
        """
        return _dataview.DataViewModelNotifier_ItemDeleted(*args, **kwargs)

    def ItemChanged(*args, **kwargs):
        """
        ItemChanged(self, DataViewItem item) -> bool

        Override this to be informed that an item's value has changed.
        """
        return _dataview.DataViewModelNotifier_ItemChanged(*args, **kwargs)

    def ItemsAdded(*args, **kwargs):
        """
        ItemsAdded(self, DataViewItem parent, DataViewItemArray items) -> bool

        Override this to be informed that several items have been added to the model.
        """
        return _dataview.DataViewModelNotifier_ItemsAdded(*args, **kwargs)

    def ItemsDeleted(*args, **kwargs):
        """
        ItemsDeleted(self, DataViewItem parent, DataViewItemArray items) -> bool

        Override this to be informed that several items have been deleted.
        """
        return _dataview.DataViewModelNotifier_ItemsDeleted(*args, **kwargs)

    def ItemsChanged(*args, **kwargs):
        """
        ItemsChanged(self, DataViewItemArray items) -> bool

        Override this to be informed that several items have been changed.
        """
        return _dataview.DataViewModelNotifier_ItemsChanged(*args, **kwargs)

    def ValueChanged(*args, **kwargs):
        """
        ValueChanged(self, DataViewItem item, unsigned int col) -> bool

        Override this to be informed that a value has changed in the model.
        This differs from `ItemChanged` in that this method is sensitive to
        changes in sub-elements of an item, not just the whole item (row).
        """
        return _dataview.DataViewModelNotifier_ValueChanged(*args, **kwargs)

    def Cleared(*args, **kwargs):
        """
        Cleared(self) -> bool

        Override this to be informed that all data has been cleared.  The
        control will read the visible data items from the model again.
        """
        return _dataview.DataViewModelNotifier_Cleared(*args, **kwargs)

    def BeforeReset(*args, **kwargs):
        """BeforeReset(self) -> bool"""
        return _dataview.DataViewModelNotifier_BeforeReset(*args, **kwargs)

    def AfterReset(*args, **kwargs):
        """AfterReset(self) -> bool"""
        return _dataview.DataViewModelNotifier_AfterReset(*args, **kwargs)

    def Resort(*args, **kwargs):
        """
        Resort(self)

        Override this to be informed that a resort has been initiated after
        the sort function has been changed.
        """
        return _dataview.DataViewModelNotifier_Resort(*args, **kwargs)

    def SetOwner(*args, **kwargs):
        """
        SetOwner(self, DataViewModel owner)

        Sets the owner (the model) of this notifier.  Used internally.
        """
        return _dataview.DataViewModelNotifier_SetOwner(*args, **kwargs)

    def GetOwner(*args, **kwargs):
        """
        GetOwner(self) -> DataViewModel

        Returns the owner (the model) of this notifier.
        """
        return _dataview.DataViewModelNotifier_GetOwner(*args, **kwargs)

    Owner = property(GetOwner,SetOwner) 
_dataview.DataViewModelNotifier_swigregister(DataViewModelNotifier)

class PyDataViewModelNotifier(DataViewModelNotifier):
    """
    This class is a version of `DataViewModelNotifier` that has been
    engineered to know how to reflect the C++ virtual method calls to
    Python methods in the derived class.  Use this class as your base
    class instead of `DataViewModelNotifier`.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PyDataViewModelNotifier

        This class is a version of `DataViewModelNotifier` that has been
        engineered to know how to reflect the C++ virtual method calls to
        Python methods in the derived class.  Use this class as your base
        class instead of `DataViewModelNotifier`.
        """
        _dataview.PyDataViewModelNotifier_swiginit(self,_dataview.new_PyDataViewModelNotifier(*args, **kwargs))
        PyDataViewModelNotifier._setCallbackInfo(self, self, PyDataViewModelNotifier)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return _dataview.PyDataViewModelNotifier__setCallbackInfo(*args, **kwargs)

_dataview.PyDataViewModelNotifier_swigregister(PyDataViewModelNotifier)

#---------------------------------------------------------------------------

class DataViewItemAttr(object):
    """Proxy of C++ DataViewItemAttr class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> DataViewItemAttr"""
        _dataview.DataViewItemAttr_swiginit(self,_dataview.new_DataViewItemAttr(*args, **kwargs))
    __swig_destroy__ = _dataview.delete_DataViewItemAttr
    __del__ = lambda self : None;
    def SetColour(*args, **kwargs):
        """SetColour(self, Colour colour)"""
        return _dataview.DataViewItemAttr_SetColour(*args, **kwargs)

    def SetBold(*args, **kwargs):
        """SetBold(self, bool set)"""
        return _dataview.DataViewItemAttr_SetBold(*args, **kwargs)

    def SetItalic(*args, **kwargs):
        """SetItalic(self, bool set)"""
        return _dataview.DataViewItemAttr_SetItalic(*args, **kwargs)

    def HasColour(*args, **kwargs):
        """HasColour(self) -> bool"""
        return _dataview.DataViewItemAttr_HasColour(*args, **kwargs)

    def GetColour(*args, **kwargs):
        """GetColour(self) -> Colour"""
        return _dataview.DataViewItemAttr_GetColour(*args, **kwargs)

    def HasFont(*args, **kwargs):
        """HasFont(self) -> bool"""
        return _dataview.DataViewItemAttr_HasFont(*args, **kwargs)

    def GetBold(*args, **kwargs):
        """GetBold(self) -> bool"""
        return _dataview.DataViewItemAttr_GetBold(*args, **kwargs)

    def GetItalic(*args, **kwargs):
        """GetItalic(self) -> bool"""
        return _dataview.DataViewItemAttr_GetItalic(*args, **kwargs)

    def IsDefault(*args, **kwargs):
        """IsDefault(self) -> bool"""
        return _dataview.DataViewItemAttr_IsDefault(*args, **kwargs)

    def GetEffectiveFont(*args, **kwargs):
        """GetEffectiveFont(self, Font font) -> Font"""
        return _dataview.DataViewItemAttr_GetEffectiveFont(*args, **kwargs)

    Colour = property(GetColour,SetColour) 
    Bold = property(GetBold,SetBold) 
    Italic = property(GetItalic,SetItalic) 
_dataview.DataViewItemAttr_swigregister(DataViewItemAttr)

#---------------------------------------------------------------------------

class DataViewModel(_core.RefCounter):
    """
    `DataViewModel` is the base class for managing all data to be
    displayed by a `DataViewCtrl`. All other models derive from it and
    must implement several of its methods in order to define a complete
    data model. In detail, you need to override `IsContainer`,
    `GetParent`, `GetChildren`, `GetColumnCount`, `GetColumnType` and
    `GetValue` in order to define the data model which acts as an
    interface between your actual data and the `DataViewCtrl`. Since you
    will usually also allow the `DataViewCtrl` to change your data through
    its graphical interface, you will also have to override `SetValue`
    which the `DataViewCtrl` will call when a change to some data has been
    commited.  To implement a custom data model derive a new class from
    `PyDataViewModel` and implement the required methods.

    The data that is presented through this data model is expected to
    change at run-time. You need to inform the data model when a change
    happened. Depending on what happened you need to call one of the
    following methods: `ValueChanged`, `ItemAdded`, `ItemDeleted`,
    `ItemChanged`, `Cleared`. There are plural forms for notification of
    addition, change or removal of several item at once. See `ItemsAdded`,
    `ItemsDeleted`, `ItemsChanged`.

    Note that ``DataViewModel`` does not define the position or index of
    any item in the control because different controls might display the
    same data differently. ``DataViewModel`` does provide a `Compare`
    method which the `DataViewCtrl` may use to sort the data either in
    conjunction with a column header or without (see `HasDefaultCompare`).

    This class maintains a list of `DataViewModelNotifier` objects which
    link this class to the specific implementations on the supported
    platforms so that e.g. calling `ValueChanged` on this model will just
    call `DataViewModelNotifier.ValueChanged` for each notifier that has
    been added. You can also add your own notifier in order to get
    informed about any changes to the data in the list model.

    Currently wxWidgets provides the following models in addition to this
    base class: `DataViewIndexListModel`, `DataViewVirtualListModel-, and
    `DataViewTreeStore`.  To create your own model from Python you will
    need to use the `PyDataViewModel` as your base class.

    :note: The C++ DataView classes use the wxVariant class to pass around
        dynamically typed data values.  In wxPython we have typemaps that
        will convert variants to Python objects of appropriate types, and
        if the type of object is not one that wxVariant will understand
        then the raw PyObject is passed through, with appropriate
        ref-counting.  The wxVariant type names and the Python types they
        are converted to or from are listed in this table:

        ============= =======================
        'bool'        Boolean
        'long'        Integer
        'double'      Float
        'string'      String or Unicode
        'PyObject'    any other Python type
        ============= =======================

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetColumnCount(*args, **kwargs):
        """
        GetColumnCount(self) -> unsigned int

        Override this to indicate the number of columns in the model.
        """
        return _dataview.DataViewModel_GetColumnCount(*args, **kwargs)

    def GetColumnType(*args, **kwargs):
        """
        GetColumnType(self, unsigned int col) -> String

        Override this to indicate what type of data is stored in the column
        specified by col. This should return a string indicating the type name of the
        data type of the column, as used by wxVariant.
        """
        return _dataview.DataViewModel_GetColumnType(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """
        GetValue(self, DataViewItem item, unsigned int col) -> wxVariant

        Override this and return the value to be used for the item, in the
        given column.  The type of the return value should match that given by
        `GetColumnType`.
        """
        return _dataview.DataViewModel_GetValue(*args, **kwargs)

    def HasValue(*args, **kwargs):
        """
        HasValue(self, DataViewItem item, unsigned int col) -> bool

        return true if the given item has a value to display in the given
        column: this is always true except for container items which by
        default only show their label in the first column (but see
        HasContainerColumns())
        """
        return _dataview.DataViewModel_HasValue(*args, **kwargs)

    def SetValue(*args, **kwargs):
        """
        SetValue(self, wxVariant variant, DataViewItem item, unsigned int col) -> bool

        This gets called in order to set a value in the data model.  The most
        common scenario is that the `DataViewCtrl` calls this method after the
        user has changed some data in the view.  The model should then update
        whatever it is using for storing the data values and then call
        `ValueChanged` so proper notifications are performed.
        """
        return _dataview.DataViewModel_SetValue(*args, **kwargs)

    def ChangeValue(*args, **kwargs):
        """ChangeValue(self, wxVariant variant, DataViewItem item, unsigned int col) -> bool"""
        return _dataview.DataViewModel_ChangeValue(*args, **kwargs)

    def GetAttr(*args, **kwargs):
        """
        GetAttr(self, DataViewItem item, unsigned int col, DataViewItemAttr attr) -> bool

        Override this to indicate that the item has special font
        attributes. This only affects the `DataViewTextRenderer` renderer.
        Return ``False`` if the default attributes should be used.
        """
        return _dataview.DataViewModel_GetAttr(*args, **kwargs)

    def IsEnabled(*args, **kwargs):
        """
        IsEnabled(self, DataViewItem item, unsigned int col) -> bool

        Override this if you want to disable specific items
        """
        return _dataview.DataViewModel_IsEnabled(*args, **kwargs)

    def GetParent(*args, **kwargs):
        """
        GetParent(self, DataViewItem item) -> DataViewItem

        Override this to indicate which item is the parent of the given item.
        If the item is a child of the (hidden) root, then simply return an
        invalid item, (one constructed with no ID.)
        """
        return _dataview.DataViewModel_GetParent(*args, **kwargs)

    def IsContainer(*args, **kwargs):
        """
        IsContainer(self, DataViewItem item) -> bool

        Override this to indicate whether an item is a container, in other
        words, if it is a parent item that can have children.
        """
        return _dataview.DataViewModel_IsContainer(*args, **kwargs)

    def HasContainerColumns(*args, **kwargs):
        """
        HasContainerColumns(self, DataViewItem item) -> bool

        Override this method to indicate if a container item merely acts as a
        headline (such as for categorisation) or if it also acts a normal item with
        entries for the other columns. The default implementation returns ``False``.
        """
        return _dataview.DataViewModel_HasContainerColumns(*args, **kwargs)

    def GetChildren(*args, **kwargs):
        """
        GetChildren(self, DataViewItem item, DataViewItemArray children) -> unsigned int

        Override this so the control can find the children of a container
        item.  The children array should be filled with the child items of the
        given item, and the number of children should be returned.
        """
        return _dataview.DataViewModel_GetChildren(*args, **kwargs)

    def ItemAdded(*args, **kwargs):
        """
        ItemAdded(self, DataViewItem parent, DataViewItem item) -> bool

        Call this to inform the registered notifiers that an item has been
        added to the model.
        """
        return _dataview.DataViewModel_ItemAdded(*args, **kwargs)

    def ItemsAdded(*args, **kwargs):
        """
        ItemsAdded(self, DataViewItem parent, DataViewItemArray items) -> bool

        Call this to inform the registered notifiers that multiple items have
        been added to the data model.
        """
        return _dataview.DataViewModel_ItemsAdded(*args, **kwargs)

    def ItemDeleted(*args, **kwargs):
        """
        ItemDeleted(self, DataViewItem parent, DataViewItem item) -> bool

        Call this to inform the registered notifiers that an item has been
        deleted from the model.
        """
        return _dataview.DataViewModel_ItemDeleted(*args, **kwargs)

    def ItemsDeleted(*args, **kwargs):
        """
        ItemsDeleted(self, DataViewItem parent, DataViewItemArray items) -> bool

        Call this to inform the registered notifiers that multiple items have
        been deleted from the data model.
        """
        return _dataview.DataViewModel_ItemsDeleted(*args, **kwargs)

    def ItemChanged(*args, **kwargs):
        """
        ItemChanged(self, DataViewItem item) -> bool

        Call this to inform the registered notifiers that an item has changed.
        This will eventually result in a EVT_DATAVIEW_ITEM_VALUE_CHANGED
        event, in which the column field will not be set.
        """
        return _dataview.DataViewModel_ItemChanged(*args, **kwargs)

    def ItemsChanged(*args, **kwargs):
        """
        ItemsChanged(self, DataViewItemArray items) -> bool

        Call this to inform the registered notifiers that multiple items have
        changed.  This will eventually result in EVT_DATAVIEW_ITEM_VALUE_CHANGED
        events, in which the column field will not be set.
        """
        return _dataview.DataViewModel_ItemsChanged(*args, **kwargs)

    def ValueChanged(*args, **kwargs):
        """
        ValueChanged(self, DataViewItem item, unsigned int col) -> bool

        Call this to inform the registered notifiers that a value in the model
        has been changed.  This will eventually result in a EVT_DATAVIEW_ITEM_VALUE_CHANGED
        event.
        """
        return _dataview.DataViewModel_ValueChanged(*args, **kwargs)

    def Cleared(*args, **kwargs):
        """
        Cleared(self) -> bool

        Call this to inform the registered notifiers that all data has been
        cleared.  The control will then reread the data from the model again.
        """
        return _dataview.DataViewModel_Cleared(*args, **kwargs)

    def BeforeReset(*args, **kwargs):
        """BeforeReset(self) -> bool"""
        return _dataview.DataViewModel_BeforeReset(*args, **kwargs)

    def AfterReset(*args, **kwargs):
        """AfterReset(self) -> bool"""
        return _dataview.DataViewModel_AfterReset(*args, **kwargs)

    def Resort(*args, **kwargs):
        """
        Resort(self)

        Call this to initiate a resort after the sort function has been changed.
        """
        return _dataview.DataViewModel_Resort(*args, **kwargs)

    def AddNotifier(*args, **kwargs):
        """AddNotifier(self, DataViewModelNotifier notifier)"""
        return _dataview.DataViewModel_AddNotifier(*args, **kwargs)

    def RemoveNotifier(*args, **kwargs):
        """RemoveNotifier(self, DataViewModelNotifier notifier)"""
        val = _dataview.DataViewModel_RemoveNotifier(*args, **kwargs)
        args[1].thisown = 1
        return val

    def Compare(*args, **kwargs):
        """
        Compare(self, DataViewItem item1, DataViewItem item2, unsigned int column, 
            bool ascending) -> int

        The compare function to be used by the control. The default compare
        function sorts by container and other items separately and in
        ascending order. Override this for a different sorting behaviour.
        """
        return _dataview.DataViewModel_Compare(*args, **kwargs)

    def HasDefaultCompare(*args, **kwargs):
        """
        HasDefaultCompare(self) -> bool

        Override this to indicate that the model provides a default compare
        function that the control should use if no column has been chosen for
        sorting. Usually, the user clicks on a column header for sorting and
        the data will be sorted alphanumerically. If any other order (e.g. by
        index or order of appearance) is required, then this should be used.
        """
        return _dataview.DataViewModel_HasDefaultCompare(*args, **kwargs)

    def IsListModel(*args, **kwargs):
        """IsListModel(self) -> bool"""
        return _dataview.DataViewModel_IsListModel(*args, **kwargs)

    def IsVirtualListModel(*args, **kwargs):
        """IsVirtualListModel(self) -> bool"""
        return _dataview.DataViewModel_IsVirtualListModel(*args, **kwargs)

_dataview.DataViewModel_swigregister(DataViewModel)

class DataViewItemObjectMapper(object):
    """
    This class provides a mechanism for mapping between Python objects and the
    DataViewItem objects used by the DataViewModel for tracking the items in
    the view. The ID used for the item is the id() of the Python object. Use
    `ObjectToItem` to create a DataViewItem using a Python object as its ID,
    and use `ItemToObject` to fetch that Python object again later for a given
    DataViewItem.
    
    By default a regular dictionary is used to implement the ID to object
    mapping. Optionally a WeakValueDictionary can be useful when there will be
    a high turnover of objects and mantaining an extra reference to the
    objects would be unwise.  If weak references are used then the objects
    associated with data items must be weak-referenceable.  (Things like
    stock lists and dictionaries are not.)  See `UseWeakRefs`.
    
    Each `PyDataViewModel` has an instance of this class named objmapper.
    """
    def __init__(self):
        self.mapper = dict()
        self.usingWeakRefs = False
        
    def ObjectToItem(self, obj):
        """
        Create a DataViewItem for the object, and remember the ID-->obj mapping.
        """
        oid = id(obj)
        self.mapper[oid] = obj
        return DataViewItem(oid)

    def ItemToObject(self, item):
        """
        Retrieve the object that was used to create an item.
        """
        oid = item.GetID()
        return self.mapper[oid]

    def UseWeakRefs(self, flag):
        """
        Switch to or from using a weak value dictionary for keeping the ID to
        object map.
        """
        if flag == self.usingWeakRefs:
            return
        if flag:
            import weakref
            newmap = weakref.WeakValueDictionary()
        else:
            newmap = dict()
        newmap.update(self.mapper)
        self.mapper = newmap
        self.usingWeakRefs = flag
        

class PyDataViewModel(DataViewModel):
    """
    This class is a version of `DataViewModel` that has been
    engineered to know how to reflect the C++ virtual method calls to
    Python methods in the derived class.  Use this class as your base
    class instead of `DataViewModel`.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PyDataViewModel

        This class is a version of `DataViewModel` that has been
        engineered to know how to reflect the C++ virtual method calls to
        Python methods in the derived class.  Use this class as your base
        class instead of `DataViewModel`.
        """
        _dataview.PyDataViewModel_swiginit(self,_dataview.new_PyDataViewModel(*args, **kwargs))
        PyDataViewModel._setCallbackInfo(self, self, PyDataViewModel); self.objmapper = DataViewItemObjectMapper()


    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return _dataview.PyDataViewModel__setCallbackInfo(*args, **kwargs)

    def ObjectToItem(self, obj):
        "Convenience access to DataViewItemObjectMapper.ObjectToItem."
        return self.objmapper.ObjectToItem(obj)

    def ItemToObject(self, item):
        "Convenience access to DataViewItemObjectMapper.ItemToObject."
        return self.objmapper.ItemToObject(item)

_dataview.PyDataViewModel_swigregister(PyDataViewModel)

#---------------------------------------------------------------------------

class DataViewIndexListModel(DataViewModel):
    """
    DataViewIndexListModel is a specialized data model which lets you
    address an item by its position (row) rather than its `DataViewItem`
    (which you can obtain from this class if needed). This model also
    provides its own `Compare` method which sorts the model's data by the
    index.  To implement a custom list-based data model derive a new class
    from `PyDataViewIndexListModel` and implement the required methods.

    This model is not a virtual model since the control stores each
    `DataViewItem` in memory. Use a `DataViewVirtualListModel` if you need
    to display millions of items or have other reasons to use a virtual
    control.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewIndexListModel
    __del__ = lambda self : None;
    def GetValueByRow(*args, **kwargs):
        """
        GetValueByRow(self, unsigned int row, unsigned int col) -> wxVariant

        Override this method to return the data value to be used for the item
        at the given row and column.
        """
        return _dataview.DataViewIndexListModel_GetValueByRow(*args, **kwargs)

    def SetValueByRow(*args, **kwargs):
        """
        SetValueByRow(self, wxVariant variant, unsigned int row, unsigned int col) -> bool

        This is called in order to set a value in the data model.
        """
        return _dataview.DataViewIndexListModel_SetValueByRow(*args, **kwargs)

    def GetAttrByRow(*args, **kwargs):
        """
        GetAttrByRow(self, unsigned int row, unsigned int col, DataViewItemAttr attr) -> bool

        Override this to indicate that the item has special font
        attributes. This only affects the `DataViewTextRenderer` renderer.
        Return ``False`` if the default attributes should be used.
        """
        return _dataview.DataViewIndexListModel_GetAttrByRow(*args, **kwargs)

    def IsEnabledByRow(*args, **kwargs):
        """IsEnabledByRow(self, unsigned int row, unsigned int col) -> bool"""
        return _dataview.DataViewIndexListModel_IsEnabledByRow(*args, **kwargs)

    def RowPrepended(*args, **kwargs):
        """
        RowPrepended(self)

        Call this after a row has been prepended to the model.
        """
        return _dataview.DataViewIndexListModel_RowPrepended(*args, **kwargs)

    def RowInserted(*args, **kwargs):
        """
        RowInserted(self, unsigned int before)

        Call this after a row has been inserted at the given position
        """
        return _dataview.DataViewIndexListModel_RowInserted(*args, **kwargs)

    def RowAppended(*args, **kwargs):
        """
        RowAppended(self)

        Call this after a row has been appended to the model.
        """
        return _dataview.DataViewIndexListModel_RowAppended(*args, **kwargs)

    def RowDeleted(*args, **kwargs):
        """
        RowDeleted(self, unsigned int row)

        Call this after a row has been deleted.
        """
        return _dataview.DataViewIndexListModel_RowDeleted(*args, **kwargs)

    def RowsDeleted(*args, **kwargs):
        """
        RowsDeleted(self, wxArrayInt rows)

        Call this after rows have been deleted. The array will internally get
        copied and sorted in descending order so that the rows with the
        highest position will be deleted first.
        """
        return _dataview.DataViewIndexListModel_RowsDeleted(*args, **kwargs)

    def RowChanged(*args, **kwargs):
        """
        RowChanged(self, unsigned int row)

        Call this after a row has been changed.
        """
        return _dataview.DataViewIndexListModel_RowChanged(*args, **kwargs)

    def RowValueChanged(*args, **kwargs):
        """
        RowValueChanged(self, unsigned int row, unsigned int col)

        Call this after a value has been changed.
        """
        return _dataview.DataViewIndexListModel_RowValueChanged(*args, **kwargs)

    def Reset(*args, **kwargs):
        """
        Reset(self, unsigned int new_size)

        Call this if the data has to be read again from the model. This is
        useful after major changes when calling methods like `RowChanged` or
        `RowDeleted` (possibly thousands of times) doesn't make sense.
        """
        return _dataview.DataViewIndexListModel_Reset(*args, **kwargs)

    def GetRow(*args, **kwargs):
        """
        GetRow(self, DataViewItem item) -> unsigned int

        Returns the row position of item.
        """
        return _dataview.DataViewIndexListModel_GetRow(*args, **kwargs)

    def GetCount(*args, **kwargs):
        """
        GetCount(self) -> unsigned int

        returns the number of rows
        """
        return _dataview.DataViewIndexListModel_GetCount(*args, **kwargs)

    def GetItem(*args, **kwargs):
        """
        GetItem(self, unsigned int row) -> DataViewItem

        Returns the DataViewItem for the item at row.
        """
        return _dataview.DataViewIndexListModel_GetItem(*args, **kwargs)

_dataview.DataViewIndexListModel_swigregister(DataViewIndexListModel)

class PyDataViewIndexListModel(DataViewIndexListModel):
    """Proxy of C++ PyDataViewIndexListModel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, unsigned int initial_size=0) -> PyDataViewIndexListModel"""
        _dataview.PyDataViewIndexListModel_swiginit(self,_dataview.new_PyDataViewIndexListModel(*args, **kwargs))
        PyDataViewIndexListModel._setCallbackInfo(self, self, PyDataViewIndexListModel)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return _dataview.PyDataViewIndexListModel__setCallbackInfo(*args, **kwargs)

_dataview.PyDataViewIndexListModel_swigregister(PyDataViewIndexListModel)

class DataViewVirtualListModel(DataViewModel):
    """
    DataViewVirtualListModel is a specialized data model which lets you
    address an item by its position (row) rather than its `DataViewItem`
    and as such offers the exact same interface as
    `DataViewIndexListModel`. The important difference is that under
    platforms other than OS X, using this model will result in a truely
    virtual control able to handle millions of items as the control
    doesn't store any per-item data in memory (a feature not supported by
    the Carbon API under OS X).

    To implement a custom list-based data model derive a new class from
    `PyDataViewVirtualListModel` and implement the required methods.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewVirtualListModel
    __del__ = lambda self : None;
    def GetValueByRow(*args, **kwargs):
        """
        GetValueByRow(self, unsigned int row, unsigned int col) -> wxVariant

        Override this method to return the data value to be used for the item
        at the given row and column.
        """
        return _dataview.DataViewVirtualListModel_GetValueByRow(*args, **kwargs)

    def SetValueByRow(*args, **kwargs):
        """
        SetValueByRow(self, wxVariant variant, unsigned int row, unsigned int col) -> bool

        This is called in order to set a value in the data model.
        """
        return _dataview.DataViewVirtualListModel_SetValueByRow(*args, **kwargs)

    def GetAttrByRow(*args, **kwargs):
        """
        GetAttrByRow(self, unsigned int row, unsigned int col, DataViewItemAttr attr) -> bool

        Override this to indicate that the item has special font
        attributes. This only affects the `DataViewTextRenderer` renderer.
        Return ``False`` if the default attributes should be used.
        """
        return _dataview.DataViewVirtualListModel_GetAttrByRow(*args, **kwargs)

    def IsEnabledByRow(*args, **kwargs):
        """IsEnabledByRow(self, unsigned int row, unsigned int col) -> bool"""
        return _dataview.DataViewVirtualListModel_IsEnabledByRow(*args, **kwargs)

    def RowPrepended(*args, **kwargs):
        """
        RowPrepended(self)

        Call this after a row has been prepended to the model.
        """
        return _dataview.DataViewVirtualListModel_RowPrepended(*args, **kwargs)

    def RowInserted(*args, **kwargs):
        """
        RowInserted(self, unsigned int before)

        Call this after a row has been inserted at the given position
        """
        return _dataview.DataViewVirtualListModel_RowInserted(*args, **kwargs)

    def RowAppended(*args, **kwargs):
        """
        RowAppended(self)

        Call this after a row has been appended to the model.
        """
        return _dataview.DataViewVirtualListModel_RowAppended(*args, **kwargs)

    def RowDeleted(*args, **kwargs):
        """
        RowDeleted(self, unsigned int row)

        Call this after a row has been deleted.
        """
        return _dataview.DataViewVirtualListModel_RowDeleted(*args, **kwargs)

    def RowsDeleted(*args, **kwargs):
        """
        RowsDeleted(self, wxArrayInt rows)

        Call this after rows have been deleted. The array will internally get
        copied and sorted in descending order so that the rows with the
        highest position will be deleted first.
        """
        return _dataview.DataViewVirtualListModel_RowsDeleted(*args, **kwargs)

    def RowChanged(*args, **kwargs):
        """
        RowChanged(self, unsigned int row)

        Call this after a row has been changed.
        """
        return _dataview.DataViewVirtualListModel_RowChanged(*args, **kwargs)

    def RowValueChanged(*args, **kwargs):
        """
        RowValueChanged(self, unsigned int row, unsigned int col)

        Call this after a value has been changed.
        """
        return _dataview.DataViewVirtualListModel_RowValueChanged(*args, **kwargs)

    def Reset(*args, **kwargs):
        """
        Reset(self, unsigned int new_size)

        Call this if the data has to be read again from the model. This is
        useful after major changes when calling methods like `RowChanged` or
        `RowDeleted` (possibly thousands of times) doesn't make sense.
        """
        return _dataview.DataViewVirtualListModel_Reset(*args, **kwargs)

    def GetRow(*args, **kwargs):
        """
        GetRow(self, DataViewItem item) -> unsigned int

        Returns the row position of item.
        """
        return _dataview.DataViewVirtualListModel_GetRow(*args, **kwargs)

    def GetCount(*args, **kwargs):
        """
        GetCount(self) -> unsigned int

        returns the number of rows
        """
        return _dataview.DataViewVirtualListModel_GetCount(*args, **kwargs)

    def GetItem(*args, **kwargs):
        """
        GetItem(self, unsigned int row) -> DataViewItem

        Returns the DataViewItem for the item at row.
        """
        return _dataview.DataViewVirtualListModel_GetItem(*args, **kwargs)

_dataview.DataViewVirtualListModel_swigregister(DataViewVirtualListModel)

class PyDataViewVirtualListModel(DataViewVirtualListModel):
    """Proxy of C++ PyDataViewVirtualListModel class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, unsigned int initial_size=0) -> PyDataViewVirtualListModel"""
        _dataview.PyDataViewVirtualListModel_swiginit(self,_dataview.new_PyDataViewVirtualListModel(*args, **kwargs))
        PyDataViewVirtualListModel._setCallbackInfo(self, self, PyDataViewVirtualListModel)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return _dataview.PyDataViewVirtualListModel__setCallbackInfo(*args, **kwargs)

_dataview.PyDataViewVirtualListModel_swigregister(PyDataViewVirtualListModel)

DATAVIEW_CELL_INERT = _dataview.DATAVIEW_CELL_INERT
DATAVIEW_CELL_ACTIVATABLE = _dataview.DATAVIEW_CELL_ACTIVATABLE
DATAVIEW_CELL_EDITABLE = _dataview.DATAVIEW_CELL_EDITABLE
DATAVIEW_CELL_SELECTED = _dataview.DATAVIEW_CELL_SELECTED
DATAVIEW_CELL_PRELIT = _dataview.DATAVIEW_CELL_PRELIT
DATAVIEW_CELL_INSENSITIVE = _dataview.DATAVIEW_CELL_INSENSITIVE
DATAVIEW_CELL_FOCUSED = _dataview.DATAVIEW_CELL_FOCUSED
class DataViewRenderer(_core.Object):
    """
    This class is used by `DataViewCtrl` to render (or draw) the
    individual cells. One instance of a renderer class is owned by each
    `DataViewColumn`. There is a number of ready-to-use renderers
    provided: `DataViewTextRenderer`, 
    `DataViewIconTextRenderer`, `DataViewToggleRenderer`,
    `DataViewProgressRenderer`, `DataViewBitmapRenderer`,
    `DataViewDateRenderer`, `DataViewSpinRenderer`,
    `DataViewChoiceRenderer`.

    To create your own custom renderer derive a new class from
    `PyDataViewCustomRenderer`.

    The mode flag controls what actions the cell data
    allows. ``DATAVIEW_CELL_ACTIVATABLE`` indicates that the user can double
    click the cell and something will happen (e.g. a window for editing a
    date will pop up). ``DATAVIEW_CELL_EDITABLE`` indicates that the user
    can edit the data in-place, i.e. an control will show up after a slow
    click on the cell. This behaviour is best known from changing the
    filename in most file managers etc.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewRenderer
    __del__ = lambda self : None;
    def Validate(*args, **kwargs):
        """Validate(self, wxVariant value) -> bool"""
        return _dataview.DataViewRenderer_Validate(*args, **kwargs)

    def SetOwner(*args, **kwargs):
        """SetOwner(self, DataViewColumn owner)"""
        return _dataview.DataViewRenderer_SetOwner(*args, **kwargs)

    def GetOwner(*args, **kwargs):
        """GetOwner(self) -> DataViewColumn"""
        return _dataview.DataViewRenderer_GetOwner(*args, **kwargs)

    def SetValue(*args, **kwargs):
        """SetValue(self, wxVariant value) -> bool"""
        return _dataview.DataViewRenderer_SetValue(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> wxVariant"""
        return _dataview.DataViewRenderer_GetValue(*args, **kwargs)

    def SetAttr(*args, **kwargs):
        """SetAttr(self, DataViewItemAttr attr)"""
        return _dataview.DataViewRenderer_SetAttr(*args, **kwargs)

    def SetEnabled(*args, **kwargs):
        """SetEnabled(self, bool enabled)"""
        return _dataview.DataViewRenderer_SetEnabled(*args, **kwargs)

    def GetVariantType(*args, **kwargs):
        """GetVariantType(self) -> String"""
        return _dataview.DataViewRenderer_GetVariantType(*args, **kwargs)

    def PrepareForItem(*args, **kwargs):
        """PrepareForItem(self, DataViewModel model, DataViewItem item, unsigned int column)"""
        return _dataview.DataViewRenderer_PrepareForItem(*args, **kwargs)

    def SetMode(*args, **kwargs):
        """SetMode(self, int mode)"""
        return _dataview.DataViewRenderer_SetMode(*args, **kwargs)

    def GetMode(*args, **kwargs):
        """GetMode(self) -> int"""
        return _dataview.DataViewRenderer_GetMode(*args, **kwargs)

    def SetAlignment(*args, **kwargs):
        """SetAlignment(self, int align)"""
        return _dataview.DataViewRenderer_SetAlignment(*args, **kwargs)

    def GetAlignment(*args, **kwargs):
        """GetAlignment(self) -> int"""
        return _dataview.DataViewRenderer_GetAlignment(*args, **kwargs)

    def EnableEllipsize(*args, **kwargs):
        """EnableEllipsize(self, int mode=ELLIPSIZE_MIDDLE)"""
        return _dataview.DataViewRenderer_EnableEllipsize(*args, **kwargs)

    def DisableEllipsize(*args, **kwargs):
        """DisableEllipsize(self)"""
        return _dataview.DataViewRenderer_DisableEllipsize(*args, **kwargs)

    def GetEllipsizeMode(*args, **kwargs):
        """GetEllipsizeMode(self) -> int"""
        return _dataview.DataViewRenderer_GetEllipsizeMode(*args, **kwargs)

    def HasEditorCtrl(*args, **kwargs):
        """HasEditorCtrl(self) -> bool"""
        return _dataview.DataViewRenderer_HasEditorCtrl(*args, **kwargs)

    def CreateEditorCtrl(*args, **kwargs):
        """CreateEditorCtrl(self, Window parent, Rect labelRect, wxVariant value) -> Window"""
        return _dataview.DataViewRenderer_CreateEditorCtrl(*args, **kwargs)

    def GetValueFromEditorCtrl(*args, **kwargs):
        """GetValueFromEditorCtrl(self, Window editor) -> wxVariant"""
        return _dataview.DataViewRenderer_GetValueFromEditorCtrl(*args, **kwargs)

    def StartEditing(*args, **kwargs):
        """StartEditing(self, DataViewItem item, Rect labelRect) -> bool"""
        return _dataview.DataViewRenderer_StartEditing(*args, **kwargs)

    def CancelEditing(*args, **kwargs):
        """CancelEditing(self)"""
        return _dataview.DataViewRenderer_CancelEditing(*args, **kwargs)

    def FinishEditing(*args, **kwargs):
        """FinishEditing(self) -> bool"""
        return _dataview.DataViewRenderer_FinishEditing(*args, **kwargs)

    def GetEditorCtrl(*args, **kwargs):
        """GetEditorCtrl(self) -> Window"""
        return _dataview.DataViewRenderer_GetEditorCtrl(*args, **kwargs)

    Owner = property(GetOwner,SetOwner) 
    Value = property(GetValue,SetValue) 
    VariantType = property(GetVariantType) 
    Mode = property(GetMode,SetMode) 
    Alignment = property(GetAlignment,SetAlignment) 
    EditorCtrl = property(GetEditorCtrl) 
_dataview.DataViewRenderer_swigregister(DataViewRenderer)

class DataViewTextRenderer(DataViewRenderer):
    """
    This class is used for rendering text. It supports in-place editing if
    desired.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String varianttype="string", int mode=DATAVIEW_CELL_INERT, 
            int align=DVR_DEFAULT_ALIGNMENT) -> DataViewTextRenderer

        This class is used for rendering text. It supports in-place editing if
        desired.
        """
        _dataview.DataViewTextRenderer_swiginit(self,_dataview.new_DataViewTextRenderer(*args, **kwargs))
_dataview.DataViewTextRenderer_swigregister(DataViewTextRenderer)

class DataViewBitmapRenderer(DataViewRenderer):
    """DataViewBitmapRenderer"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String varianttype="wxBitmap", int mode=DATAVIEW_CELL_INERT, 
            int align=DVR_DEFAULT_ALIGNMENT) -> DataViewBitmapRenderer

        DataViewBitmapRenderer
        """
        _dataview.DataViewBitmapRenderer_swiginit(self,_dataview.new_DataViewBitmapRenderer(*args, **kwargs))
_dataview.DataViewBitmapRenderer_swigregister(DataViewBitmapRenderer)

class DataViewIconTextRenderer(DataViewRenderer):
    """
    The `DataViewIconTextRenderer` class is used to display text with a
    small icon next to it as it is typically done in a file manager. This
    class uses the `DataViewIconText` helper class to store its
    data.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String varianttype="wxDataViewIconText", int mode=DATAVIEW_CELL_INERT, 
            int align=DVR_DEFAULT_ALIGNMENT) -> DataViewIconTextRenderer

        The `DataViewIconTextRenderer` class is used to display text with a
        small icon next to it as it is typically done in a file manager. This
        class uses the `DataViewIconText` helper class to store its
        data.
        """
        _dataview.DataViewIconTextRenderer_swiginit(self,_dataview.new_DataViewIconTextRenderer(*args, **kwargs))
_dataview.DataViewIconTextRenderer_swigregister(DataViewIconTextRenderer)

class DataViewIconText(_core.Object):
    """
    DataViewIconText is used to hold the data for columns using the
    `DataViewIconTextRenderer`
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String text=wxEmptyString, Icon icon=wxNullIcon) -> DataViewIconText

        DataViewIconText is used to hold the data for columns using the
        `DataViewIconTextRenderer`
        """
        _dataview.DataViewIconText_swiginit(self,_dataview.new_DataViewIconText(*args, **kwargs))
    __swig_destroy__ = _dataview.delete_DataViewIconText
    __del__ = lambda self : None;
    def SetText(*args, **kwargs):
        """SetText(self, String text)"""
        return _dataview.DataViewIconText_SetText(*args, **kwargs)

    def GetText(*args, **kwargs):
        """GetText(self) -> String"""
        return _dataview.DataViewIconText_GetText(*args, **kwargs)

    def SetIcon(*args, **kwargs):
        """SetIcon(self, Icon icon)"""
        return _dataview.DataViewIconText_SetIcon(*args, **kwargs)

    def GetIcon(*args, **kwargs):
        """GetIcon(self) -> Icon"""
        return _dataview.DataViewIconText_GetIcon(*args, **kwargs)

_dataview.DataViewIconText_swigregister(DataViewIconText)

class DataViewToggleRenderer(DataViewRenderer):
    """DataViewToggleRenderer"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String varianttype="bool", int mode=DATAVIEW_CELL_INERT, 
            int align=DVR_DEFAULT_ALIGNMENT) -> DataViewToggleRenderer

        DataViewToggleRenderer
        """
        _dataview.DataViewToggleRenderer_swiginit(self,_dataview.new_DataViewToggleRenderer(*args, **kwargs))
_dataview.DataViewToggleRenderer_swigregister(DataViewToggleRenderer)

class DataViewProgressRenderer(DataViewRenderer):
    """DataViewProgressRenderer"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String label=wxEmptyString, String varianttype="long", 
            int mode=DATAVIEW_CELL_INERT, int align=DVR_DEFAULT_ALIGNMENT) -> DataViewProgressRenderer

        DataViewProgressRenderer
        """
        _dataview.DataViewProgressRenderer_swiginit(self,_dataview.new_DataViewProgressRenderer(*args, **kwargs))
_dataview.DataViewProgressRenderer_swigregister(DataViewProgressRenderer)

class DataViewSpinRenderer(DataViewRenderer):
    """
    This is a specialized renderer for rendering integer values. It
    supports modifying the values in-place by using a `wx.SpinCtrl`. The
    renderer only support integer data items.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int min, int max, int mode=DATAVIEW_CELL_EDITABLE, 
            int alignment=DVR_DEFAULT_ALIGNMENT) -> DataViewSpinRenderer

        This is a specialized renderer for rendering integer values. It
        supports modifying the values in-place by using a `wx.SpinCtrl`. The
        renderer only support integer data items.
        """
        _dataview.DataViewSpinRenderer_swiginit(self,_dataview.new_DataViewSpinRenderer(*args, **kwargs))
_dataview.DataViewSpinRenderer_swigregister(DataViewSpinRenderer)

class DataViewCustomRenderer(DataViewRenderer):
    """See `PyDataViewCustomRenderer`."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetAttr(*args, **kwargs):
        """GetAttr(self) -> DataViewItemAttr"""
        return _dataview.DataViewCustomRenderer_GetAttr(*args, **kwargs)

    def GetEnabled(*args, **kwargs):
        """GetEnabled(self) -> bool"""
        return _dataview.DataViewCustomRenderer_GetEnabled(*args, **kwargs)

_dataview.DataViewCustomRenderer_swigregister(DataViewCustomRenderer)

class DataViewChoiceRenderer(DataViewCustomRenderer):
    """Proxy of C++ DataViewChoiceRenderer class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, wxArrayString choices, int mode=DATAVIEW_CELL_EDITABLE, 
            int alignment=DVR_DEFAULT_ALIGNMENT) -> DataViewChoiceRenderer
        """
        _dataview.DataViewChoiceRenderer_swiginit(self,_dataview.new_DataViewChoiceRenderer(*args, **kwargs))
    def GetChoice(*args, **kwargs):
        """GetChoice(self, size_t index) -> String"""
        return _dataview.DataViewChoiceRenderer_GetChoice(*args, **kwargs)

    def GetChoices(*args, **kwargs):
        """GetChoices(self) -> wxArrayString"""
        return _dataview.DataViewChoiceRenderer_GetChoices(*args, **kwargs)

_dataview.DataViewChoiceRenderer_swigregister(DataViewChoiceRenderer)

class DataViewChoiceByIndexRenderer(DataViewChoiceRenderer):
    """Proxy of C++ DataViewChoiceByIndexRenderer class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, wxArrayString choices, int mode=DATAVIEW_CELL_EDITABLE, 
            int alignment=DVR_DEFAULT_ALIGNMENT) -> DataViewChoiceByIndexRenderer
        """
        _dataview.DataViewChoiceByIndexRenderer_swiginit(self,_dataview.new_DataViewChoiceByIndexRenderer(*args, **kwargs))
_dataview.DataViewChoiceByIndexRenderer_swigregister(DataViewChoiceByIndexRenderer)

class DataViewDateRenderer(DataViewRenderer):
    """Proxy of C++ DataViewDateRenderer class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String varianttype="datetime", int mode=DATAVIEW_CELL_ACTIVATABLE, 
            int align=DVR_DEFAULT_ALIGNMENT) -> DataViewDateRenderer
        """
        _dataview.DataViewDateRenderer_swiginit(self,_dataview.new_DataViewDateRenderer(*args, **kwargs))
_dataview.DataViewDateRenderer_swigregister(DataViewDateRenderer)

class PyDataViewCustomRenderer(DataViewCustomRenderer):
    """Proxy of C++ PyDataViewCustomRenderer class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String varianttype="string", int mode=DATAVIEW_CELL_INERT, 
            int align=DVR_DEFAULT_ALIGNMENT) -> PyDataViewCustomRenderer
        """
        _dataview.PyDataViewCustomRenderer_swiginit(self,_dataview.new_PyDataViewCustomRenderer(*args, **kwargs))
        PyDataViewCustomRenderer._setCallbackInfo(self, self, PyDataViewCustomRenderer)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return _dataview.PyDataViewCustomRenderer__setCallbackInfo(*args, **kwargs)

    def RenderText(*args, **kwargs):
        """
        RenderText(self, String text, int xoffset, Rect cell, DC dc, int state)

        This method should be called from within your `Render` override
        whenever you need to render simple text. This will help ensure that the
        correct colour, font and vertical alignment will be chosen so the text
        will look the same as text drawn by native renderers.
        """
        return _dataview.PyDataViewCustomRenderer_RenderText(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """
        GetSize(self) -> Size

        Returns the size required to show content.  This must be overridden in
        derived classes.
        """
        return _dataview.PyDataViewCustomRenderer_GetSize(*args, **kwargs)

    def Render(*args, **kwargs):
        """
        Render(self, Rect cell, DC dc, int state) -> bool

        Override this to render the cell. Before this is called, `SetValue`
        was called so that this instance knows what to render.  This must be
        overridden in derived classes.
        """
        return _dataview.PyDataViewCustomRenderer_Render(*args, **kwargs)

    def Activate(*args, **kwargs):
        """
        Activate(self, Rect cell, DataViewModel model, DataViewItem item, 
            unsigned int col) -> bool

        Override this to react to double clicks or <ENTER>.
        """
        return _dataview.PyDataViewCustomRenderer_Activate(*args, **kwargs)

    def LeftClick(*args, **kwargs):
        """
        LeftClick(self, Point cursor, Rect cell, DataViewModel model, DataViewItem item, 
            unsigned int col) -> bool

        Overrride this to react to a left click.
        """
        return _dataview.PyDataViewCustomRenderer_LeftClick(*args, **kwargs)

    def StartDrag(*args, **kwargs):
        """
        StartDrag(self, Point cursor, Rect cell, DataViewModel model, DataViewItem item, 
            unsigned int col) -> bool

        Overrride this to react to the start of a drag operation.
        """
        return _dataview.PyDataViewCustomRenderer_StartDrag(*args, **kwargs)

    def GetDC(*args, **kwargs):
        """GetDC(self) -> DC"""
        return _dataview.PyDataViewCustomRenderer_GetDC(*args, **kwargs)

    def GetTextExtent(*args, **kwargs):
        """GetTextExtent(self, String str) -> Size"""
        return _dataview.PyDataViewCustomRenderer_GetTextExtent(*args, **kwargs)

    def GetView(*args, **kwargs):
        """GetView(self) -> DataViewCtrl"""
        return _dataview.PyDataViewCustomRenderer_GetView(*args, **kwargs)

_dataview.PyDataViewCustomRenderer_swigregister(PyDataViewCustomRenderer)

DATAVIEW_COL_RESIZABLE = _dataview.DATAVIEW_COL_RESIZABLE
DATAVIEW_COL_SORTABLE = _dataview.DATAVIEW_COL_SORTABLE
DATAVIEW_COL_REORDERABLE = _dataview.DATAVIEW_COL_REORDERABLE
DATAVIEW_COL_HIDDEN = _dataview.DATAVIEW_COL_HIDDEN
class DataViewColumn(_core.SettableHeaderColumn):
    """Proxy of C++ DataViewColumn class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, PyObject title_or_bitmap, DataViewRenderer renderer, 
            unsigned int model_column, int width=80, int align=ALIGN_CENTER, 
            int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        _dataview.DataViewColumn_swiginit(self,_dataview.new_DataViewColumn(*args, **kwargs))
    def SetOwner(*args, **kwargs):
        """SetOwner(self, DataViewCtrl owner)"""
        return _dataview.DataViewColumn_SetOwner(*args, **kwargs)

    def GetModelColumn(*args, **kwargs):
        """GetModelColumn(self) -> unsigned int"""
        return _dataview.DataViewColumn_GetModelColumn(*args, **kwargs)

    def GetOwner(*args, **kwargs):
        """GetOwner(self) -> DataViewCtrl"""
        return _dataview.DataViewColumn_GetOwner(*args, **kwargs)

    def GetRenderer(*args, **kwargs):
        """GetRenderer(self) -> DataViewRenderer"""
        return _dataview.DataViewColumn_GetRenderer(*args, **kwargs)

    ModelColumn = property(GetModelColumn) 
    Owner = property(GetOwner,SetOwner) 
    Renderer = property(GetRenderer) 
_dataview.DataViewColumn_swigregister(DataViewColumn)

DV_SINGLE = _dataview.DV_SINGLE
DV_MULTIPLE = _dataview.DV_MULTIPLE
DV_NO_HEADER = _dataview.DV_NO_HEADER
DV_HORIZ_RULES = _dataview.DV_HORIZ_RULES
DV_VERT_RULES = _dataview.DV_VERT_RULES
DV_ROW_LINES = _dataview.DV_ROW_LINES
DV_VARIABLE_LINE_HEIGHT = _dataview.DV_VARIABLE_LINE_HEIGHT
class DataViewCtrl(_core.Control):
    """Proxy of C++ DataViewCtrl class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=ID_ANY, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=0, Validator validator=DefaultValidator, 
            String name=wxDataViewCtrlNameStr) -> DataViewCtrl
        """
        _dataview.DataViewCtrl_swiginit(self,_dataview.new_DataViewCtrl(*args, **kwargs))
        self._setOORInfo(self)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=0, Validator validator=DefaultValidator, 
            String name=wxDataViewCtrlNameStr) -> bool

        Do the 2nd phase and create the GUI control.
        """
        return _dataview.DataViewCtrl_Create(*args, **kwargs)

    def AssociateModel(*args, **kwargs):
        """AssociateModel(self, DataViewModel model) -> bool"""
        return _dataview.DataViewCtrl_AssociateModel(*args, **kwargs)

    def GetModel(*args, **kwargs):
        """GetModel(self) -> DataViewModel"""
        return _dataview.DataViewCtrl_GetModel(*args, **kwargs)

    def PrependTextColumn(*args, **kwargs):
        """
        PrependTextColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_NOT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_PrependTextColumn(*args, **kwargs)

    def PrependIconTextColumn(*args, **kwargs):
        """
        PrependIconTextColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_NOT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_PrependIconTextColumn(*args, **kwargs)

    def PrependToggleColumn(*args, **kwargs):
        """
        PrependToggleColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=DVC_TOGGLE_DEFAULT_WIDTH, 
            int align=ALIGN_CENTER, 
            int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_PrependToggleColumn(*args, **kwargs)

    def PrependProgressColumn(*args, **kwargs):
        """
        PrependProgressColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=DVC_DEFAULT_WIDTH, 
            int align=ALIGN_CENTER, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_PrependProgressColumn(*args, **kwargs)

    def PrependDateColumn(*args, **kwargs):
        """
        PrependDateColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_ACTIVATABLE, int width=-1, 
            int align=ALIGN_NOT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_PrependDateColumn(*args, **kwargs)

    def PrependBitmapColumn(*args, **kwargs):
        """
        PrependBitmapColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_CENTER, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_PrependBitmapColumn(*args, **kwargs)

    def AppendTextColumn(*args, **kwargs):
        """
        AppendTextColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_NOT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_AppendTextColumn(*args, **kwargs)

    def AppendIconTextColumn(*args, **kwargs):
        """
        AppendIconTextColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_NOT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_AppendIconTextColumn(*args, **kwargs)

    def AppendToggleColumn(*args, **kwargs):
        """
        AppendToggleColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=DVC_TOGGLE_DEFAULT_WIDTH, 
            int align=ALIGN_CENTER, 
            int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_AppendToggleColumn(*args, **kwargs)

    def AppendProgressColumn(*args, **kwargs):
        """
        AppendProgressColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=DVC_DEFAULT_WIDTH, 
            int align=ALIGN_CENTER, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_AppendProgressColumn(*args, **kwargs)

    def AppendDateColumn(*args, **kwargs):
        """
        AppendDateColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_ACTIVATABLE, int width=-1, 
            int align=ALIGN_NOT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_AppendDateColumn(*args, **kwargs)

    def AppendBitmapColumn(*args, **kwargs):
        """
        AppendBitmapColumn(self, PyObject label_or_bitmap, unsigned int model_column, 
            int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_CENTER, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewCtrl_AppendBitmapColumn(*args, **kwargs)

    def PrependColumn(*args, **kwargs):
        """PrependColumn(self, DataViewColumn col) -> bool"""
        return _dataview.DataViewCtrl_PrependColumn(*args, **kwargs)

    def InsertColumn(*args, **kwargs):
        """InsertColumn(self, unsigned int pos, DataViewColumn col) -> bool"""
        return _dataview.DataViewCtrl_InsertColumn(*args, **kwargs)

    def AppendColumn(*args, **kwargs):
        """AppendColumn(self, DataViewColumn col) -> bool"""
        return _dataview.DataViewCtrl_AppendColumn(*args, **kwargs)

    def GetColumnCount(*args, **kwargs):
        """GetColumnCount(self) -> unsigned int"""
        return _dataview.DataViewCtrl_GetColumnCount(*args, **kwargs)

    def GetColumn(*args, **kwargs):
        """GetColumn(self, unsigned int pos) -> DataViewColumn"""
        return _dataview.DataViewCtrl_GetColumn(*args, **kwargs)

    def GetColumns(self):
        """Returns a list of column objects."""
        return [self.GetColumn(i) for i in range(self.GetColumnCount())]

    def GetColumnPosition(*args, **kwargs):
        """GetColumnPosition(self, DataViewColumn column) -> int"""
        return _dataview.DataViewCtrl_GetColumnPosition(*args, **kwargs)

    def DeleteColumn(*args, **kwargs):
        """DeleteColumn(self, DataViewColumn column) -> bool"""
        return _dataview.DataViewCtrl_DeleteColumn(*args, **kwargs)

    def ClearColumns(*args, **kwargs):
        """ClearColumns(self) -> bool"""
        return _dataview.DataViewCtrl_ClearColumns(*args, **kwargs)

    def SetExpanderColumn(*args, **kwargs):
        """SetExpanderColumn(self, DataViewColumn col)"""
        return _dataview.DataViewCtrl_SetExpanderColumn(*args, **kwargs)

    def GetExpanderColumn(*args, **kwargs):
        """GetExpanderColumn(self) -> DataViewColumn"""
        return _dataview.DataViewCtrl_GetExpanderColumn(*args, **kwargs)

    def GetSortingColumn(*args, **kwargs):
        """GetSortingColumn(self) -> DataViewColumn"""
        return _dataview.DataViewCtrl_GetSortingColumn(*args, **kwargs)

    def SetIndent(*args, **kwargs):
        """SetIndent(self, int indent)"""
        return _dataview.DataViewCtrl_SetIndent(*args, **kwargs)

    def GetIndent(*args, **kwargs):
        """GetIndent(self) -> int"""
        return _dataview.DataViewCtrl_GetIndent(*args, **kwargs)

    def GetCurrentItem(*args, **kwargs):
        """GetCurrentItem(self) -> DataViewItem"""
        return _dataview.DataViewCtrl_GetCurrentItem(*args, **kwargs)

    def SetCurrentItem(*args, **kwargs):
        """SetCurrentItem(self, DataViewItem item)"""
        return _dataview.DataViewCtrl_SetCurrentItem(*args, **kwargs)

    def GetCurrentColumn(*args, **kwargs):
        """GetCurrentColumn(self) -> DataViewColumn"""
        return _dataview.DataViewCtrl_GetCurrentColumn(*args, **kwargs)

    def GetSelectedItemsCount(*args, **kwargs):
        """GetSelectedItemsCount(self) -> int"""
        return _dataview.DataViewCtrl_GetSelectedItemsCount(*args, **kwargs)

    def HasSelection(*args, **kwargs):
        """HasSelection(self) -> bool"""
        return _dataview.DataViewCtrl_HasSelection(*args, **kwargs)

    def GetSelection(*args, **kwargs):
        """GetSelection(self) -> DataViewItem"""
        return _dataview.DataViewCtrl_GetSelection(*args, **kwargs)

    def GetSelections(*args, **kwargs):
        """GetSelections(self) -> DataViewItemArray"""
        return _dataview.DataViewCtrl_GetSelections(*args, **kwargs)

    def SetSelections(*args, **kwargs):
        """SetSelections(self, DataViewItemArray sel)"""
        return _dataview.DataViewCtrl_SetSelections(*args, **kwargs)

    def Select(*args, **kwargs):
        """Select(self, DataViewItem item)"""
        return _dataview.DataViewCtrl_Select(*args, **kwargs)

    def Unselect(*args, **kwargs):
        """Unselect(self, DataViewItem item)"""
        return _dataview.DataViewCtrl_Unselect(*args, **kwargs)

    def IsSelected(*args, **kwargs):
        """IsSelected(self, DataViewItem item) -> bool"""
        return _dataview.DataViewCtrl_IsSelected(*args, **kwargs)

    def SelectAll(*args, **kwargs):
        """SelectAll(self)"""
        return _dataview.DataViewCtrl_SelectAll(*args, **kwargs)

    def UnselectAll(*args, **kwargs):
        """UnselectAll(self)"""
        return _dataview.DataViewCtrl_UnselectAll(*args, **kwargs)

    def Expand(*args, **kwargs):
        """Expand(self, DataViewItem item)"""
        return _dataview.DataViewCtrl_Expand(*args, **kwargs)

    def ExpandAncestors(*args, **kwargs):
        """ExpandAncestors(self, DataViewItem item)"""
        return _dataview.DataViewCtrl_ExpandAncestors(*args, **kwargs)

    def Collapse(*args, **kwargs):
        """Collapse(self, DataViewItem item)"""
        return _dataview.DataViewCtrl_Collapse(*args, **kwargs)

    def IsExpanded(*args, **kwargs):
        """IsExpanded(self, DataViewItem item) -> bool"""
        return _dataview.DataViewCtrl_IsExpanded(*args, **kwargs)

    def EnsureVisible(*args, **kwargs):
        """EnsureVisible(self, DataViewItem item, DataViewColumn column=None)"""
        return _dataview.DataViewCtrl_EnsureVisible(*args, **kwargs)

    def HitTest(*args, **kwargs):
        """HitTest(self, Point point, DataViewItem item, DataViewColumn column)"""
        return _dataview.DataViewCtrl_HitTest(*args, **kwargs)

    def GetItemRect(*args, **kwargs):
        """GetItemRect(self, DataViewItem item, DataViewColumn column=None) -> Rect"""
        return _dataview.DataViewCtrl_GetItemRect(*args, **kwargs)

    def SetRowHeight(*args, **kwargs):
        """SetRowHeight(self, int rowHeight) -> bool"""
        return _dataview.DataViewCtrl_SetRowHeight(*args, **kwargs)

    def EditItem(*args, **kwargs):
        """EditItem(self, DataViewItem item, DataViewColumn column)"""
        return _dataview.DataViewCtrl_EditItem(*args, **kwargs)

    def EnableDragSource(*args, **kwargs):
        """EnableDragSource(self, wxDataFormat format) -> bool"""
        return _dataview.DataViewCtrl_EnableDragSource(*args, **kwargs)

    def EnableDropTarget(*args, **kwargs):
        """EnableDropTarget(self, wxDataFormat format) -> bool"""
        return _dataview.DataViewCtrl_EnableDropTarget(*args, **kwargs)

    Model = property(GetModel,AssociateModel) 
    ColumnCount = property(GetColumnCount) 
    Columns = property(GetColumns) 
    ExpanderColumn = property(GetExpanderColumn,SetExpanderColumn) 
    SortingColumn = property(GetSortingColumn) 
    Indent = property(GetIndent,SetIndent) 
    Selection = property(GetSelection) 
    def GetClassDefaultAttributes(*args, **kwargs):
        """
        GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

        Get the default attributes for this class.  This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        user's system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignore under other platforms. Under Mac, it will change the size of
        the returned font. See `wx.Window.SetWindowVariant` for more about
        this.
        """
        return _dataview.DataViewCtrl_GetClassDefaultAttributes(*args, **kwargs)

    GetClassDefaultAttributes = staticmethod(GetClassDefaultAttributes)
_dataview.DataViewCtrl_swigregister(DataViewCtrl)

def PreDataViewCtrl(*args, **kwargs):
    """PreDataViewCtrl() -> DataViewCtrl"""
    val = _dataview.new_PreDataViewCtrl(*args, **kwargs)
    return val

def DataViewCtrl_GetClassDefaultAttributes(*args, **kwargs):
  """
    DataViewCtrl_GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

    Get the default attributes for this class.  This is useful if you want
    to use the same font or colour in your own control as in a standard
    control -- which is a much better idea than hard coding specific
    colours or fonts which might look completely out of place on the
    user's system, especially if it uses themes.

    The variant parameter is only relevant under Mac currently and is
    ignore under other platforms. Under Mac, it will change the size of
    the returned font. See `wx.Window.SetWindowVariant` for more about
    this.
    """
  return _dataview.DataViewCtrl_GetClassDefaultAttributes(*args, **kwargs)

class DataViewEvent(_core.NotifyEvent):
    """Proxy of C++ DataViewEvent class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, EventType commandType=wxEVT_NULL, int winid=0) -> DataViewEvent"""
        _dataview.DataViewEvent_swiginit(self,_dataview.new_DataViewEvent(*args, **kwargs))
    def GetItem(*args, **kwargs):
        """GetItem(self) -> DataViewItem"""
        return _dataview.DataViewEvent_GetItem(*args, **kwargs)

    def SetItem(*args, **kwargs):
        """SetItem(self, DataViewItem item)"""
        return _dataview.DataViewEvent_SetItem(*args, **kwargs)

    def GetColumn(*args, **kwargs):
        """GetColumn(self) -> int"""
        return _dataview.DataViewEvent_GetColumn(*args, **kwargs)

    def SetColumn(*args, **kwargs):
        """SetColumn(self, int col)"""
        return _dataview.DataViewEvent_SetColumn(*args, **kwargs)

    def GetModel(*args, **kwargs):
        """GetModel(self) -> DataViewModel"""
        return _dataview.DataViewEvent_GetModel(*args, **kwargs)

    def SetModel(*args, **kwargs):
        """SetModel(self, DataViewModel model)"""
        return _dataview.DataViewEvent_SetModel(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> wxVariant"""
        return _dataview.DataViewEvent_GetValue(*args, **kwargs)

    def SetValue(*args, **kwargs):
        """SetValue(self, wxVariant value)"""
        return _dataview.DataViewEvent_SetValue(*args, **kwargs)

    def IsEditCancelled(*args, **kwargs):
        """IsEditCancelled(self) -> bool"""
        return _dataview.DataViewEvent_IsEditCancelled(*args, **kwargs)

    def SetEditCanceled(*args, **kwargs):
        """SetEditCanceled(self, bool editCancelled)"""
        return _dataview.DataViewEvent_SetEditCanceled(*args, **kwargs)

    def SetDataViewColumn(*args, **kwargs):
        """SetDataViewColumn(self, DataViewColumn col)"""
        return _dataview.DataViewEvent_SetDataViewColumn(*args, **kwargs)

    def GetDataViewColumn(*args, **kwargs):
        """GetDataViewColumn(self) -> DataViewColumn"""
        return _dataview.DataViewEvent_GetDataViewColumn(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> Point"""
        return _dataview.DataViewEvent_GetPosition(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, int x, int y)"""
        return _dataview.DataViewEvent_SetPosition(*args, **kwargs)

    def GetCacheFrom(*args, **kwargs):
        """GetCacheFrom(self) -> int"""
        return _dataview.DataViewEvent_GetCacheFrom(*args, **kwargs)

    def GetCacheTo(*args, **kwargs):
        """GetCacheTo(self) -> int"""
        return _dataview.DataViewEvent_GetCacheTo(*args, **kwargs)

    def SetCache(*args, **kwargs):
        """SetCache(self, int from, int to)"""
        return _dataview.DataViewEvent_SetCache(*args, **kwargs)

    def SetDataObject(*args, **kwargs):
        """SetDataObject(self, wxDataObject obj)"""
        return _dataview.DataViewEvent_SetDataObject(*args, **kwargs)

    def GetDataObject(*args, **kwargs):
        """GetDataObject(self) -> wxDataObject"""
        return _dataview.DataViewEvent_GetDataObject(*args, **kwargs)

    def SetDataFormat(*args, **kwargs):
        """SetDataFormat(self, wxDataFormat format)"""
        return _dataview.DataViewEvent_SetDataFormat(*args, **kwargs)

    def GetDataFormat(*args, **kwargs):
        """GetDataFormat(self) -> wxDataFormat"""
        return _dataview.DataViewEvent_GetDataFormat(*args, **kwargs)

    def SetDataSize(*args, **kwargs):
        """SetDataSize(self, size_t size)"""
        return _dataview.DataViewEvent_SetDataSize(*args, **kwargs)

    def GetDataSize(*args, **kwargs):
        """GetDataSize(self) -> size_t"""
        return _dataview.DataViewEvent_GetDataSize(*args, **kwargs)

    def SetDataBuffer(*args, **kwargs):
        """SetDataBuffer(self, void buf)"""
        return _dataview.DataViewEvent_SetDataBuffer(*args, **kwargs)

    def GetDataBuffer(*args, **kwargs):
        """GetDataBuffer(self) -> void"""
        return _dataview.DataViewEvent_GetDataBuffer(*args, **kwargs)

    Column = property(GetColumn,SetColumn) 
    Model = property(GetModel,SetModel) 
    Value = property(GetValue,SetValue) 
    DataViewColumn = property(GetDataViewColumn,SetDataViewColumn) 
    Position = property(GetPosition,SetPosition) 
    DataObject = property(GetDataObject,SetDataObject) 
    DataFormat = property(GetDataFormat,SetDataFormat) 
_dataview.DataViewEvent_swigregister(DataViewEvent)

wxEVT_COMMAND_DATAVIEW_SELECTION_CHANGED = _dataview.wxEVT_COMMAND_DATAVIEW_SELECTION_CHANGED
wxEVT_COMMAND_DATAVIEW_ITEM_ACTIVATED = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_ACTIVATED
wxEVT_COMMAND_DATAVIEW_ITEM_COLLAPSED = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_COLLAPSED
wxEVT_COMMAND_DATAVIEW_ITEM_EXPANDED = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_EXPANDED
wxEVT_COMMAND_DATAVIEW_ITEM_COLLAPSING = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_COLLAPSING
wxEVT_COMMAND_DATAVIEW_ITEM_EXPANDING = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_EXPANDING
wxEVT_COMMAND_DATAVIEW_ITEM_START_EDITING = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_START_EDITING
wxEVT_COMMAND_DATAVIEW_ITEM_EDITING_STARTED = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_EDITING_STARTED
wxEVT_COMMAND_DATAVIEW_ITEM_EDITING_DONE = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_EDITING_DONE
wxEVT_COMMAND_DATAVIEW_ITEM_VALUE_CHANGED = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_VALUE_CHANGED
wxEVT_COMMAND_DATAVIEW_ITEM_CONTEXT_MENU = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_CONTEXT_MENU
wxEVT_COMMAND_DATAVIEW_COLUMN_HEADER_CLICK = _dataview.wxEVT_COMMAND_DATAVIEW_COLUMN_HEADER_CLICK
wxEVT_COMMAND_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK = _dataview.wxEVT_COMMAND_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK
wxEVT_COMMAND_DATAVIEW_COLUMN_SORTED = _dataview.wxEVT_COMMAND_DATAVIEW_COLUMN_SORTED
wxEVT_COMMAND_DATAVIEW_COLUMN_REORDERED = _dataview.wxEVT_COMMAND_DATAVIEW_COLUMN_REORDERED
wxEVT_COMMAND_DATAVIEW_ITEM_BEGIN_DRAG = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_BEGIN_DRAG
wxEVT_COMMAND_DATAVIEW_ITEM_DROP_POSSIBLE = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_DROP_POSSIBLE
wxEVT_COMMAND_DATAVIEW_ITEM_DROP = _dataview.wxEVT_COMMAND_DATAVIEW_ITEM_DROP
wxEVT_COMMAND_DATAVIEW_CACHE_HINT = _dataview.wxEVT_COMMAND_DATAVIEW_CACHE_HINT
EVT_DATAVIEW_SELECTION_CHANGED         = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_SELECTION_CHANGED, 1)
EVT_DATAVIEW_ITEM_ACTIVATED            = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_ACTIVATED, 1)
EVT_DATAVIEW_ITEM_COLLAPSED            = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_COLLAPSED, 1)
EVT_DATAVIEW_ITEM_EXPANDED             = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_EXPANDED, 1)
EVT_DATAVIEW_ITEM_COLLAPSING           = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_COLLAPSING, 1)
EVT_DATAVIEW_ITEM_EXPANDING            = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_EXPANDING, 1)
EVT_DATAVIEW_ITEM_START_EDITING        = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_START_EDITING, 1)    
EVT_DATAVIEW_ITEM_EDITING_STARTED      = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_EDITING_STARTED, 1)
EVT_DATAVIEW_ITEM_EDITING_DONE         = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_EDITING_DONE, 1)
EVT_DATAVIEW_ITEM_VALUE_CHANGED        = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_VALUE_CHANGED, 1)
EVT_DATAVIEW_ITEM_CONTEXT_MENU         = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_CONTEXT_MENU, 1)
EVT_DATAVIEW_COLUMN_HEADER_CLICK       = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_COLUMN_HEADER_CLICK, 1)
EVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK, 1)
EVT_DATAVIEW_COLUMN_SORTED             = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_COLUMN_SORTED, 1)
EVT_DATAVIEW_COLUMN_REORDERED          = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_COLUMN_REORDERED, 1)
EVT_DATAVIEW_ITEM_BEGIN_DRAG           = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_BEGIN_DRAG, 1)
EVT_DATAVIEW_ITEM_DROP_POSSIBLE        = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_DROP_POSSIBLE, 1)      
EVT_DATAVIEW_ITEM_DROP                 = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_ITEM_DROP, 1)
EVT_DATAVIEW_CACHE_HINT                = wx.PyEventBinder( wxEVT_COMMAND_DATAVIEW_CACHE_HINT, 1 )
    

class DataViewListStore(DataViewIndexListModel):
    """Proxy of C++ DataViewListStore class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> DataViewListStore"""
        _dataview.DataViewListStore_swiginit(self,_dataview.new_DataViewListStore(*args, **kwargs))
_dataview.DataViewListStore_swigregister(DataViewListStore)

class DataViewListCtrl(DataViewCtrl):
    """Proxy of C++ DataViewListCtrl class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=DV_ROW_LINES, 
            Validator validator=DefaultValidator) -> DataViewListCtrl
        """
        _dataview.DataViewListCtrl_swiginit(self,_dataview.new_DataViewListCtrl(*args, **kwargs))
        self._setOORInfo(self)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=DV_ROW_LINES, 
            Validator validator=DefaultValidator) -> bool

        Do the 2nd phase and create the GUI control.
        """
        return _dataview.DataViewListCtrl_Create(*args, **kwargs)

    def GetStore(*args, **kwargs):
        """GetStore(self) -> DataViewListStore"""
        return _dataview.DataViewListCtrl_GetStore(*args, **kwargs)

    def ItemToRow(*args, **kwargs):
        """ItemToRow(self, DataViewItem item) -> int"""
        return _dataview.DataViewListCtrl_ItemToRow(*args, **kwargs)

    def RowToItem(*args, **kwargs):
        """RowToItem(self, int row) -> DataViewItem"""
        return _dataview.DataViewListCtrl_RowToItem(*args, **kwargs)

    def GetSelectedRow(*args, **kwargs):
        """GetSelectedRow(self) -> int"""
        return _dataview.DataViewListCtrl_GetSelectedRow(*args, **kwargs)

    def SelectRow(*args, **kwargs):
        """SelectRow(self, unsigned int row)"""
        return _dataview.DataViewListCtrl_SelectRow(*args, **kwargs)

    def UnselectRow(*args, **kwargs):
        """UnselectRow(self, unsigned int row)"""
        return _dataview.DataViewListCtrl_UnselectRow(*args, **kwargs)

    def IsRowSelected(*args, **kwargs):
        """IsRowSelected(self, unsigned int row) -> bool"""
        return _dataview.DataViewListCtrl_IsRowSelected(*args, **kwargs)

    def AppendColumn(*args, **kwargs):
        """AppendColumn(self, DataViewColumn column, String varianttype="string") -> bool"""
        return _dataview.DataViewListCtrl_AppendColumn(*args, **kwargs)

    def PrependColumn(*args, **kwargs):
        """PrependColumn(self, DataViewColumn column, String varianttype="string") -> bool"""
        return _dataview.DataViewListCtrl_PrependColumn(*args, **kwargs)

    def InsertColumn(*args, **kwargs):
        """InsertColumn(self, unsigned int pos, DataViewColumn column, String varianttype="string") -> bool"""
        return _dataview.DataViewListCtrl_InsertColumn(*args, **kwargs)

    def AppendTextColumn(*args, **kwargs):
        """
        AppendTextColumn(self, String label, int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_LEFT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewListCtrl_AppendTextColumn(*args, **kwargs)

    def AppendToggleColumn(*args, **kwargs):
        """
        AppendToggleColumn(self, String label, int mode=DATAVIEW_CELL_ACTIVATABLE, int width=-1, 
            int align=ALIGN_LEFT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewListCtrl_AppendToggleColumn(*args, **kwargs)

    def AppendProgressColumn(*args, **kwargs):
        """
        AppendProgressColumn(self, String label, int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_LEFT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewListCtrl_AppendProgressColumn(*args, **kwargs)

    def AppendIconTextColumn(*args, **kwargs):
        """
        AppendIconTextColumn(self, String label, int mode=DATAVIEW_CELL_INERT, int width=-1, 
            int align=ALIGN_LEFT, int flags=DATAVIEW_COL_RESIZABLE) -> DataViewColumn
        """
        return _dataview.DataViewListCtrl_AppendIconTextColumn(*args, **kwargs)

    def AppendItem(*args, **kwargs):
        """AppendItem(self, wxVariantVector values, UIntPtr data=None)"""
        return _dataview.DataViewListCtrl_AppendItem(*args, **kwargs)

    def PrependItem(*args, **kwargs):
        """PrependItem(self, wxVariantVector values, UIntPtr data=None)"""
        return _dataview.DataViewListCtrl_PrependItem(*args, **kwargs)

    def InsertItem(*args, **kwargs):
        """InsertItem(self, unsigned int row, wxVariantVector values, UIntPtr data=None)"""
        return _dataview.DataViewListCtrl_InsertItem(*args, **kwargs)

    def DeleteItem(*args, **kwargs):
        """DeleteItem(self, unsigned int row)"""
        return _dataview.DataViewListCtrl_DeleteItem(*args, **kwargs)

    def DeleteAllItems(*args, **kwargs):
        """DeleteAllItems(self)"""
        return _dataview.DataViewListCtrl_DeleteAllItems(*args, **kwargs)

    def SetValue(*args, **kwargs):
        """SetValue(self, wxVariant value, unsigned int row, unsigned int col)"""
        return _dataview.DataViewListCtrl_SetValue(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self, unsigned int row, unsigned int col) -> wxVariant"""
        return _dataview.DataViewListCtrl_GetValue(*args, **kwargs)

    def SetTextValue(*args, **kwargs):
        """SetTextValue(self, String value, unsigned int row, unsigned int col)"""
        return _dataview.DataViewListCtrl_SetTextValue(*args, **kwargs)

    def GetTextValue(*args, **kwargs):
        """GetTextValue(self, unsigned int row, unsigned int col) -> String"""
        return _dataview.DataViewListCtrl_GetTextValue(*args, **kwargs)

    def SetToggleValue(*args, **kwargs):
        """SetToggleValue(self, bool value, unsigned int row, unsigned int col)"""
        return _dataview.DataViewListCtrl_SetToggleValue(*args, **kwargs)

    def GetToggleValue(*args, **kwargs):
        """GetToggleValue(self, unsigned int row, unsigned int col) -> bool"""
        return _dataview.DataViewListCtrl_GetToggleValue(*args, **kwargs)

    def SetItemData(*args, **kwargs):
        """SetItemData(self, DataViewItem item, UIntPtr data)"""
        return _dataview.DataViewListCtrl_SetItemData(*args, **kwargs)

    def GetItemData(*args, **kwargs):
        """GetItemData(self, DataViewItem item) -> UIntPtr"""
        return _dataview.DataViewListCtrl_GetItemData(*args, **kwargs)

_dataview.DataViewListCtrl_swigregister(DataViewListCtrl)

def PreDataViewListCtrl(*args, **kwargs):
    """PreDataViewListCtrl() -> DataViewListCtrl"""
    val = _dataview.new_PreDataViewListCtrl(*args, **kwargs)
    return val

class DataViewTreeStoreNode(object):
    """Proxy of C++ DataViewTreeStoreNode class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, DataViewTreeStoreNode parent, String text, Icon icon=wxNullIcon, 
            wxClientData data=None) -> DataViewTreeStoreNode
        """
        _dataview.DataViewTreeStoreNode_swiginit(self,_dataview.new_DataViewTreeStoreNode(*args, **kwargs))
    __swig_destroy__ = _dataview.delete_DataViewTreeStoreNode
    __del__ = lambda self : None;
    def SetText(*args, **kwargs):
        """SetText(self, String text)"""
        return _dataview.DataViewTreeStoreNode_SetText(*args, **kwargs)

    def GetText(*args, **kwargs):
        """GetText(self) -> String"""
        return _dataview.DataViewTreeStoreNode_GetText(*args, **kwargs)

    def SetIcon(*args, **kwargs):
        """SetIcon(self, Icon icon)"""
        return _dataview.DataViewTreeStoreNode_SetIcon(*args, **kwargs)

    def GetIcon(*args, **kwargs):
        """GetIcon(self) -> Icon"""
        return _dataview.DataViewTreeStoreNode_GetIcon(*args, **kwargs)

    def SetData(*args, **kwargs):
        """SetData(self, wxClientData data)"""
        return _dataview.DataViewTreeStoreNode_SetData(*args, **kwargs)

    def GetData(*args, **kwargs):
        """GetData(self) -> wxClientData"""
        return _dataview.DataViewTreeStoreNode_GetData(*args, **kwargs)

    def GetItem(*args, **kwargs):
        """GetItem(self) -> DataViewItem"""
        return _dataview.DataViewTreeStoreNode_GetItem(*args, **kwargs)

    def IsContainer(*args, **kwargs):
        """IsContainer(self) -> bool"""
        return _dataview.DataViewTreeStoreNode_IsContainer(*args, **kwargs)

    def GetParent(*args, **kwargs):
        """GetParent(self) -> DataViewTreeStoreNode"""
        return _dataview.DataViewTreeStoreNode_GetParent(*args, **kwargs)

_dataview.DataViewTreeStoreNode_swigregister(DataViewTreeStoreNode)

class DataViewTreeStoreNodeList_iterator(object):
    """This class serves as an iterator for a wxDataViewTreeStoreNodeList object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewTreeStoreNodeList_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> DataViewTreeStoreNode"""
        return _dataview.DataViewTreeStoreNodeList_iterator_next(*args, **kwargs)

_dataview.DataViewTreeStoreNodeList_iterator_swigregister(DataViewTreeStoreNodeList_iterator)

class DataViewTreeStoreNodeList(object):
    """
    This class wraps a wxList-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _dataview.delete_DataViewTreeStoreNodeList
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return _dataview.DataViewTreeStoreNodeList___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> DataViewTreeStoreNode"""
        return _dataview.DataViewTreeStoreNodeList___getitem__(*args, **kwargs)

    def __contains__(*args, **kwargs):
        """__contains__(self, DataViewTreeStoreNode obj) -> bool"""
        return _dataview.DataViewTreeStoreNodeList___contains__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> DataViewTreeStoreNodeList_iterator"""
        return _dataview.DataViewTreeStoreNodeList___iter__(*args, **kwargs)

    def index(*args, **kwargs):
        """index(self, DataViewTreeStoreNode obj) -> int"""
        return _dataview.DataViewTreeStoreNodeList_index(*args, **kwargs)

    def __repr__(self):
        return "wxDataViewTreeStoreNodeList: " + repr(list(self))

_dataview.DataViewTreeStoreNodeList_swigregister(DataViewTreeStoreNodeList)

class DataViewTreeStoreContainerNode(DataViewTreeStoreNode):
    """Proxy of C++ DataViewTreeStoreContainerNode class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, DataViewTreeStoreNode parent, String text, Icon icon=wxNullIcon, 
            Icon expanded=wxNullIcon, wxClientData data=None) -> DataViewTreeStoreContainerNode
        """
        _dataview.DataViewTreeStoreContainerNode_swiginit(self,_dataview.new_DataViewTreeStoreContainerNode(*args, **kwargs))
    __swig_destroy__ = _dataview.delete_DataViewTreeStoreContainerNode
    __del__ = lambda self : None;
    def GetChildren(*args):
        """
        GetChildren(self) -> DataViewTreeStoreNodeList
        GetChildren(self) -> DataViewTreeStoreNodeList
        """
        return _dataview.DataViewTreeStoreContainerNode_GetChildren(*args)

    def SetExpandedIcon(*args, **kwargs):
        """SetExpandedIcon(self, Icon icon)"""
        return _dataview.DataViewTreeStoreContainerNode_SetExpandedIcon(*args, **kwargs)

    def GetExpandedIcon(*args, **kwargs):
        """GetExpandedIcon(self) -> Icon"""
        return _dataview.DataViewTreeStoreContainerNode_GetExpandedIcon(*args, **kwargs)

    def SetExpanded(*args, **kwargs):
        """SetExpanded(self, bool expanded=True)"""
        return _dataview.DataViewTreeStoreContainerNode_SetExpanded(*args, **kwargs)

    def IsExpanded(*args, **kwargs):
        """IsExpanded(self) -> bool"""
        return _dataview.DataViewTreeStoreContainerNode_IsExpanded(*args, **kwargs)

_dataview.DataViewTreeStoreContainerNode_swigregister(DataViewTreeStoreContainerNode)

class DataViewTreeStore(DataViewModel):
    """Proxy of C++ DataViewTreeStore class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> DataViewTreeStore"""
        _dataview.DataViewTreeStore_swiginit(self,_dataview.new_DataViewTreeStore(*args, **kwargs))
    __swig_destroy__ = _dataview.delete_DataViewTreeStore
    __del__ = lambda self : None;
    def AppendItem(*args, **kwargs):
        """
        AppendItem(self, DataViewItem parent, String text, Icon icon=wxNullIcon, 
            wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeStore_AppendItem(*args, **kwargs)

    def PrependItem(*args, **kwargs):
        """
        PrependItem(self, DataViewItem parent, String text, Icon icon=wxNullIcon, 
            wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeStore_PrependItem(*args, **kwargs)

    def InsertItem(*args, **kwargs):
        """
        InsertItem(self, DataViewItem parent, DataViewItem previous, String text, 
            Icon icon=wxNullIcon, wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeStore_InsertItem(*args, **kwargs)

    def PrependContainer(*args, **kwargs):
        """
        PrependContainer(self, DataViewItem parent, String text, Icon icon=wxNullIcon, 
            Icon expanded=wxNullIcon, wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeStore_PrependContainer(*args, **kwargs)

    def AppendContainer(*args, **kwargs):
        """
        AppendContainer(self, DataViewItem parent, String text, Icon icon=wxNullIcon, 
            Icon expanded=wxNullIcon, wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeStore_AppendContainer(*args, **kwargs)

    def InsertContainer(*args, **kwargs):
        """
        InsertContainer(self, DataViewItem parent, DataViewItem previous, String text, 
            Icon icon=wxNullIcon, Icon expanded=wxNullIcon, 
            wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeStore_InsertContainer(*args, **kwargs)

    def GetNthChild(*args, **kwargs):
        """GetNthChild(self, DataViewItem parent, unsigned int pos) -> DataViewItem"""
        return _dataview.DataViewTreeStore_GetNthChild(*args, **kwargs)

    def GetChildCount(*args, **kwargs):
        """GetChildCount(self, DataViewItem parent) -> int"""
        return _dataview.DataViewTreeStore_GetChildCount(*args, **kwargs)

    def SetItemText(*args, **kwargs):
        """SetItemText(self, DataViewItem item, String text)"""
        return _dataview.DataViewTreeStore_SetItemText(*args, **kwargs)

    def GetItemText(*args, **kwargs):
        """GetItemText(self, DataViewItem item) -> String"""
        return _dataview.DataViewTreeStore_GetItemText(*args, **kwargs)

    def SetItemIcon(*args, **kwargs):
        """SetItemIcon(self, DataViewItem item, Icon icon)"""
        return _dataview.DataViewTreeStore_SetItemIcon(*args, **kwargs)

    def GetItemIcon(*args, **kwargs):
        """GetItemIcon(self, DataViewItem item) -> Icon"""
        return _dataview.DataViewTreeStore_GetItemIcon(*args, **kwargs)

    def SetItemExpandedIcon(*args, **kwargs):
        """SetItemExpandedIcon(self, DataViewItem item, Icon icon)"""
        return _dataview.DataViewTreeStore_SetItemExpandedIcon(*args, **kwargs)

    def GetItemExpandedIcon(*args, **kwargs):
        """GetItemExpandedIcon(self, DataViewItem item) -> Icon"""
        return _dataview.DataViewTreeStore_GetItemExpandedIcon(*args, **kwargs)

    def SetItemData(*args, **kwargs):
        """SetItemData(self, DataViewItem item, wxClientData data)"""
        return _dataview.DataViewTreeStore_SetItemData(*args, **kwargs)

    def GetItemData(*args, **kwargs):
        """GetItemData(self, DataViewItem item) -> wxClientData"""
        return _dataview.DataViewTreeStore_GetItemData(*args, **kwargs)

    def DeleteItem(*args, **kwargs):
        """DeleteItem(self, DataViewItem item)"""
        return _dataview.DataViewTreeStore_DeleteItem(*args, **kwargs)

    def DeleteChildren(*args, **kwargs):
        """DeleteChildren(self, DataViewItem item)"""
        return _dataview.DataViewTreeStore_DeleteChildren(*args, **kwargs)

    def DeleteAllItems(*args, **kwargs):
        """DeleteAllItems(self)"""
        return _dataview.DataViewTreeStore_DeleteAllItems(*args, **kwargs)

_dataview.DataViewTreeStore_swigregister(DataViewTreeStore)

class DataViewTreeCtrl(DataViewCtrl,_core.WithImages):
    """Proxy of C++ DataViewTreeCtrl class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=wxDV_NO_HEADER|wxDV_ROW_LINES, 
            Validator validator=DefaultValidator) -> DataViewTreeCtrl
        """
        _dataview.DataViewTreeCtrl_swiginit(self,_dataview.new_DataViewTreeCtrl(*args, **kwargs))
        self._setOORInfo(self)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=wxDV_NO_HEADER|wxDV_ROW_LINES, 
            Validator validator=DefaultValidator) -> bool

        Do the 2nd phase and create the GUI control.
        """
        return _dataview.DataViewTreeCtrl_Create(*args, **kwargs)

    def GetStore(*args, **kwargs):
        """GetStore(self) -> DataViewTreeStore"""
        return _dataview.DataViewTreeCtrl_GetStore(*args, **kwargs)

    def IsContainer(*args, **kwargs):
        """IsContainer(self, DataViewItem item) -> bool"""
        return _dataview.DataViewTreeCtrl_IsContainer(*args, **kwargs)

    def AppendItem(*args, **kwargs):
        """AppendItem(self, DataViewItem parent, String text, int icon=-1, wxClientData data=None) -> DataViewItem"""
        return _dataview.DataViewTreeCtrl_AppendItem(*args, **kwargs)

    def PrependItem(*args, **kwargs):
        """PrependItem(self, DataViewItem parent, String text, int icon=-1, wxClientData data=None) -> DataViewItem"""
        return _dataview.DataViewTreeCtrl_PrependItem(*args, **kwargs)

    def InsertItem(*args, **kwargs):
        """
        InsertItem(self, DataViewItem parent, DataViewItem previous, String text, 
            int icon=-1, wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeCtrl_InsertItem(*args, **kwargs)

    def PrependContainer(*args, **kwargs):
        """
        PrependContainer(self, DataViewItem parent, String text, int icon=-1, int expanded=-1, 
            wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeCtrl_PrependContainer(*args, **kwargs)

    def AppendContainer(*args, **kwargs):
        """
        AppendContainer(self, DataViewItem parent, String text, int icon=-1, int expanded=-1, 
            wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeCtrl_AppendContainer(*args, **kwargs)

    def InsertContainer(*args, **kwargs):
        """
        InsertContainer(self, DataViewItem parent, DataViewItem previous, String text, 
            int icon=-1, int expanded=-1, wxClientData data=None) -> DataViewItem
        """
        return _dataview.DataViewTreeCtrl_InsertContainer(*args, **kwargs)

    def GetNthChild(*args, **kwargs):
        """GetNthChild(self, DataViewItem parent, unsigned int pos) -> DataViewItem"""
        return _dataview.DataViewTreeCtrl_GetNthChild(*args, **kwargs)

    def GetChildCount(*args, **kwargs):
        """GetChildCount(self, DataViewItem parent) -> int"""
        return _dataview.DataViewTreeCtrl_GetChildCount(*args, **kwargs)

    def SetItemText(*args, **kwargs):
        """SetItemText(self, DataViewItem item, String text)"""
        return _dataview.DataViewTreeCtrl_SetItemText(*args, **kwargs)

    def GetItemText(*args, **kwargs):
        """GetItemText(self, DataViewItem item) -> String"""
        return _dataview.DataViewTreeCtrl_GetItemText(*args, **kwargs)

    def SetItemIcon(*args, **kwargs):
        """SetItemIcon(self, DataViewItem item, Icon icon)"""
        return _dataview.DataViewTreeCtrl_SetItemIcon(*args, **kwargs)

    def GetItemIcon(*args, **kwargs):
        """GetItemIcon(self, DataViewItem item) -> Icon"""
        return _dataview.DataViewTreeCtrl_GetItemIcon(*args, **kwargs)

    def SetItemExpandedIcon(*args, **kwargs):
        """SetItemExpandedIcon(self, DataViewItem item, Icon icon)"""
        return _dataview.DataViewTreeCtrl_SetItemExpandedIcon(*args, **kwargs)

    def GetItemExpandedIcon(*args, **kwargs):
        """GetItemExpandedIcon(self, DataViewItem item) -> Icon"""
        return _dataview.DataViewTreeCtrl_GetItemExpandedIcon(*args, **kwargs)

    def SetItemData(*args, **kwargs):
        """SetItemData(self, DataViewItem item, wxClientData data)"""
        return _dataview.DataViewTreeCtrl_SetItemData(*args, **kwargs)

    def GetItemData(*args, **kwargs):
        """GetItemData(self, DataViewItem item) -> wxClientData"""
        return _dataview.DataViewTreeCtrl_GetItemData(*args, **kwargs)

    def DeleteItem(*args, **kwargs):
        """DeleteItem(self, DataViewItem item)"""
        return _dataview.DataViewTreeCtrl_DeleteItem(*args, **kwargs)

    def DeleteChildren(*args, **kwargs):
        """DeleteChildren(self, DataViewItem item)"""
        return _dataview.DataViewTreeCtrl_DeleteChildren(*args, **kwargs)

    def DeleteAllItems(*args, **kwargs):
        """DeleteAllItems(self)"""
        return _dataview.DataViewTreeCtrl_DeleteAllItems(*args, **kwargs)

_dataview.DataViewTreeCtrl_swigregister(DataViewTreeCtrl)

def PreDataViewTreeCtrl(*args, **kwargs):
    """PreDataViewTreeCtrl() -> DataViewTreeCtrl"""
    val = _dataview.new_PreDataViewTreeCtrl(*args, **kwargs)
    return val



