# -*- coding: utf-8 -*-
u"""Release data for the pyreadline project.

$Id$"""

#*****************************************************************************
#       Copyright (C) 2006  Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#*****************************************************************************

# Name of the package for release purposes.  This is the name which labels
# the tarballs and RPMs made by distutils, so it's best to lowercase it.
name = u'pyreadline'

# For versions with substrings (like 0.6.16.svn), use an extra . to separate
# the new substring.  We have to avoid using either dashes or underscores,
# because bdist_rpm does not accept dashes (an RPM) convention, and
# bdist_deb does not accept underscores (a Debian convention).

branch = u''

version = u'1.7.1'

revision = u'$Revision$'

description = u"A python implmementation of GNU readline."

long_description = \
u"""
The pyreadline package is a python implementation of GNU readline functionality
it is based on the ctypes based UNC readline package by Gary Bishop. 
It is not complete. It has been tested for use with windows 2000 and windows xp.

Version 1.7.1 includes fixes for 64-bit windows, thanks to Christoph Gohlke for
helping out.

Version 1.7 will be the last release with compatibility with 2.4 and 2.5. The next
major release will target 2.6, 2.7 and 3.x. The 1.7 series will only receive bugfixes
from now on.

Features:
 *  keyboard text selection and copy/paste
 *  Shift-arrowkeys for text selection
 *  Control-c can be used for copy activate with allow_ctrl_c(True) in config file
 *  Double tapping ctrl-c will raise a KeyboardInterrupt, use ctrl_c_tap_time_interval(x)
    where x is your preferred tap time window, default 0.3 s.
 *  paste pastes first line of content on clipboard. 
 *  ipython_paste, pastes tab-separated data as list of lists or numpy array if all data is numeric
 *  paste_mulitline_code pastes multi line code, removing any empty lines.
 
 
 The latest development version is always available at the IPython subversion
 repository_.

.. _repository:
 """

license = u'BSD'

authors = {u'Jorgen' : (u'Jorgen Stenarson',u'jorgen.stenarson@bostream.nu'),
           u'Gary':    (u'Gary Bishop', ''),         
           u'Jack':    (u'Jack Trainor', ''),         
           }

url = u'http://ipython.scipy.org/moin/PyReadline/Intro'

download_url = u'https://launchpad.net/pyreadline/+download'

platforms = [u'Windows XP/2000/NT',
             u'Windows 95/98/ME']

keywords = [u'readline',
            u'pyreadline']

classifiers = [u'Development Status :: 5 - Production/Stable',
               u'Environment :: Console',
               u'Operating System :: Microsoft :: Windows',
               u'License :: OSI Approved :: BSD License',
               u'Programming Language :: Python :: 2.4',
               u'Programming Language :: Python :: 2.5',
               u'Programming Language :: Python :: 2.6',
               u'Programming Language :: Python :: 2.7',
               ]
               
               
