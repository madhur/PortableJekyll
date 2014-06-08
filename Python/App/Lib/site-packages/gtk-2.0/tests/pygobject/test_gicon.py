# -*- Mode: Python -*-

import os
import unittest

import glib
import gio


class TestIcon(unittest.TestCase):
    def test_eq(self):
        self.assertEquals(gio.FileIcon(gio.File('foo.png')),
                          gio.FileIcon(gio.File('foo.png')))
        self.assertEquals(gio.ThemedIcon('foo'),
                          gio.ThemedIcon('foo'))

        self.assertNotEqual(gio.FileIcon(gio.File('foo.png')),
                            gio.FileIcon(gio.File('bar.png')))
        self.assertNotEquals(gio.ThemedIcon('foo'),
                             gio.ThemedIcon('bar'))
        self.assertNotEquals(gio.FileIcon(gio.File('foo.png')),
                             gio.ThemedIcon('foo'))

    def test_hash(self):
        self.assertEquals(hash(gio.FileIcon(gio.File('foo.png'))),
                          hash(gio.FileIcon(gio.File('foo.png'))))
        self.assertEquals(hash(gio.ThemedIcon('foo')),
                          hash(gio.ThemedIcon('foo')))

class TestLoadableIcon(unittest.TestCase):
    def setUp(self):
        self.file = open('temp.svg', 'w')
        self.svg = ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
                    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN" '
                    '"http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">'
                    '<svg width="32" height="32"/>')
        self.file.write(self.svg)
        self.file.close()
        self.icon = gio.FileIcon(gio.File('temp.svg'))

    def tearDown(self):
        if os.path.exists('temp.svg'):
            os.unlink('temp.svg')

    def test_load(self):
        stream, type = self.icon.load()
        try:
            self.assert_(isinstance(stream, gio.InputStream))
            self.assertEquals(self.svg, stream.read())
        finally:
            stream.close()

    def test_load_async(self):
        def callback(icon, result):
            try:
                stream, type = icon.load_finish(result)
                self.assert_(isinstance(stream, gio.InputStream))
                self.assertEquals(self.svg, stream.read())
            finally:
                loop.quit()
                stream.close()

        self.icon.load_async(callback)

        loop = glib.MainLoop()
        loop.run()

class TestFileIcon(unittest.TestCase):
    def test_constructor(self):
        file = gio.File('foo.png')
        self.assert_(file is gio.FileIcon(file).get_file())

class TestThemedIcon(unittest.TestCase):
    def setUp(self):
        self.icon = gio.ThemedIcon("open")

    def test_constructor(self):
        have_use_default_fallbacks = ('use_default_fallbacks'
                                      in gio.ThemedIcon.props.__members__)
        icon = gio.ThemedIcon('foo')
        self.assertEquals(['foo'], icon.props.names)
        self.assert_(not have_use_default_fallbacks
                     or not icon.props.use_default_fallbacks)

        icon = gio.ThemedIcon(['foo', 'bar', 'baz'])
        self.assertEquals(['foo', 'bar', 'baz'], icon.props.names)
        self.assert_(not have_use_default_fallbacks
                     or not icon.props.use_default_fallbacks)

        icon = gio.ThemedIcon('xxx-yyy-zzz', True)
        self.assertEquals(['xxx-yyy-zzz', 'xxx-yyy', 'xxx'], icon.props.names)
        self.assert_(not have_use_default_fallbacks
                     or icon.props.use_default_fallbacks)

    def test_constructor_illegals(self):
        self.assertRaises(TypeError, lambda: gio.ThemedIcon(42))
        self.assertRaises(TypeError, lambda: gio.ThemedIcon(['foo', 42, 'bar']))

    def test_get_names(self):
        self.assertEquals(self.icon.get_names(), ['open'])

    def test_append_name(self):
        self.assertEquals(self.icon.get_names(), ['open'])
        self.icon.append_name('close')
        self.assertEquals(self.icon.get_names(), ['open', 'close'])

class TestEmblemedIcon(unittest.TestCase):
    def test_emblemed_icon(self):
        icon = gio.FileIcon(gio.File('foo.png'))
        emblem = gio.Emblem(icon)
        emblemed = gio.EmblemedIcon(icon, emblem)
        self.assertEquals(emblemed.get_emblems()[0], emblem)
