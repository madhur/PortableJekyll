PyQt4 and Python v3
===================

PyQt4 fully supports all versions of Python v3.  The default behaviour is
different in some areas to the default behaviour with Python v2.  These
incompatible differences were introduced in order to make PyQt4 more Pythonic.
However it is very easy to revert to the default Python v2 behaviour on a class
by class basis if required.  (See the section :ref:`ref-incompat-apis`.)


QAbstractSpinBox
----------------

The following PyQt4 calls have changed signatures to avoid the need for mutable
strings::

    QAbstractSpinBox.fixup(str input) -> str
    QAbstractSpinBox.validate(str input, int pos) -> QValidator.State, str, int


QChar
-----

The ``QChar`` class is implemented as a mapped type that is automatically
converted to and from a Python string.


QClipboard
----------

The following PyQt4 call has a changed signature to avoid the need for mutable
strings::

    QClipboard.text(str subtype, QClipboard.Mode mode=QClipboard.Clipboard) -> str, str


QDate
-----

The ``QDate.__hash__()`` returns a hash of the string representation so that
two objects with the same date will have the same hash.

The default behaviour with Python v2 is to return the object's ``id()`` so that
two objects with the same date will have different hashes.


QDateTime
---------

The ``QDateTime.__hash__()`` method returns a hash of the string representation
so that two objects with the same date and time will have the same hash.

The default behaviour with Python v2 is to return the object's ``id()`` so that
two objects with the same date and time will have different hashes.


QDateTimeEdit
-------------

The following PyQt4 calls have changed signatures to avoid the need for mutable
strings::

    QDateTimeEdit.fixup(str input) -> str
    QDateTimeEdit.validate(str input, int pos) -> QValidator.State, str, int


QDoubleSpinBox
--------------

The following PyQt4 calls have changed signatures to avoid the need for mutable
strings::

    QDoubleSpinBox.fixup(str input) -> str
    QDoubleSpinBox.validate(str input, int pos) -> QValidator.State, str, int


QDoubleValidator
----------------

The following PyQt4 call has a changed signature to avoid the need for mutable
strings::

    QDoubleValidator.validate(str input, int pos) -> QValidator.State, str, int


QFileDialog
-----------

The following PyQt4 calls have changed signatures to avoid the need for mutable
strings::

    QFileDialog.getOpenFileName(QWidget parent=None, str caption=None, str dir=None, str filter=None, QFileDialog.Options options=0) -> str
    QFileDialog.getOpenFileNames(QWidget parent=None, str caption=None, str dir=None, str filter=None, QFileDialog.Options options=0) -> list(str)
    QFileDialog.getSaveFileName(QWidget parent=None, str caption=None, str dir=None, str filter=None, QFileDialog.Options options=0) -> str

The static methods ``QFileDialog.getOpenFileNameAndFilter()``,
``QFileDialog.getOpenFileNamesAndFilter()`` and
``QFileDialog.getSaveFileNameAndFilter()`` have been added which return a tuple
of the name(s) and the selected filter.  These can also be used with Python v2.


QFontMetrics
------------

The methods ``QFontMetrics.widthChar()`` and
``QFontMetrics.boundingRectChar()`` have been added which accept a Python
string of length one and call the C++ ``QFontMetrics::width()`` and
``QFontMetrics::boundingRect()`` methods passing the character as a ``QChar``
(rather than a single character ``QString``).


QFontMetricsF
-------------

The methods ``QFontMetricsF.widthChar()`` and
``QFontMetricsF.boundingRectChar()`` have been added which accept a Python
string of length one and call the C++ ``QFontMetricsF::width()`` and
``QFontMetricsF::boundingRect()`` methods passing the character as a ``QChar``
(rather than a single character ``QString``).


QIntValidator
-------------

The following PyQt4 call has a changed signature to avoid the need for mutable
strings::

    QIntValidator.validate(str input, int pos) -> QValidator.State, str, int


QLatin1Char
-----------

The ``QLatin1Char`` class is not implemented.


QLatin1String
-------------

The ``QLatin1String`` class is not implemented.


QPyNullVariant
--------------

The ``QPyNullVariant`` class is used to represent a null ``QVariant``.  It is
automatically converted to a C++ ``QVariant`` when required.

A null C++ ``QVariant`` is automatically converted to a ``QPyNullVariant``
unless the type of the data in the ``QVariant`` itself supports the concept of
a null value (i.e. it has an ``isNull()`` method).  In this case a null C++
``QVariant`` is converted to a null instance of the data type.  The exception
to this rule is that a C++ ``QVariant`` containing a null ``QString`` is always
converted to a ``QPyNullVariant``.


QRegExpValidator
----------------

The following PyQt4 call has a changed signature to avoid the need for mutable
strings::

    QRegExpValidator.validate(str input, int pos) -> QValidator.State, str, int


QSettings
---------

The ``QSettings.value()`` method takes an optional ``type`` keyword argument
that specifies the type of the value to return.  It can either be a Python type
object or a string specifying the name of a C++ type.

Using this argument avoids potential portability problems where the type of a
value may not be as expected because the platform specific backend to
``QSettings`` may not store the necessary type information.

The argument can also be used with Python v2.


QSpinBox
--------

The following PyQt4 calls have changed signatures to avoid the need for mutable
strings::

    QSpinBox.fixup(str input) -> str
    QSpinBox.validate(str input, int pos) -> QValidator.State, str, int


QString
-------

The ``QString`` class is implemented as a mapped type that is automatically
converted to and from a Python string.  In addition a ``None`` is converted to
a null ``QString``.  However, a null ``QString`` is converted to an empty
Python string (and not ``None``).  (This is because Qt often returns a null
``QString`` when it should probably return an empty ``QString``.)


QStringList
-----------

The ``QStringList`` class is implemented as a mapped type that is
automatically converted to and from a Python list of strings.


QStringMatcher
--------------

The ``QStringMatcher`` class is not implemented.


QStringRef
----------

The ``QStringRef`` class is implemented as a mapped type that is automatically
converted to and from a Python string.


QTextDecoder
------------

The following C++ call is not wrapped because it expects ``QString`` to be
mutable::

    void toUnicode(QString *target, const char *chars, int len)


QTextStream
-----------

The C++ functions ``bin()``, ``hex()`` and ``oct()`` are named ``bin_()``,
``hex_()`` and ``oct_()`` respectively in Python.  This allows the import
style ``from PyQt4.QtCore import *`` to be used without them clashing with the
Python built-in functions with the same names.

The following C++ calls are not wrapped because they expect ``QString`` to be
mutable::

    QTextStream(QString *string, QIODevice::OpenMode openMode = QIODevice::ReadWrite)
    void setString(QString *string, QIODevice::OpenMode openMode = QIODevice::ReadWrite)
    QString *string()
    QTextStream &operator>>(QChar &c)
    QTextStream &operator>>(QString &s)


QTime
-----

The ``QTime.__hash__()`` returns a hash of the string representation so that
two objects with the same time will have the same hash.

The default behaviour with Python v2 is to return the object's ``id()`` so that
two objects with the same time will have different hashes.


QUrl
----

The ``QUrl.__hash__()`` method returns a hash of the string representation so
that two objects with the same URL will have the same hash.

The default behaviour with Python v2 is to return the object's ``id()`` so that
two objects with the same URL will have different hashes.


QValidator
----------

The following PyQt4 calls have changed signatures to avoid the need for mutable
strings::

    QValidator.fixup(str input) -> str
    QValidator.validate(str input, int pos) -> QValidator.State, str, int


QVariant
--------

The ``QVariant`` class is implemented as a mapped type.  Any Python object can
be passed when a ``QVariant`` instance is expected.  When Qt returns a
``QVariant`` then it will automatically be converted to the original Python
object or an equivalent.

``None`` is interpreted as an invalid ``QVariant`` and vice versa.

The ``QPyNullVariant`` class is used to represent a null ``QVariant``.


QWebPage
--------

The following PyQt4 call has a changed signature to avoid the need for mutable
strings::

    QWebPage.javaScriptPrompt(QWebFrame originatingFrame, str msg, str defaultValue) -> bool, str


QXmlStreamWriter
----------------

The following C++ call is not wrapped because it expects ``QString`` to be
mutable::

    QXmlStreamWriter(QString *string)
