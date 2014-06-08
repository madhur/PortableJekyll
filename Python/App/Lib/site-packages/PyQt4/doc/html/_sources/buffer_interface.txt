Support for Python's Buffer Interface
=====================================

If SIP v4.7.5 or later is used then any Python object that supports the buffer
interface can be used whenever a ``char`` or ``char *`` is expected.  If the
buffer has multiple segments then all but the first will be ignored.
