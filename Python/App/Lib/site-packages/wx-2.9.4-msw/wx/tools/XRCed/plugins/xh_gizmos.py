# Name:         gizmos.py
# Purpose:      XML handlers for wx.gismos classes
# Author:       Roman Rolinsky <rolinsky@femagsoft.com>
# Created:      09.07.2007
# RCS-ID:       $Id$

import wx
import wx.xrc as xrc
import wx.gizmos as gizmos

class LEDNumberCtrlXmlHandler(xrc.XmlResourceHandler):
    def __init__(self):
        xrc.XmlResourceHandler.__init__(self)
        # Standard styles
        self.AddWindowStyles()
        # Custom styles
        self.AddStyle('wxLED_ALIGN_LEFT', gizmos.LED_ALIGN_LEFT)
        self.AddStyle('wxLED_ALIGN_RIGHT', gizmos.LED_ALIGN_RIGHT)
        self.AddStyle('wxLED_ALIGN_CENTER', gizmos.LED_ALIGN_CENTER)
        self.AddStyle('wxLED_DRAW_FADED', gizmos.LED_DRAW_FADED)
        
    def CanHandle(self,node):
        return self.IsOfClass(node, 'LEDNumberCtrl')

    # Process XML parameters and create the object
    def DoCreateResource(self):
        assert self.GetInstance() is None
        w = gizmos.LEDNumberCtrl(self.GetParentAsWindow(),
                                 self.GetID(),
                                 self.GetPosition(),
                                 self.GetSize(),
                                 self.GetStyle())
        # wxLED_ALIGN_MASK was incorrect
        align = self.GetStyle() & 7
        if align: w.SetAlignment(self.GetStyle() & 7)
        w.SetValue(self.GetText('value'))
        self.SetupWindow(w)
        return w


class EditableListBoxXmlHandler(xrc.XmlResourceHandler):
    def __init__(self):
        xrc.XmlResourceHandler.__init__(self)
        # Standard styles
        self.AddWindowStyles()
        # Custom styles
        self.AddStyle('wxEL_ALLOW_NEW', gizmos.EL_ALLOW_NEW)
        self.AddStyle('wxEL_ALLOW_EDIT', gizmos.EL_ALLOW_EDIT)
        self.AddStyle('wxEL_ALLOW_DELETE', gizmos.EL_ALLOW_DELETE)
        
    def CanHandle(self, node):
        return self.IsOfClass(node, 'EditableListBox')
#        return self.IsOfClass(node, 'EditableListBox') or \
#               self.insideBox and node.GetName() == 'item'

    # Process XML parameters and create the object
    def DoCreateResource(self):
        assert self.GetInstance() is None
        
        w = gizmos.EditableListBox(self.GetParentAsWindow(),
                                   self.GetID(),
                                   self.GetText("label"),
                                   self.GetPosition(),
                                   self.GetSize(),
                                   self.GetStyle(),
                                   self.GetName())
        
        # Doesn't work
        #self.insideBox = True
        #self.CreateChildrenPrivately(None, self.GetParamNode('content'))
        #self.insideBox = False
        
        # Long way
        strings = []
        n = self.GetParamNode('content')
        if n: n = n.GetChildren()
        while n:
            if n.GetType() != xrc.XML_ELEMENT_NODE or n.GetName() != "item":
                n = n.GetNext()
                continue
            strings.append(n.GetNodeContent())
            n = n.GetNext()
        w.SetStrings(strings)
        self.SetupWindow(w)
        return w


class TreeListCtrlXmlHandler(xrc.XmlResourceHandler):
    def __init__(self):
        xrc.XmlResourceHandler.__init__(self)
        # Standard styles
        self.AddWindowStyles()
        # Custom styles
        self.AddStyle('wxTR_DEFAULT_STYLE', wx.TR_DEFAULT_STYLE)
        self.AddStyle('wxTR_EDIT_LABELS', wx.TR_EDIT_LABELS)
        self.AddStyle('wxTR_NO_BUTTONS', wx.TR_NO_BUTTONS)
        self.AddStyle('wxTR_HAS_BUTTONS', wx.TR_HAS_BUTTONS)
        self.AddStyle('wxTR_TWIST_BUTTONS', wx.TR_TWIST_BUTTONS)
        self.AddStyle('wxTR_NO_LINES', wx.TR_NO_LINES)
        self.AddStyle('wxTR_FULL_ROW_HIGHLIGHT', wx.TR_FULL_ROW_HIGHLIGHT)
        self.AddStyle('wxTR_LINES_AT_ROOT', wx.TR_LINES_AT_ROOT)
        self.AddStyle('wxTR_HIDE_ROOT', wx.TR_HIDE_ROOT)
        self.AddStyle('wxTR_ROW_LINES', wx.TR_ROW_LINES)
        self.AddStyle('wxTR_HAS_VARIABLE_ROW_HEIGHT', wx.TR_HAS_VARIABLE_ROW_HEIGHT)
        self.AddStyle('wxTR_SINGLE', wx.TR_SINGLE)
        self.AddStyle('wxTR_MULTIPLE', wx.TR_MULTIPLE)
        self.AddStyle('wxTR_EXTENDED', wx.TR_EXTENDED)
        
    def CanHandle(self, node):
        return self.IsOfClass(node, 'TreeListCtrl')

    # Process XML parameters and create the object
    def DoCreateResource(self):
        assert self.GetInstance() is None
        
        w = gizmos.TreeListCtrl(self.GetParentAsWindow(),
                                self.GetID(),
                                style=self.GetStyle(),
                                name=self.GetName())
        w.AddColumn("Main column")
        w.AddColumn('Column 1')
        w.SetMainColumn(0)
        w.SetColumnWidth(0, 50)
        w.SetColumnWidth(1, 50)
        root = w.AddRoot('Root')
        w.SetItemText(root, "col 1", 1)
        item1 = w.AppendItem(root, 'item 1')
        w.SetItemText(item1, "col 1", 1)
        w.Expand(root)
        return w


class DynamicSashWindowXmlHandler(xrc.XmlResourceHandler):
    def __init__(self):
        xrc.XmlResourceHandler.__init__(self)
        # Standard styles
        self.AddWindowStyles()
        # Custom styles
        self.AddStyle('wxDS_MANAGE_SCROLLBARS', gizmos.DS_MANAGE_SCROLLBARS)
        self.AddStyle('wxDS_DRAG_CORNER', gizmos.DS_DRAG_CORNER)
        
    def CanHandle(self, node):
        return self.IsOfClass(node, 'DynamicSashWindow')

    # Process XML parameters and create the object
    def DoCreateResource(self):
        assert self.GetInstance() is None
        
        w = gizmos.DynamicSashWindow(self.GetParentAsWindow(),
                                     self.GetID(),
                                     self.GetPosition(),
                                     self.GetSize(),
                                     self.GetStyle(),
                                     self.GetName())
        
        self.SetupWindow(w)
        return w

