#!/usr/bin/env python


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


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

from PyQt4 import QtCore, QtGui

try:
    import embeddeddialogs_rc3
except ImportError:
    import embeddeddialogs_rc2

from embeddeddialog import Ui_embeddedDialog


class CustomProxy(QtGui.QGraphicsProxyWidget):
    def __init__(self, parent=None, wFlags=0):
        super(CustomProxy, self).__init__(parent, wFlags)

        self.popupShown = False
        self.timeLine = QtCore.QTimeLine(250, self)
        self.timeLine.valueChanged.connect(self.updateStep)
        self.timeLine.stateChanged.connect(self.stateChanged)

    def boundingRect(self):
        return QtGui.QGraphicsProxyWidget.boundingRect(self).adjusted(0, 0, 10, 10)

    def paintWindowFrame(self, painter, option, widget):
        color = QtGui.QColor(0, 0, 0, 64)

        r = self.windowFrameRect()
        right = QtCore.QRectF(r.right(), r.top()+10, 10, r.height()-10)
        bottom = QtCore.QRectF(r.left()+10, r.bottom(), r.width(), 10)
        intersectsRight = right.intersects(option.exposedRect)
        intersectsBottom = bottom.intersects(option.exposedRect)
        if intersectsRight and intersectsBottom:
            path=QtGui.QPainterPath()
            path.addRect(right)
            path.addRect(bottom)
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(color)
            painter.drawPath(path)
        elif intersectsBottom:
            painter.fillRect(bottom, color)
        elif intersectsRight:
            painter.fillRect(right, color)

        super(CustomProxy, self).paintWindowFrame(painter, option, widget)

    def hoverEnterEvent(self, event):
        super(CustomProxy, self).hoverEnterEvent(event)

        self.scene().setActiveWindow(self)
        if self.timeLine.currentValue != 1:
            self.zoomIn()

    def hoverLeaveEvent(self, event):
        super(CustomProxy, self).hoverLeaveEvent(event)

        if not self.popupShown and (self.timeLine.direction() != QtCore.QTimeLine.Backward or self.timeLine.currentValue() != 0):
            self.zoomOut()

    def sceneEventFilter(self, watched, event):
        if watched.isWindow() and (event.type() == QtCore.QEvent.UngrabMouse or event.type() == QtCore.QEvent.GrabMouse):
            self.popupShown = watched.isVisible()
            if not self.popupShown and not self.isUnderMouse():
                self.zoomOut()

        return super(CustomProxy, self).sceneEventFilter(watched, event)

    def itemChange(self, change, value):
        if change == self.ItemChildAddedChange or change == self.ItemChildRemovedChange :
            # how to translate this line to python?
            # QGraphicsItem *item = qVariantValue<QGraphicsItem *>(value);
            item = value
            try:
                if change == self.ItemChildAddedChange:
                    item.installSceneEventFilter(self)
                else:
                    item.removeSceneEventFilter(self)
            except:
                pass

        return super(CustomProxy, self).itemChange(change, value)

    def updateStep(self, step):
        r=self.boundingRect()
        self.setTransform( QtGui.QTransform() \
                            .translate(r.width() / 2, r.height() / 2)\
                            .rotate(step * 30, QtCore.Qt.XAxis)\
                            .rotate(step * 10, QtCore.Qt.YAxis)\
                            .rotate(step * 5, QtCore.Qt.ZAxis)\
                            .scale(1 + 1.5 * step, 1 + 1.5 * step)\
                            .translate(-r.width() / 2, -r.height() / 2))

    def stateChanged(self, state):
        if state == QtCore.QTimeLine.Running:
            if self.timeLine.direction() == QtCore.QTimeLine.Forward:
                self.setCacheMode(self.NoCache)
            elif state == QtCore.QTimeLine.NotRunning:
                if self.timeLine.direction() == QtCore.QTimeLine.Backward:
                    self.setCacheMode(self.DeviceCoordinateCache)

    def zoomIn(self):
        if self.timeLine.direction() != QtCore.QTimeLine.Forward:
            self.timeLine.setDirection(QtCore.QTimeLine.Forward)
        if self.timeLine.state() == QtCore.QTimeLine.NotRunning:
            self.timeLine.start()

    def zoomOut(self):
        if self.timeLine.direction() != QtCore.QTimeLine.Backward:
            self.timeLine.setDirection(QtCore.QTimeLine.Backward)
        if self.timeLine.state() == QtCore.QTimeLine.NotRunning:
            self.timeLine.start()


class EmbeddedDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(EmbeddedDialog, self).__init__(parent)

        self.ui = Ui_embeddedDialog()
        self.ui.setupUi(self)
        self.ui.layoutDirection.setCurrentIndex(self.layoutDirection() != QtCore.Qt.LeftToRight)

        for styleName in QtGui.QStyleFactory.keys():
            self.ui.style.addItem(styleName)
            if self.style().objectName().lower() == styleName.lower():
                self.ui.style.setCurrentIndex(self.ui.style.count() -1)

        self.ui.layoutDirection.activated.connect(self.layoutDirectionChanged)
        self.ui.spacing.valueChanged.connect(self.spacingChanged)
        self.ui.fontComboBox.currentFontChanged.connect(self.fontChanged)
        self.ui.style.activated[str].connect(self.styleChanged)

    def layoutDirectionChanged(self, index):
        if index == 0:
            self.setLayoutDirection(QtCore.Qt.LeftToRight)
        else:
            self.setLayoutDirection(QtCore.Qt.RightToLeft)

    def spacingChanged(self, spacing):
        self.layout().setSpacing(spacing)
        self.adjustSize()

    def fontChanged(self, font):
        self.setFont(font)

    def setStyleHelper(self, widget, style):
        widget.setStyle(style)
        widget.setPalette(style.standardPalette())
        for child in widget.children():
            if isinstance(child, QtGui.QWidget):
                self.setStyleHelper(child, style)
    
    def styleChanged(self, styleName):
        style=QtGui.QStyleFactory.create(styleName)
        if style:
            self.setStyleHelper(self, style)

        # Keep a reference to the style.
        self._style = style


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    scene = QtGui.QGraphicsScene()
    for y in range(10):
        for x in range(10):
            proxy = CustomProxy(None, QtCore.Qt.Window)
            proxy.setWidget(EmbeddedDialog())

            rect = proxy.boundingRect()

            proxy.setPos( x * rect.width()*1.05, y*rect.height()*1.05 )
            proxy.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)
            scene.addItem(proxy)

    scene.setSceneRect(scene.itemsBoundingRect())

    view = QtGui.QGraphicsView(scene)
    view.scale(0.5, 0.5)
    view.setRenderHints(view.renderHints() | QtGui.QPainter.Antialiasing  | QtGui.QPainter.SmoothPixmapTransform)
    view.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap(':/No-Ones-Laughing-3.jpg')))
    view.setCacheMode(QtGui.QGraphicsView.CacheBackground)
    view.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)
    view.show()
    view.setWindowTitle("Embedded Dialogs Demo")

    sys.exit(app.exec_())
