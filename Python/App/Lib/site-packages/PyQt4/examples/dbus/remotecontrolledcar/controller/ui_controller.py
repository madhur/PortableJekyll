# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller.ui'
#
# Created: Fri Nov 18 14:20:56 2011
#      by: PyQt4 UI code generator snapshot-4.9-4af996c32961
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Controller(object):
    def setupUi(self, Controller):
        Controller.setObjectName(_fromUtf8("Controller"))
        Controller.resize(255, 111)
        Controller.setWindowTitle(QtGui.QApplication.translate("Controller", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.gridlayout = QtGui.QGridLayout(Controller)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(Controller)
        self.label.setText(QtGui.QApplication.translate("Controller", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 1, 1, 1)
        self.decelerate = QtGui.QPushButton(Controller)
        self.decelerate.setText(QtGui.QApplication.translate("Controller", "Decelerate", None, QtGui.QApplication.UnicodeUTF8))
        self.decelerate.setObjectName(_fromUtf8("decelerate"))
        self.gridlayout.addWidget(self.decelerate, 2, 1, 1, 1)
        self.accelerate = QtGui.QPushButton(Controller)
        self.accelerate.setText(QtGui.QApplication.translate("Controller", "Accelerate", None, QtGui.QApplication.UnicodeUTF8))
        self.accelerate.setObjectName(_fromUtf8("accelerate"))
        self.gridlayout.addWidget(self.accelerate, 0, 1, 1, 1)
        self.right = QtGui.QPushButton(Controller)
        self.right.setText(QtGui.QApplication.translate("Controller", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.right.setObjectName(_fromUtf8("right"))
        self.gridlayout.addWidget(self.right, 1, 2, 1, 1)
        self.left = QtGui.QPushButton(Controller)
        self.left.setText(QtGui.QApplication.translate("Controller", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.left.setObjectName(_fromUtf8("left"))
        self.gridlayout.addWidget(self.left, 1, 0, 1, 1)

        self.retranslateUi(Controller)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    def retranslateUi(self, Controller):
        pass

