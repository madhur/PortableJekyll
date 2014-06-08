# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Mon Nov 29 17:25:27 2010
#      by: PyQt4 UI code generator snapshot-4.8.2-241fbaf4620d
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(Window)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(Window)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://webkit.org/")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.elementLabel = QtGui.QLabel(Window)
        self.elementLabel.setObjectName(_fromUtf8("elementLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.elementLabel)
        self.elementLineEdit = QtGui.QLineEdit(Window)
        self.elementLineEdit.setObjectName(_fromUtf8("elementLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.elementLineEdit)
        self.horizontalLayout.addLayout(self.formLayout)
        self.highlightButton = QtGui.QPushButton(Window)
        self.highlightButton.setObjectName(_fromUtf8("highlightButton"))
        self.horizontalLayout.addWidget(self.highlightButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.elementLabel.setBuddy(self.elementLineEdit)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Web Element Selector", None, QtGui.QApplication.UnicodeUTF8))
        self.elementLabel.setText(QtGui.QApplication.translate("Window", "&Element:", None, QtGui.QApplication.UnicodeUTF8))
        self.elementLineEdit.setText(QtGui.QApplication.translate("Window", "li a", None, QtGui.QApplication.UnicodeUTF8))
        self.highlightButton.setText(QtGui.QApplication.translate("Window", "&Highlight", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
