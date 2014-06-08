# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatsetnickname.ui'
#
# Created: Tue Nov  8 18:44:43 2011
#      by: PyQt4 UI code generator snapshot-4.9-7e4361f52744
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NicknameDialog(object):
    def setupUi(self, NicknameDialog):
        NicknameDialog.setObjectName(_fromUtf8("NicknameDialog"))
        NicknameDialog.resize(396, 105)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1), QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NicknameDialog.sizePolicy().hasHeightForWidth())
        NicknameDialog.setSizePolicy(sizePolicy)
        NicknameDialog.setWindowTitle(QtGui.QApplication.translate("NicknameDialog", "Set nickname", None, QtGui.QApplication.UnicodeUTF8))
        self.vboxlayout = QtGui.QVBoxLayout(NicknameDialog)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.label = QtGui.QLabel(NicknameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1), QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(QtGui.QApplication.translate("NicknameDialog", "New nickname:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout1.addWidget(self.label)
        self.nickname = QtGui.QLineEdit(NicknameDialog)
        self.nickname.setObjectName(_fromUtf8("nickname"))
        self.vboxlayout1.addWidget(self.nickname)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(131, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(NicknameDialog)
        self.okButton.setText(QtGui.QApplication.translate("NicknameDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(NicknameDialog)
        self.cancelButton.setText(QtGui.QApplication.translate("NicknameDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(NicknameDialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), NicknameDialog.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), NicknameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NicknameDialog)

    def retranslateUi(self, NicknameDialog):
        pass

