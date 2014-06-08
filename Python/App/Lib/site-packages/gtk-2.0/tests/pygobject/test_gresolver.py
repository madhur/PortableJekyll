# -*- Mode: Python -*-

import unittest

import glib
import gio


class TestResolver(unittest.TestCase):
    def setUp(self):
        self.resolver = gio.resolver_get_default()

    def test_resolver_lookup_by_name(self):
        addresses = self.resolver.lookup_by_name("pygtk.org", cancellable=None)
        self.failUnless(isinstance(addresses[0], gio.InetAddress))

    def test_resolver_lookup_by_address(self):
        address = gio.inet_address_new_from_string("8.8.8.8")
        dns = self.resolver.lookup_by_address(address, cancellable=None)
        self.failUnlessEqual(dns, "google-public-dns-a.google.com")
    
    def test_resolver_lookup_by_name_async(self):
        def callback(resolver, result):
            try:
                addresses = resolver.lookup_by_name_finish(result)
                self.failUnless(isinstance(addresses[0], gio.InetAddress))
            finally:
                loop.quit()

        self.resolver.lookup_by_name_async(callback, "pygtk.org")

        loop = glib.MainLoop()
        loop.run()

    def test_resolver_lookup_by_address_async(self):
        def callback(resolver, result):
            try:
                dns = resolver.lookup_by_address_finish(result)
                self.failUnlessEqual(dns, "google-public-dns-b.google.com")
            finally:
                loop.quit()

        address = gio.inet_address_new_from_string("8.8.4.4")
        self.resolver.lookup_by_address_async(callback, address)

        loop = glib.MainLoop()
        loop.run()

""" Commented out because this requires an active internet connection and a
    router that supports SRV lookups

    def test_resolver_lookup_service(self):
        targets = self.resolver.lookup_service("xmpp-client", "tcp", "google.com")
        self.failUnless(isinstance(targets[0], gio.SrvTarget))

    def test_resolver_lookup_service_async(self):
        def callback(resolver, result):
            try:
                targets = resolver.lookup_service_finish(result)
                self.failUnless(isinstance(targets[0], gio.SrvTarget))
            finally:
                loop.quit()

        self.resolver.lookup_service_async(callback, "xmpp-client", "tcp", "google.com")

        loop = glib.MainLoop()
        loop.run()
"""
