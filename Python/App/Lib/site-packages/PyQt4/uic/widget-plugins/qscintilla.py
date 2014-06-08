#############################################################################
##
## Copyright (c) 2013 Riverbank Computing Limited <info@riverbankcomputing.com>
## 
## This file is part of PyQt.
## 
## This file may be used under the terms of the GNU General Public
## License versions 2.0 or 3.0 as published by the Free Software
## Foundation and appearing in the files LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file.  Alternatively you may (at
## your option) use any later version of the GNU General Public
## License if such license has been publicly approved by Riverbank
## Computing Limited (or its successors, if any) and the KDE Free Qt
## Foundation. In addition, as a special exception, Riverbank gives you
## certain additional rights. These rights are described in the Riverbank
## GPL Exception version 1.1, which can be found in the file
## GPL_EXCEPTION.txt in this package.
## 
## If you are unsure which license is appropriate for your use, please
## contact the sales department at sales@riverbankcomputing.com.
## 
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
#############################################################################


# If pluginType is MODULE, the plugin loader will call moduleInformation.  The
# variable MODULE is inserted into the local namespace by the plugin loader.
pluginType = MODULE


# moduleInformation() must return a tuple (module, widget_list).  If "module"
# is "A" and any widget from this module is used, the code generator will write
# "import A".  If "module" is "A[.B].C", the code generator will write
# "from A[.B] import C".  Each entry in "widget_list" must be unique.
def moduleInformation():
    return "PyQt4.Qsci", ("QsciScintilla", )
