The PyQt4 Resource System
=========================

PyQt4 supports Qt's resource system.  This is a facility for embedding
resources such as icons and translation files in an application.  This makes
the packaging and distribution of those resources much easier.

A ``.qrc`` resource collection file is an XML file used to specify which
resource files are to be embedded.  The application then refers to the resource
files by their original names but preceded by a colon.

For a full description, including the format of the ``.qrc`` files, see the Qt
Resource System in the Qt documentation.


:program:`pyrcc4`
-----------------

:program:`pyrcc4` is PyQt4's equivalent to Qt's :program:`rcc` utility and is
used in exactly the same way.  :program:`pyrcc4` reads the ``.qrc`` file, and
the resource files, and generates a Python module that only needs to be
``import`` ed by the application in order for those resources to be made
available just as if they were the original files.

In addition to the command line options that are common with :program:`rcc`,
the following are also supported:

.. program:: pyrcc4

.. cmdoption:: -py2

    Generate code that will work for all versions of Python v2.x.  Although
    this is the default, the option should be specified explicitly in case the
    default is changed in a future version.

.. cmdoption:: -py3

    Generate code that will work for all versions of Python starting with
    Python v2.6.

:program:`pyrcc4` will only be included if your copy of Qt includes the XML
module.
