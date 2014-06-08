#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
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
###########################################################################


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

from PyQt4 import QtCore, QtGui, QtNetwork, QtWebKit

from ui_form import Ui_Form


class GoogleChat(QtGui.QWidget):

    URL = 'http://talkgadget.google.com/talkgadget/m'

    def __init__(self):
        super(GoogleChat, self).__init__()

        self.userName = ""
        self.password = ""

        self.form = Ui_Form()
        self.form.setupUi(self)

        self.setFixedSize(320, 480)

        self.form.userNameEdit.setFocus()
        self.form.userNameEdit.textChanged.connect(self.adjustLoginButton)
        self.form.userNameEdit.returnPressed.connect(self.inputPassword)

        self.form.passwordEdit.textChanged.connect(self.adjustLoginButton)
        self.form.passwordEdit.returnPressed.connect(self.doLogin)

        self.form.loginButton.setEnabled(False)
        self.form.loginButton.clicked.connect(self.doLogin)

        self.form.webView.loadFinished.connect(self.initialPage)
        self.form.webView.loadProgress.connect(self.form.progressBar.setValue)
        self.form.webView.setUrl(QtCore.QUrl(GoogleChat.URL))
        self.form.webView.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        self.showStatus("Wait...")

    def showStatus(self, msg):
        self.form.statusLabel.setText(msg)
        self.form.stackedWidget.setCurrentIndex(0)

    def showError(self, msg):
        self.form.progressBar.hide()
        self.showStatus("Error: %s" % msg)

    def document(self):
        return self.form.webView.page().mainFrame().documentElement()

    def adjustLoginButton(self):
        self.userName = self.form.userNameEdit.text()
        self.password = self.form.passwordEdit.text()
        self.form.loginButton.setEnabled(bool(self.userName and self.password))
 
    def inputPassword(self):
        if self.form.userNameEdit.text():
            self.form.passwordEdit.setFocus()

    def doLogin(self):
        self.userName = self.form.userNameEdit.text()
        self.password = self.form.passwordEdit.text()
        if not (self.userName and self.password):
            return

        self.form.progressBar.setValue(0)
        self.form.progressBar.show()
        self.form.webView.loadFinished.connect(self.loginPage)
        self.form.webView.loadProgress.connect(self.form.progressBar.setValue)
        self.showStatus("Logging in...")
        userEmail = self.userName + '@gmail.com'
        self.document().findFirst('#Email').setAttribute('value', userEmail)
        self.document().findFirst('#Passwd').setAttribute('value', self.password)
        self.document().findFirst('#gaia_loginform').evaluateJavaScript('this.submit();')

    @QtCore.pyqtSlot(bool)
    def initialPage(self, ok):
        if not QtNetwork.QSslSocket.supportsSsl():
            self.showError("This example requires SSL support.")
            return

        if ok:
            email = self.document().findFirst('#Email')
            passwd = self.document().findFirst('#Passwd')
            loginForm = self.document().findFirst('#gaia_loginform')
            if not email.isNull() and not passwd.isNull() and not loginForm.isNull():
                self.form.stackedWidget.setCurrentIndex(1)
                self.form.userNameEdit.setFocus()
                self.form.webView.loadFinished.disconnect()
                self.form.webView.loadProgress.disconnect()
                return

        self.showError("Service unavailable.")

    def hideElements(self):
        self.document().findFirst('.footer-footer').removeFromDocument()
        self.document().findFirst('.title-bar-bg .title-bar').removeFromDocument()
        QtCore.QTimer.singleShot(2000, self.hideElements)

    def loginPage(self, ok):
        location = self.form.webView.url().toString()
        if not ok:
            if 'CheckCookie' in location:
                return

            self.showError("Service unavailable")
        else:
            # Check for any error message.
            e = self.document().findFirst('.errormsg')
            if e.isNull():
                self.form.stackedWidget.setCurrentIndex(2)
                QtCore.QTimer.singleShot(500, self.hideElements)
                return

            err = "Unknown login failure."
            errorMessage = e.toPlainText()

            if errorMessage:
                err = errorMessage
                err = err.simplified()

            self.showError(err)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)

    chat = GoogleChat()
    chat.show()

    sys.exit(app.exec_())
