# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formextractor.ui'
#
# Created: Sun Nov 28 14:37:13 2010
#      by: PyQt4 UI code generator snapshot-4.8.2-a935ffc263c2
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
        Form.resize(680, 218)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.webFormGroupBox = QtGui.QGroupBox(Form)
        self.webFormGroupBox.setObjectName(_fromUtf8("webFormGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.webFormGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(self.webFormGroupBox)
        self.webView.setMinimumSize(QtCore.QSize(200, 150))
        self.webView.setMaximumSize(QtCore.QSize(400, 16777215))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.webFormGroupBox)
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dataGroupBox = QtGui.QGroupBox(Form)
        self.dataGroupBox.setObjectName(_fromUtf8("dataGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dataGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.firstNameLabel = QtGui.QLabel(self.dataGroupBox)
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameEdit = QtGui.QLineEdit(self.dataGroupBox)
        self.firstNameEdit.setReadOnly(True)
        self.firstNameEdit.setObjectName(_fromUtf8("firstNameEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstNameEdit)
        self.lastNameLabel = QtGui.QLabel(self.dataGroupBox)
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameEdit = QtGui.QLineEdit(self.dataGroupBox)
        self.lastNameEdit.setReadOnly(True)
        self.lastNameEdit.setObjectName(_fromUtf8("lastNameEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lastNameEdit)
        self.genderLabel = QtGui.QLabel(self.dataGroupBox)
        self.genderLabel.setObjectName(_fromUtf8("genderLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.genderLabel)
        self.genderEdit = QtGui.QLineEdit(self.dataGroupBox)
        self.genderEdit.setReadOnly(True)
        self.genderEdit.setObjectName(_fromUtf8("genderEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.genderEdit)
        self.updatesLabel = QtGui.QLabel(self.dataGroupBox)
        self.updatesLabel.setObjectName(_fromUtf8("updatesLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.updatesLabel)
        self.updatesEdit = QtGui.QLineEdit(self.dataGroupBox)
        self.updatesEdit.setReadOnly(True)
        self.updatesEdit.setObjectName(_fromUtf8("updatesEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.updatesEdit)
        self.verticalLayout_3.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.dataGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.webFormGroupBox.setTitle(QtGui.QApplication.translate("Form", "Web Form", None, QtGui.QApplication.UnicodeUTF8))
        self.dataGroupBox.setTitle(QtGui.QApplication.translate("Form", "Extracted Data", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setText(QtGui.QApplication.translate("Form", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setText(QtGui.QApplication.translate("Form", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.genderLabel.setText(QtGui.QApplication.translate("Form", "Gender", None, QtGui.QApplication.UnicodeUTF8))
        self.updatesLabel.setText(QtGui.QApplication.translate("Form", "Receive Updates", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
