# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatorform.ui'
#
# Created: Mon Jan 23 13:21:45 2006
#      by: PyQt4 UI code generator vsnapshot-20060120
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_CalculatorForm(object):
    def setupUi(self, CalculatorForm):
        CalculatorForm.setObjectName("CalculatorForm")
        CalculatorForm.resize(QtCore.QSize(QtCore.QRect(0,0,400,300).size()).expandedTo(CalculatorForm.minimumSizeHint()))
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalculatorForm.sizePolicy().hasHeightForWidth())
        CalculatorForm.setSizePolicy(sizePolicy)
        
        self.gridlayout = QtGui.QGridLayout(CalculatorForm)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem,0,6,1,1)
        
        self.label_3_2 = QtGui.QLabel(CalculatorForm)
        self.label_3_2.setGeometry(QtCore.QRect(169,9,20,52))
        self.label_3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3_2.setObjectName("label_3_2")
        self.gridlayout.addWidget(self.label_3_2,0,4,1,1)
        
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(1)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        
        self.label_2_2_2 = QtGui.QLabel(CalculatorForm)
        self.label_2_2_2.setGeometry(QtCore.QRect(1,1,36,17))
        self.label_2_2_2.setObjectName("label_2_2_2")
        self.vboxlayout.addWidget(self.label_2_2_2)
        
        self.outputWidget = QtGui.QLabel(CalculatorForm)
        self.outputWidget.setGeometry(QtCore.QRect(1,24,36,27))
        self.outputWidget.setFrameShape(QtGui.QFrame.Box)
        self.outputWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.outputWidget.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignBottom|QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignHorizontal_Mask|QtCore.Qt.AlignJustify|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignVertical_Mask)
        self.outputWidget.setObjectName("outputWidget")
        self.vboxlayout.addWidget(self.outputWidget)
        self.gridlayout.addLayout(self.vboxlayout,0,5,1,1)
        
        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1,1,2,1,1)
        
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(1)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        
        self.label_2 = QtGui.QLabel(CalculatorForm)
        self.label_2.setGeometry(QtCore.QRect(1,1,46,19))
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)
        
        self.inputSpinBox2 = QtGui.QSpinBox(CalculatorForm)
        self.inputSpinBox2.setGeometry(QtCore.QRect(1,26,46,25))
        self.inputSpinBox2.setObjectName("inputSpinBox2")
        self.vboxlayout1.addWidget(self.inputSpinBox2)
        self.gridlayout.addLayout(self.vboxlayout1,0,3,1,1)
        
        self.label_3 = QtGui.QLabel(CalculatorForm)
        self.label_3.setGeometry(QtCore.QRect(63,9,20,52))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,0,1,1,1)
        
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(1)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        
        self.label = QtGui.QLabel(CalculatorForm)
        self.label.setGeometry(QtCore.QRect(1,1,46,19))
        self.label.setObjectName("label")
        self.vboxlayout2.addWidget(self.label)
        
        self.inputSpinBox1 = QtGui.QSpinBox(CalculatorForm)
        self.inputSpinBox1.setGeometry(QtCore.QRect(1,26,46,25))
        self.inputSpinBox1.setObjectName("inputSpinBox1")
        self.vboxlayout2.addWidget(self.inputSpinBox1)
        self.gridlayout.addLayout(self.vboxlayout2,0,0,1,1)
        
        self.retranslateUi(CalculatorForm)
        QtCore.QMetaObject.connectSlotsByName(CalculatorForm)
    
    def tr(self, string):
        return QtGui.QApplication.translate("CalculatorForm", string, None, QtGui.QApplication.UnicodeUTF8)
    
    def retranslateUi(self, CalculatorForm):
        CalculatorForm.setObjectName(self.tr("CalculatorForm"))
        CalculatorForm.setWindowTitle(self.tr("Calculator Form"))
        self.label_3_2.setObjectName(self.tr("label_3_2"))
        self.label_3_2.setText(self.tr("="))
        self.label_2_2_2.setObjectName(self.tr("label_2_2_2"))
        self.label_2_2_2.setText(self.tr("Output"))
        self.outputWidget.setObjectName(self.tr("outputWidget"))
        self.outputWidget.setText(self.tr("0"))
        self.label_2.setObjectName(self.tr("label_2"))
        self.label_2.setText(self.tr("Input 2"))
        self.inputSpinBox2.setObjectName(self.tr("inputSpinBox2"))
        self.label_3.setObjectName(self.tr("label_3"))
        self.label_3.setText(self.tr("+"))
        self.label.setObjectName(self.tr("label"))
        self.label.setText(self.tr("Input 1"))
        self.inputSpinBox1.setObjectName(self.tr("inputSpinBox1"))
