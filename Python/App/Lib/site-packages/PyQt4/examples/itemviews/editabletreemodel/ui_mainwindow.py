# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar 20 14:23:30 2013
#      by: PyQt4 UI code generator snapshot-4.10.1-90522b46ebd0
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(573, 468)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.view = QtGui.QTreeView(self.centralwidget)
        self.view.setAlternatingRowColors(True)
        self.view.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.view.setAnimated(False)
        self.view.setAllColumnsShowFocus(True)
        self.view.setObjectName(_fromUtf8("view"))
        self.vboxlayout.addWidget(self.view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        self.actionsMenu = QtGui.QMenu(self.menubar)
        self.actionsMenu.setObjectName(_fromUtf8("actionsMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction = QtGui.QAction(MainWindow)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.insertRowAction = QtGui.QAction(MainWindow)
        self.insertRowAction.setObjectName(_fromUtf8("insertRowAction"))
        self.removeRowAction = QtGui.QAction(MainWindow)
        self.removeRowAction.setObjectName(_fromUtf8("removeRowAction"))
        self.insertColumnAction = QtGui.QAction(MainWindow)
        self.insertColumnAction.setObjectName(_fromUtf8("insertColumnAction"))
        self.removeColumnAction = QtGui.QAction(MainWindow)
        self.removeColumnAction.setObjectName(_fromUtf8("removeColumnAction"))
        self.insertChildAction = QtGui.QAction(MainWindow)
        self.insertChildAction.setObjectName(_fromUtf8("insertChildAction"))
        self.fileMenu.addAction(self.exitAction)
        self.actionsMenu.addAction(self.insertRowAction)
        self.actionsMenu.addAction(self.insertColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.addAction(self.removeRowAction)
        self.actionsMenu.addAction(self.removeColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.addAction(self.insertChildAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.actionsMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Editable Tree Model", None))
        self.fileMenu.setTitle(_translate("MainWindow", "&File", None))
        self.actionsMenu.setTitle(_translate("MainWindow", "&Actions", None))
        self.exitAction.setText(_translate("MainWindow", "E&xit", None))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.insertRowAction.setText(_translate("MainWindow", "Insert Row", None))
        self.insertRowAction.setShortcut(_translate("MainWindow", "Ctrl+I, R", None))
        self.removeRowAction.setText(_translate("MainWindow", "Remove Row", None))
        self.removeRowAction.setShortcut(_translate("MainWindow", "Ctrl+R, R", None))
        self.insertColumnAction.setText(_translate("MainWindow", "Insert Column", None))
        self.insertColumnAction.setShortcut(_translate("MainWindow", "Ctrl+I, C", None))
        self.removeColumnAction.setText(_translate("MainWindow", "Remove Column", None))
        self.removeColumnAction.setShortcut(_translate("MainWindow", "Ctrl+R, C", None))
        self.insertChildAction.setText(_translate("MainWindow", "Insert Child", None))
        self.insertChildAction.setShortcut(_translate("MainWindow", "Ctrl+N", None))

