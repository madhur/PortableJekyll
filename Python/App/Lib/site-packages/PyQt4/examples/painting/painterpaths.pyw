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
sip.setapi('QVariant', 2)

from math import cos, pi, sin

from PyQt4 import QtCore, QtGui


class RenderArea(QtGui.QWidget):
    def __init__(self, path, parent=None):
        super(RenderArea, self).__init__(parent)

        self.path = path

        self.penWidth = 1
        self.rotationAngle = 0
        self.setBackgroundRole(QtGui.QPalette.Base)

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(100, 100)

    def setFillRule(self, rule):
        self.path.setFillRule(rule)
        self.update()

    def setFillGradient(self, color1, color2):
        self.fillColor1 = color1
        self.fillColor2 = color2
        self.update()

    def setPenWidth(self, width):
        self.penWidth = width
        self.update()

    def setPenColor(self, color):
        self.penColor = color
        self.update()

    def setRotationAngle(self, degrees):
        self.rotationAngle = degrees
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.scale(self.width() / 100.0, self.height() / 100.0)
        painter.translate(50.0, 50.0)
        painter.rotate(-self.rotationAngle)
        painter.translate(-50.0, -50.0)

        painter.setPen(QtGui.QPen(self.penColor, self.penWidth,
                QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        gradient = QtGui.QLinearGradient(0, 0, 0, 100)
        gradient.setColorAt(0.0, self.fillColor1)
        gradient.setColorAt(1.0, self.fillColor2)
        painter.setBrush(QtGui.QBrush(gradient))
        painter.drawPath(self.path)


class Window(QtGui.QWidget):
    NumRenderAreas = 9

    def __init__(self):
        super(Window, self).__init__()

        rectPath = QtGui.QPainterPath()
        rectPath.moveTo(20.0, 30.0)
        rectPath.lineTo(80.0, 30.0)
        rectPath.lineTo(80.0, 70.0)
        rectPath.lineTo(20.0, 70.0)
        rectPath.closeSubpath()

        roundRectPath = QtGui.QPainterPath()
        roundRectPath.moveTo(80.0, 35.0)
        roundRectPath.arcTo(70.0, 30.0, 10.0, 10.0, 0.0, 90.0)
        roundRectPath.lineTo(25.0, 30.0)
        roundRectPath.arcTo(20.0, 30.0, 10.0, 10.0, 90.0, 90.0)
        roundRectPath.lineTo(20.0, 65.0)
        roundRectPath.arcTo(20.0, 60.0, 10.0, 10.0, 180.0, 90.0)
        roundRectPath.lineTo(75.0, 70.0)
        roundRectPath.arcTo(70.0, 60.0, 10.0, 10.0, 270.0, 90.0)
        roundRectPath.closeSubpath()

        ellipsePath = QtGui.QPainterPath()
        ellipsePath.moveTo(80.0, 50.0)
        ellipsePath.arcTo(20.0, 30.0, 60.0, 40.0, 0.0, 360.0)

        piePath = QtGui.QPainterPath()
        piePath.moveTo(50.0, 50.0)
        piePath.lineTo(65.0, 32.6795)
        piePath.arcTo(20.0, 30.0, 60.0, 40.0, 60.0, 240.0)
        piePath.closeSubpath()

        polygonPath = QtGui.QPainterPath()
        polygonPath.moveTo(10.0, 80.0)
        polygonPath.lineTo(20.0, 10.0)
        polygonPath.lineTo(80.0, 30.0)
        polygonPath.lineTo(90.0, 70.0)
        polygonPath.closeSubpath()

        groupPath = QtGui.QPainterPath()
        groupPath.moveTo(60.0, 40.0)
        groupPath.arcTo(20.0, 20.0, 40.0, 40.0, 0.0, 360.0)
        groupPath.moveTo(40.0, 40.0)
        groupPath.lineTo(40.0, 80.0)
        groupPath.lineTo(80.0, 80.0)
        groupPath.lineTo(80.0, 40.0)
        groupPath.closeSubpath()

        textPath = QtGui.QPainterPath()
        timesFont = QtGui.QFont("Times", 50)
        timesFont.setStyleStrategy(QtGui.QFont.ForceOutline)
        textPath.addText(10, 70, timesFont, "Qt")

        bezierPath = QtGui.QPainterPath()
        bezierPath.moveTo(20, 30)
        bezierPath.cubicTo(80, 0, 50, 50, 80, 80)

        starPath = QtGui.QPainterPath()
        starPath.moveTo(90, 50)
        for i in range(1, 5):
            starPath.lineTo(50 + 40 * cos(0.8 * i * pi),
                    50 + 40 * sin(0.8 * i * pi))
        starPath.closeSubpath()

        self.renderAreas = [RenderArea(rectPath), RenderArea(roundRectPath),
                RenderArea(ellipsePath), RenderArea(piePath),
                RenderArea(polygonPath), RenderArea(groupPath),
                RenderArea(textPath), RenderArea(bezierPath),
                RenderArea(starPath)]
        assert len(self.renderAreas) == 9

        self.fillRuleComboBox = QtGui.QComboBox()
        self.fillRuleComboBox.addItem("Odd Even", QtCore.Qt.OddEvenFill)
        self.fillRuleComboBox.addItem("Winding", QtCore.Qt.WindingFill)

        fillRuleLabel = QtGui.QLabel("Fill &Rule:")
        fillRuleLabel.setBuddy(self.fillRuleComboBox)

        self.fillColor1ComboBox = QtGui.QComboBox()
        self.populateWithColors(self.fillColor1ComboBox)
        self.fillColor1ComboBox.setCurrentIndex(
                self.fillColor1ComboBox.findText("mediumslateblue"))

        self.fillColor2ComboBox = QtGui.QComboBox()
        self.populateWithColors(self.fillColor2ComboBox)
        self.fillColor2ComboBox.setCurrentIndex(
                self.fillColor2ComboBox.findText("cornsilk"))

        fillGradientLabel = QtGui.QLabel("&Fill Gradient:")
        fillGradientLabel.setBuddy(self.fillColor1ComboBox)

        fillToLabel = QtGui.QLabel("to")
        fillToLabel.setSizePolicy(QtGui.QSizePolicy.Fixed,
                QtGui.QSizePolicy.Fixed)

        self.penWidthSpinBox = QtGui.QSpinBox()
        self.penWidthSpinBox.setRange(0, 20)

        penWidthLabel = QtGui.QLabel("&Pen Width:")
        penWidthLabel.setBuddy(self.penWidthSpinBox)

        self.penColorComboBox = QtGui.QComboBox()
        self.populateWithColors(self.penColorComboBox)
        self.penColorComboBox.setCurrentIndex(
                self.penColorComboBox.findText('darkslateblue'))

        penColorLabel = QtGui.QLabel("Pen &Color:")
        penColorLabel.setBuddy(self.penColorComboBox)

        self.rotationAngleSpinBox = QtGui.QSpinBox()
        self.rotationAngleSpinBox.setRange(0, 359)
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix('\xB0')

        rotationAngleLabel = QtGui.QLabel("&Rotation Angle:")
        rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)

        self.fillRuleComboBox.activated.connect(self.fillRuleChanged)
        self.fillColor1ComboBox.activated.connect(self.fillGradientChanged)
        self.fillColor2ComboBox.activated.connect(self.fillGradientChanged)
        self.penColorComboBox.activated.connect(self.penColorChanged)

        for i in range(Window.NumRenderAreas):
            self.penWidthSpinBox.valueChanged.connect(self.renderAreas[i].setPenWidth)
            self.rotationAngleSpinBox.valueChanged.connect(self.renderAreas[i].setRotationAngle)

        topLayout = QtGui.QGridLayout()
        for i in range(Window.NumRenderAreas):
            topLayout.addWidget(self.renderAreas[i], i / 3, i % 3)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 4)
        mainLayout.addWidget(fillRuleLabel, 1, 0)
        mainLayout.addWidget(self.fillRuleComboBox, 1, 1, 1, 3)
        mainLayout.addWidget(fillGradientLabel, 2, 0)
        mainLayout.addWidget(self.fillColor1ComboBox, 2, 1)
        mainLayout.addWidget(fillToLabel, 2, 2)
        mainLayout.addWidget(self.fillColor2ComboBox, 2, 3)
        mainLayout.addWidget(penWidthLabel, 3, 0)
        mainLayout.addWidget(self.penWidthSpinBox, 3, 1, 1, 3)
        mainLayout.addWidget(penColorLabel, 4, 0)
        mainLayout.addWidget(self.penColorComboBox, 4, 1, 1, 3)
        mainLayout.addWidget(rotationAngleLabel, 5, 0)
        mainLayout.addWidget(self.rotationAngleSpinBox, 5, 1, 1, 3)
        self.setLayout(mainLayout)

        self.fillRuleChanged()
        self.fillGradientChanged()
        self.penColorChanged()
        self.penWidthSpinBox.setValue(2)

        self.setWindowTitle("Painter Paths")

    def fillRuleChanged(self):
        rule = QtCore.Qt.FillRule(self.currentItemData(self.fillRuleComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setFillRule(rule)

    def fillGradientChanged(self):
        color1 = QtGui.QColor(self.currentItemData(self.fillColor1ComboBox))
        color2 = QtGui.QColor(self.currentItemData(self.fillColor2ComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setFillGradient(color1, color2)

    def penColorChanged(self):
        color = QtGui.QColor(self.currentItemData(self.penColorComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setPenColor(color)

    def populateWithColors(self, comboBox):
        colorNames = QtGui.QColor.colorNames()
        for name in colorNames:
            comboBox.addItem(name, name)

    def currentItemData(self, comboBox):
        return comboBox.itemData(comboBox.currentIndex())


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
