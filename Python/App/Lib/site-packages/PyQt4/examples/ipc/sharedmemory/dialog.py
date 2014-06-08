# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Thu Nov  4 13:41:31 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(451, 322)
        self.gridlayout = QtGui.QGridLayout(Dialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.loadFromFileButton = QtGui.QPushButton(Dialog)
        self.loadFromFileButton.setObjectName(_fromUtf8("loadFromFileButton"))
        self.gridlayout.addWidget(self.loadFromFileButton, 0, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.loadFromSharedMemoryButton = QtGui.QPushButton(Dialog)
        self.loadFromSharedMemoryButton.setObjectName(_fromUtf8("loadFromSharedMemoryButton"))
        self.gridlayout.addWidget(self.loadFromSharedMemoryButton, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.loadFromFileButton.setText(QtGui.QApplication.translate("Dialog", "Load Image From File...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Launch two of these dialogs.  In the first, press the top button and load an image from a file.  In the second, press the bottom button and display the loaded image from shared memory.", None, QtGui.QApplication.UnicodeUTF8))
        self.loadFromSharedMemoryButton.setText(QtGui.QApplication.translate("Dialog", "Display Image From Shared Memory", None, QtGui.QApplication.UnicodeUTF8))

