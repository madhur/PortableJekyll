#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import glob
import unittest

import common


SKIP_FILES = ['runtests',
              'common']
#              'test_glade']     # python crash


if __name__ == '__main__':
    dir = os.path.split(os.path.abspath(__file__))[0]
    os.chdir(dir)

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
