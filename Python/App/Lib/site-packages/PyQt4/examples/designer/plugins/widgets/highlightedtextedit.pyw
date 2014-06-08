#!/usr/bin/env python

"""
highlightedtextedit.py

A PyQt custom widget example for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from PyQt4 import QtCore, QtGui


class HighlightedTextEdit(QtGui.QTextEdit):

    """HighlightedTextEdit(QtGui.QTextEdit)
    
    Provides a custom text editor with a simple built-in Python syntax
    highlighter.
    """
    
    def __init__(self, parent=None):
    
        super(HighlightedTextEdit, self).__init__(parent)
        
        self.setFrameShape(QtGui.QFrame.Box)
        self.setFrameShadow(QtGui.QFrame.Plain)
        char_format = QtGui.QTextCharFormat()
        char_format.setFont(self.font())
        self.highlighter = PythonHighlighter(self.document(), char_format)
    
    # The code property is implemented with the getCode() and setCode()
    # methods, and contains the plain text shown in the editor.
    
    def getCode(self):
        self._code = self.toPlainText()
        return self._code
    
    def setCode(self, text):
        self.setPlainText(text)
    
    code = QtCore.pyqtProperty(str, getCode, setCode)

    # The displayFont property is implemented with the getDisplayFont() and
    # setDisplayFont() methods, and contains the font used to display the
    # text in the editor.
    
    def getDisplayFont(self):
        return QtGui.QWidget.font(self)
    
    def setDisplayFont(self, font):
        QtGui.QWidget.setFont(self, font)
        self.highlighter.updateHighlighter(font)
        self.update()
    
    displayFont = QtCore.pyqtProperty(QtGui.QFont, getDisplayFont, setDisplayFont)


class PythonHighlighter(QtGui.QSyntaxHighlighter):

    keywords = (
        "and",       "del",       "for",       "is",        "raise",
        "assert",    "elif",      "from",      "lambda",    "return",
        "break",     "else",      "global",    "not",       "try",
        "class",     "except",    "if",        "or",        "while",
        "continue",  "exec",      "import",    "pass",      "yield",
        "def",       "finally",   "in",        "print"
        )
    
    def __init__(self, document, base_format):
    
        super(PythonHighlighter, self).__init__(document)
        
        self.base_format = base_format
        self.document = document
        
        self.updateHighlighter(base_format.font())
    
    def highlightBlock(self, text):
    
        self.setCurrentBlockState(0)
        
        if text.trimmed().isEmpty():
            self.setFormat(0, len(text), self.empty_format)
            return
        
        self.setFormat(0, len(text), self.base_format)
        
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = text.indexOf(self.multiLineStringBegin)
        
        if startIndex > -1:
            self.highlightRules(text, 0, startIndex)
        else:
            self.highlightRules(text, 0, len(text))
        
        while startIndex >= 0:
        
            endIndex = text.indexOf(self.multiLineStringEnd,
                startIndex + len(self.multiLineStringBegin.pattern()))
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = text.length() - startIndex
            else:
                commentLength = endIndex - startIndex + \
                                self.multiLineStringEnd.matchedLength()
                self.highlightRules(text, endIndex, len(text))
            
            self.setFormat(startIndex, commentLength, self.multiLineStringFormat)
            startIndex = text.indexOf(self.multiLineStringBegin,
                                      startIndex + commentLength)
    
    def highlightRules(self, text, start, finish):
    
        for expression, format in self.rules:
        
            index = expression.indexIn(text, start)
            while index >= start and index < finish:
                length = expression.matchedLength()
                self.setFormat(index, min(length, finish - index), format)
                index = expression.indexIn(text, index + length)
    
    def updateFonts(self, font):
    
        self.base_format.setFont(font)
        self.empty_format = QtGui.QTextCharFormat(self.base_format)
        self.empty_format.setFontPointSize(font.pointSize()/4.0)
        
        self.keywordFormat = QtGui.QTextCharFormat(self.base_format)
        self.keywordFormat.setForeground(QtCore.Qt.darkBlue)
        self.keywordFormat.setFontWeight(QtGui.QFont.Bold)
        self.callableFormat = QtGui.QTextCharFormat(self.base_format)
        self.callableFormat.setForeground(QtCore.Qt.darkBlue)
        self.magicFormat = QtGui.QTextCharFormat(self.base_format)
        self.magicFormat.setForeground(QtGui.QColor(224,128,0))
        self.qtFormat = QtGui.QTextCharFormat(self.base_format)
        self.qtFormat.setForeground(QtCore.Qt.blue)
        self.qtFormat.setFontWeight(QtGui.QFont.Bold)
        self.selfFormat = QtGui.QTextCharFormat(self.base_format)
        self.selfFormat.setForeground(QtCore.Qt.red)
        #self.selfFormat.setFontItalic(True)
        self.singleLineCommentFormat = QtGui.QTextCharFormat(self.base_format)
        self.singleLineCommentFormat.setForeground(QtCore.Qt.darkGreen)
        self.multiLineStringFormat = QtGui.QTextCharFormat(self.base_format)
        self.multiLineStringFormat.setBackground(
            QtGui.QBrush(QtGui.QColor(127,127,255)))
        self.quotationFormat1 = QtGui.QTextCharFormat(self.base_format)
        self.quotationFormat1.setForeground(QtCore.Qt.blue)
        self.quotationFormat2 = QtGui.QTextCharFormat(self.base_format)
        self.quotationFormat2.setForeground(QtCore.Qt.blue)
    
    def updateRules(self):
    
        self.rules = []
        self.rules += map(lambda s: (QtCore.QRegExp(r"\b"+s+r"\b"),
                          self.keywordFormat), self.keywords)
        
        self.rules.append((QtCore.QRegExp(r"\b[A-Za-z_]+\(.*\)"), self.callableFormat))
        self.rules.append((QtCore.QRegExp(r"\b__[a-z]+__\b"), self.magicFormat))
        self.rules.append((QtCore.QRegExp(r"\bself\b"), self.selfFormat))
        self.rules.append((QtCore.QRegExp(r"\bQ([A-Z][a-z]*)+\b"), self.qtFormat))
        
        self.rules.append((QtCore.QRegExp(r"#[^\n]*"), self.singleLineCommentFormat))
        
        self.multiLineStringBegin = QtCore.QRegExp(r'\"\"\"')
        self.multiLineStringEnd = QtCore.QRegExp(r'\"\"\"')
        
        self.rules.append((QtCore.QRegExp(r'\"[^\n]*\"'), self.quotationFormat1))
        self.rules.append((QtCore.QRegExp(r"'[^\n]*'"), self.quotationFormat2))
    
    def updateHighlighter(self, font):
    
        self.updateFonts(font)
        self.updateRules()
        self.setDocument(self.document)


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    widget = HighlightedTextEdit()
    widget.show()
    sys.exit(app.exec_())
