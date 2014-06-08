# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab

import unittest

import sys
sys.path.insert(0, "../")

import gobject
from gi.repository import GLib
from gi.repository import Gio

class TestGDBusClient(unittest.TestCase):
    def setUp(self):
        self.bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)

        self.dbus_proxy = Gio.DBusProxy.new_sync(self.bus,
                Gio.DBusProxyFlags.NONE, None, 
                'org.freedesktop.DBus',
                '/org/freedesktop/DBus',
                'org.freedesktop.DBus', None)

    def test_native_calls_sync(self):
        result = self.dbus_proxy.call_sync('ListNames', None, 
                Gio.DBusCallFlags.NO_AUTO_START, 500, None)
        self.assertTrue(isinstance(result, GLib.Variant))
        result = result.unpack()[0] # result is always a tuple
        self.assertTrue(len(result) > 1)
        self.assertTrue('org.freedesktop.DBus' in result)

        result = self.dbus_proxy.call_sync('GetNameOwner', 
                GLib.Variant('(s)', ('org.freedesktop.DBus',)),
                Gio.DBusCallFlags.NO_AUTO_START, 500, None)
        self.assertTrue(isinstance(result, GLib.Variant))
        self.assertEqual(type(result.unpack()[0]), type(''))

    def test_native_calls_sync_errors(self):
        # error case: invalid argument types
        try:
            self.dbus_proxy.call_sync('GetConnectionUnixProcessID', None,
                    Gio.DBusCallFlags.NO_AUTO_START, 500, None)
            self.fail('call with invalid arguments should raise an exception')
        except Exception:
            etype, e = sys.exc_info()[:2]
            self.assertTrue('InvalidArgs' in str(e))

        # error case: invalid argument
        try:
            self.dbus_proxy.call_sync('GetConnectionUnixProcessID', 
                    GLib.Variant('(s)', (' unknown',)),
                    Gio.DBusCallFlags.NO_AUTO_START, 500, None)
            self.fail('call with invalid arguments should raise an exception')
        except Exception:
            etype, e = sys.exc_info()[:2]

            self.assertTrue('NameHasNoOwner' in str(e))

        # error case: unknown method
        try:
            self.dbus_proxy.call_sync('UnknownMethod', None,
                    Gio.DBusCallFlags.NO_AUTO_START, 500, None)
            self.fail('call for unknown method should raise an exception')
        except Exception:
            etype, e = sys.exc_info()[:2]

            self.assertTrue('UnknownMethod' in str(e))

    def test_native_calls_async(self):
        def call_done(obj, result, user_data):
            user_data['result'] = obj.call_finish(result)
            user_data['main_loop'].quit()

        main_loop = gobject.MainLoop()
        data = {'main_loop': main_loop}
        self.dbus_proxy.call('ListNames', None, 
                Gio.DBusCallFlags.NO_AUTO_START, 500, None,
                call_done, data)
        main_loop.run()

        self.assertTrue(isinstance(data['result'], GLib.Variant))
        result = data['result'].unpack()[0] # result is always a tuple
        self.assertTrue(len(result) > 1)
        self.assertTrue('org.freedesktop.DBus' in result)

    def test_native_calls_async_errors(self):
        def call_done(obj, result, user_data):
            try:
                obj.call_finish(result)
                self.fail('call_finish() for unknown method should raise an exception')
            except Exception:
                etype, e = sys.exc_info()[:2]

                self.assertTrue('UnknownMethod' in str(e))
            finally:
                user_data['main_loop'].quit()

        main_loop = gobject.MainLoop()
        data = {'main_loop': main_loop}
        self.dbus_proxy.call('UnknownMethod', None,
                Gio.DBusCallFlags.NO_AUTO_START, 500, None, call_done, data)
        main_loop.run()

    def test_python_calls_sync(self):
        # single value return tuples get unboxed to the one element
        result = self.dbus_proxy.ListNames('()')
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result) > 1)
        self.assertTrue('org.freedesktop.DBus' in result)

        result = self.dbus_proxy.GetNameOwner('(s)', 'org.freedesktop.DBus')
        self.assertEqual(type(result), type(''))

        # empty return tuples get unboxed to None
        self.assertEqual(self.dbus_proxy.ReloadConfig('()'), None)

        # multiple return values remain a tuple; unfortunately D-BUS itself
        # does not have any method returning multiple results, so try talking
        # to notification-daemon (and don't fail the test if it does not exist)
        try:
            notification_daemon = Gio.DBusProxy.new_sync(self.bus,
                    Gio.DBusProxyFlags.NONE, None,
                    'org.freedesktop.Notifications',
                    '/org/freedesktop/Notifications',
                    'org.freedesktop.Notifications', None)
            result = notification_daemon.GetServerInformation('()')
            self.assertTrue(isinstance(result, tuple))
            self.assertEqual(len(result), 4)
            for i in result:
                self.assertEqual(type(i), type(''))
        except Exception:
            etype, e = sys.exc_info()[:2]

            if 'Error.ServiceUnknown' not in str(e):
                raise

        # test keyword argument; timeout=0 will fail immediately
        try:
            self.dbus_proxy.GetConnectionUnixProcessID('()', timeout=0)
            self.fail('call with timeout=0 should raise an exception')
        except Exception:
            etype, e = sys.exc_info()[:2]

            self.assertTrue('Timeout' in str(e), str(e))

    def test_python_calls_sync_noargs(self):
        # methods without arguments don't need an explicit signature
        result = self.dbus_proxy.ListNames()
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result) > 1)
        self.assertTrue('org.freedesktop.DBus' in result)

    def test_python_calls_sync_errors(self):
        # error case: invalid argument types
        try:
            self.dbus_proxy.GetConnectionUnixProcessID('()')
            self.fail('call with invalid arguments should raise an exception')
        except Exception:
            etype, e = sys.exc_info()[:2]

            self.assertTrue('InvalidArgs' in str(e), str(e))

        try:
            self.dbus_proxy.GetConnectionUnixProcessID(None, 'foo')
            self.fail('call with None signature should raise an exception')
        except TypeError as e:
            self.assertTrue('signature' in str(e), str(e))

    def test_python_calls_async(self):
        def call_done(obj, result, user_data):
            user_data['result'] = result
            user_data['main_loop'].quit()

        main_loop = gobject.MainLoop()
        data = {'main_loop': main_loop}
        self.dbus_proxy.ListNames('()', result_handler=call_done,
                user_data=data)
        main_loop.run()

        result = data['result']
        self.assertEqual(type(result), type([]))
        self.assertTrue(len(result) > 1)
        self.assertTrue('org.freedesktop.DBus' in result)

    def test_python_calls_async_error_result(self):
        # when only specifying a result handler, this will get the error
        def call_done(obj, result, user_data):
            user_data['result'] = result
            user_data['main_loop'].quit()

        main_loop = gobject.MainLoop()
        data = {'main_loop': main_loop}
        self.dbus_proxy.ListNames('(s)', 'invalid_argument',
                result_handler=call_done, user_data=data)
        main_loop.run()

        self.assertTrue(isinstance(data['result'], Exception))
        self.assertTrue('InvalidArgs' in str(data['result']), str(data['result']))

    def test_python_calls_async_error(self):
        # when specifying an explicit error handler, this will get the error
        def call_done(obj, result, user_data):
            user_data['main_loop'].quit()
            self.fail('result handler should not be called')

        def call_error(obj, error, user_data):
            user_data['error'] = error
            user_data['main_loop'].quit()

        main_loop = gobject.MainLoop()
        data = {'main_loop': main_loop}
        self.dbus_proxy.ListNames('(s)', 'invalid_argument',
                result_handler=call_done, error_handler=call_error,
                user_data=data)
        main_loop.run()

        self.assertTrue(isinstance(data['error'], Exception))
        self.assertTrue('InvalidArgs' in str(data['error']), str(data['error']))

