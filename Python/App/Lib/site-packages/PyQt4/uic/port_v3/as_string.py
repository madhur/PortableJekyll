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


import re


def as_string(obj, encode=True):
    if isinstance(obj, str):
        s = '"' + _escape(obj) + '"'

        if encode:
            # Using _fromUtf8() ensures that (for the default QString API) the
            # code will run under both Python v2 and v3.
            s =  '_fromUtf8(' + s + ')'

        return s

    return str(obj)


_esc_regex = re.compile(r"(\"|\'|\\)")

def _escape(text):
    # This escapes any escaped single or double quote or backslash.
    x = _esc_regex.sub(r"\\\1", text)

    # This replaces any '\n' with an escaped version and a real line break.
    return re.sub(r'\n', r'\\n"\n"', x)
