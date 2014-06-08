Installing PyQt4
================

Downloading SIP
---------------

SIP must be installed before building and using PyQt4.  You can get the latest
release of the SIP source code from
http://www.riverbankcomputing.com/software/sip/download.

The SIP documentation can be found at http://pyqt.sourceforge.net/Docs/sip4/.


Downloading PyQt4
-----------------

You can get the latest release of the GPL version of the PyQt4 source code from
http://www.riverbankcomputing.com/software/pyqt/download.

If you are using the commercial version of PyQt4 then you should use the
download instructions which were sent to you when you made your purchase.  You
must also download your license file.


Configuring PyQt4
-----------------

After unpacking the source package (either a ``.tar.gz`` or a ``.zip`` file
depending on your platform) you should then check for any :file:`README` files
that relate to your platform.

If you are using the commercial version of PyQt4 then you must copy your
license file to the :file:`sip` directory.

You need to make sure your environment variables are set properly for your
development environment.

In order to configure the build of PyQt4 you need to run either the
:program:`configure-ng.py` or the :program:`configure.py` script.

:program:`configure.py` is the original configuration script that uses the
build system of SIP v4 (i.e. the :mod:`sip.sipconfig` module).  It will be
supported for the life of PyQt4.

:program:`configure-ng.py` is the new configuration script that uses Qt's
:program:`qmake` program to do all the heavy lifting.  It has the following
advantages:

- a future version will support cross-compilation

- it is the basis of PyQt5's configuration script

- generated Makefiles have an uninstall target

- it will work with SIP v5 (which will have no build system).

Users are encouraged to switch to using :program:`configure-ng.py` in order to
ease the future transition to SIP v5 and/or PyQt5.


Using :program:`configure-ng.py`
................................

.. versionadded:: 4.10.1

The :program:`configure-ng.py` script is used to configure PyQt4 as follows::

    python configure-ng.py

This assumes that the Python interpreter is on your path.  Something like the
following may be appropriate on Windows::

    c:\python33\python configure-ng.py

If you have multiple versions of Python installed then make sure you use the
interpreter for which you wish to build PyQt4 for.

The full set of command line options is:

.. program:: configure-ng.py

.. cmdoption:: --assume-shared

    Normally Qt is checked to see if it has been built as shared libraries.
    Some Linux distributions configure their Qt builds to make this check
    unreliable.  This option ignores the result of the check and assumes that
    Qt has been built as shared libraries.

.. cmdoption:: --bindir <DIR>, -b <DIR>

    The :program:`pyuic4`, :program:`pyrcc4` and :program:`pylupdate4`
    utilities will be installed in the directory ``<DIR>``.

.. cmdoption:: --concatenate, -c

    The C++ source files for a Python module will be concatenated.  This
    results in significantly reduced compilation times.  Most, but not all,
    C++ compilers can handle the large files that result.  See also the
    :option:`--concatenate-split` option.

.. cmdoption:: --concatenate-split <N>, -j <N>

    If the :option:`--concatenate` option is used to concatenate the C++ source
    files then this option determines how many files are created.  The default
    is 1.

.. cmdoption:: --configuration <FILE>

    ``<FILE>`` contains the configuration of the PyQt4 build to be used instead
    of dynamically introspecting the system and is used when cross-compiling.
    The format of ``<FILE>`` will be documented in a later version when
    cross-compilation is fully supported.

.. cmdoption:: --confirm-license

    Using this confirms that you accept the terms of the PyQt4 license.

.. cmdoption:: --consolidate, -g

    Normally each PyQt4 module (except for the :mod:`~PyQt4.Qt` module) is
    linked against the corresponding Qt library.  This option creates a module
    called :mod:`~PyQt4._qt` which is linked against all the required Qt
    libraries and the other modules are stub modules that populate their module
    dictionaries from this one.  This is useful when linking against static Qt
    libraries to eliminate the need to distribute the Qt libraries while
    minimising the memory footprint of the PyQt4 modules.

.. cmdoption:: --dbus <DIR>, -s <DIR>

    The :file:`dbus-python.h` header file of the dbus-python package can be
    found in the directory ``<DIR>/dbus``.

.. cmdoption:: --debug, -u

    The PyQt4 modules will be built with debugging symbols.  On Windows this
    requires that a debug version of Python is installed.

.. cmdoption:: --designer-plugindir <DIR>

    The Python plugin for Qt Designer will be installed in the directory
    ``<DIR>``.

.. cmdoption:: --destdir <DIR>, -d <DIR>

    The PyQt4 Python package will be installed in the directory ``<DIR>``.  The
    default is the Python installation's :file:`site-packages` directory.  If
    you use this option then the :envvar:`PYTHONPATH` environment variable must
    include ``<DIR>``.

.. cmdoption:: --enable <MODULE>, -e <MODULE>

    Normally all PyQt4 modules are enabled and are built if the corresponding
    Qt library can be found.  Using this option only those modules specifically
    enabled will be checked for and built.  The option may be specified any
    number of times.

.. cmdoption:: --help, -h

    Display a help message.

.. cmdoption:: --no-deprecated

    All Qt v4 features that have been deprecated in Qt v5 will be disabled.
    This is useful when porting PyQt4 applications to PyQt5.

.. cmdoption:: --no-designer-plugin

    The Qt Designer plugin will not be built.

.. cmdoption:: --no-docstrings

    The PyQt4 modules will not contain automatically generated docstrings.

.. cmdoption:: --no-qsci-api

    The :file:`PyQt4.api` QScintilla API file is not installed even if
    QScintilla does appear to be installed.

.. cmdoption:: --no-sip-files

    The ``.sip`` files for the PyQt4 modules will not be installed.

.. cmdoption:: --no-timestamp, -T

    Normally the header comments of each generated C/C++ source file includes
    a timestamp corresponding to when the file was generated.  This option
    suppresses the inclusion of the timestamp.

.. cmdoption:: --plugin <PLUGIN>, -t <PLUGIN>

    If Qt has been built as static libraries then the static plugin
    ``<PLUGIN>`` will be linked with the appropriate PyQt4 module.  The option
    may be specified any number of times.

.. cmdoption:: --protected-is-public

    On certain platforms the size of PyQt4 modules can be significantly reduced
    by redefining the C++ ``protected`` keyword as ``public`` during
    compilation.  This option enables this behaviour and is the default on
    Linux and MacOS/X.

.. cmdoption:: --protected-not-public

    The default redefinition of ``protected`` to ``public`` during compilation
    on Linux and MacOS/X is disabled.

.. cmdoption:: --pyuic4-interpreter <FILE>

    ``<FILE>`` is the name of the Python interpreter used in the pyuic4
    wrapper.  The default is platform dependent.

.. cmdoption:: --qmake <FILE>, -q <FILE>

    Qt's :program:`qmake` program is used to determine how your Qt installation
    is laid out.  Normally :program:`qmake` is found on your :envvar:`PATH`.
    This option can be used to specify a particular instance of
    :program:`qmake` to use.  This option is not available on Windows where
    :program:`qmake` must be on :envvar:`PATH`.

.. cmdoption:: --qsci-api, -a

    The :file:`PyQt4.api` QScintilla API file is installed even if QScintilla
    does not appear to be installed.  This option is implied if the
    :option:`--qsci-api-destdir` option is specified.

.. cmdoption:: --qsci-api-destdir <DIR>, -n <DIR>

    The QScintilla API file will be installed in the :file:`python`
    subdirectory of the :file:`api` subdirectory of the directory ``<DIR>``.

.. cmdoption:: --sip <FILE>

    The :program:`sip` program is used to generate PyQt4's C++ source code.
    Normally :program:`sip` is found on your :envvar:`PATH`.  This option can
    be used to specify a particular instance of :program:`sip` to use.

.. cmdoption:: --sip-incdir <DIR>

    The ``sip.h`` header file can be found in the directory ``<DIR>``.

.. cmdoption:: --sipdir <DIR>, -v <DIR>

    The ``.sip`` files for the PyQt4 modules will be installed in the directory
    ``<DIR>``.

.. cmdoption:: --spec <SPEC>

    The argument ``-spec SPEC`` will be passed to :program:`qmake`.  The
    default behaviour is platform specific.  On Windows
    :program:`configure-ng.py` will choose the value that is correct for the
    version of Python that is being used.  (However if you have built Python
    yourself then you may need to explicitly specify ``<SPEC>``.)  On MacOS
    :program:`configure-ng.py` will try and avoid ``macx-xcode`` if possible.)

.. cmdoption:: --static, -k

    The PyQt4 modules will be built as static libraries.  This is useful when
    building a custom interpreter with the PyQt4 modules built in to the
    interpreter.

.. cmdoption:: --trace, -r

    The generated PyQt4 modules contain additional tracing code that is enabled
    using SIP's :func:`sip.settracemask` function.

.. cmdoption:: --vendorid, -i

    The checking of signed Python interpreters using the `VendorID
    <http://www.riverbankcomputing.com/software/vendorid/>`__ package is
    enabled.  See also the :option:`--vendorid-incdir` and
    :option:`--vendorid-libdir` options and :ref:`ref-deploy-commercial`.

.. cmdoption:: --vendorid-incdir <DIR>, -l <DIR>

    The header file of the VendorID package can be found in the directory
    ``<DIR>``.

.. cmdoption:: --vendorid-libdir <DIR>, -m <DIR>

    The library of the VendorID package can be found in the directory
    ``<DIR>``.

.. cmdoption:: --verbose, -w

    Compiler commands and any output issued during configuration is displayed
    instead of being suppressed.  Use this if :program:`configure-ng.py` is
    having problems to see what exactly is going wrong.

.. cmdoption:: --version

    Display the PyQt4 version number.

Any remaining command line arguments are expected to be in the form
``name=value`` or ``name+=value``.  Such arguments are added to any
:program:`qmake` ``.pro`` file created by :program:`configure-ng.py`.


Using :program:`configure.py`
.............................

The :program:`configure.py` script is used to configure PyQt4 as follows::

    python configure.py

This assumes that the Python interpreter is on your path.  Something like the
following may be appropriate on Windows::

    c:\python33\python configure.py

If you have multiple versions of Python installed then make sure you use the
interpreter for which you wish to build PyQt4 for.

The full set of command line options is:

.. program:: configure.py

.. cmdoption:: --assume-shared

    Normally Qt is checked to see if it has been built as shared libraries.
    Some Linux distributions configure their Qt builds to make this check
    unreliable.  This option ignores the result of the check and assumes that
    Qt has been built as shared libraries.

.. cmdoption:: --bindir <DIR>, -b <DIR>

    The :program:`pyuic4`, :program:`pyrcc4` and :program:`pylupdate4`
    utilities will be installed in the directory ``<DIR>``.

.. cmdoption:: --concatenate, -c

    The C++ source files for a Python module will be concatenated.  This
    results in significantly reduced compilation times.  Most, but not all,
    C++ compilers can handle the large files that result.  See also the
    :option:`--concatenate-split` option.

.. cmdoption:: --concatenate-split <N>, -j <N>

    If the :option:`--concatenate` option is used to concatenate the C++ source
    files then this option determines how many files are created.  The default
    is 1.

.. cmdoption:: --confirm-license

    Using this confirms that you accept the terms of the PyQt4 license.

.. cmdoption:: --consolidate, -g

    Normally each PyQt4 module (except for the :mod:`~PyQt4.Qt` module) is
    linked against the corresponding Qt library.  This option creates a module
    called :mod:`~PyQt4._qt` which is linked against all the required Qt
    libraries and the other modules are stub modules that populate their module
    dictionaries from this one.  This is useful when linking against static Qt
    libraries to eliminate the need to distribute the Qt libraries while
    minimising the memory footprint of the PyQt4 modules.

.. cmdoption:: --dbus <DIR>, -s <DIR>

    The :file:`dbus-python.h` header file of the dbus-python package can be
    found in the directory ``<DIR>/dbus``.

.. cmdoption:: --debug, -u

    The PyQt4 modules will be built with debugging symbols.  On Windows this
    requires that a debug version of Python is installed.

.. cmdoption:: --destdir <DIR>, -d <DIR>

    The PyQt4 Python package will be installed in the directory ``<DIR>``.  The
    default is the Python installation's :file:`site-packages` directory.  If
    you use this option then the :envvar:`PYTHONPATH` environment variable must
    include ``<DIR>``.

.. cmdoption:: --enable <MODULE>, -e <MODULE>

    Normally all PyQt4 modules are enabled and are built if the corresponding
    Qt library can be found.  Using this option only those modules specifically
    enabled will be checked for and built.  The option may be specified any
    number of times.

.. cmdoption:: --help, -h

    Display a help message.

.. cmdoption:: --no-deprecated

    All Qt v4 features that have been deprecated in Qt v5 will be disabled.
    This is useful when porting PyQt4 applications to PyQt5.

.. cmdoption:: --no-designer-plugin

    The Qt Designer plugin will not be built.

.. cmdoption:: --no-docstrings

    The PyQt4 modules will not contain automatically generated docstrings.

.. cmdoption:: --no-qsci-api

    The :file:`PyQt4.api` QScintilla API file is not installed even if
    QScintilla does appear to be installed.

.. cmdoption:: --no-sip-files

    The ``.sip`` files for the PyQt4 modules will not be installed.

.. cmdoption:: --no-timestamp, -T

    Normally the header comments of each generated C/C++ source file includes
    a timestamp corresponding to when the file was generated.  This option
    suppresses the inclusion of the timestamp.

.. cmdoption:: --plugin <PLUGIN>, -t <PLUGIN>

    If Qt has been built as static libraries then the static plugin
    ``<PLUGIN>`` will be linked with the appropriate PyQt4 module.  The option
    may be specified any number of times.

.. cmdoption:: --plugin-destdir <DIR>, -p <DIR>

    The Qt Designer plugin that manages plugins implemented in Python will be
    installed in the :file:`designer` subdirectory of the directory ``<DIR>``.

.. cmdoption:: --protected-is-public

    On certain platforms the size of PyQt4 modules can be significantly reduced
    by redefining the C++ ``protected`` keyword as ``public`` during
    compilation.  This option enables this behaviour and is the default on
    Linux and MacOS/X.

.. cmdoption:: --protected-not-public

    The default redefinition of ``protected`` to ``public`` during compilation
    on Linux and MacOS/X is disabled.

.. cmdoption:: --qmake <FILE>, -q <FILE>

    Qt's :program:`qmake` program is used to determine how your Qt installation
    is laid out.  Normally :program:`qmake` is found on your :envvar:`PATH`.
    This option can be used to specify a particular instance of
    :program:`qmake` to use.  This option is not available on Windows.

.. cmdoption:: --qsci-api, -a

    The :file:`PyQt4.api` QScintilla API file is installed even if QScintilla
    does not appear to be installed.  This option is implied if the
    :option:`--qsci-api-destdir` option is specified.

.. cmdoption:: --qsci-api-destdir <DIR>, -n <DIR>

    The QScintilla API file will be installed in the :file:`python`
    subdirectory of the :file:`api` subdirectory of the directory ``<DIR>``.

.. cmdoption:: --sipdir <DIR>, -v <DIR>

    The ``.sip`` files for the PyQt4 modules will be installed in the directory
    ``<DIR>``.

.. cmdoption:: --static, -k

    The PyQt4 modules will be built as static libraries.  This is useful when
    building a custom interpreter with the PyQt4 modules built in to the
    interpreter.

.. cmdoption:: --trace, -r

    The generated PyQt4 modules contain additional tracing code that is enabled
    using SIP's :func:`sip.settracemask` function.

.. cmdoption:: --use-arch <ARCH>

    When :program:`pyuic4` calls the Python interpreter on MacOS it will be run
    using the architecture ``<ARCH>``.  See the section :ref:`ref-macos`.

.. cmdoption:: --vendorid, -i

    The checking of signed Python interpreters using the `VendorID
    <http://www.riverbankcomputing.com/software/vendorid/>`__ package is
    enabled.  See also the :option:`--vendorid-incdir` and
    :option:`--vendorid-libdir` options and :ref:`ref-deploy-commercial`.

.. cmdoption:: --vendorid-incdir <DIR>, -l <DIR>

    The header file of the VendorID package can be found in the directory
    ``<DIR>``.

.. cmdoption:: --vendorid-libdir <DIR>, -m <DIR>

    The library of the VendorID package can be found in the directory
    ``<DIR>``.

.. cmdoption:: --verbose, -w

    Compiler commands and any output issued during configuration is displayed
    instead of being suppressed.  Use this if :program:`configure.py` is having
    problems to see what exactly is going wrong.

.. cmdoption:: --version

    Display the PyQt4 version number.


.. _ref-macos:

Configuring SIP and PyQt4 for MacOS
...................................

Note that this section only applies if you are using the
:program:`configure.py` script to configure PyQt4.  The
:program:`configure-ng.py` script leaves it to Qt's :program:`qmake` program to
handle the details.  :program:`configure-ng.py` does not support the creation
of universal binaries.

Building applications for MacOS can be a complex process.  Typically the
following need to be taken into account:

- the architectures (i.e. i386, x86_64, ppc) that you want to support

- the earliest version of MacOS you want to support (i.e. the deployment
  target)

- the version of the SDK you want to use.

If you are using a binary installer for Python and/or Qt then you also need to
consider how they have been built regarding the above, and what bugs they have.

SIP's and PyQt4's :program:`configure.py` scripts provide the necessary command
line options to allow the correct configurations to be specified - the trick is
to work out which options to use depending on the versions of Python and Qt you
have installed.

SIP provides the following command line options to its :program:`configure.py`
script.

- ``--arch <ARCH>`` specifies the target architecture and may be specified a
  number of times.

- ``--universal`` is a shortcut for ``--arch i386 --arch ppc``.

- ``--deployment-target <VERSION>`` specifies the earliest version of MacOS you
  want to support.  This sets the :envvar:`MACOSX_DEPLOYMENT_TARGET`
  environment variable and should be used rather than setting the environment
  variable in the shell (to work around bugs in some versions of Python).

- ``--sdk <SDK>`` specifies the SDK to use.

PyQt4 provides the :option:`--use-arch <configure.py --use-arch>` option that
specifies which architecture certain PyQt4 tools (actually only
:program:`pyuic4` at the moment) will use when running Python.  For example, if
your Qt installation is 32 bits, and your Python installation is 32 bits and
64 bits then you will need to specify ``--use-arch i386`` to ensure that
:program:`pyuic4` runs the 32 bit version of Python.


Building PyQt4
--------------

The next step is to build PyQt4 by running your platform's :program:`make`
command.  For example::

    make

The final step is to install PyQt4 by running the following command::

    make install

(Depending on your system you may require root or administrator privileges.)

This will install the various PyQt4 components.
