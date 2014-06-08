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


from PyQt4 import QtCore, QtGui


class CircleWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CircleWidget, self).__init__(parent)

        self.floatBased = False
        self.antialiased = False
        self.frameNo = 0

        self.setBackgroundRole(QtGui.QPalette.Base)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

    def setFloatBased(self, floatBased):
        self.floatBased = floatBased
        self.update()

    def setAntialiased(self, antialiased):
        self.antialiased = antialiased
        self.update()

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(180, 180)

    def nextAnimationFrame(self):
        self.frameNo += 1
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, self.antialiased)
        painter.translate(self.width() / 2, self.height() / 2)

        for diameter in range(0, 256, 9):
            delta = abs((self.frameNo % 128) - diameter / 2)
            alpha = 255 - (delta * delta) / 4 - diameter
            if alpha > 0:
                painter.setPen(QtGui.QPen(QtGui.QColor(0, diameter / 2, 127,
                        alpha), 3))

                if self.floatBased:
                    painter.drawEllipse(QtCore.QRectF(-diameter / 2.0,
                            -diameter / 2.0, diameter, diameter))
                else:
                    painter.drawEllipse(QtCore.QRect(-diameter / 2,
                            -diameter / 2, diameter, diameter))


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        aliasedLabel = self.createLabel("Aliased")
        antialiasedLabel = self.createLabel("Antialiased")
        intLabel = self.createLabel("Int")
        floatLabel = self.createLabel("Float")

        layout = QtGui.QGridLayout()
        layout.addWidget(aliasedLabel, 0, 1)
        layout.addWidget(antialiasedLabel, 0, 2)
        layout.addWidget(intLabel, 1, 0)
        layout.addWidget(floatLabel, 2, 0)

        timer = QtCore.QTimer(self)

        self.circleWidgets = []
        for i in range(2):
            self.circleWidgets.append([None]*2)
            for j in range(2):
                self.circleWidgets[i][j] = CircleWidget()
                self.circleWidgets[i][j].setAntialiased(j != 0)
                self.circleWidgets[i][j].setFloatBased(i != 0)

                timer.timeout.connect(self.circleWidgets[i][j].nextAnimationFrame)

                layout.addWidget(self.circleWidgets[i][j], i + 1, j + 1)

        timer.start(100)
        self.setLayout(layout)

        self.setWindowTitle("Concentric Circles")

    def createLabel(self, text):
        label = QtGui.QLabel(text)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setMargin(2)
        label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Sunken)
        return label


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
