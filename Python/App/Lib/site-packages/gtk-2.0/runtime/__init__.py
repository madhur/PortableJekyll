# -*- coding: utf-8 -*-


import os
import sys

from ctypes import windll
from ctypes import cdll
from ctypes.util import find_msvcrt


def _putenv(name, value):
    '''
    :param name: environment variable name
    :param value: environment variable value

    This function ensures that changes to an environment variable are applied
    to each copy of the environment variables used by a process. Starting from
    Python 2.4, os.environ changes only apply to the copy Python keeps (os.environ)
    and are no longer automatically applied to the other copies for the process.

    On Microsoft Windows, each process has multiple copies of the environment
    variables, one managed by the OS and one managed by the C library. We also
    need to take care of the fact that the C library used by Python is not
    necessarily the same as the C library used by PyGTK and friends. This because
    the latest releases of PyGTK and friends are built with mingw32 and are thus
    linked against msvcrt.dll. The official GTK+ binaries have always been built
    in this way.
    '''

    # Update Python's copy of the environment variables
    os.environ[name] = value

    # Update the copy maintained by Windows (so SysInternals Process Explorer sees it)
    try:
        result = windll.kernel32.SetEnvironmentVariableW(name, value)
        if result == 0: raise Warning
    except Exception:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: "kernel32.SetEnvironmentVariableW" failed\n')
            sys.stderr.flush()
    else:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: "kernel32.SetEnvironmentVariableW" successful\n')
            sys.stderr.flush()

    # Update the copy maintained by msvcrt (used by GTK+ runtime)
    try:
        result = cdll.msvcrt._putenv('%s=%s' % (name, value))
        if result != 0: raise Warning
    except Exception:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: "msvcrt._putenv" failed\n')
            sys.stderr.flush()
    else:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: "msvcrt._putenv" successful\n')
            sys.stderr.flush()

    # Update the copy maintained by whatever c runtime is used by Python
    try:
        msvcrt = find_msvcrt()
        msvcrtname = str(msvcrt).split('.')[0] if '.' in msvcrt else str(msvcrt)
        result = cdll.LoadLibrary(msvcrt)._putenv('%s=%s' % (name, value))
        if result != 0: raise Warning
    except Exception:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: "%s._putenv" failed\n' % msvcrtname)
            sys.stderr.flush()
    else:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: "%s._putenv" successful\n' % msvcrtname)
            sys.stderr.flush()


if sys.platform == 'win32' or sys.platform == 'nt':
    RUNTIME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bin'))
    PATH = os.environ['PATH'].split(os.pathsep)
    ABSPATH = [os.path.abspath(x) for x in PATH]

    if ABSPATH[0] != RUNTIME:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: prepending "%s" to PATH\n' % RUNTIME)
            sys.stderr.write('* pygtk-runtime: original PATH="%s"\n' % os.pathsep.join(PATH))
            sys.stderr.flush()

        PATH.insert(0, RUNTIME)
        _putenv('PATH', os.pathsep.join(PATH))

        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: modified PATH="%s"\n' % os.pathsep.join(PATH))
    else:
        if sys.flags.verbose:
            sys.stderr.write('* pygtk-runtime: "%s" already on PATH\n' % RUNTIME)
            sys.stderr.flush()
