Python Objects and QVariant
===========================

Qt uses the ``QVariant`` class as a wrapper for any C++ data type.  PyQt4
allows any Python object to be wrapped as a ``QVariant`` and passed around Qt's
meta-object system like any other type.

PyQt4 will try to convert the Python object to a C++ equivalent if it can so
that the ``QVariant`` can be passed to other C++ code that doesn't know what a
Python object is.

Version 2 of PyQt4's ``QVariant`` API will automatically convert a ``QVariant``
back to a Python object of the correct type.

Version 1 of the ``QVariant`` API provides the ``QVariant.toPyObject()`` method
to convert the ``QVariant`` back to a Python object of the correct type.

Both versions will raise a Python exception if the conversion cannot be done.
