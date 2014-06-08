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
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui


class ColorListEditor(QtGui.QComboBox):
    def __init__(self, widget=None):
        super(ColorListEditor, self).__init__(widget)

        self.populateList()

    def getColor(self):
        color = self.itemData(self.currentIndex(), QtCore.Qt.DecorationRole)
        return color

    def setColor(self, color):
        self.setCurrentIndex(self.findData(color, QtCore.Qt.DecorationRole))

    color = QtCore.pyqtProperty(QtGui.QColor, getColor, setColor, user=True)

    def populateList(self):
        for i, colorName in enumerate(QtGui.QColor.colorNames()):
            color = QtGui.QColor(colorName)
            self.insertItem(i, colorName)
            self.setItemData(i, color, QtCore.Qt.DecorationRole)


class ColorListItemEditorCreator(QtGui.QItemEditorCreatorBase):
    def createWidget(self, parent):
        return ColorListEditor(parent)


class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        factory = QtGui.QItemEditorFactory()
        factory.registerEditor(QtCore.QVariant.Color,
                ColorListItemEditorCreator())
        QtGui.QItemEditorFactory.setDefaultFactory(factory)

        self.createGUI()

    def createGUI(self):
        tableData = [
            ("Alice", QtGui.QColor('aliceblue')),
            ("Neptun", QtGui.QColor('aquamarine')),
            ("Ferdinand", QtGui.QColor('springgreen'))
        ]

        table = QtGui.QTableWidget(3, 2)
        table.setHorizontalHeaderLabels(["Name", "Hair Color"])
        table.verticalHeader().setVisible(False)
        table.resize(150, 50)

        for i, (name, color) in enumerate(tableData):
            nameItem = QtGui.QTableWidgetItem(name)
            colorItem = QtGui.QTableWidgetItem()
            colorItem.setData(QtCore.Qt.DisplayRole, color)
            table.setItem(i, 0, nameItem)
            table.setItem(i, 1, colorItem)

        table.resizeColumnToContents(0)
        table.horizontalHeader().setStretchLastSection(True)

        layout = QtGui.QGridLayout()
        layout.addWidget(table, 0, 0)
        self.setLayout(layout)

        self.setWindowTitle("Color Editor Factory")


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
