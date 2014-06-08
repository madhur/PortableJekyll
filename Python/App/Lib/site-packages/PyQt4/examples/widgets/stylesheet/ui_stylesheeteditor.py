# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stylesheeteditor.ui'
#
# Created: Fri Dec  3 17:11:04 2010
#      by: PyQt4 UI code generator snapshot-4.8.2-4dddaa7e9c07
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StyleSheetEditor(object):
    def setupUi(self, StyleSheetEditor):
        StyleSheetEditor.setObjectName(_fromUtf8("StyleSheetEditor"))
        StyleSheetEditor.resize(445, 289)
        self.gridlayout = QtGui.QGridLayout(StyleSheetEditor)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        spacerItem = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 0, 6, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.styleSheetCombo = QtGui.QComboBox(StyleSheetEditor)
        self.styleSheetCombo.setObjectName(_fromUtf8("styleSheetCombo"))
        self.styleSheetCombo.addItem(_fromUtf8(""))
        self.styleSheetCombo.addItem(_fromUtf8(""))
        self.styleSheetCombo.addItem(_fromUtf8(""))
        self.gridlayout.addWidget(self.styleSheetCombo, 0, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(10, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.styleCombo = QtGui.QComboBox(StyleSheetEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.styleCombo.sizePolicy().hasHeightForWidth())
        self.styleCombo.setSizePolicy(sizePolicy)
        self.styleCombo.setObjectName(_fromUtf8("styleCombo"))
        self.gridlayout.addWidget(self.styleCombo, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(StyleSheetEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridlayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem3 = QtGui.QSpacerItem(321, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.saveButton = QtGui.QPushButton(StyleSheetEditor)
        self.saveButton.setEnabled(True)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.hboxlayout.addWidget(self.saveButton)
        self.applyButton = QtGui.QPushButton(StyleSheetEditor)
        self.applyButton.setEnabled(False)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.hboxlayout.addWidget(self.applyButton)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 7)
        self.styleTextEdit = QtGui.QTextEdit(StyleSheetEditor)
        self.styleTextEdit.setObjectName(_fromUtf8("styleTextEdit"))
        self.gridlayout.addWidget(self.styleTextEdit, 1, 0, 1, 7)
        self.label_8 = QtGui.QLabel(StyleSheetEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridlayout.addWidget(self.label_8, 0, 4, 1, 1)

        self.retranslateUi(StyleSheetEditor)
        QtCore.QMetaObject.connectSlotsByName(StyleSheetEditor)

    def retranslateUi(self, StyleSheetEditor):
        StyleSheetEditor.setWindowTitle(QtGui.QApplication.translate("StyleSheetEditor", "Style Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.styleSheetCombo.setItemText(0, QtGui.QApplication.translate("StyleSheetEditor", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.styleSheetCombo.setItemText(1, QtGui.QApplication.translate("StyleSheetEditor", "Coffee", None, QtGui.QApplication.UnicodeUTF8))
        self.styleSheetCombo.setItemText(2, QtGui.QApplication.translate("StyleSheetEditor", "Pagefold", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("StyleSheetEditor", "Style:", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("StyleSheetEditor", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("StyleSheetEditor", "&Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("StyleSheetEditor", "Style Sheet:", None, QtGui.QApplication.UnicodeUTF8))

