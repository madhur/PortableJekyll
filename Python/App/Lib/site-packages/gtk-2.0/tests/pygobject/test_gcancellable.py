# -*- Mode: Python -*-

import unittest

import glib
import gio


class TestResolver(unittest.TestCase):
    def setUp(self):
        self.cancellable = gio.Cancellable()
    
    def test_make_poll_fd(self):
        poll = self.cancellable.make_pollfd()
        self.failUnless(isinstance(poll, glib.PollFD))
