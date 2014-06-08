#############################################################################
##
## Copyright (C) 2011 Riverbank Computing Limited.
## Copyright (C) 2006 Thorsten Marek.
## All right reserved.
##
## This file is part of PyQt.
##
## You may use this file under the terms of the GPL v2 or the revised BSD
## license as follows:
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
##   * Neither the name of the Riverbank Computing Limited nor the names
##     of its contributors may be used to endorse or promote products
##     derived from this software without specific prior written
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
##
#############################################################################


import sys

from PyQt4.uic.properties import Properties
from PyQt4.uic.uiparser import UIParser
from PyQt4.uic.Compiler import qtproxies
from PyQt4.uic.Compiler.indenter import createCodeIndenter, getIndenter, \
        write_code
from PyQt4.uic.Compiler.qobjectcreator import CompilerCreatorPolicy
from PyQt4.uic.Compiler.misc import write_import


class UICompiler(UIParser):
    def __init__(self):
        UIParser.__init__(self, qtproxies.QtCore, qtproxies.QtGui,
                CompilerCreatorPolicy())

    def reset(self):
        qtproxies.i18n_strings = []
        UIParser.reset(self)

    def setContext(self, context):
        qtproxies.i18n_context = context

    def createToplevelWidget(self, classname, widgetname):
        indenter = getIndenter()
        indenter.level = 0

        indenter.write("from PyQt4 import QtCore, QtGui")
        indenter.write("")

        indenter.write("try:")
        indenter.indent()
        indenter.write("_fromUtf8 = QtCore.QString.fromUtf8")
        indenter.dedent()
        indenter.write("except AttributeError:")
        indenter.indent()
        indenter.write("def _fromUtf8(s):")
        indenter.indent()
        indenter.write("return s")
        indenter.dedent()
        indenter.dedent()
        indenter.write("")

        indenter.write("try:")
        indenter.indent()
        indenter.write("_encoding = QtGui.QApplication.UnicodeUTF8")
        indenter.write("def _translate(context, text, disambig):")
        indenter.indent()
        indenter.write("return QtGui.QApplication.translate(context, text, disambig, _encoding)")
        indenter.dedent()
        indenter.dedent()
        indenter.write("except AttributeError:")
        indenter.indent()
        indenter.write("def _translate(context, text, disambig):")
        indenter.indent()
        indenter.write("return QtGui.QApplication.translate(context, text, disambig)")
        indenter.dedent()
        indenter.dedent()
        indenter.write("")

        indenter.write("class Ui_%s(object):" % self.uiname)
        indenter.indent()
        indenter.write("def setupUi(self, %s):" % widgetname)
        indenter.indent()
        w = self.factory.createQObject(classname, widgetname, (),
                                   is_attribute = False,
                                   no_instantiation = True)
        w.baseclass = classname
        w.uiclass = "Ui_%s" % self.uiname
        return w

    def setDelayedProps(self):
        write_code("")
        write_code("self.retranslateUi(%s)" % self.toplevelWidget)
        UIParser.setDelayedProps(self)

    def finalize(self):
        indenter = getIndenter()
        indenter.level = 1
        indenter.write("")
        indenter.write("def retranslateUi(self, %s):" % self.toplevelWidget)
        indenter.indent()

        if qtproxies.i18n_strings:
            for s in qtproxies.i18n_strings:
                indenter.write(s)
        else:
            indenter.write("pass")

        indenter.dedent()
        indenter.dedent()

        # Make a copy of the resource modules to import because the parser will
        # reset() before returning.
        self._resources = self.resources

    def compileUi(self, input_stream, output_stream, from_imports, resource_suffix):
        createCodeIndenter(output_stream)
        w = self.parse(input_stream, resource_suffix)

        indenter = getIndenter()
        indenter.write("")

        self.factory._cpolicy._writeOutImports()

        for res in self._resources:
            write_import(res, from_imports)

        return {"widgetname": str(w),
                "uiclass" : w.uiclass,
                "baseclass" : w.baseclass}
