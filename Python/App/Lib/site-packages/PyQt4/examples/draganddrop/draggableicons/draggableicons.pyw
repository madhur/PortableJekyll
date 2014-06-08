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

try:
    import draggableicons_rc3
except ImportError:
    import draggableicons_rc2


class DragWidget(QtGui.QFrame):
    def __init__(self, parent=None):
        super(DragWidget, self).__init__(parent)

        self.setMinimumSize(200, 200)
        self.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        self.setAcceptDrops(True)

        boatIcon = QtGui.QLabel(self)
        boatIcon.setPixmap(QtGui.QPixmap(':/images/boat.png'))
        boatIcon.move(20, 20)
        boatIcon.show()
        boatIcon.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        carIcon = QtGui.QLabel(self)
        carIcon.setPixmap(QtGui.QPixmap(':/images/car.png'))
        carIcon.move(120, 20)
        carIcon.show()
        carIcon.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        houseIcon = QtGui.QLabel(self)
        houseIcon.setPixmap(QtGui.QPixmap(':/images/house.png'))
        houseIcon.move(20, 120)
        houseIcon.show()
        houseIcon.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-dnditemdata'):
            if event.source() == self:
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    dragMoveEvent = dragEnterEvent

    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-dnditemdata'):
            itemData = event.mimeData().data('application/x-dnditemdata')
            dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.ReadOnly)

            pixmap = QtGui.QPixmap()
            offset = QtCore.QPoint()
            dataStream >> pixmap >> offset

            newIcon = QtGui.QLabel(self)
            newIcon.setPixmap(pixmap)
            newIcon.move(event.pos() - offset)
            newIcon.show()
            newIcon.setAttribute(QtCore.Qt.WA_DeleteOnClose)

            if event.source() == self:
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        child = self.childAt(event.pos())
        if not child:
            return

        pixmap = QtGui.QPixmap(child.pixmap())

        itemData = QtCore.QByteArray()
        dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
        dataStream << pixmap << QtCore.QPoint(event.pos() - child.pos())

        mimeData = QtCore.QMimeData()
        mimeData.setData('application/x-dnditemdata', itemData)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - child.pos())

        tempPixmap = QtGui.QPixmap(pixmap)
        painter = QtGui.QPainter()
        painter.begin(tempPixmap)
        painter.fillRect(pixmap.rect(), QtGui.QColor(127, 127, 127, 127))
        painter.end()

        child.setPixmap(tempPixmap)

        if drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction, QtCore.Qt.CopyAction) == QtCore.Qt.MoveAction:
            child.close()
        else:
            child.show()
            child.setPixmap(pixmap)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    mainWidget = QtGui.QWidget()
    horizontalLayout = QtGui.QHBoxLayout()
    horizontalLayout.addWidget(DragWidget())
    horizontalLayout.addWidget(DragWidget())

    mainWidget.setLayout(horizontalLayout)
    mainWidget.setWindowTitle(QtCore.QObject.tr(mainWidget, "Draggable Icons"))
    mainWidget.show()

    sys.exit(app.exec_())
