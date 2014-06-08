Integrating Python and JavaScript in QtWebKit
=============================================

QtWebKit uses slots to expose class methods implemented in C++ as JavaScript
methods that can be called from scripts embedded in HTML.  Python class
methods that have been decorated behave in exactly the same way.

In the same way, properties created using :func:`~PyQt4.QtCore.pyqtProperty`
are also automatically exposed as JavaScript properties.
