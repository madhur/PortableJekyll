# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'previewer.ui'
#
# Created: Mon Nov 29 17:09:55 2010
#      by: PyQt4 UI code generator snapshot-4.8.2-241fbaf4620d
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(911, 688)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.editorBox = QtGui.QGroupBox(self.splitter)
        self.editorBox.setObjectName(_fromUtf8("editorBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.editorBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.editorBox)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clearButton = QtGui.QPushButton(self.editorBox)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.previewButton = QtGui.QPushButton(self.editorBox)
        self.previewButton.setObjectName(_fromUtf8("previewButton"))
        self.horizontalLayout.addWidget(self.previewButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.previewerBox = QtGui.QGroupBox(self.splitter)
        self.previewerBox.setObjectName(_fromUtf8("previewerBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.previewerBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.webView = QtWebKit.QWebView(self.previewerBox)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout_3.addWidget(self.webView)
        self.horizontalLayout_4.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.editorBox.setTitle(QtGui.QApplication.translate("Form", "HTML Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.previewButton.setText(QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.previewerBox.setTitle(QtGui.QApplication.translate("Form", "HTML Preview", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
