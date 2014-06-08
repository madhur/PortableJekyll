Install instructions for pyreadline
===================================

The pyreadline package is based on the readline package by Gary Bishop. It is
not a complete replacement for GNU readline. The pyreadline package is
currently only for the win32 platform. The pyreadline package tries to improve
the integration with the win32 platform by including such things as copy
paste.

The pyreadline package installs as pyreadline, you may want to add readline.py
containing the line: 
from pyreadline import *

Dependencies
------------

  * PyWin32, the win32 Python extensions from
    http://starship.python.net/crew/mhammond.

  * This in turn requires Tomas Heller's ctypes from
    http://starship.python.net/crew/theller/ctypes.

