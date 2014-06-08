Using PyQt4 from the Python Shell
=================================

PyQt4 installs an input hook (using ``PyOS_InputHook``) that processes events
when an interactive interpreter is waiting for user input.  This means that
you can, for example, create widgets from the Python shell prompt, interact
with them, and still being able to enter other Python commands.

For example, if you enter the following in the Python shell::

    >>> from PyQt4 import QtGui
    >>> a = QtGui.QApplication([])
    >>> w = QtGui.QWidget()
    >>> w.show()
    >>> w.hide()
    >>>

The widget would be displayed when ``w.show()`` was entered amd hidden as soon
as ``w.hide()`` was entered.

The installation of an input hook can cause problems for certain applications
(particularly those that implement a similar feature using different means).
The :mod:`~PyQt4.QtCore` module contains the
:func:`~PyQt4.QtCore.pyqtRemoveInputHook` and
:func:`~PyQt4.QtCore.pyqtRestoreInputHook` functions that remove and restore
the input hook respectively.
