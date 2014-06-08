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


import random

from PyQt4 import QtCore, QtGui, QtDeclarative


class TileData(QtCore.QObject):
    hasFlagChanged = QtCore.pyqtSignal()

    hasMineChanged = QtCore.pyqtSignal()

    hintChanged = QtCore.pyqtSignal()

    flippedChanged = QtCore.pyqtSignal()

    def __init__(self):
        super(TileData, self).__init__()

        self._hasFlag = False
        self._hasMine = False
        self._hint = -1
        self._flipped = False

    @QtCore.pyqtProperty(bool, notify=hasFlagChanged)
    def hasFlag(self):
        return self._hasFlag

    @hasFlag.setter
    def hasFlag(self, flag):
        if self._hasFlag != flag:
            self._hasFlag = flag
            self.hasFlagChanged.emit()

    @QtCore.pyqtProperty(bool, notify=hasMineChanged)
    def hasMine(self):
        return self._hasMine

    def setHasMine(self, mine):
        if self._hasMine != mine:
            self._hasMine = mine
            self.hasMineChanged.emit()

    @QtCore.pyqtProperty(int, notify=hintChanged)
    def hint(self):
        return self._hint

    def setHint(self, hint):
        if self._hint != hint:
            self._hint = hint
            self.hintChanged.emit()

    @QtCore.pyqtProperty(bool, notify=flippedChanged)
    def flipped(self):
        return self._flipped

    def flip(self):
        if not self._flipped:
            self._flipped = True
            self.flippedChanged.emit()

    def unflip(self):
        if self._flipped:
            self._flipped = False
            self.flippedChanged.emit()


class MinehuntGame(QtCore.QObject):
    isPlayingChanged = QtCore.pyqtSignal()

    hasWonChanged = QtCore.pyqtSignal()

    numMinesChanged = QtCore.pyqtSignal()

    numFlagsChanged = QtCore.pyqtSignal()

    def __init__(self):
        super(MinehuntGame, self).__init__()

        self._numCols = 9
        self._numRows = 9
        self._playing = True
        self._won = False

        self._remaining = 0
        self._nMines = 0
        self._nFlags = 0

        self.setObjectName('mainObject')
        random.seed()

        self._tiles = []
        for ii in range(self._numRows * self._numCols):
            self._tiles.append(TileData())

        self.reset()

    @QtCore.pyqtProperty(QtDeclarative.QPyDeclarativeListProperty, constant=True)
    def tiles(self):
        return QtDeclarative.QPyDeclarativeListProperty(self, self._tiles)

    @QtCore.pyqtProperty(bool, notify=isPlayingChanged)
    def isPlaying(self):
        return self._playing

    @QtCore.pyqtProperty(bool, notify=hasWonChanged)
    def hasWon(self):
        return self._won

    @QtCore.pyqtProperty(int, notify=numMinesChanged)
    def numMines(self):
        return self._nMines

    @QtCore.pyqtProperty(int, notify=numFlagsChanged)
    def numFlags(self):
        return self._nFlags

    @QtCore.pyqtSlot(int, int)
    def flip(self, row, col):
        if not self._playing:
            return False

        t = self._tile(row, col)
        if t is None or t.hasFlag:
            return False

        if t.flipped:
            flags = 0

            for c in (col - 1, col, col + 1):
                for r in (row - 1, row, row + 1):
                    nearT = self._tile(r, c)
                    if nearT is None or nearT is t:
                        continue

                    if nearT.hasFlag:
                        flags += 1

            if t.hint == 0 or t.hint != flags:
                return False

            for c in (col - 1, col, col + 1):
                for r in (row - 1, row, row + 1):
                    nearT = self._tile(r, c)
                    if nearT is not None and not nearT.flipped and not nearT.hasFlag:
                        self.flip(r, c)

            return True

        t.flip()

        if t.hint == 0:
            for c in (col - 1, col, col + 1):
                for r in (row - 1, row, row + 1):
                    nearT = self._tile(r, c)
                    if nearT is not None and not nearT.flipped:
                        self.flip(r, c)

        if t.hasMine:
            # Flip all other mines.
            for r in range(self._numRows):
                for c in range(self._numCols):
                    t = self._tile(r, c)
                    if t is not None and t.hasMine:
                        self.flip(r, c)

            self._won = False
            self.hasWonChanged.emit()
            self._setPlaying(False)

        self._remaining -= 1
        if self._remaining == 0:
            self._won = True
            self.hasWonChanged.emit()
            self._setPlaying(False)

        return True

    @QtCore.pyqtSlot(int, int)
    def flag(self, row, col):
        t = self._tile(row, col)
        if t is None:
            return False

        t.hasFlag = not t.hasFlag
        if t.hasFlag:
            self._nFlags += 1
        else:
            self._nFlags -= 1

        self.numFlagsChanged.emit()

        return True

    @QtCore.pyqtSlot()
    def setBoard(self):
        for t in self._tiles:
            t.setHasMine(False)
            t.setHint(-1)

        # Place the mines.
        mines = self._nMines;
        self._remaining = self._numRows * self._numCols - mines
        while mines > 0:
            col = random.randint(0, self._numCols - 1)
            row = random.randint(0, self._numRows - 1)

            t = self._tile(row, col)
            if t is not None and not t.hasMine:
                t.setHasMine(True)
                mines -= 1

        # Set the hints.
        for row in range(self._numRows):
            for col in range(self._numCols):
                t = self._tile(row, col)
                if t is not None and not t.hasMine:
                    t.setHint(self._getHint(row, col))

        self._setPlaying(True)

    @QtCore.pyqtSlot()
    def reset(self):
        for t in self._tiles:
            t.unflip()
            t.hasFlag = False

        self._nMines = 12
        self._nFlags = 0
        self.numMinesChanged.emit()
        self.numFlagsChanged.emit()
        self._setPlaying(False)
        QtCore.QTimer.singleShot(600, self.setBoard)

    def _onBoard(self, row, col):
        return (row >= 0 and row < self._numRows and col >= 0 and col < self._numCols)

    def _tile(self, row, col):
        if self._onBoard(row, col):
            return self._tiles[col + self._numRows * row]

        return None

    def _getHint(self, row, col):
        hint = 0

        for c in (col - 1, col, col + 1):
            for r in (row - 1, row, row + 1):
                t = self._tile(r, c)
                if t is not None and t.hasMine:
                    hint += 1

        return hint

    def _setPlaying(self, playing):
        if self._playing != playing:
            self._playing = playing
            self.isPlayingChanged.emit()


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    canvas = QtDeclarative.QDeclarativeView()
    engine = canvas.engine()

    game = MinehuntGame()

    engine.rootContext().setContextObject(game)
    canvas.setSource(QtCore.QUrl.fromLocalFile('minehunt.qml'))
    engine.quit.connect(app.quit)

    canvas.setGeometry(QtCore.QRect(100, 100, 450, 450))
    canvas.show()

    sys.exit(app.exec_())
