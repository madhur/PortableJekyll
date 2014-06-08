#!/usr/bin/env python

#============================================================================#
# PyQt4 port of the designer/containerextension example from Qt v4.x         #
#----------------------------------------------------------------------------#
from PyQt4 import QtCore, QtGui


#============================================================================#
# Implementation of a MultiPageWidget using a QComboBox and a QStackedWidget #
#----------------------------------------------------------------------------#
class PyMultiPageWidget(QtGui.QWidget):

    currentIndexChanged = QtCore.pyqtSignal(int)

    pageTitleChanged = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(PyMultiPageWidget, self).__init__(parent)

        self.comboBox = QtGui.QComboBox()
        # MAGIC
        # It is important that the combo box has an object name beginning
        # with '__qt__passive_', otherwise, it is inactive in the form editor
        # of the designer and you can't change the current page via the
        # combo box.
        # MAGIC
        self.comboBox.setObjectName('__qt__passive_comboBox')        
        self.stackWidget = QtGui.QStackedWidget()
        self.comboBox.activated.connect(self.setCurrentIndex)
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.stackWidget)
        self.setLayout(self.layout)

    def sizeHint(self):
        return QtCore.QSize(200, 150)

    def count(self):
        return self.stackWidget.count()

    def widget(self, index):
        return self.stackWidget.widget(index)

    @QtCore.pyqtSlot(QtGui.QWidget)
    def addPage(self, page):
        self.insertPage(self.count(), page)

    @QtCore.pyqtSlot(int, QtGui.QWidget)
    def insertPage(self, index, page):
        page.setParent(self.stackWidget)
        self.stackWidget.insertWidget(index, page)
        title = page.windowTitle()
        if title.isEmpty():
            title = QtCore.QCoreApplication.translate('PyMultiPageWidget','Page %1').arg(self.comboBox.count() + 1)
            page.setWindowTitle(title)
        self.comboBox.insertItem(index, title)

    @QtCore.pyqtSlot(int)
    def removePage(self, index):
        widget = self.stackWidget.widget(index)
        self.stackWidget.removeWidget(widget)
        self.comboBox.removeItem(index)

    def getPageTitle(self):
        return self.stackWidget.currentWidget().windowTitle()
    
    @QtCore.pyqtSlot(str)
    def setPageTitle(self, newTitle):
        self.comboBox.setItemText(self.getCurrentIndex(), newTitle)
        self.stackWidget.currentWidget().setWindowTitle(newTitle)
        self.pageTitleChanged.emit(newTitle)

    def getCurrentIndex(self):
        return self.stackWidget.currentIndex()

    @QtCore.pyqtSlot(int)
    def setCurrentIndex(self, index):
        if index != self.getCurrentIndex():
            self.stackWidget.setCurrentIndex(index)
            self.comboBox.setCurrentIndex(index)
            self.currentIndexChanged.emit(index)

    pageTitle = QtCore.pyqtProperty(str, fget=getPageTitle, fset=setPageTitle, stored=False)
    currentIndex = QtCore.pyqtProperty(int, fget=getCurrentIndex, fset=setCurrentIndex)


#============================================================================#
# Main for testing the class                                                 #
#----------------------------------------------------------------------------#
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = PyMultiPageWidget()
    widget.addPage(QtGui.QLabel('This is page #1'))
    widget.addPage(QtGui.QLabel('This is page #2'))
    widget.show()
    sys.exit(app.exec_())

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
