# -*- coding: utf-8 -*-


import os
import sys

import pygtk
pygtk.require('2.0')
import gobject

sys.path.insert(0, os.path.dirname(__file__))
sys.argv.append('--g-fatal-warnings')

import atk
import pango
import gtk
import gtk.gdk

try:
    import gtk.glade
except ImportError:
    print ('* gtk.glade is not available.')

os.environ['PYGTK_USE_GIL_STATE_API'] = ''
gobject.threads_init()
