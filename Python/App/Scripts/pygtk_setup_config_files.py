#!/usr/bin/env python


import os
import sys
import subprocess


if len(sys.argv) == 3:
    # Run from the all-in-one installer
    TARGETDIR = os.path.abspath(sys.argv[1].strip())
    TMPDIR = os.path.abspath(sys.argv[2].strip())

    # We'll redirect output to a logfile
    sys.stdout = open(os.path.join(TMPDIR, 'pygtk_setup_config_files.log'), 'w')
    sys.stderr = open(os.path.join(TMPDIR, 'pygtk_setup_config_files.log'), 'w')

    # And need to make sure Popen calls point stderr to subprocess.PIPE or
    # suffer ugly popup "Command Prompts" during install...
    stderr = subprocess.PIPE
else:
    # Run from the Scripts directory
    TARGETDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    stderr = sys.stderr


def redirect(executable, configile):
    output=open(configfile, 'w')
    subprocess.Popen(executable, shell=True, stdout=output, stderr=stderr)
    output.close()


if __name__ == '__main__':
    # gdk-pixbuf-query-loaders
    executable = os.path.join(TARGETDIR, 'Lib', 'site-packages', 'gtk-2.0',
                              'runtime', 'bin', 'gdk-pixbuf-query-loaders.exe')
    configfile = os.path.join(TARGETDIR, 'Lib', 'site-packages', 'gtk-2.0',
                              'runtime', 'lib', 'gdk-pixbuf-2.0', '2.10.0',
                              'loaders.cache')
    redirect(executable, configfile)

    # gtk-query-immodules
    executable = os.path.join(TARGETDIR, 'Lib', 'site-packages', 'gtk-2.0',
                              'runtime', 'bin', 'gtk-query-immodules-2.0.exe')
    configfile = os.path.join(TARGETDIR, 'Lib', 'site-packages', 'gtk-2.0',
                              'runtime', 'etc', 'gtk-2.0', 'gtk.immodules')
    redirect(executable, configfile)

    # pango-querymodules
    executable = os.path.join(TARGETDIR, 'Lib', 'site-packages', 'gtk-2.0',
                              'runtime', 'bin', 'pango-querymodules.exe')
    configfile = os.path.join(TARGETDIR, 'Lib', 'site-packages', 'gtk-2.0',
                              'runtime', 'etc', 'pango', 'pango.modules')
    redirect(executable, configfile)

    sys.exit(0)
