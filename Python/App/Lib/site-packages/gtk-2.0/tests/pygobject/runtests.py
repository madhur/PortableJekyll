#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import glob
import unittest

os.environ['PYGTK_USE_GIL_STATE_API'] = ''
sys.path.insert(0, os.path.dirname(__file__))
sys.argv.append('--g-fatal-warnings')

import gobject
gobject.threads_init()


SKIP_FILES = ['runtests',
              'test_gio',           # python crash
              'test_gresolver',     # python crash
              'test_gsocket',       # blocks on test_socket_condition_wait
              'test_mainloop',      # no os.fork on windows
              'test_subprocess']    # blocks on testChildWatch


if __name__ == '__main__':
    testdir = os.path.split(os.path.abspath(__file__))[0]
    os.chdir(testdir)

    def gettestnames():
        files = glob.glob('*.py')
        names = map(lambda x: x[:-3], files)
        map(names.remove, SKIP_FILES)
        return names

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for name in gettestnames():
        try:
            suite.addTest(loader.loadTestsFromName(name))
        except Exception, e:
            print 'Could not load %s: %s' % (name, e)

    testRunner = unittest.TextTestRunner()
    testRunner.verbosity = 2
    testRunner.run(suite)
