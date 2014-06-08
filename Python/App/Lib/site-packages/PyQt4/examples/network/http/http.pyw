#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
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
#############################################################################


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

from PyQt4 import QtCore, QtGui, QtNetwork


class HttpWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(HttpWindow, self).__init__(parent)

        self.outFile = None
        self.httpGetId = 0
        self.httpRequestAborted = False

        self.urlLineEdit = QtGui.QLineEdit('https://')

        urlLabel = QtGui.QLabel("&URL:")
        urlLabel.setBuddy(self.urlLineEdit)
        self.statusLabel = QtGui.QLabel("Please enter the URL of a file you "
                "want to download.")

        self.downloadButton = QtGui.QPushButton("Download")
        self.downloadButton.setDefault(True)
        self.quitButton = QtGui.QPushButton("Quit")
        self.quitButton.setAutoDefault(False)

        buttonBox = QtGui.QDialogButtonBox()
        buttonBox.addButton(self.downloadButton,
                QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(self.quitButton, QtGui.QDialogButtonBox.RejectRole)

        self.progressDialog = QtGui.QProgressDialog(self)

        self.http = QtNetwork.QHttp(self)

        self.urlLineEdit.textChanged.connect(self.enableDownloadButton)
        self.http.requestFinished.connect(self.httpRequestFinished)
        self.http.dataReadProgress.connect(self.updateDataReadProgress)
        self.http.responseHeaderReceived.connect(self.readResponseHeader)
        self.http.authenticationRequired.connect(self.slotAuthenticationRequired)
        self.http.sslErrors.connect(self.sslErrors)
        self.progressDialog.canceled.connect(self.cancelDownload)
        self.downloadButton.clicked.connect(self.downloadFile)
        self.quitButton.clicked.connect(self.close)

        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(urlLabel)
        topLayout.addWidget(self.urlLineEdit)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(self.statusLabel)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("HTTP")
        self.urlLineEdit.setFocus()

    def downloadFile(self):
        url = QtCore.QUrl(self.urlLineEdit.text())
        fileInfo = QtCore.QFileInfo(url.path())
        fileName = fileInfo.fileName()

        if not fileName:
            fileName = 'index.html'

        if QtCore.QFile.exists(fileName):
            ret = QtGui.QMessageBox.question(self, "HTTP",
                    "There already exists a file called %s in the current "
                    "directory." % fileName,
                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
                    QtGui.QMessageBox.Cancel)

            if ret == QtGui.QMessageBox.Cancel:
                return

            QtCore.QFile.remove(fileName)

        self.outFile = QtCore.QFile(fileName)
        if not self.outFile.open(QtCore.QIODevice.WriteOnly):
            QtGui.QMessageBox.information(self, "HTTP",
                    "Unable to save the file %s: %s." % (fileName, self.outFile.errorString()))
            self.outFile = None
            return

        if url.scheme().lower() == 'https':
            mode = QtNetwork.QHttp.ConnectionModeHttps
        else:
            mode = QtNetwork.QHttp.ConnectionModeHttp

        port = url.port()

        if port == -1:
            port = 0

        self.http.setHost(url.host(), mode, port)

        if url.userName():
            self.http.setUser(url.userName(), url.password())

        self.httpRequestAborted = False

        path = QtCore.QUrl.toPercentEncoding(url.path(), "!$&'()*+,;=:@/")
        if path:
            try:
                # Python v3.
                path = str(path, encoding='utf-8')
            except TypeError:
                # Python v2.
                path = str(path)
        else:
            path = '/'

        self.httpGetId = self.http.get(path, self.outFile)

        self.progressDialog.setWindowTitle("HTTP")
        self.progressDialog.setLabelText("Downloading %s." % fileName)
        self.downloadButton.setEnabled(False)

    def cancelDownload(self):
        self.statusLabel.setText("Download canceled.")
        self.httpRequestAborted = True
        self.http.abort()
        self.downloadButton.setEnabled(True)

    def httpRequestFinished(self, requestId, error):
        if requestId != self.httpGetId:
            return

        if self.httpRequestAborted:
            if self.outFile is not None:
                self.outFile.close()
                self.outFile.remove()
                self.outFile = None

            self.progressDialog.hide()
            return

        self.progressDialog.hide()
        self.outFile.close()

        if error:
            self.outFile.remove()
            QtGui.QMessageBox.information(self, "HTTP",
                    "Download failed: %s." % self.http.errorString())
        else:
            fileName = QtCore.QFileInfo(QtCore.QUrl(self.urlLineEdit.text()).path()).fileName()
            self.statusLabel.setText("Downloaded %s to current directory." % fileName)

        self.downloadButton.setEnabled(True)
        self.outFile = None

    def readResponseHeader(self, responseHeader):
        # Check for genuine error conditions.
        if responseHeader.statusCode() not in (200, 300, 301, 302, 303, 307):
            QtGui.QMessageBox.information(self, "HTTP",
                    "Download failed: %s." % responseHeader.reasonPhrase())
            self.httpRequestAborted = True
            self.progressDialog.hide()
            self.http.abort()

    def updateDataReadProgress(self, bytesRead, totalBytes):
        if self.httpRequestAborted:
            return

        self.progressDialog.setMaximum(totalBytes)
        self.progressDialog.setValue(bytesRead)

    def enableDownloadButton(self):
        self.downloadButton.setEnabled(bool(self.urlLineEdit.text()))

    def slotAuthenticationRequired(self, hostName, _, authenticator):
        import os
        from PyQt4 import uic

        ui = os.path.join(os.path.dirname(__file__), 'authenticationdialog.ui')
        dlg = uic.loadUi(ui)
        dlg.adjustSize()
        dlg.siteDescription.setText("%s at %s" % (authenticator.realm(), hostName))

        if dlg.exec_() == QtGui.QDialog.Accepted:
            authenticator.setUser(dlg.userEdit.text())
            authenticator.setPassword(dlg.passwordEdit.text())

    def sslErrors(self, errors):
        errorString = ", ".join([str(error.errorString()) for error in errors])

        ret = QtGui.QMessageBox.warning(self, "HTTP Example",
                "One or more SSL errors has occurred: %s" % errorString,
                QtGui.QMessageBox.Ignore | QtGui.QMessageBox.Abort)

        if ret == QtGui.QMessageBox.Ignore:
            self.http.ignoreSslErrors()


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    httpWin = HttpWindow()
    httpWin.show()
    sys.exit(httpWin.exec_())
