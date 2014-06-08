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

from PyQt4 import QtCore, QtGui


SUBJECT, SENDER, DATE = range(3)

# Work around the fact that QSortFilterProxyModel always filters datetime
# values in QtCore.Qt.ISODate format, but the tree views display using
# QtCore.Qt.DefaultLocaleShortDate format.
class SortFilterProxyModel(QtGui.QSortFilterProxyModel):
    def filterAcceptsRow(self, sourceRow, sourceParent):
        # Do we filter for the date column?
        if self.filterKeyColumn() == DATE:
            # Fetch datetime value.
            index = self.sourceModel().index(sourceRow, DATE, sourceParent)
            data = self.sourceModel().data(index)

            # Return, if regExp match in displayed format.
            return (self.filterRegExp().indexIn(data.toString(QtCore.Qt.DefaultLocaleShortDate)) >= 0)

        # Not our business.
        return super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.proxyModel = SortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.sourceGroupBox = QtGui.QGroupBox("Original Model")
        self.proxyGroupBox = QtGui.QGroupBox("Sorted/Filtered Model")

        self.sourceView = QtGui.QTreeView()
        self.sourceView.setRootIsDecorated(False)
        self.sourceView.setAlternatingRowColors(True)

        self.proxyView = QtGui.QTreeView()
        self.proxyView.setRootIsDecorated(False)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)

        self.sortCaseSensitivityCheckBox = QtGui.QCheckBox("Case sensitive sorting")
        self.filterCaseSensitivityCheckBox = QtGui.QCheckBox("Case sensitive filter")

        self.filterPatternLineEdit = QtGui.QLineEdit()
        self.filterPatternLabel = QtGui.QLabel("&Filter pattern:")
        self.filterPatternLabel.setBuddy(self.filterPatternLineEdit)

        self.filterSyntaxComboBox = QtGui.QComboBox()
        self.filterSyntaxComboBox.addItem("Regular expression",
                QtCore.QRegExp.RegExp)
        self.filterSyntaxComboBox.addItem("Wildcard",
                QtCore.QRegExp.Wildcard)
        self.filterSyntaxComboBox.addItem("Fixed string",
                QtCore.QRegExp.FixedString)
        self.filterSyntaxLabel = QtGui.QLabel("Filter &syntax:")
        self.filterSyntaxLabel.setBuddy(self.filterSyntaxComboBox)

        self.filterColumnComboBox = QtGui.QComboBox()
        self.filterColumnComboBox.addItem("Subject")
        self.filterColumnComboBox.addItem("Sender")
        self.filterColumnComboBox.addItem("Date")
        self.filterColumnLabel = QtGui.QLabel("Filter &column:")
        self.filterColumnLabel.setBuddy(self.filterColumnComboBox)

        self.filterPatternLineEdit.textChanged.connect(self.filterRegExpChanged)
        self.filterSyntaxComboBox.currentIndexChanged.connect(self.filterRegExpChanged)
        self.filterColumnComboBox.currentIndexChanged.connect(self.filterColumnChanged)
        self.filterCaseSensitivityCheckBox.toggled.connect(self.filterRegExpChanged)
        self.sortCaseSensitivityCheckBox.toggled.connect(self.sortChanged)

        sourceLayout = QtGui.QHBoxLayout()
        sourceLayout.addWidget(self.sourceView)
        self.sourceGroupBox.setLayout(sourceLayout)

        proxyLayout = QtGui.QGridLayout()
        proxyLayout.addWidget(self.proxyView, 0, 0, 1, 3)
        proxyLayout.addWidget(self.filterPatternLabel, 1, 0)
        proxyLayout.addWidget(self.filterPatternLineEdit, 1, 1, 1, 2)
        proxyLayout.addWidget(self.filterSyntaxLabel, 2, 0)
        proxyLayout.addWidget(self.filterSyntaxComboBox, 2, 1, 1, 2)
        proxyLayout.addWidget(self.filterColumnLabel, 3, 0)
        proxyLayout.addWidget(self.filterColumnComboBox, 3, 1, 1, 2)
        proxyLayout.addWidget(self.filterCaseSensitivityCheckBox, 4, 0, 1, 2)
        proxyLayout.addWidget(self.sortCaseSensitivityCheckBox, 4, 2)
        self.proxyGroupBox.setLayout(proxyLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.sourceGroupBox)
        mainLayout.addWidget(self.proxyGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Basic Sort/Filter Model")
        self.resize(500, 450)

        self.proxyView.sortByColumn(SENDER, QtCore.Qt.AscendingOrder)
        self.filterColumnComboBox.setCurrentIndex(SENDER)

        self.filterPatternLineEdit.setText("Andy|Grace")
        self.filterCaseSensitivityCheckBox.setChecked(True)
        self.sortCaseSensitivityCheckBox.setChecked(True)

    def setSourceModel(self, model):
        self.proxyModel.setSourceModel(model)
        self.sourceView.setModel(model)

    def filterRegExpChanged(self):
        syntax_nr = self.filterSyntaxComboBox.itemData(self.filterSyntaxComboBox.currentIndex())
        syntax = QtCore.QRegExp.PatternSyntax(syntax_nr)

        if self.filterCaseSensitivityCheckBox.isChecked():
            caseSensitivity = QtCore.Qt.CaseSensitive
        else:
            caseSensitivity = QtCore.Qt.CaseInsensitive

        regExp = QtCore.QRegExp(self.filterPatternLineEdit.text(),
                caseSensitivity, syntax)
        self.proxyModel.setFilterRegExp(regExp)

    def filterColumnChanged(self):
        self.proxyModel.setFilterKeyColumn(self.filterColumnComboBox.currentIndex())

    def sortChanged(self):
        if self.sortCaseSensitivityCheckBox.isChecked():
            caseSensitivity = QtCore.Qt.CaseSensitive
        else:
            caseSensitivity = QtCore.Qt.CaseInsensitive

        self.proxyModel.setSortCaseSensitivity(caseSensitivity)


def addMail(model, subject, sender, date):
    model.insertRow(0)
    model.setData(model.index(0, SUBJECT), subject)
    model.setData(model.index(0, SENDER), sender)
    model.setData(model.index(0, DATE), date)


def createMailModel(parent):
    model = QtGui.QStandardItemModel(0, 3, parent)

    model.setHeaderData(SUBJECT, QtCore.Qt.Horizontal, "Subject")
    model.setHeaderData(SENDER, QtCore.Qt.Horizontal, "Sender")
    model.setHeaderData(DATE, QtCore.Qt.Horizontal, "Date")

    addMail(model, "Happy New Year!", "Grace K. <grace@software-inc.com>",
            QtCore.QDateTime(QtCore.QDate(2006, 12, 31), QtCore.QTime(17, 3)))
    addMail(model, "Radically new concept", "Grace K. <grace@software-inc.com>",
            QtCore.QDateTime(QtCore.QDate(2006, 12, 22), QtCore.QTime(9, 44)))
    addMail(model, "Accounts", "pascale@nospam.com",
            QtCore.QDateTime(QtCore.QDate(2006, 12, 31), QtCore.QTime(12, 50)))
    addMail(model, "Expenses", "Joe Bloggs <joe@bloggs.com>",
            QtCore.QDateTime(QtCore.QDate(2006, 12, 25), QtCore.QTime(11, 39)))
    addMail(model, "Re: Expenses", "Andy <andy@nospam.com>",
            QtCore.QDateTime(QtCore.QDate(2007, 1, 2), QtCore.QTime(16, 5)))
    addMail(model, "Re: Accounts", "Joe Bloggs <joe@bloggs.com>",
            QtCore.QDateTime(QtCore.QDate(2007, 1, 3), QtCore.QTime(14, 18)))
    addMail(model, "Re: Accounts", "Andy <andy@nospam.com>",
            QtCore.QDateTime(QtCore.QDate(2007, 1, 3), QtCore.QTime(14, 26)))
    addMail(model, "Sports", "Linda Smith <linda.smith@nospam.com>",
            QtCore.QDateTime(QtCore.QDate(2007, 1, 5), QtCore.QTime(11, 33)))
    addMail(model, "AW: Sports", "Rolf Newschweinstein <rolfn@nospam.com>",
            QtCore.QDateTime(QtCore.QDate(2007, 1, 5), QtCore.QTime(12, 0)))
    addMail(model, "RE: Sports", "Petra Schmidt <petras@nospam.com>",
            QtCore.QDateTime(QtCore.QDate(2007, 1, 5), QtCore.QTime(12, 1)))

    return model


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.setSourceModel(createMailModel(window))
    window.show()
    sys.exit(app.exec_())
