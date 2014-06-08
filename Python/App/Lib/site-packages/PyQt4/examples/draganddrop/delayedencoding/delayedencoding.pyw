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
#############################################################################


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

from PyQt4 import QtCore, QtGui, QtSvg

try:
    import delayedencoding_rc3
except ImportError:
    import delayedencoding_rc2


class MimeData(QtCore.QMimeData):

    dataRequested = QtCore.pyqtSignal(str)

    def formats(self):
        formats = QtCore.QMimeData.formats(self)
        formats.append('image/png')

        return formats

    def retrieveData(self, mimeType, qvtype):
        self.dataRequested.emit(mimeType)

        return QtCore.QMimeData.retrieveData(self, mimeType, qvtype)


class SourceWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SourceWidget, self).__init__(parent)

        self.mimeData = None

        imageFile = QtCore.QFile(':/images/example.svg')
        imageFile.open(QtCore.QIODevice.ReadOnly)
        self.imageData = imageFile.readAll()
        imageFile.close()

        imageArea = QtGui.QScrollArea()
        self.imageLabel = QtSvg.QSvgWidget()
        self.imageLabel.renderer().load(self.imageData)
        imageArea.setWidget(self.imageLabel)

        instructTopLabel = QtGui.QLabel("This is an SVG drawing:")
        instructBottomLabel = QtGui.QLabel("Drag the icon to copy the drawing as a PNG file:")
        dragIcon = QtGui.QPushButton("Export")
        dragIcon.setIcon(QtGui.QIcon(':/images/drag.png'))
        dragIcon.pressed.connect(self.startDrag)

        layout = QtGui.QGridLayout()
        layout.addWidget(instructTopLabel, 0, 0, 1, 2)
        layout.addWidget(imageArea, 1, 0, 2, 2)
        layout.addWidget(instructBottomLabel, 3, 0)
        layout.addWidget(dragIcon, 3, 1)
        self.setLayout(layout)
        self.setWindowTitle("Delayed Encoding")

    def createData(self, mimeType):
        if mimeType != 'image/png':
            return

        image = QtGui.QImage(self.imageLabel.size(), QtGui.QImage.Format_RGB32)
        painter = QtGui.QPainter()
        painter.begin(image)
        self.imageLabel.renderer().render(painter)
        painter.end()

        data = QtCore.QByteArray()
        buffer = QtCore.QBuffer(data)
        buffer.open(QtCore.QIODevice.WriteOnly)
        image.save(buffer, 'PNG')
        buffer.close()
        self.mimeData.setData('image/png', data)

    def startDrag(self):
        self.mimeData = MimeData()
        self.mimeData.dataRequested.connect(self.createData, QtCore.Qt.DirectConnection)

        drag = QtGui.QDrag(self)
        drag.setMimeData(self.mimeData)
        drag.setPixmap(QtGui.QPixmap(':/images/drag.png'))
        drag.exec_(QtCore.Qt.CopyAction)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = SourceWidget()
    window.show()
    sys.exit(app.exec_())
