# -*- Mode: Python -*-

import unittest

import glib
import testhelper


class TestThread(unittest.TestCase):
    def setUp(self):
        self.main = glib.MainLoop()

    def from_thread_cb(self, test, enum):
        assert test == self.obj
        assert int(enum) == 0
        assert type(enum) != int

    def idle_cb(self):
        self.obj = testhelper.get_test_thread()
        self.obj.connect('from-thread', self.from_thread_cb)
        self.obj.emit('emit-signal')

    def testExtensionModule(self):
        glib.idle_add(self.idle_cb)
        glib.timeout_add(50, self.timeout_cb)
        self.main.run()

    def timeout_cb(self):
        self.main.quit()
