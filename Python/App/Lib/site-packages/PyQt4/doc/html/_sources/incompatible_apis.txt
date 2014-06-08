.. _ref-incompat-apis:

Selecting Incompatible APIs
===========================

PyQt4 provides limited support for multiple incompatible APIs and the ability
for an application to select between them at run-time.  For example, an
application can choose whether ``QString`` is implemented as a Python type, or
is automatically converted to and from a Python v2 unicode object or a Python
v3 string object.

This ability allows developers to decide how to manage the transition from an
older deprecated, API to a newer incompatible API.

Each API that can be selected in this way has a name and a range of version
numbers.  An application calls :func:`sip.setapi` to set the version number of
a particular API.  This call must be made before any module that implements the
API is imported.  Once set the version number cannot be changed.  If not set
then an API will use its default version.

For example the following code will disable the use of ``QString``::

    import sip
    sip.setapi('QString', 2)

    from PyQt4 import QtCore

    # This will raise an attribute exception because QString is only wrapped
    # in version 1 of the API.
    s = QtCore.QString()

The following APIs are currently implemented:

- QDate v1, v2
- QDateTime v1, v2
- QString v1, v2
- QTextStream v1, v2
- QTime v1, v2
- QUrl v1, v2
- QVariant v1, v2
