#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


from PyQt4 import QtGui

from colors import Colors
from demoitem import DemoItem


class DockItem(DemoItem):
    UP, DOWN, LEFT, RIGHT = range(4)

    def __init__(self, orien, x, y, width, length, scene=None, parent=None):
        super(DockItem, self).__init__(scene, parent)

        self.orientation = orien
        self.width = width
        self.length = length
        self.setPos(x, y)
        self.setZValue(40)
        self.setupPixmap()

    def setupPixmap(self):
        self.pixmap = QtGui.QPixmap(int(self.boundingRect().width()),
                int(self.boundingRect().height()))
        self.pixmap.fill(QtGui.QColor(0, 0, 0, 0))

        painter = QtGui.QPainter(self.pixmap)

        # Create brush.
        background = Colors.sceneBg1
        brush = QtGui.QLinearGradient(0, 0, 0, self.boundingRect().height())
        brush.setSpread(QtGui.QGradient.PadSpread)

        if self.orientation == DockItem.DOWN:
            brush.setColorAt(0.0, background)
            brush.setColorAt(0.2, background)
            background.setAlpha(0)
            brush.setColorAt(1.0, background)
        elif self.orientation == DockItem.UP:
            brush.setColorAt(1.0, background)
            brush.setColorAt(0.8, background)
            background.setAlpha(0)
            brush.setColorAt(0.0, background)

        painter.fillRect(0, 0, int(self.boundingRect().width()),
                int(self.boundingRect().height()), brush)

    def boundingRect(self):
        if self.orientation in (DockItem.UP, DockItem.DOWN):
            return QtCore.QRectF(0, 0, self.length, self.width)
        else:
            return QtCore.QRectF(0, 0, self.width, self.length)

    def paint(self, painter, option, widget):
        painter.drawPixmap(0, 0, self.pixmap)
