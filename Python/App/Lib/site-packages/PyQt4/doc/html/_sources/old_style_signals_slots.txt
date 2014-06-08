Old-style Signal and Slot Support
=================================

This section describes the older style for connecting signals and slots.  It
uses the same API that a C++ application would use.  This has a number of
advantages.

- It is well understood and documented.

- Any future changes to the C++ API should be easily included.

It also has a number of disadvantages.

- It requires knowledge of the C++ types of signal arguments.

- It is error prone in that if you mis-type the signal name or signature then
  no exception is raised, either when the signal is connected or emitted.

- It is verbose.

- It is not Pythonic.

This older style of connecting signals and slots will continue to be supported
throughout the life of PyQt4.


PyQt4 Signals and Qt Signals
----------------------------

Qt signals are statically defined as part of a C++ class.  They are referenced
using the ``QtCore.SIGNAL()`` function.  This method takes a single string
argument that is the name of the signal and its C++ signature.  For example::

    QtCore.SIGNAL('finished(int)')

The returned value is normally passed to the ``QtCore.QObject.connect()``
method.

PyQt4 allows new signals to be defined dynamically.  The act of emitting a
PyQt4 signal implicitly defines it.  PyQt4 signals are also referenced using
the ``QtCore.SIGNAL()`` function.


The ``PyQt_PyObject`` Signal Argument Type
------------------------------------------

It is possible to pass any Python object as a signal argument by specifying
``PyQt_PyObject`` as the type of the argument in the signature.  For example::

    QtCore.SIGNAL('finished(PyQt_PyObject)')

While this would normally be used for passing objects like lists and
dictionaries as signal arguments, it can be used for any Python type.  Its
advantage when passing, for example, an integer is that the normal conversions
from a Python object to a C++ integer and back again are not required.

The reference count of the object being passed is maintained automatically.
There is no need for the emitter of a signal to keep a reference to the object
after the call to ``QtCore.QObject.emit()``, even if a connection is queued.


Short-circuit Signals
---------------------

There is also a special form of a PyQt4 signal known as a short-circuit signal.
Short-circut signals implicitly declare each argument as being of type
``PyQt_PyObject``.

Short-circuit signals do not have a list of arguments or the surrounding
parentheses.

Short-circuit signals may only be connected to slots that have been implemented
in Python.  They cannot be connected to Qt slots or the Python callables that
wrap Qt slots.


PyQt4 Slots and Qt Slots
------------------------

Qt slots are statically defined as part of a C++ class.  They are referenced
using the ``QtCore.SLOT()`` function.  This method takes a single string
argument that is the name of the slot and its C++ signature.  For example::

    QtCore.SLOT('done(int)')

The returned value is normally passed to the ``QtCore.QObject.connect()``
method.

PyQt4 allows any Python callable to be used as a slot, not just Qt slots.  This
is done by simply referencing the callable.  Because Qt slots are implemented
as class methods they are also available as Python callables.  Therefore it is
not usually necessary to use ``QtCore.SLOT()`` for Qt slots.  However, doing so
is more efficient as it avoids a conversion to Python and back to C++.

Qt allows a signal to be connected to a slot that requires fewer arguments than
the signal passes.  The extra arguments are quietly discarded.  PyQt4 slots can
be used in the same way.

Note that when a slot is a Python callable its reference count is not
increased.  This means that a class instance can be deleted without having to
explicitly disconnect any signals connected to its methods.  However, if a slot
is a lambda function or a partial function then its reference count is
automatically incremented to prevent it from being immediately garbage
collected.


Connecting Signals and Slots
----------------------------

Connections between signals and slots (and other signals) are made using the
``QtCore.QObject.connect()`` method.  For example::

    QtCore.QObject.connect(a, QtCore.SIGNAL('QtSig()'), pyFunction)
    QtCore.QObject.connect(a, QtCore.SIGNAL('QtSig()'), pyClass.pyMethod)
    QtCore.QObject.connect(a, QtCore.SIGNAL('QtSig()'), b, QtCore.SLOT('QtSlot()'))
    QtCore.QObject.connect(a, QtCore.SIGNAL('PySig()'), b, QtCore.SLOT('QtSlot()'))
    QtCore.QObject.connect(a, QtCore.SIGNAL('PySig'), pyFunction)

Disconnecting signals works in exactly the same way using the
``QtCore.QObject.disconnect()`` method.  However, not all the variations of
that method are supported by PyQt4.  Signals must be disconnected one at a
time.


Emitting Signals
----------------

Any instance of a class that is derived from the ``QtCore.QObject`` class can
emit a signal using its ``emit()`` method.  This takes a minimum of one
argument which is the signal.  Any other arguments are passed to the connected
slots as the signal arguments.  For example::

    a.emit(QtCore.SIGNAL('clicked()'))
    a.emit(QtCore.SIGNAL('pySig'), "Hello", "World")


The ``QtCore.pyqtSignature()`` Decorator
----------------------------------------

The ``QtCore.pyqtSignature()`` serves the same purpose as the
:func:`~PyQt4.QtCore.pyqtSlot` decorator but has a less Pythonic API.
