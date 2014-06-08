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

import math

from PyQt4 import QtCore, QtGui

try:
    import stickman_rc3
except ImportError:
    import stickman_rc2


class Node(QtGui.QGraphicsObject):
    positionChanged = QtCore.pyqtSignal()

    def __init__(self, pos, parent=None):
        super(Node, self).__init__(parent)

        self.m_dragging = False

        self.setPos(pos)
        self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)

    def boundingRect(self):
        return QtCore.QRectF(-6.0, -6.0, 12.0, 12.0)

    def paint(self, painter, option, widget):
        painter.setPen(QtCore.Qt.white)
        painter.drawEllipse(QtCore.QPointF(0.0, 0.0), 5.0, 5.0)

    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemPositionChange:
            self.positionChanged.emit()

        return super(Node, self).itemChange(change, value)

    def mousePressEvent(self, event):
        self.m_dragging = True

    def mouseMoveEvent(self, event):
        if self.m_dragging:
            self.setPos(self.mapToParent(event.pos()))

    def mouseReleaseEvent(self, event):
        self.m_dragging = False


Coords = (
    # Head: 0
    (0.0, -150.0),

    # Body pentagon, top->bottom, left->right: 1 - 5
    (0.0, -100.0),
    (-50.0, -50.0),
    (50.0, -50.0),
    (-25.0, 50.0),
    (25.0, 50.0),

    # Right arm: 6 - 7
    (-100.0, 0.0),
    (-125.0, 50.0),

    # Left arm: 8 - 9
    (100.0, 0.0),
    (125.0, 50.0),

    # Lower body: 10 - 11
    (-35.0, 75.0),
    (35.0, 75.0),

    # Right leg: 12 - 13
    (-25.0, 200.0),
    (-30.0, 300.0),

    # Left leg: 14 - 15
    (25.0, 200.0),
    (30.0, 300.0))


Bones = (
    # Neck.
    (0, 1),

    # Body.
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 5),

    # Right arm.
    (2, 6),
    (6, 7),

    # Left arm.
    (3, 8),
    (8, 9),

    # Lower body.
    (4, 10),
    (4, 11),
    (5, 10),
    (5, 11),
    (10, 11),

    # Right leg.
    (10, 12),
    (12, 13),

    # Left leg.
    (11, 14),
    (14, 15))


class StickMan(QtGui.QGraphicsObject):
    def __init__(self):
        super(StickMan, self).__init__()

        self.m_sticks = True
        self.m_isDead = False
        self.m_pixmap = QtGui.QPixmap('images/head.png')
        self.m_penColor = QtGui.QColor(QtCore.Qt.white)
        self.m_fillColor = QtGui.QColor(QtCore.Qt.black)

        # Set up start position of limbs.
        self.m_nodes = []
        for x, y in Coords:
            node = Node(QtCore.QPointF(x, y), self)
            node.positionChanged.connect(self.childPositionChanged)
            self.m_nodes.append(node)

        self.m_perfectBoneLengths = []
        for n1, n2 in Bones:
            node1 = self.m_nodes[n1]
            node2 = self.m_nodes[n2]

            dist = node1.pos() - node2.pos()
            self.m_perfectBoneLengths.append(math.hypot(dist.x(), dist.y()))

        self.startTimer(10)

    def childPositionChanged(self):
        self.prepareGeometryChange()

    def setDrawSticks(self, on):
        self.m_sticks = on

        for node in self.m_nodes:
            node.setVisible(on)

    def drawSticks(self):
        return self.m_sticks

    def boundingRect(self):
        # Account for head radius of 50.0 plus pen which is 5.0.
        return self.childrenBoundingRect().adjusted(-55.0, -55.0, 55.0, 55.0)

    def nodeCount(self):
        return len(self.m_nodes)

    def node(self, idx):
        if idx >= 0 and idx < len(self.m_nodes):
            return self.m_nodes[idx]

        return None

    def timerEvent(self, e):
        self.update()

    def stabilize(self):
        threshold = 0.001

        for i, (n1, n2) in enumerate(Bones):
            node1 = self.m_nodes[n1]
            node2 = self.m_nodes[n2]

            pos1 = node1.pos()
            pos2 = node2.pos()

            dist = pos1 - pos2
            length = math.hypot(dist.x(), dist.y())
            diff = (length - self.m_perfectBoneLengths[i]) / length

            p = dist * (0.5 * diff)
            if p.x() > threshold and p.y() > threshold:
                pos1 -= p
                pos2 += p

                node1.setPos(pos1)
                node2.setPos(pos2)

    def posFor(self, idx):
        return self.m_nodes[idx].pos()

    @QtCore.pyqtProperty(QtGui.QColor)
    def penColor(self):
        return QtGui.QColor(self.m_penColor)

    @penColor.setter
    def penColor(self, color):
        self.m_penColor = QtGui.QColor(color)

    @QtCore.pyqtProperty(QtGui.QColor)
    def fillColor(self):
        return QtGui.QColor(self.m_fillColor)

    @fillColor.setter
    def fillColor(self, color):
        self.m_fillColor = QtGui.QColor(color)

    @QtCore.pyqtProperty(bool)
    def isDead(self):
        return self.m_isDead

    @isDead.setter
    def isDead(self, isDead):
        self.m_isDead = isDead

    def paint(self, painter, option, widget):
        self.stabilize()

        if self.m_sticks:
            painter.setPen(QtCore.Qt.white)

            for n1, n2 in Bones:
                node1 = self.m_nodes[n1]
                node2 = self.m_nodes[n2]

                painter.drawLine(node1.pos(), node2.pos())
        else:
            # First bone is neck and will be used for head.

            path = QtGui.QPainterPath()
            path.moveTo(self.posFor(0))
            path.lineTo(self.posFor(1))

            # Right arm.
            path.lineTo(self.posFor(2))
            path.lineTo(self.posFor(6))
            path.lineTo(self.posFor(7))

            # Left arm.
            path.moveTo(self.posFor(3))
            path.lineTo(self.posFor(8))
            path.lineTo(self.posFor(9))

            # Body.
            path.moveTo(self.posFor(2))
            path.lineTo(self.posFor(4))
            path.lineTo(self.posFor(10))
            path.lineTo(self.posFor(11))
            path.lineTo(self.posFor(5))
            path.lineTo(self.posFor(3))
            path.lineTo(self.posFor(1))

            # Right leg.
            path.moveTo(self.posFor(10))
            path.lineTo(self.posFor(12))
            path.lineTo(self.posFor(13))

            # Left leg.
            path.moveTo(self.posFor(11))
            path.lineTo(self.posFor(14))
            path.lineTo(self.posFor(15))

            painter.setPen(QtGui.QPen(self.m_penColor, 5.0, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))
            painter.drawPath(path)

            n1, n2 = Bones[0]
            node1 = self.m_nodes[n1]
            node2 = self.m_nodes[n2]

            dist = node2.pos() - node1.pos()

            sinAngle = dist.x() / math.hypot(dist.x(), dist.y())
            angle = math.degrees(math.asin(sinAngle))

            headPos = node1.pos()
            painter.translate(headPos)
            painter.rotate(-angle)

            painter.setBrush(self.m_fillColor)
            painter.drawEllipse(QtCore.QPointF(0, 0), 50.0, 50.0)

            painter.setBrush(self.m_penColor)
            painter.setPen(QtGui.QPen(self.m_penColor, 2.5, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))

            # Eyes.
            if self.m_isDead:
                painter.drawLine(-30.0, -30.0, -20.0, -20.0)
                painter.drawLine(-20.0, -30.0, -30.0, -20.0)

                painter.drawLine(20.0, -30.0, 30.0, -20.0)
                painter.drawLine(30.0, -30.0, 20.0, -20.0)
            else:
                painter.drawChord(QtCore.QRectF(-30.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)
                painter.drawChord(QtCore.QRectF(5.0, -30.0, 25.0, 70.0), 30.0 * 16, 120.0 * 16)

            # Mouth.
            if self.m_isDead:
                painter.drawLine(-28.0, 2.0, 29.0, 2.0)
            else:
                painter.setBrush(QtGui.QColor(128, 0, 64 ))
                painter.drawChord(QtCore.QRectF(-28.0, 2.0 - 55.0 / 2.0, 57.0, 55.0), 0.0, -180.0 * 16)

            # Pupils.
            if not self.m_isDead:
                painter.setPen(QtGui.QPen(self.m_fillColor, 1.0, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))
                painter.setBrush(self.m_fillColor)
                painter.drawEllipse(QtCore.QPointF(-12.0, -25.0), 5.0, 5.0)
                painter.drawEllipse(QtCore.QPointF(22.0, -25.0), 5.0, 5.0)


class GraphicsView(QtGui.QGraphicsView):
    keyPressed = QtCore.pyqtSignal(int)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

        self.keyPressed.emit(QtCore.Qt.Key(e.key()))


class Frame(object):
    def __init__(self):
        self.m_nodePositions = []

    def nodeCount(self):
        return len(self.m_nodePositions)

    def setNodeCount(self, nodeCount):
        while nodeCount > len(self.m_nodePositions):
            self.m_nodePositions.append(QtCore.QPointF())

        while nodeCount < len(self.m_nodePositions):
            self.m_nodePositions.pop()

    def nodePos(self, idx):
        return QtCore.QPointF(self.m_nodePositions[idx])

    def setNodePos(self, idx, pos):
        self.m_nodePositions[idx] = QtCore.QPointF(pos)


class Animation(object):
    def __init__(self):
        self.m_currentFrame = 0
        self.m_frames = [Frame()]
        self.m_name = ''

    def setTotalFrames(self, totalFrames):
        while len(self.m_frames) < totalFrames:
            self.m_frames.append(Frame())

        while totalFrames < len(self.m_frames):
            self.m_frames.pop()

    def totalFrames(self):
        return len(self.m_frames)

    def setCurrentFrame(self, currentFrame):
        self.m_currentFrame = max(min(currentFrame, self.totalFrames() - 1), 0)

    def currentFrame(self):
        return self.m_currentFrame

    def setNodeCount(self, nodeCount):
        frame = self.m_frames[self.m_currentFrame]
        frame.setNodeCount(nodeCount)

    def nodeCount(self):
        frame = self.m_frames[self.m_currentFrame]
        return frame.nodeCount()

    def setNodePos(self, idx, pos):
        frame = self.m_frames[self.m_currentFrame]
        frame.setNodePos(idx, pos)

    def nodePos(self, idx):
        frame = self.m_frames[self.m_currentFrame]
        return frame.nodePos(idx)

    def name(self):
        return self.m_name

    def setName(self, name):
        self.m_name = name

    def save(self, device):
        stream = QtCore.QDataStream(device)
        stream.writeQString(self.m_name)
        stream.writeInt(len(self.m_frames))

        for frame in self.m_frames:
            stream.writeInt(frame.nodeCount())

            for i in range(frame.nodeCount()):
                stream << frame.nodePos(i)

    def load(self, device):
        self.m_frames = []

        stream = QtCore.QDataStream(device)
        self.m_name = stream.readQString()
        frameCount = stream.readInt()

        for i in range(frameCount):
            nodeCount = stream.readInt()

            frame = Frame()
            frame.setNodeCount(nodeCount)

            for j in range(nodeCount):
                pos = QtCore.QPointF()
                stream >> pos

                frame.setNodePos(j, pos)

            self.m_frames.append(frame)


class KeyPressTransition(QtCore.QSignalTransition):
    def __init__(self, receiver, key, target=None):
        super(KeyPressTransition, self).__init__(receiver.keyPressed)

        self.m_key = key

        if target is not None:
            self.setTargetState(target)

    def eventTest(self, e):
        if super(KeyPressTransition, self).eventTest(e):
            key = e.arguments()[0]
            return key == self.m_key

        return False


class LightningStrikesTransition(QtCore.QEventTransition):
    def __init__(self, target):
        super(LightningStrikesTransition, self).__init__()

        self.setEventSource(self)
        self.setEventType(QtCore.QEvent.Timer)
        self.setTargetState(target)
        QtCore.qsrand(QtCore.QDateTime.currentDateTime().toTime_t())
        self.startTimer(1000)

    def eventTest(self, e):
        return (super(LightningStrikesTransition, self).eventTest(e) and
                (QtCore.qrand() % 50) == 0)


class LifeCycle(object):
    def __init__(self, stickMan, keyReceiver):
        self.m_stickMan = stickMan
        self.m_keyReceiver = keyReceiver

        # Create animation group to be used for all transitions.
        self.m_animationGroup = QtCore.QParallelAnimationGroup()
        stickManNodeCount = self.m_stickMan.nodeCount()
        self._pas = []
        for i in range(stickManNodeCount):
            pa = QtCore.QPropertyAnimation(self.m_stickMan.node(i), 'pos')
            self._pas.append(pa)
            self.m_animationGroup.addAnimation(pa)

        # Set up intial state graph.
        self.m_machine = QtCore.QStateMachine()
        self.m_machine.addDefaultAnimation(self.m_animationGroup)

        self.m_alive = QtCore.QState(self.m_machine)
        self.m_alive.setObjectName('alive')

        # Make it blink when lightning strikes before entering dead animation.
        lightningBlink = QtCore.QState(self.m_machine)
        lightningBlink.assignProperty(self.m_stickMan.scene(),
                'backgroundBrush', QtCore.Qt.white)
        lightningBlink.assignProperty(self.m_stickMan, 'penColor',
                QtCore.Qt.black)
        lightningBlink.assignProperty(self.m_stickMan, 'fillColor',
                QtCore.Qt.white)
        lightningBlink.assignProperty(self.m_stickMan, 'isDead', True)

        timer = QtCore.QTimer(lightningBlink)
        timer.setSingleShot(True)
        timer.setInterval(100)
        lightningBlink.entered.connect(timer.start)
        lightningBlink.exited.connect(timer.stop)

        self.m_dead = QtCore.QState(self.m_machine)
        self.m_dead.assignProperty(self.m_stickMan.scene(), 'backgroundBrush',
                QtCore.Qt.black)
        self.m_dead.assignProperty(self.m_stickMan, 'penColor',
                QtCore.Qt.white)
        self.m_dead.assignProperty(self.m_stickMan, 'fillColor',
                QtCore.Qt.black)
        self.m_dead.setObjectName('dead')

        # Idle state (sets no properties).
        self.m_idle = QtCore.QState(self.m_alive)
        self.m_idle.setObjectName('idle')

        self.m_alive.setInitialState(self.m_idle)

        # Lightning strikes at random.
        self.m_alive.addTransition(LightningStrikesTransition(lightningBlink))
        lightningBlink.addTransition(timer.timeout, self.m_dead)

        self.m_machine.setInitialState(self.m_alive)

    def setDeathAnimation(self, fileName):
        deathAnimation = self.makeState(self.m_dead, fileName)
        self.m_dead.setInitialState(deathAnimation)

    def start(self):
        self.m_machine.start()

    def addActivity(self, fileName, key):
        state = self.makeState(self.m_alive, fileName)
        self.m_alive.addTransition(KeyPressTransition(self.m_keyReceiver, key, state))

    def makeState(self, parentState, animationFileName):
        topLevel = QtCore.QState(parentState)

        animation = Animation()

        file = QtCore.QFile(animationFileName)
        if file.open(QtCore.QIODevice.ReadOnly):
            animation.load(file)

        frameCount = animation.totalFrames()
        previousState = None
        for i in range(frameCount):
            animation.setCurrentFrame(i)

            frameState = QtCore.QState(topLevel)
            nodeCount = animation.nodeCount()
            for j in range(nodeCount):
                frameState.assignProperty(self.m_stickMan.node(j), 'pos',
                        animation.nodePos(j))

            frameState.setObjectName('frame %d' % i)

            if previousState is None:
                topLevel.setInitialState(frameState)
            else:
                previousState.addTransition(previousState.propertiesAssigned,
                        frameState)

            previousState = frameState

        previousState.addTransition(previousState.propertiesAssigned,
                topLevel.initialState())

        return topLevel


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    stickMan = StickMan()
    stickMan.setDrawSticks(False)

    textItem = QtGui.QGraphicsTextItem()
    textItem.setHtml("<font color=\"white\"><b>Stickman</b>"
        "<p>"
        "Tell the stickman what to do!"
        "</p>"
        "<p><i>"
        "<li>Press <font color=\"purple\">J</font> to make the stickman jump.</li>"
        "<li>Press <font color=\"purple\">D</font> to make the stickman dance.</li>"
        "<li>Press <font color=\"purple\">C</font> to make him chill out.</li>"
        "<li>When you are done, press <font color=\"purple\">Escape</font>.</li>"
        "</i></p>"
        "<p>If he is unlucky, the stickman will get struck by lightning, and never jump, dance or chill out again."
        "</p></font>")

    w = textItem.boundingRect().width()
    stickManBoundingRect = stickMan.mapToScene(stickMan.boundingRect()).boundingRect()
    textItem.setPos(-w / 2.0, stickManBoundingRect.bottom() + 25.0)

    scene = QtGui.QGraphicsScene()
    scene.addItem(stickMan)
    scene.addItem(textItem)
    scene.setBackgroundBrush(QtCore.Qt.black)

    view = GraphicsView()
    view.setRenderHints(QtGui.QPainter.Antialiasing)
    view.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
    view.setScene(scene)
    view.show()
    view.setFocus()

    # Make enough room in the scene for stickman to jump and die.
    sceneRect = scene.sceneRect()
    view.resize(sceneRect.width() + 100, sceneRect.height() + 100)
    view.setSceneRect(sceneRect)

    cycle = LifeCycle(stickMan, view)
    cycle.setDeathAnimation(':/animations/dead')

    cycle.addActivity(':/animations/jumping', QtCore.Qt.Key_J)
    cycle.addActivity(':/animations/dancing', QtCore.Qt.Key_D)
    cycle.addActivity(':/animations/chilling', QtCore.Qt.Key_C)
    cycle.start()

    sys.exit(app.exec_())
