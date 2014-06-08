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
###########################################################################


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.createPreviewGroupBox()
        self.createGeneralOptionsGroupBox()
        self.createDatesGroupBox()
        self.createTextFormatsGroupBox()

        layout = QtGui.QGridLayout()
        layout.addWidget(self.previewGroupBox, 0, 0)
        layout.addWidget(self.generalOptionsGroupBox, 0, 1)
        layout.addWidget(self.datesGroupBox, 1, 0)
        layout.addWidget(self.textFormatsGroupBox, 1, 1)
        layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.setLayout(layout)

        self.previewLayout.setRowMinimumHeight(0,
                self.calendar.sizeHint().height())
        self.previewLayout.setColumnMinimumWidth(0,
                self.calendar.sizeHint().width())

        self.setWindowTitle("Calendar Widget")

    def localeChanged(self, index):
        self.calendar.setLocale(self.localeCombo.itemData(index))

    def firstDayChanged(self, index):
        self.calendar.setFirstDayOfWeek(
                QtCore.Qt.DayOfWeek(self.firstDayCombo.itemData(index)))

    def selectionModeChanged(self, index):
        self.calendar.setSelectionMode(
                QtGui.QCalendarWidget.SelectionMode(
                        self.selectionModeCombo.itemData(index)))

    def horizontalHeaderChanged(self, index):
        self.calendar.setHorizontalHeaderFormat(
                QtGui.QCalendarWidget.HorizontalHeaderFormat(
                        self.horizontalHeaderCombo.itemData(index)))

    def verticalHeaderChanged(self, index):
        self.calendar.setVerticalHeaderFormat(
                QtGui.QCalendarWidget.VerticalHeaderFormat(
                        self.verticalHeaderCombo.itemData(index)))

    def selectedDateChanged(self):
        self.currentDateEdit.setDate(self.calendar.selectedDate())

    def minimumDateChanged(self, date):
        self.calendar.setMinimumDate(date)
        self.maximumDateEdit.setDate(self.calendar.maximumDate())

    def maximumDateChanged(self, date):
        self.calendar.setMaximumDate(date)
        self.minimumDateEdit.setDate(self.calendar.minimumDate())

    def weekdayFormatChanged(self):
        format = QtGui.QTextCharFormat()
        format.setForeground(
                QtCore.Qt.GlobalColor(
                        self.weekdayColorCombo.itemData(
                                self.weekdayColorCombo.currentIndex())))

        self.calendar.setWeekdayTextFormat(QtCore.Qt.Monday, format)
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Tuesday, format)
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Wednesday, format)
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Thursday, format)
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Friday, format)

    def weekendFormatChanged(self):
        format = QtGui.QTextCharFormat()
        format.setForeground(
                QtCore.Qt.GlobalColor(
                        self.weekendColorCombo.itemData(
                                self.weekendColorCombo.currentIndex())))

        self.calendar.setWeekdayTextFormat(QtCore.Qt.Saturday, format)
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Sunday, format)

    def reformatHeaders(self):
        text = self.headerTextFormatCombo.currentText()
        format = QtGui.QTextCharFormat()

        if text == "Bold":
            format.setFontWeight(QtGui.QFont.Bold)
        elif text == "Italic":
            format.setFontItalic(True)
        elif text == "Green":
            format.setForeground(QtCore.Qt.green)

        self.calendar.setHeaderTextFormat(format)

    def reformatCalendarPage(self):
        if self.firstFridayCheckBox.isChecked():
            firstFriday = QtCore.QDate(self.calendar.yearShown(),
                    self.calendar.monthShown(), 1)

            while firstFriday.dayOfWeek() != QtCore.Qt.Friday:
                firstFriday = firstFriday.addDays(1)

            firstFridayFormat = QtGui.QTextCharFormat()
            firstFridayFormat.setForeground(QtCore.Qt.blue)

            self.calendar.setDateTextFormat(firstFriday, firstFridayFormat)

        # May 1st in Red takes precedence.
        if self.mayFirstCheckBox.isChecked():
            mayFirst = QtCore.QDate(self.calendar.yearShown(), 5, 1)

            mayFirstFormat = QtGui.QTextCharFormat()
            mayFirstFormat.setForeground(QtCore.Qt.red)

            self.calendar.setDateTextFormat(mayFirst, mayFirstFormat)

    def createPreviewGroupBox(self):
        self.previewGroupBox = QtGui.QGroupBox("Preview")

        self.calendar = QtGui.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QtCore.QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.currentPageChanged.connect(self.reformatCalendarPage)

        self.previewLayout = QtGui.QGridLayout()
        self.previewLayout.addWidget(self.calendar, 0, 0,
                QtCore.Qt.AlignCenter)
        self.previewGroupBox.setLayout(self.previewLayout)
 
    def createGeneralOptionsGroupBox(self):
        self.generalOptionsGroupBox = QtGui.QGroupBox("General Options")

        self.localeCombo = QtGui.QComboBox()

        curLocaleIndex = -1
        index = 0

        for lid in range(QtCore.QLocale.C, QtCore.QLocale.LastLanguage + 1):
            lang = QtCore.QLocale.Language(lid)
            countries = QtCore.QLocale.countriesForLanguage(lang)
            for country in countries:
                label = "%s/%s" % (QtCore.QLocale.languageToString(lang),
                                   QtCore.QLocale.countryToString(country))
                locale = QtCore.QLocale(lang, country)
                if self.locale().language() == lang and self.locale().country() == country:
                    curLocaleIndex = index

                self.localeCombo.addItem(label, locale)
                index += 1

        if curLocaleIndex != -1:
            self.localeCombo.setCurrentIndex(curLocaleIndex)

        self.localeLabel = QtGui.QLabel("&Locale")
        self.localeLabel.setBuddy(self.localeCombo)

        self.firstDayCombo = QtGui.QComboBox()
        self.firstDayCombo.addItem("Sunday", QtCore.Qt.Sunday)
        self.firstDayCombo.addItem("Monday", QtCore.Qt.Monday)
        self.firstDayCombo.addItem("Tuesday", QtCore.Qt.Tuesday)
        self.firstDayCombo.addItem("Wednesday", QtCore.Qt.Wednesday)
        self.firstDayCombo.addItem("Thursday", QtCore.Qt.Thursday)
        self.firstDayCombo.addItem("Friday", QtCore.Qt.Friday)
        self.firstDayCombo.addItem("Saturday", QtCore.Qt.Saturday)

        self.firstDayLabel = QtGui.QLabel("Wee&k starts on:")
        self.firstDayLabel.setBuddy(self.firstDayCombo)

        self.selectionModeCombo = QtGui.QComboBox()
        self.selectionModeCombo.addItem("Single selection",
                QtGui.QCalendarWidget.SingleSelection)
        self.selectionModeCombo.addItem("None",
                QtGui.QCalendarWidget.NoSelection)
        self.selectionModeLabel = QtGui.QLabel("&Selection mode:")
        self.selectionModeLabel.setBuddy(self.selectionModeCombo)

        self.gridCheckBox = QtGui.QCheckBox("&Grid")
        self.gridCheckBox.setChecked(self.calendar.isGridVisible())

        self.navigationCheckBox = QtGui.QCheckBox("&Navigation bar")
        self.navigationCheckBox.setChecked(True)

        self.horizontalHeaderCombo = QtGui.QComboBox()
        self.horizontalHeaderCombo.addItem("Single letter day names",
                QtGui.QCalendarWidget.SingleLetterDayNames)
        self.horizontalHeaderCombo.addItem("Short day names",
                QtGui.QCalendarWidget.ShortDayNames)
        self.horizontalHeaderCombo.addItem("Long day names",
                QtGui.QCalendarWidget.LongDayNames)
        self.horizontalHeaderCombo.addItem("None",
                QtGui.QCalendarWidget.NoHorizontalHeader)
        self.horizontalHeaderCombo.setCurrentIndex(1)

        self.horizontalHeaderLabel = QtGui.QLabel("&Horizontal header:")
        self.horizontalHeaderLabel.setBuddy(self.horizontalHeaderCombo)

        self.verticalHeaderCombo = QtGui.QComboBox()
        self.verticalHeaderCombo.addItem("ISO week numbers",
                QtGui.QCalendarWidget.ISOWeekNumbers)
        self.verticalHeaderCombo.addItem("None",
                QtGui.QCalendarWidget.NoVerticalHeader)

        self.verticalHeaderLabel = QtGui.QLabel("&Vertical header:")
        self.verticalHeaderLabel.setBuddy(self.verticalHeaderCombo)

        self.localeCombo.currentIndexChanged.connect(self.localeChanged)
        self.firstDayCombo.currentIndexChanged.connect(self.firstDayChanged)
        self.selectionModeCombo.currentIndexChanged.connect(
                self.selectionModeChanged)
        self.gridCheckBox.toggled.connect(self.calendar.setGridVisible)
        self.navigationCheckBox.toggled.connect(
                self.calendar.setNavigationBarVisible)
        self.horizontalHeaderCombo.currentIndexChanged.connect(
                self.horizontalHeaderChanged)
        self.verticalHeaderCombo.currentIndexChanged.connect(
                self.verticalHeaderChanged)

        checkBoxLayout = QtGui.QHBoxLayout()
        checkBoxLayout.addWidget(self.gridCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.addWidget(self.navigationCheckBox)

        outerLayout = QtGui.QGridLayout()
        outerLayout.addWidget(self.localeLabel, 0, 0)
        outerLayout.addWidget(self.localeCombo, 0, 1)
        outerLayout.addWidget(self.firstDayLabel, 1, 0)
        outerLayout.addWidget(self.firstDayCombo, 1, 1)
        outerLayout.addWidget(self.selectionModeLabel, 2, 0)
        outerLayout.addWidget(self.selectionModeCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        outerLayout.addWidget(self.horizontalHeaderLabel, 4, 0)
        outerLayout.addWidget(self.horizontalHeaderCombo, 4, 1)
        outerLayout.addWidget(self.verticalHeaderLabel, 5, 0)
        outerLayout.addWidget(self.verticalHeaderCombo, 5, 1)
        self.generalOptionsGroupBox.setLayout(outerLayout)

        self.firstDayChanged(self.firstDayCombo.currentIndex())
        self.selectionModeChanged(self.selectionModeCombo.currentIndex())
        self.horizontalHeaderChanged(self.horizontalHeaderCombo.currentIndex())
        self.verticalHeaderChanged(self.verticalHeaderCombo.currentIndex())
 
    def createDatesGroupBox(self):
        self.datesGroupBox = QtGui.QGroupBox(self.tr("Dates"))

        self.minimumDateEdit = QtGui.QDateEdit()
        self.minimumDateEdit.setDisplayFormat('MMM d yyyy')
        self.minimumDateEdit.setDateRange(self.calendar.minimumDate(),
                                          self.calendar.maximumDate())
        self.minimumDateEdit.setDate(self.calendar.minimumDate())

        self.minimumDateLabel = QtGui.QLabel("&Minimum Date:")
        self.minimumDateLabel.setBuddy(self.minimumDateEdit)

        self.currentDateEdit = QtGui.QDateEdit()
        self.currentDateEdit.setDisplayFormat('MMM d yyyy')
        self.currentDateEdit.setDate(self.calendar.selectedDate())
        self.currentDateEdit.setDateRange(self.calendar.minimumDate(),
                self.calendar.maximumDate())

        self.currentDateLabel = QtGui.QLabel("&Current Date:")
        self.currentDateLabel.setBuddy(self.currentDateEdit)

        self.maximumDateEdit = QtGui.QDateEdit()
        self.maximumDateEdit.setDisplayFormat('MMM d yyyy')
        self.maximumDateEdit.setDateRange(self.calendar.minimumDate(),
                self.calendar.maximumDate())
        self.maximumDateEdit.setDate(self.calendar.maximumDate())

        self.maximumDateLabel = QtGui.QLabel("Ma&ximum Date:")
        self.maximumDateLabel.setBuddy(self.maximumDateEdit)

        self.currentDateEdit.dateChanged.connect(self.calendar.setSelectedDate)
        self.calendar.selectionChanged.connect(self.selectedDateChanged)
        self.minimumDateEdit.dateChanged.connect(self.minimumDateChanged)
        self.maximumDateEdit.dateChanged.connect(self.maximumDateChanged)
 
        dateBoxLayout = QtGui.QGridLayout()
        dateBoxLayout.addWidget(self.currentDateLabel, 1, 0)
        dateBoxLayout.addWidget(self.currentDateEdit, 1, 1)
        dateBoxLayout.addWidget(self.minimumDateLabel, 0, 0)
        dateBoxLayout.addWidget(self.minimumDateEdit, 0, 1)
        dateBoxLayout.addWidget(self.maximumDateLabel, 2, 0)
        dateBoxLayout.addWidget(self.maximumDateEdit, 2, 1)
        dateBoxLayout.setRowStretch(3, 1)

        self.datesGroupBox.setLayout(dateBoxLayout)

    def createTextFormatsGroupBox(self):
        self.textFormatsGroupBox = QtGui.QGroupBox("Text Formats")

        self.weekdayColorCombo = self.createColorComboBox()
        self.weekdayColorCombo.setCurrentIndex(
                self.weekdayColorCombo.findText("Black"))

        self.weekdayColorLabel = QtGui.QLabel("&Weekday color:")
        self.weekdayColorLabel.setBuddy(self.weekdayColorCombo)

        self.weekendColorCombo = self.createColorComboBox()
        self.weekendColorCombo.setCurrentIndex(
                self.weekendColorCombo.findText("Red"))

        self.weekendColorLabel = QtGui.QLabel("Week&end color:")
        self.weekendColorLabel.setBuddy(self.weekendColorCombo)

        self.headerTextFormatCombo = QtGui.QComboBox()
        self.headerTextFormatCombo.addItem("Bold")
        self.headerTextFormatCombo.addItem("Italic")
        self.headerTextFormatCombo.addItem("Plain")

        self.headerTextFormatLabel = QtGui.QLabel("&Header text:")
        self.headerTextFormatLabel.setBuddy(self.headerTextFormatCombo)

        self.firstFridayCheckBox = QtGui.QCheckBox("&First Friday in blue")

        self.mayFirstCheckBox = QtGui.QCheckBox("May &1 in red")

        self.weekdayColorCombo.currentIndexChanged.connect(
                self.weekdayFormatChanged)
        self.weekendColorCombo.currentIndexChanged.connect(
                self.weekendFormatChanged)
        self.headerTextFormatCombo.currentIndexChanged.connect(
                self.reformatHeaders)
        self.firstFridayCheckBox.toggled.connect(self.reformatCalendarPage)
        self.mayFirstCheckBox.toggled.connect(self.reformatCalendarPage)

        checkBoxLayout = QtGui.QHBoxLayout()
        checkBoxLayout.addWidget(self.firstFridayCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.addWidget(self.mayFirstCheckBox)

        outerLayout = QtGui.QGridLayout()
        outerLayout.addWidget(self.weekdayColorLabel, 0, 0)
        outerLayout.addWidget(self.weekdayColorCombo, 0, 1)
        outerLayout.addWidget(self.weekendColorLabel, 1, 0)
        outerLayout.addWidget(self.weekendColorCombo, 1, 1)
        outerLayout.addWidget(self.headerTextFormatLabel, 2, 0)
        outerLayout.addWidget(self.headerTextFormatCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        self.textFormatsGroupBox.setLayout(outerLayout)

        self.weekdayFormatChanged()
        self.weekendFormatChanged()

        self.reformatHeaders()
        self.reformatCalendarPage()
 
    def createColorComboBox(self):
        comboBox = QtGui.QComboBox()
        comboBox.addItem("Red", QtCore.Qt.red)
        comboBox.addItem("Blue", QtCore.Qt.blue)
        comboBox.addItem("Black", QtCore.Qt.black)
        comboBox.addItem("Magenta", QtCore.Qt.magenta)

        return comboBox


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
