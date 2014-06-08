Potential Incompatibilities with Earlier Versions
=================================================

PyQt4 v4.9.2
------------

QPyNullVariant
**************

In previous versions a ``QPyNullVariant`` would always evaluate to ``True``
when converted to a bool.

In this version a ``QPyNullVariant`` will always evaluate to ``False`` when
converted to a bool.  This makes it behave like ``None`` in these
circumstances.


PyQt4 v4.8.3
------------

SQL Models
**********

In previous versions, when using v2 of the QVariant API (the default for Python
v3), there was no way to represent a null ``QVariant``.  Therefore when reading
values of certain types from an SQL model it was impossible to distinguish
between, for example, a null integer and an integer with the value zero.

In this version the ``QPyNullVariant`` class is used to represent a null
QVariant.  Therefore the object read from an SQL model may now be a
``QPyNullVariant`` instance.

A null ``QVariant`` is only converted to a ``QPyNullVariant`` if the underlying
C++ type of the ``QVariant`` cannot be tested for null, i.e. it does not
implement an ``isNull()`` method.  This ensures that existing code that uses
non-SQL models will continue to work unchanged.


PyQt4 v4.8
----------

QVariantList
************

In previous versions PyQt4 would always try and convert a Python list to a
``QVariantList``.  In this version PyQt4 will first try to convert it to a
``QVariant`` containing a ``QList<QObject *>``, but only if
``QList<QObject *>`` has been registered with Qt as a meta-type.

Normally it is only the :mod:`~PyQt4.QtDeclarative` module that registers this
meta-type and so the behaviour of existing applications should be unchanged.
It is possible however that you might observe different conversion behaviour
after importing the :mod:`~PyQt4.QtDeclarative` module.


PyQt4 v4.7.4
------------

:func:`~PyQt4.QtCore.pyqtSignal` with dict and list
***************************************************

In previous versions a Qt signal defined using
:func:`~PyQt4.QtCore.pyqtSignal` that had an argument specified as a dict then,
when emitting a value, PyQt4 would try and convert the value to a
``QVariantMap`` if possible.  If it wasn't possible, normally because the dict
had non-string keys, then the value would be left as a dict object.

In this version PyQt4 will not attempt to convert the value to a
``QVariantMap`` and will always leave it as a dict object.  If you want the
value to be converted to a ``QVariantMap`` then define the signal argument as
``'QVariantMap'``.

The same applies to conversions between lists and ``QVariantList``.


PyQt4 v4.7.1
------------

QVariant
********

This version introduces a slight incompatibility in the conversion between
sub-classes of standard Python types and ``QVariant``.

Take, for example, the following code::

    from PyQt4.QtCore import QVariant

    class MyFloat(float):
        pass

    myfloat = MyFloat(5.0)
    variant = QVariant(myfloat)

With this version of PyQt4 ``myfloat`` will be converted in such a way as to
preserve any additional attributes (including methods) and will not be
converted to a C++ ``double``.  In other words, the following assertions are
true::

    assert(variant.type() != QVariant.Double)
    assert(variant.toPyObject() is myfloat)

Prior to this version ``myfloat`` would be converted to a C++ ``double``.  In
other words, the following assertions would be true::

    assert(variant.type() == QVariant.Double)
    assert(variant.toPyObject() == myfloat)
    assert(type(variant.toPyObject()) is float)

The same change also affects objects that implement the sequence protocol.
Prior to this version such an object would be converted to a ``QVariantList``
which would mean that it was converted back to a Python ``list`` rather than to
the original type.


PyQt4 v4.5
----------

QVariant
********

This version introduces a slight incompatibility in the conversion between
Python sub-classes of certain Qt classes and ``QVariant``.  The Qt classes
affected are those that ``QVariant`` has explicit support for, e.g. ``QSize``,
``QBitmap``.

Take, for example, the following code::

    from PyQt4.QtCore import QSize, QVariant

    class MySize(QSize):
        pass

    mysize = MySize(5, 5)
    variant = QVariant(mysize)

With this version of PyQt4 ``mysize`` will be converted in such a way as to
preserve any additional attributes (including methods) and will not be
converted to a C++ ``QSize`` instance.  In other words, the following
assertions are true::

    assert(variant.type() != QVariant.Size)
    assert(variant.toPyObject() is mysize)

Prior to this version ``mysize`` would be converted to a C++ ``QSize``
instance.  In other words, the following assertions would be true::

    assert(variant.type() == QVariant.Size)
    assert(variant.toPyObject() == mysize)
    assert(type(variant.toPyObject()) is QSize)

It is hoped that this change of behaviour will not have a significant impact.
However if you need the old behaviour then simply create a copy of your
sub-class instance using the base class constructor as shown below::

    variant = QVariant(QSize(mysize))

A similar issue also affects the conversion of the Python ``datetime``,
``date`` and ``time`` types to ``QVariant``.  These are no longer converted to
the corresponding ``QDateTime``, ``QDate`` and ``QTime`` classes.  The values
can be retrieved using ``QVariant.toPyObject()``.  Again, the old behaviour can
be achieved using an explicit conversion to the Qt class before converting to
``QVariant``.

A further incompatible change is the handling of Python sub-classes of
``QObject``.  In previous versions ``QVariant.userType()`` would return an
internal type and an extra reference would be kept to the Python object.  In
the current version ``QVariant.userType()`` will correctly return
``QMetaType.QObjectStar`` (or ``QMetaType.QWidgetStar``) but an extra
reference to the Python object is not kept.  To avoid a potential crash you
should ensure that you keep a separate reference to the Python object, either
explicitly or implicitly by giving it a parent.


:program:`pyrcc4` Support for Python v3
***************************************

:program:`pyrcc4` will now generate code for Python v3 when the new
:option:`-py3 <pyrcc4 -py3>` command line option is used.  The generated code
will also work with Python v2.6 and later.

By default :program:`pyrcc4` will generate code for all Python v2 versions but
you should use the new :option:`-py2 <pyrcc4 -py2>` command line option to
enforce this in case the default is changed in the future.
