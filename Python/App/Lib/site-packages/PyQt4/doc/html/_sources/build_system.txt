.. _ref-build-system:

The PyQt4 Build System
======================

.. versionadded:: 4.10

SIP v5 will not include an extensible build system, i.e it will not provide an
equivalent of SIP v4's :mod:`sipconfig` module.  Consequently a version of PyQt
built with SIP v5 will not provide an equivalent of the
:mod:`~PyQt4.pyqtconfig` module.  However there is still a need for certain
information to be shared between PyQt and other modules (such as QScintilla's
:mod:`~PyQt4.Qsci` module) that are built on top of it.  Specifically it is
important that the same ``-t`` and ``-x`` command line flags are passed to the
``sip`` executable to create, for example, the QScintilla bindings as were
passed to create the PyQt bindings.

Starting with v4.10, :attr:`PyQt4.QtCore.PYQT_CONFIGURATION` is a dict that
describes how PyQt was configured.  At the moment it contains a single value
called ``sip_flags`` which is a string containing the appropriate ``-t`` and
``-x`` flags.


The Old Build System
--------------------

.. deprecated:: 4.10

The old PyQt4 build system is an extension of the SIP v4 build system and is
implemented by the :mod:`~PyQt4.pyqtconfig` module.  It can be used by
configuration scripts of other bindings that build on top of PyQt4 and takes
care of the details of the Qt installation.

Note that the :mod:`~PyQt4.pyqtconfig` module is only created if you use
:program:`configure.py` and not if you use :program:`configure-ng.py`.

.. module:: PyQt4.pyqtconfig

.. class:: Configuration(sub_cfg=None)

    This class encapsulates configuration values that can be accessed as
    instance objects.  It is derived from :class:`sipconfig.Configuration`.

    :param sub_cfg:
        an optional list of sub-class configurations.  It should only be used
        by the ``__init__()`` method of a sub-class to append its own
        dictionary of configuration values before passing the list to its
        super-class.

    .. attribute:: pyqt_bin_dir

        The name of the directory where the PyQt4 utilities are installed.

    .. attribute:: pyqt_config_args

        The command line passed to :program:`configure.py` when PyQt4 was
        configured.

    .. attribute:: pyqt_mod_dir

        The name of the directory where the :mod:`PyQt4` Python package is
        installed.

    .. attribute:: pyqt_modules

        A space separated string of installed PyQt4 modules.  The :mod:`Qt`
        module is not included.

    .. attribute:: pyqt_sip_dir

        The name of the base directory where PyQt4's ``.sip`` files are
        installed.  Each module's ``.sip`` files are installed in a
        sub-directory with the same name as the module.

    .. attribute:: pyqt_sip_flags

        A space separated string of the :program:`sip` command line options
        used to build the PyQt4 modules.  These should also be used when
        building bindings that ``%Import`` any PyQt4 modules.

    .. attribute:: pyqt_version

        The PyQt4 version as a 3 part hexadecimal number (e.g. v4.0.1 is
        represented as ``0x040001``).

    .. attribute:: pyqt_version_str

        The PyQt4 version as a string.  For development snapshots it will start
        with ``snapshot-``.

    .. attribute:: qt_data_dir

        The value of ``QLibraryInfo::location(DataPath)`` for the Qt
        installation.

    .. attribute:: qt_archdata_dir

        When building against Qt v5 this is the value of
        ``QLibraryInfo::location(ArchDataPath)``.  When building against Qt v4
        it is the value of ``QLibraryInfo::location(DataPath)``.

    .. attribute:: qt_dir

        The root directory of the Qt installation (normally the directory that
        contains the :file:`bin` directory).

    .. attribute:: qt_edition

        The Qt edition.

    .. attribute:: qt_framework

        Set if Qt is built as a MacOS/X framework.

    .. attribute:: qt_inc_dir

        The value of ``QLibraryInfo::location(HeadersPath)`` for the Qt
        installation.

    .. attribute:: qt_lib_dir

        The value of ``QLibraryInfo::location(LibrariesPath)`` for the Qt
        installation.

    .. attribute:: qt_threaded

        Set if Qt is built with thread support (always set for PyQt4).

    .. attribute:: qt_version

        The Qt version as a 3 part hexadecimal number (e.g. v4.1.2 is
        represented as ``0x040102``).

    .. attribute:: qt_winconfig

        Additional Windows specific configuration.


.. class:: QtAssistantModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtAssistant`
    module.


.. class:: QAxContainerModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QAxContainer`
    module.


.. class:: QtCoreModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtCore` module.


.. class:: QtDBusModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtDBus` module.


.. class:: QtDeclarativeModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtDeclarative`
    module.


.. class:: QtDesignerModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtDesigner`
    module.


.. class:: QtGuiModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtGui` module.


.. class:: QtHelpModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtHelp` module.


.. class:: QtMultimediaModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtMultimedia`
    module.


.. class:: QtNetworkModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtNetwork` module.


.. class:: QtOpenGLModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtOpenGL` module.


.. class:: QtScriptModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtScript` module.


.. class:: QtScriptToolsModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtScriptTools`
    module.


.. class:: QtSqlModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtSql` module.


.. class:: QtSvgModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtSvg` module.


.. class:: QtTestModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtTest` module.


.. class:: QtWebKitModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtWebKit` module.


.. class:: QtXmlModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtXml` module.


.. class:: QtXmlPatternsModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.QtXmlPatterns`
    module.


.. class:: phononModuleMakefile

    This class encapsulates a Makefile to build a SIP generated Python
    extension module that is built on the PyQt4 :mod:`~PyQt4.phonon` module.
