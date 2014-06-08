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


from PyQt4 import QtCore, QtGui

from colors import Colors
from demoitem import DemoItem


class HeadingItem(DemoItem):
    def __init__(self, text, scene=None, parent=None):
        super(HeadingItem, self).__init__(scene, parent)

        self.text = text
        self.noSubPixeling = True

    def createImage(self, matrix):
        sx = min(matrix.m11(), matrix.m22())
        sy = max(matrix.m22(), sx)
        fm = QtGui.QFontMetrics(Colors.headingFont())

        w = fm.width(self.text) + 1
        h = fm.height()
        xShadow = 3.0
        yShadow = 3.0

        image = QtGui.QImage(int((w + xShadow) * sx), int((h + yShadow) * sy),
                QtGui.QImage.Format_ARGB32_Premultiplied)
        image.fill(QtGui.QColor(0, 0, 0, 0).rgba())
        painter = QtGui.QPainter(image)
        painter.setFont(Colors.headingFont())
        painter.scale(sx, sy)

        # Draw shadow.
        brush_shadow = QtGui.QLinearGradient(xShadow, yShadow, w, yShadow)
        brush_shadow.setSpread(QtGui.QLinearGradient.PadSpread)
        if Colors.useEightBitPalette:
            brush_shadow.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        else:
            brush_shadow.setColorAt(0.0, QtGui.QColor(0, 0, 0, 100))
        pen_shadow = QtGui.QPen()
        pen_shadow.setBrush(brush_shadow)
        painter.setPen(pen_shadow)
        painter.drawText(int(xShadow), int(yShadow), int(w), int(h),
                QtCore.Qt.AlignLeft, self.text)

        # Draw text.
        brush_text = QtGui.QLinearGradient(0, 0, w, w)
        brush_text.setSpread(QtGui.QLinearGradient.PadSpread)
        brush_text.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        brush_text.setColorAt(0.2, QtGui.QColor(255, 255, 255))
        brush_text.setColorAt(0.5, QtGui.QColor(190, 190, 190))
        pen_text = QtGui.QPen()
        pen_text.setBrush(brush_text)
        painter.setPen(pen_text)
        painter.drawText(0, 0, int(w), int(h), QtCore.Qt.AlignLeft, self.text)

        return image

    def animationStarted(self, id=0):
        self.noSubPixeling = False

    def animationStopped(self, id=0):
        self.noSubPixeling = True
