#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2011 Riverbank Computing Limited.
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

from PyQt4 import QtCore, QtGui, QtDBus

from ui_chatmainwindow import Ui_ChatMainWindow
from ui_chatsetnickname import Ui_NicknameDialog


class ChatAdaptor(QtDBus.QDBusAbstractAdaptor):

    QtCore.Q_CLASSINFO("D-Bus Interface", 'com.trolltech.chat')

    QtCore.Q_CLASSINFO("D-Bus Introspection", ''
        '  <interface name="com.trolltech.chat">\n'
        '    <signal name="message">\n'
        '      <arg direction="out" type="s" name="nickname"/>\n'
        '      <arg direction="out" type="s" name="text"/>\n'
        '    </signal>\n'
        '    <signal name="action">\n'
        '      <arg direction="out" type="s" name="nickname"/>\n'
        '      <arg direction="out" type="s" name="text"/>\n'
        '    </signal>\n'
        '  </interface>\n'
        '')

    action = QtCore.pyqtSignal(str, str)

    message = QtCore.pyqtSignal(str, str)

    def __init__(self, parent):
        super(ChatAdaptor, self).__init__(parent)

        self.setAutoRelaySignals(True)


class ChatInterface(QtDBus.QDBusAbstractInterface):

    action = QtCore.pyqtSignal(str, str)

    message = QtCore.pyqtSignal(str, str)

    def __init__(self, service, path, connection, parent=None):
        super(ChatInterface, self).__init__(service, path,
                'com.trolltech.chat', connection, parent)


class ChatMainWindow(QtGui.QMainWindow, Ui_ChatMainWindow):

    action = QtCore.pyqtSignal(str, str)

    message = QtCore.pyqtSignal(str, str)

    def __init__(self):
        super(ChatMainWindow, self).__init__()

        self.m_nickname = "nickname"
        self.m_messages = []

        self.setupUi(self)
        self.sendButton.setEnabled(False)

        self.messageLineEdit.textChanged.connect(self.textChangedSlot)
        self.sendButton.clicked.connect(self.sendClickedSlot)
        self.actionChangeNickname.triggered.connect(self.changeNickname)
        self.actionAboutQt.triggered.connect(self.aboutQt)
        QtGui.qApp.lastWindowClosed.connect(self.exiting)

        # Add our D-Bus interface and connect to D-Bus.
        ChatAdaptor(self)
        QtDBus.QDBusConnection.sessionBus().registerObject('/', self)

        iface = ChatInterface('', '', QtDBus.QDBusConnection.sessionBus(),
                self)
        QtDBus.QDBusConnection.sessionBus().connect('', '',
                'com.trolltech.chat', 'message', self.messageSlot)
        iface.action.connect(self.actionSlot)

        dialog = NicknameDialog()
        dialog.cancelButton.setVisible(False)
        dialog.exec_()
        self.m_nickname = dialog.nickname.text().strip()
        self.action.emit(self.m_nickname, "joins the chat")

    def rebuildHistory(self):
        history = '\n'.join(self.m_messages)
        self.chatHistory.setPlainText(history)

    @QtCore.pyqtSlot(str, str)
    def messageSlot(self, nickname, text):
        self.m_messages.append("<%s> %s" % (nickname, text))

        if len(self.m_messages) > 100:
            self.m_messages.pop(0)

        self.rebuildHistory()

    @QtCore.pyqtSlot(str, str)
    def actionSlot(self, nickname, text):
        self.m_messages.append("* %s %s" % (nickname, text))

        if len(self.m_messages) > 100:
            self.m_messages.pop(0)

        self.rebuildHistory()

    @QtCore.pyqtSlot(str)
    def textChangedSlot(self, newText):
        self.sendButton.setEnabled(newText != '')

    @QtCore.pyqtSlot()
    def sendClickedSlot(self):
        msg = QtDBus.QDBusMessage.createSignal('/', 'com.trolltech.chat',
                'message')
        msg << self.m_nickname << self.messageLineEdit.text()
        QtDBus.QDBusConnection.sessionBus().send(msg)
        self.messageLineEdit.setText('')

    @QtCore.pyqtSlot()
    def changeNickname(self):
        dialog = NicknameDialog(self)

        if dialog.exec_() == QtGui.QDialog.Accepted:
            old = self.m_nickname
            self.m_nickname = dialog.nickname.text().strip()
            self.action.emit(old, "is now known as %s" % self.m_nickname)

    @QtCore.pyqtSlot()
    def aboutQt(self):
        QtGui.QMessageBox.aboutQt(self)

    @QtCore.pyqtSlot()
    def exiting(self):
        self.action.emit(self.m_nickname, "leaves the chat")


class NicknameDialog(QtGui.QDialog, Ui_NicknameDialog):

    def __init__(self, parent=None):
        super(NicknameDialog, self).__init__(parent)

        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    if not QtDBus.QDBusConnection.sessionBus().isConnected():
        sys.stderr.write("Cannot connect to the D-Bus session bus.\n"
                "Please check your system settings and try again.\n")
        sys.exit(1)

    chat = ChatMainWindow()
    chat.show()

    sys.exit(app.exec_())
