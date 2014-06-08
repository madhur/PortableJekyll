#!/usr/bin/env python

"""
highlightedtextplugin.py

A display text custom widget plugin for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from PyQt4 import QtCore, QtGui, QtDesigner
from highlightedtextedit import HighlightedTextEdit


def Q_TYPEID(class_name):

    return "com.trolltech.Qt.Designer.TaskMenu"


class HighlightedTextEditPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    """HighlightedTextEditPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin)

    Provides a Python custom plugin for Qt Designer by implementing the
    QDesignerCustomWidgetPlugin via a PyQt-specific custom plugin class.
    """

    # The __init__() method is only used to set up the plugin and define its
    # initialized variable.
    def __init__(self, parent=None):

        super(HighlightedTextEditPlugin, self).__init__(parent)

        self.initialized = False

    # The initialize() and isInitialized() methods allow the plugin to set up
    # any required resources, ensuring that this can only happen once for each
    # plugin.
    def initialize(self, formEditor):

        if self.initialized:
            return

        # We register an extension factory to add a extension to each form's
        # task menu.
        manager = formEditor.extensionManager()
        if manager:
            self.factory = HighlightedTextEditTaskMenuFactory(manager)
            manager.registerExtensions(
                self.factory, Q_TYPEID("QPyDesignerTaskMenuExtension")
                )

        self.initialized = True

    def isInitialized(self):

        return self.initialized

    # This factory method creates new instances of our custom widget with the
    # appropriate parent.
    def createWidget(self, parent):
        widget = HighlightedTextEdit(parent)

        # We install an event filter on the text editor to prevent the
        # contents from being modified outside the custom editor dialog.
        widget.installEventFilter(self)
        return widget

    def eventFilter(self, obj, event):

        if isinstance(obj, QtGui.QTextEdit):

            if isinstance(event, QtGui.QKeyEvent):
                return True
            elif isinstance(event, QtGui.QFocusEvent):
                return True

        return False

    # This method returns the name of the custom widget class that is provided
    # by this plugin.
    def name(self):
        return "HighlightedTextEdit"

    # Returns the name of the group in Qt Designer's widget box that this
    # widget belongs to.
    def group(self):
        return "PyQt Examples"

    # Returns the icon used to represent the custom widget in Qt Designer's
    # widget box.
    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

    # Returns a short description of the custom widget for use in a tool tip.
    def toolTip(self):
        return ""

    # Returns a short description of the custom widget for use in a "What's
    # This?" help message for the widget.
    def whatsThis(self):
        return ""

    # Returns True if the custom widget acts as a container for other widgets;
    # otherwise returns False. Note that plugins for custom containers also
    # need to provide an implementation of the QDesignerContainerExtension
    # interface if they need to add custom editing support to Qt Designer.
    def isContainer(self):
        return False

    # Returns an XML description of a custom widget instance that describes
    # default values for its properties. Each custom widget created by this
    # plugin will be configured using this description.
    def domXml(self):
        return '<widget class="HighlightedTextEdit" name="highlightedTextEdit" />\n'

    # Returns the module containing the custom widget class. It may include
    # a module path.
    def includeFile(self):
        return "highlightedtextedit"


class HighlightedTextEditTaskMenuFactory(QtDesigner.QExtensionFactory):

    """HighlightedTextEditTaskMenuFactory(QtDesigner.QExtensionFactory)

    Provides 
    """
    def __init__(self, parent = None):

        QtDesigner.QExtensionFactory.__init__(self, parent)

    # This standard factory function returns an object to represent a task
    # menu entry.
    def createExtension(self, obj, iid, parent):

        if iid != Q_TYPEID("QPyDesignerTaskMenuExtension"):
            return None

        # We pass the instance of the custom widget to the object representing
        # the task menu entry so that the contents of the custom widget can be
        # modified.
        if isinstance(obj, HighlightedTextEdit):
            return HighlightedTextEditTaskMenu(obj, parent)

        return None


class HighlightedTextEditTaskMenu(QtDesigner.QPyDesignerTaskMenuExtension):

    """HighlightedTextEditTaskMenu(QtDesigner.QPyDesignerTaskMenuExtension)

    Provides a task menu entry to enable text in the highlighted text
    editor to be edited via a dialog.
    """

    def __init__(self, textEdit, parent):

        super(HighlightedTextEditTaskMenu, self).__init__(parent)

        self.textEdit = textEdit

        # Create the action to be added to the form's existing task menu
        # and connect it to a slot in this class.
        self.editStateAction = QtGui.QAction("Edit Text...", self,
                triggered=self.editText)

    def preferredEditAction(self):

        return self.editStateAction

    def taskActions(self):

        return [self.editStateAction]

    # The editText() slot is called when the action that represents our task
    # menu entry is triggered. We open a dialog, passing the custom widget as
    # an argument.
    @QtCore.pyqtSlot()
    def editText(self):

        HighlightedTextEditDialog(self.textEdit).exec_()


class HighlightedTextEditDialog(QtGui.QDialog):

    """HighlightedTextEditDialog(QtGui.QDialog)

    Provides a dialog that is used to edit the contents of the custom widget.
    """

    def __init__(self, editor, parent=None):

        super(HighlightedTextEditDialog, self).__init__(parent)

        self.editor = editor
        self.textEdit = HighlightedTextEdit()
        self.textEdit.setCode(editor.getCode())

        self.textEdit.installEventFilter(self)

        okButton = QtGui.QPushButton("&OK")
        okButton.clicked.connect(self.updateText)

        cancelButton = QtGui.QPushButton("&Cancel")
        cancelButton.clicked.connect(self.reject)

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def eventFilter(self, obj, event):

        if obj == self.textEdit:

            if isinstance(event, QtGui.QKeyEvent):
                if event.key() == QtCore.Qt.Key_Return and \
                    int(event.modifiers() & QtCore.Qt.ControlModifier) == QtCore.Qt.ControlModifier:

                    if event.type() == QtGui.QEvent.KeyPress:

                        cursor = self.textEdit.textCursor()
                        char_format = cursor.charFormat()
                        char_format.setFontPointSize(self.textEdit.font.pointSizeF()/2.0)
                        block_format = cursor.blockFormat()
                        cursor.insertBlock(block_format, char_format)
                        self.textEdit.setTextCursor(cursor)
                        return True

        return False

    # When we update the contents of the custom widget, we access its
    # properties via the QDesignerFormWindowInterface API so that Qt Designer
    # can integrate the changes we make into its undo-redo management.
    def updateText(self):

        formWindow = QtDesigner.QDesignerFormWindowInterface.findFormWindow(self.editor)
        if formWindow:
            formWindow.cursor().setProperty("code", self.textEdit.getCode())

        self.accept()


# Define the image used for the icon.
_logo_16x16_xpm = [
    "16 16 6 1",
    " 	c None",
    ".	c #FFFFFF",
    "a	c #000000",
    "b	c #FF4040",
    "c	c #40C040",
    "d	c #4040FF",
    ".........b......",
    ".........b......",
    ".........b......",
    "...aaaa..bbbb...",
    "..a...a..b...b..",
    "..a...a..b...b..",
    "..a...a..b...b..",
    "...aaa.a.bbbb...",
    ".............d..",
    ".............d..",
    ".............d..",
    "...ccc....dddd..",
    "..c...c..d...d..",
    "..c......d...d..",
    "..c...c..d...d..",
    "...ccc....dddd.."]

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)
