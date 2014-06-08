# -*- Mode: Python -*-

import os
import unittest

import glib
import gobject
import gio


class TestSocket(unittest.TestCase):
    def setUp(self):
        self.sock = gio.Socket(gio.SOCKET_FAMILY_IPV4,
                               gio.SOCKET_TYPE_STREAM,
                               gio.SOCKET_PROTOCOL_TCP)

    def test_socket_condition_check(self):
        check = self.sock.condition_check(glib.IO_OUT)
        self.failUnless(isinstance(check, gobject.GFlags))
        self.failUnlessEqual(check, glib.IO_OUT | glib.IO_HUP)

    def test_socket_condition_wait(self):
        res = self.sock.condition_wait(glib.IO_OUT)
        self.failUnless(res)

    def tearDown(self):
        self.sock.close()

class TestSocketAddress(unittest.TestCase):
    def test_socket_address_enumerator_next_async(self):
        def callback(enumerator, result):
            try:
                address = enumerator.next_finish(result)
                self.failUnless(isinstance(address, gio.SocketAddress))
            finally:
                loop.quit()

        socket = gio.NetworkAddress("www.pygtk.org", 80)
        enumerator = socket.enumerate()
        enumerator.next_async(callback)

        loop = glib.MainLoop()
        loop.run()

class TestSocketListener(unittest.TestCase):
    def test_socket_listener_add_address(self):
        address = gio.inet_address_new_from_string("127.0.0.1")
        inetsock = gio.InetSocketAddress(address, 1024)
        
        listener = gio.SocketListener()
        effective = listener.add_address(inetsock, gio.SOCKET_TYPE_STREAM, gio.SOCKET_PROTOCOL_TCP)
        self.failUnless(isinstance(effective, gio.InetSocketAddress))

    def test_socket_listener_accept(self):
        address = gio.inet_address_new_from_string("127.0.0.1")
        inetsock = gio.InetSocketAddress(address, 1024)

        listener = gio.SocketListener()
        listener.add_address(inetsock, gio.SOCKET_TYPE_STREAM, gio.SOCKET_PROTOCOL_TCP)

        client = gio.SocketClient()
        client.connect_to_host("127.0.0.1:1024", 1024)

        connection, source = listener.accept(cancellable=None)
        self.failUnless(isinstance(connection, gio.TcpConnection))

    def test_socket_listener_accept_socket(self):
        address = gio.inet_address_new_from_string("127.0.0.1")
        inetsock = gio.InetSocketAddress(address, 1024)

        listener = gio.SocketListener()
        listener.add_address(inetsock, gio.SOCKET_TYPE_STREAM, gio.SOCKET_PROTOCOL_TCP)

        client = gio.SocketClient()
        client.connect_to_host("127.0.0.1:1024", 1024)

        socket, source = listener.accept_socket(cancellable=None)
        self.failUnless(isinstance(socket, gio.Socket))

    def test_socket_listener_accept_async(self):
        def callback(listener, result):
            try:
                connection, source = listener.accept_finish(result)
                self.failUnless(isinstance(connection, gio.TcpConnection))
            finally:
                loop.quit()

        address = gio.inet_address_new_from_string("127.0.0.1")
        inetsock = gio.InetSocketAddress(address, 1024)
        
        listener = gio.SocketListener()
        listener.add_address(inetsock,
                             gio.SOCKET_TYPE_STREAM,
                             gio.SOCKET_PROTOCOL_TCP)

        client = gio.SocketClient()
        client.connect_to_host("127.0.0.1:1024", 1024)
        
        listener.accept_async(callback)

        loop = glib.MainLoop()
        loop.run()

    def test_socket_listener_accept_socket_async(self):
        def callback(listener, result):
            try:
                socket, source = listener.accept_socket_finish(result)
                self.failUnless(isinstance(socket, gio.Socket))
            finally:
                loop.quit()

        address = gio.inet_address_new_from_string("127.0.0.1")
        inetsock = gio.InetSocketAddress(address, 1024)
        
        listener = gio.SocketListener()
        listener.add_address(inetsock,
                             gio.SOCKET_TYPE_STREAM,
                             gio.SOCKET_PROTOCOL_TCP)

        client = gio.SocketClient()
        client.connect_to_host("127.0.0.1:1024", 1024)
        
        listener.accept_socket_async(callback)

        loop = glib.MainLoop()
        loop.run()
