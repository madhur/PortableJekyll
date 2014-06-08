#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
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

import sys

from PyQt4 import QtCore, QtGui

try:
    import textedit_rc3
except ImportError:
    import textedit_rc2


if sys.platform.startswith('darwin'):
    rsrcPath = ":/images/mac"
else:
    rsrcPath = ":/images/win"


class TextEdit(QtGui.QMainWindow):
    def __init__(self, fileName=None, parent=None):
        super(TextEdit, self).__init__(parent)

        self.setWindowIcon(QtGui.QIcon(':/images/logo.png'))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.setupFileActions()
        self.setupEditActions()
        self.setupTextActions()

        helpMenu = QtGui.QMenu("Help", self)
        self.menuBar().addMenu(helpMenu)
        helpMenu.addAction("About", self.about)
        helpMenu.addAction("About &Qt", QtGui.qApp.aboutQt)
 
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.currentCharFormatChanged.connect(
                self.currentCharFormatChanged)
        self.textEdit.cursorPositionChanged.connect(self.cursorPositionChanged)
        self.setCentralWidget(self.textEdit)
        self.textEdit.setFocus()
        self.setCurrentFileName()
        self.fontChanged(self.textEdit.font())
        self.colorChanged(self.textEdit.textColor())
        self.alignmentChanged(self.textEdit.alignment())
        self.textEdit.document().modificationChanged.connect(
                self.actionSave.setEnabled)
        self.textEdit.document().modificationChanged.connect(
                self.setWindowModified)
        self.textEdit.document().undoAvailable.connect(
                self.actionUndo.setEnabled)
        self.textEdit.document().redoAvailable.connect(
                self.actionRedo.setEnabled)
        self.setWindowModified(self.textEdit.document().isModified())
        self.actionSave.setEnabled(self.textEdit.document().isModified())
        self.actionUndo.setEnabled(self.textEdit.document().isUndoAvailable())
        self.actionRedo.setEnabled(self.textEdit.document().isRedoAvailable())
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCut.setEnabled(False)
        self.actionCopy.setEnabled(False)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.textEdit.copyAvailable.connect(self.actionCut.setEnabled)
        self.textEdit.copyAvailable.connect(self.actionCopy.setEnabled)
        QtGui.QApplication.clipboard().dataChanged.connect(
                self.clipboardDataChanged)

        if fileName is None:
            fileName = ':/example.html'

        if not self.load(fileName):
            self.fileNew()

    def closeEvent(self, e):
        if self.maybeSave():
            e.accept()
        else:
            e.ignore()

    def setupFileActions(self):
        tb = QtGui.QToolBar(self)
        tb.setWindowTitle("File Actions")
        self.addToolBar(tb)

        menu = QtGui.QMenu("&File", self)
        self.menuBar().addMenu(menu)

        self.actionNew = QtGui.QAction(
                QtGui.QIcon.fromTheme('document-new',
                        QtGui.QIcon(rsrcPath + '/filenew.png')),
                "&New", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtGui.QKeySequence.New, triggered=self.fileNew)
        tb.addAction(self.actionNew)
        menu.addAction(self.actionNew)

        self.actionOpen = QtGui.QAction(
                QtGui.QIcon.fromTheme('document-open',
                        QtGui.QIcon(rsrcPath + '/fileopen.png')),
                "&Open...", self, shortcut=QtGui.QKeySequence.Open,
                triggered=self.fileOpen)
        tb.addAction(self.actionOpen)
        menu.addAction(self.actionOpen)
        menu.addSeparator()

        self.actionSave = QtGui.QAction(
                QtGui.QIcon.fromTheme('document-save',
                        QtGui.QIcon(rsrcPath + '/filesave.png')),
                "&Save", self, shortcut=QtGui.QKeySequence.Save,
                triggered=self.fileSave, enabled=False)
        tb.addAction(self.actionSave)
        menu.addAction(self.actionSave)

        self.actionSaveAs = QtGui.QAction("Save &As...", self,
                priority=QtGui.QAction.LowPriority,
                shortcut=QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_S,
                triggered=self.fileSaveAs)
        menu.addAction(self.actionSaveAs)
        menu.addSeparator()
 
        self.actionPrint = QtGui.QAction(
                QtGui.QIcon.fromTheme('document-print',
                        QtGui.QIcon(rsrcPath + '/fileprint.png')),
                "&Print...", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtGui.QKeySequence.Print, triggered=self.filePrint)
        tb.addAction(self.actionPrint)
        menu.addAction(self.actionPrint)

        self.actionPrintPreview = QtGui.QAction(
                QtGui.QIcon.fromTheme('fileprint',
                        QtGui.QIcon(rsrcPath + '/fileprint.png')),
                "Print Preview...", self,
                shortcut=QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_P,
                triggered=self.filePrintPreview)
        menu.addAction(self.actionPrintPreview)

        self.actionPrintPdf = QtGui.QAction(
                QtGui.QIcon.fromTheme('exportpdf',
                        QtGui.QIcon(rsrcPath + '/exportpdf.png')),
                "&Export PDF...", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtCore.Qt.CTRL + QtCore.Qt.Key_D,
                triggered=self.filePrintPdf)
        tb.addAction(self.actionPrintPdf)
        menu.addAction(self.actionPrintPdf)
        menu.addSeparator()

        self.actionQuit = QtGui.QAction("&Quit", self,
                shortcut=QtGui.QKeySequence.Quit, triggered=self.close)
        menu.addAction(self.actionQuit)

    def setupEditActions(self):
        tb = QtGui.QToolBar(self)
        tb.setWindowTitle("Edit Actions")
        self.addToolBar(tb)

        menu = QtGui.QMenu("&Edit", self)
        self.menuBar().addMenu(menu)

        self.actionUndo = QtGui.QAction(
                QtGui.QIcon.fromTheme('edit-undo',
                        QtGui.QIcon(rsrcPath + '/editundo.png')),
                "&Undo", self, shortcut=QtGui.QKeySequence.Undo)
        tb.addAction(self.actionUndo)
        menu.addAction(self.actionUndo)

        self.actionRedo = QtGui.QAction(
                QtGui.QIcon.fromTheme('edit-redo',
                        QtGui.QIcon(rsrcPath + '/editredo.png')),
                "&Redo", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtGui.QKeySequence.Redo)
        tb.addAction(self.actionRedo)
        menu.addAction(self.actionRedo)
        menu.addSeparator()

        self.actionCut = QtGui.QAction(
                QtGui.QIcon.fromTheme('edit-cut',
                        QtGui.QIcon(rsrcPath + '/editcut.png')),
                "Cu&t", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtGui.QKeySequence.Cut)
        tb.addAction(self.actionCut)
        menu.addAction(self.actionCut)

        self.actionCopy = QtGui.QAction(
                QtGui.QIcon.fromTheme('edit-copy',
                        QtGui.QIcon(rsrcPath + '/editcopy.png')),
                "&Copy", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtGui.QKeySequence.Copy)
        tb.addAction(self.actionCopy)
        menu.addAction(self.actionCopy)

        self.actionPaste = QtGui.QAction(
                QtGui.QIcon.fromTheme('edit-paste',
                        QtGui.QIcon(rsrcPath + '/editpaste.png')),
                "&Paste", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtGui.QKeySequence.Paste,
                enabled=(len(QtGui.QApplication.clipboard().text()) != 0))
        tb.addAction(self.actionPaste)
        menu.addAction(self.actionPaste)

    def setupTextActions(self):
        tb = QtGui.QToolBar(self)
        tb.setWindowTitle("Format Actions")
        self.addToolBar(tb)

        menu = QtGui.QMenu("F&ormat", self)
        self.menuBar().addMenu(menu)

        self.actionTextBold = QtGui.QAction(
                QtGui.QIcon.fromTheme('format-text-bold',
                        QtGui.QIcon(rsrcPath + '/textbold.png')),
                "&Bold", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtCore.Qt.CTRL + QtCore.Qt.Key_B,
                triggered=self.textBold, checkable=True)
        bold = QtGui.QFont()
        bold.setBold(True)
        self.actionTextBold.setFont(bold)
        tb.addAction(self.actionTextBold)
        menu.addAction(self.actionTextBold)

        self.actionTextItalic = QtGui.QAction(
                QtGui.QIcon.fromTheme('format-text-italic',
                        QtGui.QIcon(rsrcPath + '/textitalic.png')),
                "&Italic", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtCore.Qt.CTRL + QtCore.Qt.Key_I,
                triggered=self.textItalic, checkable=True)
        italic = QtGui.QFont()
        italic.setItalic(True)
        self.actionTextItalic.setFont(italic)
        tb.addAction(self.actionTextItalic)
        menu.addAction(self.actionTextItalic)

        self.actionTextUnderline = QtGui.QAction(
                QtGui.QIcon.fromTheme('format-text-underline',
                        QtGui.QIcon(rsrcPath + '/textunder.png')),
                "&Underline", self, priority=QtGui.QAction.LowPriority,
                shortcut=QtCore.Qt.CTRL + QtCore.Qt.Key_U,
                triggered=self.textUnderline, checkable=True)
        underline = QtGui.QFont()
        underline.setUnderline(True)
        self.actionTextUnderline.setFont(underline)
        tb.addAction(self.actionTextUnderline)
        menu.addAction(self.actionTextUnderline)

        menu.addSeparator()

        grp = QtGui.QActionGroup(self, triggered=self.textAlign)

        # Make sure the alignLeft is always left of the alignRight.
        if QtGui.QApplication.isLeftToRight():
            self.actionAlignLeft = QtGui.QAction(
                    QtGui.QIcon.fromTheme('format-justify-left',
                            QtGui.QIcon(rsrcPath + '/textleft.png')),
                    "&Left", grp)
            self.actionAlignCenter = QtGui.QAction(
                    QtGui.QIcon.fromTheme('format-justify-center',
                            QtGui.QIcon(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            self.actionAlignRight = QtGui.QAction(
                    QtGui.QIcon.fromTheme('format-justify-right',
                            QtGui.QIcon(rsrcPath + '/textright.png')),
                    "&Right", grp)
        else:
            self.actionAlignRight = QtGui.QAction(
                    QtGui.QIcon.fromTheme('format-justify-right',
                            QtGui.QIcon(rsrcPath + '/textright.png')),
                    "&Right", grp)
            self.actionAlignCenter = QtGui.QAction(
                    QtGui.QIcon.fromTheme('format-justify-center',
                            QtGui.QIcon(rsrcPath + '/textcenter.png')),
                    "C&enter", grp)
            self.actionAlignLeft = QtGui.QAction(
                    QtGui.QIcon.fromTheme('format-justify-left',
                            QtGui.QIcon(rsrcPath + '/textleft.png')),
                    "&Left", grp)
 
        self.actionAlignJustify = QtGui.QAction(
                QtGui.QIcon.fromTheme('format-justify-fill',
                        QtGui.QIcon(rsrcPath + '/textjustify.png')),
                "&Justify", grp)

        self.actionAlignLeft.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_L)
        self.actionAlignLeft.setCheckable(True)
        self.actionAlignLeft.setPriority(QtGui.QAction.LowPriority)

        self.actionAlignCenter.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_E)
        self.actionAlignCenter.setCheckable(True)
        self.actionAlignCenter.setPriority(QtGui.QAction.LowPriority)

        self.actionAlignRight.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_R)
        self.actionAlignRight.setCheckable(True)
        self.actionAlignRight.setPriority(QtGui.QAction.LowPriority)

        self.actionAlignJustify.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_J)
        self.actionAlignJustify.setCheckable(True)
        self.actionAlignJustify.setPriority(QtGui.QAction.LowPriority)

        tb.addActions(grp.actions())
        menu.addActions(grp.actions())
        menu.addSeparator()

        pix = QtGui.QPixmap(16, 16)
        pix.fill(QtCore.Qt.black)
        self.actionTextColor = QtGui.QAction(QtGui.QIcon(pix), "&Color...",
                self, triggered=self.textColor)
        tb.addAction(self.actionTextColor)
        menu.addAction(self.actionTextColor)

        tb = QtGui.QToolBar(self)
        tb.setAllowedAreas(
                QtCore.Qt.TopToolBarArea | QtCore.Qt.BottomToolBarArea)
        tb.setWindowTitle("Format Actions")
        self.addToolBarBreak(QtCore.Qt.TopToolBarArea)
        self.addToolBar(tb)

        comboStyle = QtGui.QComboBox(tb)
        tb.addWidget(comboStyle)
        comboStyle.addItem("Standard")
        comboStyle.addItem("Bullet List (Disc)")
        comboStyle.addItem("Bullet List (Circle)")
        comboStyle.addItem("Bullet List (Square)")
        comboStyle.addItem("Ordered List (Decimal)")
        comboStyle.addItem("Ordered List (Alpha lower)")
        comboStyle.addItem("Ordered List (Alpha upper)")
        comboStyle.addItem("Ordered List (Roman lower)")
        comboStyle.addItem("Ordered List (Roman upper)")
        comboStyle.activated.connect(self.textStyle)

        self.comboFont = QtGui.QFontComboBox(tb)
        tb.addWidget(self.comboFont)
        self.comboFont.activated[str].connect(self.textFamily)

        self.comboSize = QtGui.QComboBox(tb)
        self.comboSize.setObjectName("comboSize")
        tb.addWidget(self.comboSize)
        self.comboSize.setEditable(True)

        db = QtGui.QFontDatabase()
        for size in db.standardSizes():
            self.comboSize.addItem("%s" % (size))

        self.comboSize.activated[str].connect(self.textSize)
        self.comboSize.setCurrentIndex(
                self.comboSize.findText(
                        "%s" % (QtGui.QApplication.font().pointSize())))

    def load(self, f):
        if not QtCore.QFile.exists(f):
            return False

        fh = QtCore.QFile(f)
        if not fh.open(QtCore.QFile.ReadOnly):
            return False

        data = fh.readAll()
        codec = QtCore.QTextCodec.codecForHtml(data)
        unistr = codec.toUnicode(data)

        if QtCore.Qt.mightBeRichText(unistr):
            self.textEdit.setHtml(unistr)
        else:
            self.textEdit.setPlainText(unistr)

        self.setCurrentFileName(f)
        return True

    def maybeSave(self):
        if not self.textEdit.document().isModified():
            return True

        if self.fileName.startswith(':/'):
            return True

        ret = QtGui.QMessageBox.warning(self, "Application",
                "The document has been modified.\n"
                "Do you want to save your changes?",
                QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
                        QtGui.QMessageBox.Cancel)

        if ret == QtGui.QMessageBox.Save:
            return self.fileSave()

        if ret == QtGui.QMessageBox.Cancel:
            return False

        return True

    def setCurrentFileName(self, fileName=''):
        self.fileName = fileName
        self.textEdit.document().setModified(False)

        if not fileName:
            shownName = 'untitled.txt'
        else:
            shownName = QtCore.QFileInfo(fileName).fileName()

        self.setWindowTitle(self.tr("%s[*] - %s" % (shownName, "Rich Text")))
        self.setWindowModified(False)

    def fileNew(self):
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFileName()

    def fileOpen(self):
        fn = QtGui.QFileDialog.getOpenFileName(self, "Open File...", None,
                "HTML-Files (*.htm *.html);;All Files (*)")

        if fn:
            self.load(fn)

    def fileSave(self):
        if not self.fileName:
            return self.fileSaveAs()

        writer = QtGui.QTextDocumentWriter(self.fileName)
        success = writer.write(self.textEdit.document())
        if success:
            self.textEdit.document().setModified(False)

        return success

    def fileSaveAs(self):
        fn = QtGui.QFileDialog.getSaveFileName(self, "Save as...", None,
                "ODF files (*.odt);;HTML-Files (*.htm *.html);;All Files (*)")

        if not fn:
            return False

        lfn = fn.lower()
        if not lfn.endswith(('.odt', '.htm', '.html')):
            # The default.
            fn += '.odt'

        self.setCurrentFileName(fn)
        return self.fileSave()

    def filePrint(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        dlg = QtGui.QPrintDialog(printer, self)

        if self.textEdit.textCursor().hasSelection():
            dlg.addEnabledOption(QtGui.QAbstractPrintDialog.PrintSelection)

        dlg.setWindowTitle("Print Document")

        if dlg.exec_() == QtGui.QDialog.Accepted:
            self.textEdit.print_(printer)

        del dlg

    def filePrintPreview(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        preview = QtGui.QPrintPreviewDialog(printer, self)
        preview.paintRequested.connect(self.printPreview)
        preview.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def filePrintPdf(self):
        fn = QtGui.QFileDialog.getSaveFileName(self, "Export PDF", None,
                "PDF files (*.pdf);;All Files (*)")

        if fn:
            if QtCore.QFileInfo(fn).suffix().isEmpty():
                fn += '.pdf'

            printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
            printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            printer.setOutputFileName(fileName)
            self.textEdit.document().print_(printer)

    def textBold(self):
        fmt = QtGui.QTextCharFormat()
        fmt.setFontWeight(self.actionTextBold.isChecked() and QtGui.QFont.Bold or QtGui.QFont.Normal)
        self.mergeFormatOnWordOrSelection(fmt)

    def textUnderline(self):
        fmt = QtGui.QTextCharFormat()
        fmt.setFontUnderline(self.actionTextUnderline.isChecked())
        self.mergeFormatOnWordOrSelection(fmt)

    def textItalic(self):
        fmt = QtGui.QTextCharFormat()
        fmt.setFontItalic(self.actionTextItalic.isChecked())
        self.mergeFormatOnWordOrSelection(fmt)

    def textFamily(self, family):
        fmt = QtGui.QTextCharFormat()
        fmt.setFontFamily(family)
        self.mergeFormatOnWordOrSelection(fmt)

    def textSize(self, pointSize):
        pointSize = float(pointSize)
        if pointSize > 0:
            fmt = QtGui.QTextCharFormat()
            fmt.setFontPointSize(pointSize)
            self.mergeFormatOnWordOrSelection(fmt)

    def textStyle(self, styleIndex):
        cursor = self.textEdit.textCursor()
        if styleIndex:
            styleDict = {
                1: QtGui.QTextListFormat.ListDisc,
                2: QtGui.QTextListFormat.ListCircle,
                3: QtGui.QTextListFormat.ListSquare,
                4: QtGui.QTextListFormat.ListDecimal,
                5: QtGui.QTextListFormat.ListLowerAlpha,
                6: QtGui.QTextListFormat.ListUpperAlpha,
                7: QtGui.QTextListFormat.ListLowerRoman,
                8: QtGui.QTextListFormat.ListUpperRoman,
            }

            style = styleDict.get(styleIndex, QtGui.QTextListFormat.ListDisc)
            cursor.beginEditBlock()
            blockFmt = cursor.blockFormat()
            listFmt = QtGui.QTextListFormat()

            if cursor.currentList():
                listFmt = cursor.currentList().format()
            else:
                listFmt.setIndent(blockFmt.indent() + 1)
                blockFmt.setIndent(0)
                cursor.setBlockFormat(blockFmt)

            listFmt.setStyle(style)
            cursor.createList(listFmt)
            cursor.endEditBlock()
        else:
            bfmt = QtGui.QTextBlockFormat()
            bfmt.setObjectIndex(-1)
            cursor.mergeBlockFormat(bfmt)

    def textColor(self):
        col = QtGui.QColorDialog.getColor(self.textEdit.textColor(), self)
        if not col.isValid():
            return

        fmt = QtGui.QTextCharFormat()
        fmt.setForeground(col)
        self.mergeFormatOnWordOrSelection(fmt)
        self.colorChanged(col)

    def textAlign(self, action):
        if action == self.actionAlignLeft:
            self.textEdit.setAlignment(
                    QtCore.Qt.AlignLeft | QtCore.Qt.AlignAbsolute)
        elif action == self.actionAlignCenter:
            self.textEdit.setAlignment(QtCore.Qt.AlignHCenter)
        elif action == self.actionAlignRight:
            self.textEdit.setAlignment(
                    QtCore.Qt.AlignRight | QtCore.Qt.AlignAbsolute)
        elif action == self.actionAlignJustify:
            self.textEdit.setAlignment(QtCore.Qt.AlignJustify)

    def currentCharFormatChanged(self, format):
        self.fontChanged(format.font())
        self.colorChanged(format.foreground().color())

    def cursorPositionChanged(self):
        self.alignmentChanged(self.textEdit.alignment())

    def clipboardDataChanged(self):
        self.actionPaste.setEnabled(
                len(QtGui.QApplication.clipboard().text()) != 0)

    def about(self):
        QtGui.QMessageBox.about(self, "About", 
                "This example demonstrates Qt's rich text editing facilities "
                "in action, providing an example document for you to "
                "experiment with.")

    def mergeFormatOnWordOrSelection(self, format):
        cursor = self.textEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QtGui.QTextCursor.WordUnderCursor)

        cursor.mergeCharFormat(format)
        self.textEdit.mergeCurrentCharFormat(format)

    def fontChanged(self, font):
        self.comboFont.setCurrentIndex(
                self.comboFont.findText(QtGui.QFontInfo(font).family()))
        self.comboSize.setCurrentIndex(
                self.comboSize.findText("%s" % font.pointSize()))
        self.actionTextBold.setChecked(font.bold())
        self.actionTextItalic.setChecked(font.italic())
        self.actionTextUnderline.setChecked(font.underline())

    def colorChanged(self, color):
        pix = QtGui.QPixmap(16, 16)
        pix.fill(color)
        self.actionTextColor.setIcon(QtGui.QIcon(pix))

    def alignmentChanged(self, alignment):
        if alignment & QtCore.Qt.AlignLeft:
            self.actionAlignLeft.setChecked(True)
        elif alignment & QtCore.Qt.AlignHCenter:
            self.actionAlignCenter.setChecked(True)
        elif alignment & QtCore.Qt.AlignRight:
            self.actionAlignRight.setChecked(True)
        elif alignment & QtCore.Qt.AlignJustify:
            self.actionAlignJustify.setChecked(True)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainWindows = []
    for fn in sys.argv[1:] or [None]:
        textEdit = TextEdit(fn)
        textEdit.resize(700, 800)
        textEdit.show()
        mainWindows.append(textEdit)

    sys.exit(app.exec_())
