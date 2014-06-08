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

from PyQt4 import QtCore, QtGui, QtWebKit

from ui_previewer import Ui_Form


class Previewer(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Previewer, self).__init__(parent)

        self.setupUi(self)
        self.baseUrl = QtCore.QUrl()
 
    def setBaseUrl(self, url):
        self.baseUrl = url

    def on_previewButton_clicked(self):
        # Update the contents in the web viewer.
        text = self.plainTextEdit.toPlainText()
        self.webView.setHtml(text, self.baseUrl)


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.createActions()
        self.createMenus()
        self.centralWidget = Previewer(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.webView.loadFinished.connect(self.updateTextEdit)
        self.setStartupText()

    def createActions(self):
        self.openAct = QtGui.QAction("&Open...", self,
                shortcut=QtGui.QKeySequence.Open,
                statusTip="Open an existing HTML file", triggered=self.open)

        self.openUrlAct = QtGui.QAction("&Open URL...", self,
                shortcut="Ctrl+U", statusTip="Open a URL",
                triggered=self.openUrl)

        self.saveAct = QtGui.QAction("&Save", self,
                shortcut=QtGui.QKeySequence.Save,
                statusTip="Save the HTML file to disk", triggered=self.save)

        self.exitAct = QtGui.QAction("E&xit", self,
                shortcut=QtGui.QKeySequence.Quit,
                statusTip="Exit the application", triggered=self.close)

        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.openUrlAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)
        self.menuBar().addSeparator()
        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def about(self):
        QtGui.QMessageBox.about(self, "About Previewer",
                "The <b>Previewer</b> example demonstrates how to view HTML "
                "documents using a QtWebKit.QWebView.")

    def open(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self)
        if fileName:
            fd = QtCore.QFile(fileName)
            if not fd.open(QtCore.QIODevice.ReadOnly):
                QtGui.QMessageBox.information(self, "Unable to open file",
                        fd.errorString())
                return

            output = QtCore.QTextStream(fd).readAll()

            # Display contents.
            self.centralWidget.plainTextEdit.setPlainText(output)
            self.centralWidget.setBaseUrl(QtCore.QUrl.fromLocalFile(fileName))

    def openUrl(self):
        url, ok = QtGui.QInputDialog.getText(self, "Enter a URL", "URL:",
                QtGui.QLineEdit.Normal, "http://")

        if ok and url:
            url = QtCore.QUrl(url)
            self.centralWidget.webView.setUrl(url)

    def save(self):
        content = self.centralWidget.plainTextEdit.toPlainText()
        fileName = QtGui.QFileDialog.getSaveFileName(self)
        if fileName:
            fd = QtCore.QFile(fileName)
            if not fd.open(QtCore.QIODevice.WriteOnly):
                QtGui.QMessageBox.information(self, "Unable to open file",
                        fd.errorString())
                return

            QtCore.QTextStream(fd) << content
 
    def updateTextEdit(self):
        mainFrame = self.centralWidget.webView.page().mainFrame()
        frameText = mainFrame.toHtml()
        self.centralWidget.plainTextEdit.setPlainText(frameText)

    def setStartupText(self):
        self.centralWidget.webView.setHtml("""
<html><body>
 <h1>HTML Previewer</h1>
  <p>This example shows you how to use QtWebKit.QWebView to
   preview HTML data written in a QtGui.QPlainTextEdit.
  </p>
</body></html>""")


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
