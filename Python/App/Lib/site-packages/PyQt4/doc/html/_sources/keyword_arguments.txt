Support for Keyword Arguments
=============================

Starting with v4.7 PyQt4 supports the use of keyword arguments for optional
arguments.

One thing to be aware of is that, although the PyQt4 and Qt documentation may
indicate that an argument has a particular name, you may find that PyQt4
actually uses a different name.  This is because the name of an argument is not
part of the Qt API and there is some inconsistency in the way that similar
arguments are named.  Different versions of Qt may use a different name for an
argument which wouldn't affect the C++ API but would break the Python API.

The docstrings that PyQt4 generates for all classes, functions and methods will
contain the correct argument names.  In a future version of PyQt4 the
documentation will also contain the correct argument names.
