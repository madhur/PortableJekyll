# -*- Mode: Python -*-

import sys
import unittest

import glib


class TestProcess(unittest.TestCase):

    def _child_watch_cb(self, pid, condition, data):
        self.data = data
        self.loop.quit()

    def testChildWatch(self):
        self.data = None
        self.loop = glib.MainLoop()
        argv = [sys.executable, '-c', 'import sys']
        pid, stdin, stdout, stderr = glib.spawn_async(
            argv, flags=glib.SPAWN_DO_NOT_REAP_CHILD)
        pid.close()
        glib.child_watch_add(pid, self._child_watch_cb, 12345)
        self.loop.run()
        self.assertEqual(self.data, 12345)
