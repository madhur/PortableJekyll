# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatmainwindow.ui'
#
# Created: Tue Nov  8 18:43:59 2011
#      by: PyQt4 UI code generator snapshot-4.9-7e4361f52744
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChatMainWindow(object):
    def setupUi(self, ChatMainWindow):
        ChatMainWindow.setObjectName(_fromUtf8("ChatMainWindow"))
        ChatMainWindow.resize(800, 600)
        ChatMainWindow.setWindowTitle(QtGui.QApplication.translate("ChatMainWindow", "QtDBus Chat", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(ChatMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.hboxlayout = QtGui.QHBoxLayout(self.centralwidget)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.chatHistory = QtGui.QTextBrowser(self.centralwidget)
        self.chatHistory.setAcceptDrops(False)
        self.chatHistory.setToolTip(QtGui.QApplication.translate("ChatMainWindow", "Messages sent and received from other users", None, QtGui.QApplication.UnicodeUTF8))
        self.chatHistory.setAcceptRichText(True)
        self.chatHistory.setObjectName(_fromUtf8("chatHistory"))
        self.vboxlayout.addWidget(self.chatHistory)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(QtGui.QApplication.translate("ChatMainWindow", "Message:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout1.addWidget(self.label)
        self.messageLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.messageLineEdit.setObjectName(_fromUtf8("messageLineEdit"))
        self.hboxlayout1.addWidget(self.messageLineEdit)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1), QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setToolTip(QtGui.QApplication.translate("ChatMainWindow", "Sends a message to other people", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setWhatsThis(_fromUtf8(""))
        self.sendButton.setText(QtGui.QApplication.translate("ChatMainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.hboxlayout1.addWidget(self.sendButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)
        ChatMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ChatMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setTitle(QtGui.QApplication.translate("ChatMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setObjectName(_fromUtf8("menuQuit"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("ChatMainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        ChatMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ChatMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ChatMainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(ChatMainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("ChatMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("ChatMainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAboutQt = QtGui.QAction(ChatMainWindow)
        self.actionAboutQt.setText(QtGui.QApplication.translate("ChatMainWindow", "About Qt...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionChangeNickname = QtGui.QAction(ChatMainWindow)
        self.actionChangeNickname.setText(QtGui.QApplication.translate("ChatMainWindow", "Change nickname...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChangeNickname.setShortcut(QtGui.QApplication.translate("ChatMainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChangeNickname.setObjectName(_fromUtf8("actionChangeNickname"))
        self.menuQuit.addAction(self.actionAboutQt)
        self.menuFile.addAction(self.actionChangeNickname)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.label.setBuddy(self.messageLineEdit)

        self.retranslateUi(ChatMainWindow)
        QtCore.QObject.connect(self.messageLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.sendButton.animateClick)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), ChatMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ChatMainWindow)
        ChatMainWindow.setTabOrder(self.chatHistory, self.messageLineEdit)
        ChatMainWindow.setTabOrder(self.messageLineEdit, self.sendButton)

    def retranslateUi(self, ChatMainWindow):
        pass

