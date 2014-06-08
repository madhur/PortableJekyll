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

import sys

from PyQt4 import QtCore, QtGui

try:
    from PyQt4.phonon import Phonon
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "Phonon Capabilities",
            "Your Qt installation does not have Phonon support.",
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.NoButton)
    sys.exit(1)


class Window(QtGui.QWidget):
    def __init__(self):
        super(QtGui.QWidget, self).__init__()

        self.setupUi()
        self.updateWidgets()

        notifier = Phonon.BackendCapabilities.notifier()
        notifier.capabilitiesChanged.connect(self.updateWidgets)
        notifier.availableAudioOutputDevicesChanged.connect(self.updateWidgets)

    def updateWidgets(self):
        # Output devices.
        devices = Phonon.BackendCapabilities.availableAudioOutputDevices()
        model = Phonon.AudioOutputDeviceModel(devices)
        self.devicesListView.setModel(model)

        # MIME types.
        self.mimeListWidget.clear()

        for mimeType in Phonon.BackendCapabilities.availableMimeTypes():
            item = QtGui.QListWidgetItem(self.mimeListWidget)
            item.setText(mimeType)

        # Effects.
        self.effectsTreeWidget.clear()

        for effect in Phonon.BackendCapabilities.availableAudioEffects():
            item = QtGui.QTreeWidgetItem(self.effectsTreeWidget)
            item.setText(0, "Effect")
            item.setText(1, effect.name())
            item.setText(2, effect.description())

            # Effects parameters.
            for parameter in Phonon.Effect(effect, self).parameters():
                defaultValue = parameter.defaultValue()
                minimumValue = parameter.minimumValue()
                maximumValue = parameter.maximumValue()

                valueString = "%s / %s / %s" % (defaultValue, minimumValue, maximumValue)

                parameterItem = QtGui.QTreeWidgetItem(item)
                parameterItem.setText(0, "Parameter")
                parameterItem.setText(1, parameter.name())
                parameterItem.setText(2, parameter.description())
                parameterItem.setText(3, QtCore.QVariant.typeToName(parameter.type()))
                parameterItem.setText(4, valueString)

        for i in range(self.effectsTreeWidget.columnCount()):
            if i == 0:
                self.effectsTreeWidget.setColumnWidth(0, 150)
            elif i == 2:
                self.effectsTreeWidget.setColumnWidth(2, 350)
            else:
                self.effectsTreeWidget.resizeColumnToContents(i)

    def setupUi(self):
        self.setupBackendBox()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.backendBox)

        self.setLayout(layout)
        self.setWindowTitle("Backend Capabilities Example")

    def setupBackendBox(self):
        self.devicesLabel = QtGui.QLabel("Available Audio Devices:")
        self.devicesListView = QtGui.QListView()

        self.mimeTypesLabel = QtGui.QLabel("Supported MIME Types:")
        self.mimeListWidget = QtGui.QListWidget()

        self.effectsLabel = QtGui.QLabel("Available Audio Effects:")

        headerLabels = ("Type", "Name", "Description", "Value Type",
                "Default/Min/Max Values")

        self.effectsTreeWidget = QtGui.QTreeWidget()
        self.effectsTreeWidget.setHeaderLabels(headerLabels)
        self.effectsTreeWidget.setColumnCount(5)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.devicesLabel, 0, 0)
        layout.addWidget(self.devicesListView, 1, 0)
        layout.addWidget(self.mimeTypesLabel, 0, 1)
        layout.addWidget(self.mimeListWidget, 1, 1)
        layout.addWidget(self.effectsLabel, 2, 0)
        layout.addWidget(self.effectsTreeWidget, 3, 0, 2, 2)
        layout.setRowStretch(3, 100)

        self.backendBox = QtGui.QGroupBox("Backend Capabilities")
        self.backendBox.setLayout(layout)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Phonon Capabilities Example")

    window = Window()
    window.show()

    sys.exit(app.exec_())
