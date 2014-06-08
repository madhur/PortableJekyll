#!/usr/bin/env python

#============================================================================#
# (Re)Implementation of QDateEdit and QDateTimeEdit. These classes force the #
# use of the calendar popup.                                                 #
#----------------------------------------------------------------------------#
# Copyright (c) 2008 by Denviso GmbH, <ulrich.berning@denviso.de>            #
#                                                                            #
# All Rights Reserved                                                        #
#                                                                            #
# Permission to use, copy, modify, and distribute this software and its      #
# documentation for any purpose and without fee is hereby granted,           #
# provided that the above copyright notice appear in all copies and that     #
# both that copyright notice and this permission notice appear in            #
# supporting documentation.                                                  #
#                                                                            #
# DENVISO DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS                       #
# SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY              #
# AND FITNESS, IN NO EVENT SHALL DENVISO BE LIABLE FOR ANY                   #
# SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES                  #
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,                    #
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER                      #
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE              #
# OR PERFORMANCE OF THIS SOFTWARE.                                           #
#----------------------------------------------------------------------------#
from PyQt4 import QtCore, QtGui


#============================================================================#
# PyDateEdit                                                                 #
#----------------------------------------------------------------------------#
class PyDateEdit(QtGui.QDateEdit):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    def __init__(self, *args):
        super(PyDateEdit, self).__init__(*args)

        self.setCalendarPopup(True)
        self.__cw = None
        self.__firstDayOfWeek = QtCore.Qt.Monday
        self.__gridVisible = False
        self.__horizontalHeaderFormat = QtGui.QCalendarWidget.ShortDayNames
        self.__verticalHeaderFormat = QtGui.QCalendarWidget.ISOWeekNumbers
        self.__navigationBarVisible = True

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    def mousePressEvent(self, event):
        super(PyDateEdit, self).mousePressEvent(event)

        if not self.__cw:
            self.__cw = self.findChild(QtGui.QCalendarWidget)
            if self.__cw:
                self.__cw.setFirstDayOfWeek(self.__firstDayOfWeek)
                self.__cw.setGridVisible(self.__gridVisible)
                self.__cw.setHorizontalHeaderFormat(self.__horizontalHeaderFormat)
                self.__cw.setVerticalHeaderFormat(self.__verticalHeaderFormat)
                self.__cw.setNavigationBarVisible(self.__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    def getCalendarPopup(self):
        return True
    calendarPopup = QtCore.pyqtProperty(bool, fget=getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    def getFirstDayOfWeek(self):
        return self.__firstDayOfWeek
    def setFirstDayOfWeek(self, dayOfWeek):
        if dayOfWeek != self.__firstDayOfWeek:
            self.__firstDayOfWeek = dayOfWeek
            if self.__cw:
                self.__cw.setFirstDayOfWeek(dayOfWeek)
    def resetFirstDayOfWeek(self):
        if self.__firstDayOfWeek != QtCore.Qt.Monday:
            self.__firstDayOfWeek = QtCore.Qt.Monday
            if self.__cw:
                self.__cw.setFirstDayOfWeek(QtCore.Qt.Monday)
    firstDayOfWeek = QtCore.pyqtProperty(QtCore.Qt.DayOfWeek,
                                         fget=getFirstDayOfWeek,
                                         fset=setFirstDayOfWeek,
                                         freset=resetFirstDayOfWeek)

    #
    # Property gridVisible: bool
    # Get: isGridVisible()
    # Set: setGridVisible()
    # Reset: resetGridVisible()
    #
    def isGridVisible(self):
        return self.__gridVisible
    def setGridVisible(self, show):
        if show != self.__gridVisible:
            self.__gridVisible = show
            if self.__cw:
                self.__cw.setGridVisible(show)
    def resetGridVisible(self):
        if self.__gridVisible != False:
            self.__gridVisible = False
            if self.__cw:
                self.__cw.setGridVisible(False)
    gridVisible = QtCore.pyqtProperty(bool,
                                      fget=isGridVisible,
                                      fset=setGridVisible,
                                      freset=resetGridVisible)

    #
    # Property horizontalHeaderFormat: QCalendarWidget::HorizontalHeaderFormat
    # Get: getHorizontalHeaderFormat()
    # Set: setHorizontalHeaderFormat()
    # Reset: resetHorizontalHeaderFormat()
    #
    def getHorizontalHeaderFormat(self):
        return self.__horizontalHeaderFormat
    def setHorizontalHeaderFormat(self, format):
        if format != self.__horizontalHeaderFormat:
            self.__horizontalHeaderFormat = format
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(format)
    def resetHorizontalHeaderFormat(self):
        if self.__horizontalHeaderFormat != QtGui.QCalendarWidget.ShortDayNames:
            self.__horizontalHeaderFormat = QtGui.QCalendarWidget.ShortDayNames
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(QtGui.QCalendarWidget.ShortDayNames)
    horizontalHeaderFormat = QtCore.pyqtProperty(QtGui.QCalendarWidget.HorizontalHeaderFormat,
                                                 fget=getHorizontalHeaderFormat,
                                                 fset=setHorizontalHeaderFormat,
                                                 freset=resetHorizontalHeaderFormat)

    #
    # Property verticalHeaderFormat: QCalendarWidget::VerticalHeaderFormat
    # Get: getVerticalHeaderFormat()
    # Set: setVerticalHeaderFormat()
    # Reset: resetVerticalHeaderFormat()
    #
    def getVerticalHeaderFormat(self):
        return self.__verticalHeaderFormat
    def setVerticalHeaderFormat(self, format):
        if format != self.__verticalHeaderFormat:
            self.__verticalHeaderFormat = format
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(format)
    def resetVerticalHeaderFormat(self):
        if self.__verticalHeaderFormat != QtGui.QCalendarWidget.ISOWeekNumbers:
            self.__verticalHeaderFormat = QtGui.QCalendarWidget.ISOWeekNumbers
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(QtGui.QCalendarWidget.ISOWeekNumbers)
    verticalHeaderFormat = QtCore.pyqtProperty(QtGui.QCalendarWidget.VerticalHeaderFormat,
                                               fget=getVerticalHeaderFormat,
                                               fset=setVerticalHeaderFormat,
                                               freset=resetVerticalHeaderFormat)

    #
    # Property navigationBarVisible: bool
    # Get: isNavigationBarVisible()
    # Set: setNavigationBarVisible()
    # Reset: resetNavigationBarVisible()
    #
    def isNavigationBarVisible(self):
        return self.__navigationBarVisible
    def setNavigationBarVisible(self, visible):
        if visible != self.__navigationBarVisible:
            self.__navigationBarVisible = visible
            if self.__cw:
                self.__cw.setNavigationBarVisible(visble)
    def resetNavigationBarVisible(self):
        if self.__navigationBarVisible != True:
            self.__navigationBarVisible = True
            if self.__cw:
                self.__cw.setNavigationBarVisible(True)
    navigationBarVisible = QtCore.pyqtProperty(bool,
                                               fget=isNavigationBarVisible,
                                               fset=setNavigationBarVisible,
                                               freset=resetNavigationBarVisible)


#============================================================================#
# PyDateTimeEdit                                                             #
#----------------------------------------------------------------------------#
class PyDateTimeEdit(QtGui.QDateTimeEdit):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    def __init__(self, *args):
        super(PyDateTimeEdit, self).__init__(*args)

        self.setCalendarPopup(True)
        self.__cw = None
        self.__firstDayOfWeek = QtCore.Qt.Monday
        self.__gridVisible = False
        self.__horizontalHeaderFormat = QtGui.QCalendarWidget.ShortDayNames
        self.__verticalHeaderFormat = QtGui.QCalendarWidget.ISOWeekNumbers
        self.__navigationBarVisible = True

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    def mousePressEvent(self, event):
        super(PyDateTimeEdit, self).mousePressEvent(event)

        if not self.__cw:
            self.__cw = self.findChild(QtGui.QCalendarWidget)
            if self.__cw:
                self.__cw.setFirstDayOfWeek(self.__firstDayOfWeek)
                self.__cw.setGridVisible(self.__gridVisible)
                self.__cw.setHorizontalHeaderFormat(self.__horizontalHeaderFormat)
                self.__cw.setVerticalHeaderFormat(self.__verticalHeaderFormat)
                self.__cw.setNavigationBarVisible(self.__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    def getCalendarPopup(self):
        return True
    calendarPopup = QtCore.pyqtProperty(bool, fget=getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    def getFirstDayOfWeek(self):
        return self.__firstDayOfWeek
    def setFirstDayOfWeek(self, dayOfWeek):
        if dayOfWeek != self.__firstDayOfWeek:
            self.__firstDayOfWeek = dayOfWeek
            if self.__cw:
                self.__cw.setFirstDayOfWeek(dayOfWeek)
    def resetFirstDayOfWeek(self):
        if self.__firstDayOfWeek != QtCore.Qt.Monday:
            self.__firstDayOfWeek = QtCore.Qt.Monday
            if self.__cw:
                self.__cw.setFirstDayOfWeek(QtCore.Qt.Monday)
    firstDayOfWeek = QtCore.pyqtProperty(QtCore.Qt.DayOfWeek,
                                         fget=getFirstDayOfWeek,
                                         fset=setFirstDayOfWeek,
                                         freset=resetFirstDayOfWeek)

    #
    # Property gridVisible: bool
    # Get: isGridVisible()
    # Set: setGridVisible()
    # Reset: resetGridVisible()
    #
    def isGridVisible(self):
        return self.__gridVisible
    def setGridVisible(self, show):
        if show != self.__gridVisible:
            self.__gridVisible = show
            if self.__cw:
                self.__cw.setGridVisible(show)
    def resetGridVisible(self):
        if self.__gridVisible != False:
            self.__gridVisible = False
            if self.__cw:
                self.__cw.setGridVisible(False)
    gridVisible = QtCore.pyqtProperty(bool,
                                      fget=isGridVisible,
                                      fset=setGridVisible,
                                      freset=resetGridVisible)

    #
    # Property horizontalHeaderFormat: QCalendarWidget::HorizontalHeaderFormat
    # Get: getHorizontalHeaderFormat()
    # Set: setHorizontalHeaderFormat()
    # Reset: resetHorizontalHeaderFormat()
    #
    def getHorizontalHeaderFormat(self):
        return self.__horizontalHeaderFormat
    def setHorizontalHeaderFormat(self, format):
        if format != self.__horizontalHeaderFormat:
            self.__horizontalHeaderFormat = format
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(format)
    def resetHorizontalHeaderFormat(self):
        if self.__horizontalHeaderFormat != QtGui.QCalendarWidget.ShortDayNames:
            self.__horizontalHeaderFormat = QtGui.QCalendarWidget.ShortDayNames
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(QtGui.QCalendarWidget.ShortDayNames)
    horizontalHeaderFormat = QtCore.pyqtProperty(QtGui.QCalendarWidget.HorizontalHeaderFormat,
                                                 fget=getHorizontalHeaderFormat,
                                                 fset=setHorizontalHeaderFormat,
                                                 freset=resetHorizontalHeaderFormat)

    #
    # Property verticalHeaderFormat: QCalendarWidget::VerticalHeaderFormat
    # Get: getVerticalHeaderFormat()
    # Set: setVerticalHeaderFormat()
    # Reset: resetVerticalHeaderFormat()
    #
    def getVerticalHeaderFormat(self):
        return self.__verticalHeaderFormat
    def setVerticalHeaderFormat(self, format):
        if format != self.__verticalHeaderFormat:
            self.__verticalHeaderFormat = format
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(format)
    def resetVerticalHeaderFormat(self):
        if self.__verticalHeaderFormat != QtGui.QCalendarWidget.ISOWeekNumbers:
            self.__verticalHeaderFormat = QtGui.QCalendarWidget.ISOWeekNumbers
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(QtGui.QCalendarWidget.ISOWeekNumbers)
    verticalHeaderFormat = QtCore.pyqtProperty(QtGui.QCalendarWidget.VerticalHeaderFormat,
                                               fget=getVerticalHeaderFormat,
                                               fset=setVerticalHeaderFormat,
                                               freset=resetVerticalHeaderFormat)

    #
    # Property navigationBarVisible: bool
    # Get: isNavigationBarVisible()
    # Set: setNavigationBarVisible()
    # Reset: resetNavigationBarVisible()
    #
    def isNavigationBarVisible(self):
        return self.__navigationBarVisible
    def setNavigationBarVisible(self, visible):
        if visible != self.__navigationBarVisible:
            self.__navigationBarVisible = visible
            if self.__cw:
                self.__cw.setNavigationBarVisible(visble)
    def resetNavigationBarVisible(self):
        if self.__navigationBarVisible != True:
            self.__navigationBarVisible = True
            if self.__cw:
                self.__cw.setNavigationBarVisible(True)
    navigationBarVisible = QtCore.pyqtProperty(bool,
                                               fget=isNavigationBarVisible,
                                               fset=setNavigationBarVisible,
                                               freset=resetNavigationBarVisible)


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    lay = QtGui.QHBoxLayout()

    lay.addWidget(PyDateEdit())
    lay.addWidget(PyDateTimeEdit())

    w.setLayout(lay)
    w.show()

    sys.exit(app.exec_())

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
