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


class DemoItemAnimation(QtGui.QGraphicsItemAnimation):
    ANIM_IN, ANIM_OUT, ANIM_UNSPECIFIED = range(3)

    def __init__(self, item, inOrOut=ANIM_UNSPECIFIED):
        super(DemoItemAnimation, self).__init__()

        self.startPos = QtCore.QPointF()
        self.opacityAt0 = 1.0
        self.opacityAt1 = 1.0
        self.startDelay = 0
        self.inOrOut = inOrOut
        self.hideOnFinished = False
        self.forcePlay = False
        self.timeline = QtCore.QTimeLine(5000)
        self.timeline.setFrameRange(0, 2000)
        self.timeline.setUpdateInterval(int(1000.0/Colors.fps))
        self.moveOnPlay = False
        self.setTimeLine(self.timeline)
        self.setItem(item)

    def prepare(self):
        self.demoItem().prepare()

    def setStartPos(self, pos):
        self.startPos = pos

    def setDuration(self, duration):
        duration = int(duration * Colors.animSpeed)
        self.timeline.setDuration(duration)
        self.moveOnPlay = True

    def setCurrentTime(self, ms):
        self.timeline.setCurrentTime(ms)

    def notOwnerOfItem(self):
        return self is not self.demoItem().currentAnimation

    def play(self, fromStart=True, force=False):
        self.fromStart = fromStart
        self.forcePlay = force

        currPos = self.demoItem().pos()

        # If the item that this animation controls in currently under the
        # control of another animation, stop that animation first.
        if self.demoItem().currentAnimation is not None:
            self.demoItem().currentAnimation.timeline.stop()
        self.demoItem().currentAnimation = self
        self.timeline.stop()

        if Colors.noAnimations and not self.forcePlay:
            self.timeline.setCurrentTime(1)
            self.demoItem().setPos(self.posAt(1))
        else:
            if self.demoItem().isVisible():
                # If the item is already visible, start the animation from the
                # items current position rather than from start..
                self.setPosAt(0.0, currPos)
            else:
                self.setPosAt(0.0, self.startPos)

            if self.fromStart:
                self.timeline.setCurrentTime(0)
                self.demoItem().setPos(self.posAt(0))

        if self.inOrOut == DemoItemAnimation.ANIM_IN:
            self.demoItem().setRecursiveVisible(True)

        if self.startDelay:
            QtCore.QTimer.singleShot(self.startDelay, self.playWithoutDelay)
            return
        else:
            self.playWithoutDelay()

    def playWithoutDelay(self):
        if self.moveOnPlay and not (Colors.noAnimations and not self.forcePlay):
            self.timeline.start()
        self.demoItem().animationStarted(self.inOrOut)

    def stop(self, reset):
        self.timeline.stop()
        if reset:
            self.demoItem().setPos(self.posAt(0))
        if self.hideOnFinished and not self.moveOnPlay:
            self.demoItem().setRecursiveVisible(False)
        self.demoItem().animationStopped(self.inOrOut)

    def setRepeat(self, nr):
        self.timeline.setLoopCount(nr)

    def playReverse(self):
        pass

    def running(self):
        return self.timeLine().state() == QtCore.QTimeLine.Running

    def runningOrItemLocked(self):
        return self.running() or self.demoItem().locked

    def lockItem(self, state):
        self.demoItem().locked = state

    def demoItem(self):
        return self.item()

    def setOpacityAt0(self, opacity):
        self.opacityAt0 = opacity

    def setOpacityAt1(self, opacity):
        self.opacityAt1 = opacity

    def setOpacity(self, step):
        demoItem = self.item()
        demoItem.opacity = self.opacityAt0 + step * step * step * (self.opacityAt1 - self.opacityAt0)

    def afterAnimationStep(self, step):
        if step == 1.0:
            if self.timeline.loopCount() > 0:
                # Animation finished.
                if self.hideOnFinished:
                    self.demoItem().setRecursiveVisible(False)
                self.demoItem().animationStopped(self.inOrOut)
        elif Colors.noAnimations and not self.forcePlay:
            # The animation is not at end, but the animations should not play,
            # so go to end.
            self.setStep(1.0)
