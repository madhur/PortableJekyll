# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab

import unittest

import sys
import os
sys.path.insert(0, "../")

from compathelper import _long, _unicode, _bytes

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import Pango
from gi.repository import GdkPixbuf
import gi.overrides as overrides
import gi.types

class TestGLib(unittest.TestCase):

    def test_gvariant_create(self):
        # simple values

        variant = GLib.Variant('i', 42)
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertEquals(variant.get_int32(), 42)

        variant = GLib.Variant('s', '')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertEquals(variant.get_string(), '')

        variant = GLib.Variant('s', 'hello')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertEquals(variant.get_string(), 'hello')

        # boxed variant
        variant = GLib.Variant('v', GLib.Variant('i', 42))
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertTrue(isinstance(variant.get_variant(), GLib.Variant))
        self.assertEqual(variant.get_type_string(), 'v')
        self.assertEqual(variant.get_variant().get_type_string(), 'i')
        self.assertEquals(variant.get_variant().get_int32(), 42)

        variant = GLib.Variant('v', GLib.Variant('v', GLib.Variant('i', 42)))
        self.assertEqual(variant.get_type_string(), 'v')
        self.assertEqual(variant.get_variant().get_type_string(), 'v')
        self.assertEqual(variant.get_variant().get_variant().get_type_string(), 'i')
        self.assertEquals(variant.get_variant().get_variant().get_int32(), 42)

        # tuples

        variant = GLib.Variant('()', ())
        self.assertEqual(variant.get_type_string(), '()')
        self.assertEquals(variant.n_children(), 0)

        variant = GLib.Variant('(i)', (3,))
        self.assertEqual(variant.get_type_string(), '(i)')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertEquals(variant.n_children(), 1)
        self.assertTrue(isinstance(variant.get_child_value(0), GLib.Variant))
        self.assertEquals(variant.get_child_value(0).get_int32(), 3)

        variant = GLib.Variant('(ss)', ('mec', 'mac'))
        self.assertEqual(variant.get_type_string(), '(ss)')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(0), GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(1), GLib.Variant))
        self.assertEquals(variant.get_child_value(0).get_string(), 'mec')
        self.assertEquals(variant.get_child_value(1).get_string(), 'mac')

        # nested tuples
        variant = GLib.Variant('((si)(ub))', (('hello', -1), (42, True)))
        self.assertEqual(variant.get_type_string(), '((si)(ub))')
        self.assertEqual(variant.unpack(), (('hello', -1), (_long(42), True)))

        # dictionaries

        variant = GLib.Variant('a{si}', {})
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertEqual(variant.get_type_string(), 'a{si}')
        self.assertEquals(variant.n_children(), 0)

        variant = GLib.Variant('a{si}', {'': 1, 'key1': 2, 'key2': 3})
        self.assertEqual(variant.get_type_string(), 'a{si}')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(0), GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(1), GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(2), GLib.Variant))
        self.assertEqual(variant.unpack(), {'': 1, 'key1': 2, 'key2': 3})

        # nested dictionaries
        variant = GLib.Variant('a{sa{si}}', {})
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertEqual(variant.get_type_string(), 'a{sa{si}}')
        self.assertEquals(variant.n_children(), 0)

        d = {'':     {'': 1, 'keyn1': 2},
             'key1': {'key11': 11, 'key12': 12}}
        variant = GLib.Variant('a{sa{si}}', d)
        self.assertEqual(variant.get_type_string(), 'a{sa{si}}')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertEqual(variant.unpack(), d)

        # arrays

        variant = GLib.Variant('ai', [])
        self.assertEqual(variant.get_type_string(), 'ai')
        self.assertEquals(variant.n_children(), 0)

        variant = GLib.Variant('ai', [1, 2])
        self.assertEqual(variant.get_type_string(), 'ai')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(0), GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(1), GLib.Variant))
        self.assertEquals(variant.get_child_value(0).get_int32(), 1)
        self.assertEquals(variant.get_child_value(1).get_int32(), 2)

        variant = GLib.Variant('as', [])
        self.assertEqual(variant.get_type_string(), 'as')
        self.assertEquals(variant.n_children(), 0)

        variant = GLib.Variant('as', [''])
        self.assertEqual(variant.get_type_string(), 'as')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(0), GLib.Variant))
        self.assertEquals(variant.get_child_value(0).get_string(), '')

        variant = GLib.Variant('as', ['hello', 'world'])
        self.assertEqual(variant.get_type_string(), 'as')
        self.assertTrue(isinstance(variant, GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(0), GLib.Variant))
        self.assertTrue(isinstance(variant.get_child_value(1), GLib.Variant))
        self.assertEquals(variant.get_child_value(0).get_string(), 'hello')
        self.assertEquals(variant.get_child_value(1).get_string(), 'world')

        # nested arrays
        variant = GLib.Variant('aai', [])
        self.assertEqual(variant.get_type_string(), 'aai')
        self.assertEquals(variant.n_children(), 0)

        variant = GLib.Variant('aai', [[]])
        self.assertEqual(variant.get_type_string(), 'aai')
        self.assertEquals(variant.n_children(), 1)
        self.assertEquals(variant.get_child_value(0).n_children(), 0)

        variant = GLib.Variant('aai', [[1, 2], [3, 4, 5]])
        self.assertEqual(variant.get_type_string(), 'aai')
        self.assertEquals(variant.unpack(), [[1, 2], [3, 4, 5]])

        #
        # complex types
        #

        variant = GLib.Variant('(as)', ([],))
        self.assertEqual(variant.get_type_string(), '(as)')
        self.assertEquals(variant.n_children(), 1)
        self.assertEquals(variant.get_child_value(0).n_children(), 0)

        variant = GLib.Variant('(as)', ([''],))
        self.assertEqual(variant.get_type_string(), '(as)')
        self.assertEquals(variant.n_children(), 1)
        self.assertEquals(variant.get_child_value(0).n_children(), 1)
        self.assertEquals(variant.get_child_value(0).get_child_value(0).get_string(), '')

        variant = GLib.Variant('(as)', (['hello'],))
        self.assertEqual(variant.get_type_string(), '(as)')
        self.assertEquals(variant.n_children(), 1)
        self.assertEquals(variant.get_child_value(0).n_children(), 1)
        self.assertEquals(variant.get_child_value(0).get_child_value(0).get_string(), 'hello')

        obj = {'a1': (1, True), 'a2': (2, False)}
        variant = GLib.Variant('a{s(ib)}', obj)
        self.assertEqual(variant.get_type_string(), 'a{s(ib)}')
        self.assertEqual(variant.unpack(), obj)

        obj = {'a1': (1, GLib.Variant('b', True)), 'a2': (2, GLib.Variant('y', 255))}
        variant = GLib.Variant('a{s(iv)}', obj)
        self.assertEqual(variant.get_type_string(), 'a{s(iv)}')
        self.assertEqual(variant.unpack(), {'a1': (1, True), 'a2': (2, 255)})

        obj = (1, {'a': {'a1': True, 'a2': False},
                   'b': {'b1': False},
                   'c': {}
                  },
               'foo')
        variant = GLib.Variant('(ia{sa{sb}}s)', obj)
        self.assertEqual(variant.get_type_string(), '(ia{sa{sb}}s)')
        self.assertEqual(variant.unpack(), obj)

    def test_gvariant_create_errors(self):
        # excess arguments
        self.assertRaises(TypeError, GLib.Variant, 'i', 42, 3)
        self.assertRaises(TypeError, GLib.Variant, '(i)', (42, 3))

        # not enough arguments
        self.assertRaises(TypeError, GLib.Variant, '(ii)', (42,))

        # data type mismatch
        self.assertRaises(TypeError, GLib.Variant, 'i', 'hello')
        self.assertRaises(TypeError, GLib.Variant, 's', 42)
        self.assertRaises(TypeError, GLib.Variant, '(ss)', 'mec', 'mac')

        # unimplemented data type
        self.assertRaises(NotImplementedError, GLib.Variant, 'Q', 1)

    def test_gvariant_unpack(self):
        # simple values
        res = GLib.Variant.new_int32(-42).unpack()
        self.assertEqual(res, -42)

        res = GLib.Variant.new_uint64(34359738368).unpack()
        self.assertEqual(res, 34359738368)

        res = GLib.Variant.new_boolean(True).unpack()
        self.assertEqual(res, True)

        res = GLib.Variant.new_object_path('/foo/Bar').unpack()
        self.assertEqual(res, '/foo/Bar')

        # variant
        res = GLib.Variant('v', GLib.Variant.new_int32(-42)).unpack()
        self.assertEqual(res, -42)

        variant = GLib.Variant('v', GLib.Variant('v', GLib.Variant('i', 42)))
        self.assertEqual(res, -42)

        # tuple
        res = GLib.Variant.new_tuple(GLib.Variant.new_int32(-1),
                GLib.Variant.new_string('hello')).unpack()
        self.assertEqual(res, (-1, 'hello'))

        # array
        vb = GLib.VariantBuilder()
        vb.init(gi._gi.variant_type_from_string('ai'))
        vb.add_value(GLib.Variant.new_int32(-1))
        vb.add_value(GLib.Variant.new_int32(3))
        res = vb.end().unpack()
        self.assertEqual(res, [-1, 3])

        # dictionary
        res = GLib.Variant('a{si}', {'key1': 1, 'key2': 2}).unpack()
        self.assertEqual(res, {'key1': 1, 'key2': 2})

    def test_gvariant_iteration(self):
        # array index access
        vb = GLib.VariantBuilder()
        vb.init(gi._gi.variant_type_from_string('ai'))
        vb.add_value(GLib.Variant.new_int32(-1))
        vb.add_value(GLib.Variant.new_int32(3))
        v = vb.end()

        self.assertEqual(len(v), 2)
        self.assertEqual(v[0], -1)
        self.assertEqual(v[1], 3)
        self.assertEqual(v[-1], 3)
        self.assertEqual(v[-2], -1)
        self.assertRaises(IndexError, v.__getitem__, 2)
        self.assertRaises(IndexError, v.__getitem__, -3)
        self.assertRaises(ValueError, v.__getitem__, 'a')

        # array iteration
        self.assertEqual([x for x in v], [-1, 3])
        self.assertEqual(list(v), [-1, 3])

        # tuple index access
        v = GLib.Variant.new_tuple(GLib.Variant.new_int32(-1),
                GLib.Variant.new_string('hello'))
        self.assertEqual(len(v), 2)
        self.assertEqual(v[0], -1)
        self.assertEqual(v[1], 'hello')
        self.assertEqual(v[-1], 'hello')
        self.assertEqual(v[-2], -1)
        self.assertRaises(IndexError, v.__getitem__, 2)
        self.assertRaises(IndexError, v.__getitem__, -3)
        self.assertRaises(ValueError, v.__getitem__, 'a')

        # tuple iteration
        self.assertEqual([x for x in v], [-1, 'hello'])
        self.assertEqual(tuple(v), (-1, 'hello'))

        # dictionary index access
        vsi = GLib.Variant('a{si}', {'key1': 1, 'key2': 2})
        vis = GLib.Variant('a{is}', {1: 'val1', 5: 'val2'})

        self.assertEqual(len(vsi), 2)
        self.assertEqual(vsi['key1'], 1)
        self.assertEqual(vsi['key2'], 2)
        self.assertRaises(KeyError, vsi.__getitem__, 'unknown')

        self.assertEqual(len(vis), 2)
        self.assertEqual(vis[1], 'val1')
        self.assertEqual(vis[5], 'val2')
        self.assertRaises(KeyError, vsi.__getitem__, 3)

        # dictionary iteration
        self.assertEqual(set(vsi.keys()), set(['key1', 'key2']))
        self.assertEqual(set(vis.keys()), set([1, 5]))

        # string index access
        v = GLib.Variant('s', 'hello')
        self.assertEqual(len(v), 5)
        self.assertEqual(v[0], 'h')
        self.assertEqual(v[4], 'o')
        self.assertEqual(v[-1], 'o')
        self.assertEqual(v[-5], 'h')
        self.assertRaises(IndexError, v.__getitem__, 5)
        self.assertRaises(IndexError, v.__getitem__, -6)

        # string iteration
        self.assertEqual([x for x in v], ['h', 'e', 'l', 'l', 'o'])

class TestPango(unittest.TestCase):

    def test_default_font_description(self):
        desc = Pango.FontDescription()
        self.assertEquals(desc.get_variant(), Pango.Variant.NORMAL)

    def test_font_description(self):
        desc = Pango.FontDescription('monospace')
        self.assertEquals(desc.get_family(), 'monospace')
        self.assertEquals(desc.get_variant(), Pango.Variant.NORMAL)

    def test_layout(self):
        self.assertRaises(TypeError, Pango.Layout)
        context = Pango.Context()
        layout = Pango.Layout(context)
        self.assertEquals(layout.get_context(), context)

class TestGdk(unittest.TestCase):

    def test_constructor(self):
        attribute = Gdk.WindowAttr()
        attribute.window_type = Gdk.WindowType.CHILD
        attributes_mask = Gdk.WindowAttributesType.X | \
            Gdk.WindowAttributesType.Y
        window = Gdk.Window(None, attribute, attributes_mask)
        self.assertEquals(window.get_window_type(), Gdk.WindowType.CHILD)

    def test_color(self):
        color = Gdk.Color(100, 200, 300)
        self.assertEquals(color.red, 100)
        self.assertEquals(color.green, 200)
        self.assertEquals(color.blue, 300)

    def test_rgba(self):
        self.assertEquals(Gdk.RGBA, overrides.Gdk.RGBA)
        rgba = Gdk.RGBA(0.1, 0.2, 0.3, 0.4)
        self.assertEquals(rgba.red, 0.1)
        self.assertEquals(rgba.green, 0.2)
        self.assertEquals(rgba.blue, 0.3)
        self.assertEquals(rgba.alpha, 0.4)
        rgba.green = 0.9
        self.assertEquals(rgba.green, 0.9)

    def test_event(self):
        event = Gdk.Event.new(Gdk.EventType.CONFIGURE)
        self.assertEquals(event.type, Gdk.EventType.CONFIGURE)
        self.assertEquals(event.send_event, 0)

        event = Gdk.Event.new(Gdk.EventType.DRAG_MOTION)
        event.x_root, event.y_root = 0, 5
        self.assertEquals(event.x_root, 0)
        self.assertEquals(event.y_root, 5)

        event = Gdk.Event()
        event.type = Gdk.EventType.SCROLL
        self.assertRaises(AttributeError, lambda: getattr(event, 'foo_bar'))

    def test_event_structures(self):
        def button_press_cb(button, event):
            self.assertTrue(isinstance(event, Gdk.EventButton))
            self.assertTrue(event.type == Gdk.EventType.BUTTON_PRESS)
            self.assertEquals(event.send_event, 0)
            self.assertEquals(event.get_state(), Gdk.ModifierType.CONTROL_MASK)
            self.assertEquals(event.get_root_coords(), (2, 5))

            event.time = 12345
            self.assertEquals(event.get_time(), 12345)

        w = Gtk.Window()
        b = Gtk.Button()
        b.connect('button-press-event', button_press_cb)
        w.add(b)
        w.show_all()
        Gdk.test_simulate_button(b.get_window(),
                                 2, 5,
                                 0,
                                 Gdk.ModifierType.CONTROL_MASK,
                                 Gdk.EventType.BUTTON_PRESS)

    def test_cursor(self):
        self.assertEquals(Gdk.Cursor, overrides.Gdk.Cursor)
        c = Gdk.Cursor(Gdk.CursorType.WATCH)
        self.assertNotEqual(c, None)
        c = Gdk.Cursor(cursor_type = Gdk.CursorType.WATCH)
        self.assertNotEqual(c, None)

        display_manager = Gdk.DisplayManager.get()
        display = display_manager.get_default_display()

        test_pixbuf = GdkPixbuf.Pixbuf.new(GdkPixbuf.Colorspace.RGB,
                                           False,
                                           8,
                                           5,
                                           10)

        c = Gdk.Cursor(display,
                       test_pixbuf,
                       y=0, x=0)

        self.assertNotEqual(c, None)
        self.assertRaises(ValueError, Gdk.Cursor, 1, 2, 3)

class TestGtk(unittest.TestCase):

    def test_container(self):
        box = Gtk.Box()
        self.assertTrue(box)
        label = Gtk.Label()
        label2 = Gtk.Label()
        box.add(label)
        box.add(label2)
        self.assertTrue(label in box)
        self.assertTrue(label2 in box)
        self.assertEqual(len(box), 2)
        self.assertTrue(box)
        l = [x for x in box]
        self.assertEqual(l, [label, label2])

    def test_actions(self):
        self.assertEquals(Gtk.Action, overrides.Gtk.Action)
        self.assertRaises(TypeError, Gtk.Action)
        action = Gtk.Action("test", "Test", "Test Action", Gtk.STOCK_COPY)
        self.assertEquals(action.get_name(), "test")
        self.assertEquals(action.get_label(), "Test")
        self.assertEquals(action.get_tooltip(), "Test Action")
        self.assertEquals(action.get_stock_id(), Gtk.STOCK_COPY)

        self.assertEquals(Gtk.RadioAction, overrides.Gtk.RadioAction)
        self.assertRaises(TypeError, Gtk.RadioAction)
        action = Gtk.RadioAction("test", "Test", "Test Action", Gtk.STOCK_COPY, 1)
        self.assertEquals(action.get_name(), "test")
        self.assertEquals(action.get_label(), "Test")
        self.assertEquals(action.get_tooltip(), "Test Action")
        self.assertEquals(action.get_stock_id(), Gtk.STOCK_COPY)
        self.assertEquals(action.get_current_value(), 1)

    def test_actiongroup(self):
        self.assertEquals(Gtk.ActionGroup, overrides.Gtk.ActionGroup)
        self.assertRaises(TypeError, Gtk.ActionGroup)

        action_group = Gtk.ActionGroup (name = 'TestActionGroup')
        callback_data = "callback data"

        def test_action_callback_data(action, user_data):
            self.assertEquals(user_data, callback_data);

        def test_radio_action_callback_data(action, current, user_data):
            self.assertEquals(user_data, callback_data);

        action_group.add_actions ([
            ('test-action1', None, 'Test Action 1',
             None, None, test_action_callback_data),
            ('test-action2', Gtk.STOCK_COPY, 'Test Action 2',
              None, None, test_action_callback_data)], callback_data)
        action_group.add_toggle_actions([
            ('test-toggle-action1', None, 'Test Toggle Action 1',
             None, None, test_action_callback_data, False),
            ('test-toggle-action2', Gtk.STOCK_COPY, 'Test Toggle Action 2',
              None, None, test_action_callback_data, True)], callback_data)
        action_group.add_radio_actions([
            ('test-radio-action1', None, 'Test Radio Action 1'),
            ('test-radio-action2', Gtk.STOCK_COPY, 'Test Radio Action 2')], 1,
            test_radio_action_callback_data,
            callback_data)

        expected_results = [('test-action1', Gtk.Action),
                            ('test-action2', Gtk.Action),
                            ('test-toggle-action1', Gtk.ToggleAction),
                            ('test-toggle-action2', Gtk.ToggleAction),
                            ('test-radio-action1', Gtk.RadioAction),
                            ('test-radio-action2', Gtk.RadioAction)]

        for action in action_group.list_actions():
            a = (action.get_name(), type(action))
            self.assertTrue(a in expected_results)
            expected_results.remove(a)
            action.activate()

    def test_uimanager(self):
        self.assertEquals(Gtk.UIManager, overrides.Gtk.UIManager)
        ui = Gtk.UIManager()
        ui.add_ui_from_string(
"""
<ui>
    <menubar name="menubar1"></menubar>
</ui>
"""
)
        menubar = ui.get_widget("/menubar1")
        self.assertEquals(type(menubar), Gtk.MenuBar)

        ag = Gtk.ActionGroup (name="ag1")
        ui.insert_action_group(ag)
        ag2 = Gtk.ActionGroup (name="ag2")
        ui.insert_action_group(ag2)
        groups = ui.get_action_groups()
        self.assertEquals(ag, groups[-2])
        self.assertEquals(ag2, groups[-1])

    def test_builder(self):
        self.assertEquals(Gtk.Builder, overrides.Gtk.Builder)

        class SignalTest(GObject.GObject):
            __gtype_name__ = "GIOverrideSignalTest"
            __gsignals__ = {
                "test-signal": (GObject.SIGNAL_RUN_FIRST,
                                GObject.TYPE_NONE,
                                []),
            }


        class SignalCheck:
            def __init__(self):
                self.sentinel = 0

            def on_signal_1(self, *args):
                self.sentinel += 1

            def on_signal_3(self, *args):
                self.sentinel += 3

        signal_checker = SignalCheck()
        builder = Gtk.Builder()

        # add object1 to the builder
        builder.add_from_string(
"""
<interface>
  <object class="GIOverrideSignalTest" id="object1">
      <signal name="test-signal" handler="on_signal_1" />
  </object>
</interface>
""")

        # only add object3 to the builder
        builder.add_objects_from_string(
"""
<interface>
  <object class="GIOverrideSignalTest" id="object2">
      <signal name="test-signal" handler="on_signal_2" />
  </object>
  <object class="GIOverrideSignalTest" id="object3">
      <signal name="test-signal" handler="on_signal_3" />
  </object>
  <object class="GIOverrideSignalTest" id="object4">
      <signal name="test-signal" handler="on_signal_4" />
  </object>
</interface>

""",
            ['object3'])

        # hook up signals
        builder.connect_signals(signal_checker)

        # call their notify signals and check sentinel
        objects = builder.get_objects()
        self.assertEquals(len(objects), 2)
        for obj in objects:
            obj.emit('test-signal')

        self.assertEquals(signal_checker.sentinel, 4)

    def test_dialogs(self):
        self.assertEquals(Gtk.Dialog, overrides.Gtk.Dialog)
        self.assertEquals(Gtk.AboutDialog, overrides.Gtk.AboutDialog)
        self.assertEquals(Gtk.MessageDialog, overrides.Gtk.MessageDialog)
        self.assertEquals(Gtk.ColorSelectionDialog, overrides.Gtk.ColorSelectionDialog)
        self.assertEquals(Gtk.FileChooserDialog, overrides.Gtk.FileChooserDialog)
        self.assertEquals(Gtk.FontSelectionDialog, overrides.Gtk.FontSelectionDialog)
        self.assertEquals(Gtk.RecentChooserDialog, overrides.Gtk.RecentChooserDialog)

        # Gtk.Dialog
        dialog = Gtk.Dialog (title='Foo',
                             flags=Gtk.DialogFlags.MODAL,
                             buttons=('test-button1', 1))

        dialog.add_buttons ('test-button2', 2, Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)

        self.assertEquals('Foo', dialog.get_title())
        self.assertTrue(dialog.get_modal())
        button = dialog.get_widget_for_response (1)
        self.assertEquals('test-button1', button.get_label())
        button = dialog.get_widget_for_response (2)
        self.assertEquals('test-button2', button.get_label())
        button = dialog.get_widget_for_response (Gtk.ResponseType.CLOSE)
        self.assertEquals(Gtk.STOCK_CLOSE, button.get_label())

        # Gtk.AboutDialog
        dialog = Gtk.AboutDialog()

        # Gtk.MessageDialog
        dialog = Gtk.MessageDialog (title='message dialog test',
                                    flags=Gtk.DialogFlags.MODAL,
                                    buttons=Gtk.ButtonsType.OK,
                                    message_format='dude!')

        self.assertEquals('message dialog test', dialog.get_title())
        self.assertTrue(dialog.get_modal())
        text = dialog.get_property('text')
        self.assertEquals('dude!', text)

        dialog.format_secondary_text('2nd text')
        self.assertEqual(dialog.get_property('secondary-text'), '2nd text')
        self.assertFalse(dialog.get_property('secondary-use-markup'))

        dialog.format_secondary_markup('2nd markup')
        self.assertEqual(dialog.get_property('secondary-text'), '2nd markup')
        self.assertTrue(dialog.get_property('secondary-use-markup'))

        # Gtk.ColorSelectionDialog
        dialog = Gtk.ColorSelectionDialog("color selection dialog test")
        self.assertEquals('color selection dialog test', dialog.get_title())

        # Gtk.FileChooserDialog
        dialog = Gtk.FileChooserDialog (title='file chooser dialog test',
                                        buttons=('test-button1', 1),
                                        action=Gtk.FileChooserAction.SAVE)

        dialog.add_buttons ('test-button2', 2, Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)
        self.assertEquals('file chooser dialog test', dialog.get_title())
        button = dialog.get_widget_for_response (1)
        self.assertEquals('test-button1', button.get_label())
        button = dialog.get_widget_for_response (2)
        self.assertEquals('test-button2', button.get_label())
        button = dialog.get_widget_for_response (Gtk.ResponseType.CLOSE)
        self.assertEquals(Gtk.STOCK_CLOSE, button.get_label())
        action = dialog.get_property('action')
        self.assertEquals(Gtk.FileChooserAction.SAVE, action)


        # Gtk.FontSelectionDialog
        dialog = Gtk.ColorSelectionDialog("font selection dialog test")
        self.assertEquals('font selection dialog test', dialog.get_title())

        # Gtk.RecentChooserDialog
        test_manager = Gtk.RecentManager()
        dialog = Gtk.RecentChooserDialog (title='recent chooser dialog test',
                                          buttons=('test-button1', 1),
                                          manager=test_manager)

        dialog.add_buttons ('test-button2', 2, Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)
        self.assertEquals('recent chooser dialog test', dialog.get_title())
        button = dialog.get_widget_for_response (1)
        self.assertEquals('test-button1', button.get_label())
        button = dialog.get_widget_for_response (2)
        self.assertEquals('test-button2', button.get_label())
        button = dialog.get_widget_for_response (Gtk.ResponseType.CLOSE)
        self.assertEquals(Gtk.STOCK_CLOSE, button.get_label())

    class TestClass(GObject.GObject):
        __gtype_name__ = "GIOverrideTreeAPITest"

        def __init__(self, tester, int_value, string_value):
            super(TestGtk.TestClass, self).__init__()
            self.tester = tester
            self.int_value = int_value
            self.string_value = string_value

        def check(self, int_value, string_value):
            self.tester.assertEquals(int_value, self.int_value)
            self.tester.assertEquals(string_value, self.string_value)

    def test_tree_store(self):
        self.assertEquals(Gtk.TreeStore, overrides.Gtk.TreeStore)
        self.assertEquals(Gtk.ListStore, overrides.Gtk.ListStore)
        self.assertEquals(Gtk.TreeModel, overrides.Gtk.TreeModel)
        self.assertEquals(Gtk.TreeViewColumn, overrides.Gtk.TreeViewColumn)

        class TestPyObject(object):
            pass

        test_pyobj = TestPyObject()
        test_pydict = {1:1, "2":2, "3":"3"}
        test_pylist = [1,"2", "3"]
        tree_store = Gtk.TreeStore(int,
                                   'gchararray',
                                   TestGtk.TestClass,
                                   object,
                                   object,
                                   object,
                                   bool,
                                   bool,
                                   GObject.TYPE_UINT,
                                   GObject.TYPE_ULONG,
                                   GObject.TYPE_INT64,
                                   GObject.TYPE_UINT64,
                                   GObject.TYPE_UCHAR,
                                   GObject.TYPE_CHAR)

        parent = None
        for i in range(100):
            label = 'this is child #%d' % i
            testobj = TestGtk.TestClass(self, i, label)
            parent = tree_store.append(parent, (i,
                                                label,
                                                testobj,
                                                test_pyobj,
                                                test_pydict,
                                                test_pylist,
                                                i % 2,
                                                bool(i % 2),
                                                i,
                                                9223372036854775808,
                                                -9223372036854775808,
                                                0xffffffffffffffff,
                                                254,
                                                _bytes('a')
                                                ))

        # len gets the number of children in the root node
        # since we kept appending to the previous node
        # there should only be one child of the root
        self.assertEquals(len(tree_store), 1)

        # walk the tree to see if the values were stored correctly
        parent = None
        i = 0

        treeiter = tree_store.iter_children(parent)
        while treeiter:
           i = tree_store.get_value(treeiter, 0)
           s = tree_store.get_value(treeiter, 1)
           obj = tree_store.get_value(treeiter, 2)
           obj.check(i, s)

           pyobj = tree_store.get_value(treeiter, 3)
           self.assertEquals(pyobj, test_pyobj)
           pydict = tree_store.get_value(treeiter, 4)
           self.assertEquals(pydict, test_pydict)
           pylist = tree_store.get_value(treeiter, 5)
           self.assertEquals(pylist, test_pylist)

           bool_1 = tree_store.get_value(treeiter, 6)
           bool_2 = tree_store.get_value(treeiter, 7)
           self.assertEquals(bool_1, bool_2)
           self.assertTrue(isinstance(bool_1, bool))
           self.assertTrue(isinstance(bool_2, bool))

           uint_ = tree_store.get_value(treeiter, 8)
           self.assertEquals(uint_, i)
           ulong_ = tree_store.get_value(treeiter, 9)
           self.assertEquals(ulong_, 9223372036854775808)
           int64_ = tree_store.get_value(treeiter, 10)
           self.assertEquals(int64_, -9223372036854775808)
           uint64_ = tree_store.get_value(treeiter, 11)
           self.assertEquals(uint64_, 0xffffffffffffffff)
           uchar_ = tree_store.get_value(treeiter, 12)
           self.assertEquals(ord(uchar_), 254)
           char_ = tree_store.get_value(treeiter, 13)
           self.assertEquals(char_, 'a')

           parent = treeiter
           treeiter = tree_store.iter_children(parent)

        self.assertEquals(i, 99)

    def test_list_store(self):
        class TestPyObject(object):
            pass

        class TestPyGObject(GObject.Object):
            __gtype_name__ = 'TestPyGObject'
            def __init__(self, i):
                GObject.Object.__init__(self)
                self.sentinal = i + 5

        test_pyobj = TestPyObject()
        test_pydict = {1:1, "2":2, "3":"3"}
        test_pylist = [1,"2", "3"]

        list_store = Gtk.ListStore(int, str, 'GIOverrideTreeAPITest', object, object, object, bool, bool, object)
        for i in range(93):
            label = 'this is row #%d' % i
            testobj = TestGtk.TestClass(self, i, label)
            testpygobj = TestPyGObject(i)
            parent = list_store.append((i,
                                        label,
                                        testobj,
                                        test_pyobj,
                                        test_pydict,
                                        test_pylist,
                                        i % 2,
                                        bool(i % 2),
                                        testpygobj))

        i = 93
        label = _unicode('this is row #93')
        treeiter = list_store.append()
        list_store.set_value(treeiter, 0, i)
        list_store.set_value(treeiter, 1, label)
        list_store.set_value(treeiter, 2, TestGtk.TestClass(self, i, label))
        list_store.set_value(treeiter, 3, test_pyobj)
        list_store.set_value(treeiter, 4, test_pydict)
        list_store.set_value(treeiter, 5, test_pylist)
        list_store.set_value(treeiter, 6, 1)
        list_store.set_value(treeiter, 7, True)
        list_store.set_value(treeiter, 8, TestPyGObject(i))

        # test automatic unicode->str conversion
        i = 94
        label = _unicode('this is row #94')
        treeiter = list_store.append((i,
                                      label,
                                      TestGtk.TestClass(self, i, label),
                                      test_pyobj,
                                      test_pydict,
                                      test_pylist,
                                      0,
                                      False,
                                      TestPyGObject(i)))

        # add sorted items out of order to test insert* apis
        # also test sending in None to not set a column
        i = 97
        label = 'this is row #97'
        treeiter = list_store.append((None,
                                      None,
                                      None,
                                      test_pyobj,
                                      None,
                                      test_pylist,
                                      1,
                                      None,
                                      TestPyGObject(i)))

        list_store.set_value(treeiter, 0, i)
        list_store.set_value(treeiter, 1, label)
        list_store.set_value(treeiter, 2, TestGtk.TestClass(self, i, label))
        list_store.set_value(treeiter, 4, test_pydict)
        list_store.set_value(treeiter, 7, True)
 
        # this should append
        i = 99
        label = 'this is row #99'
        list_store.insert(9999, (i,
                                 label,
                                 TestGtk.TestClass(self, i, label),
                                 test_pyobj,
                                 test_pydict,
                                 test_pylist,
                                 1,
                                 True,
                                 TestPyGObject(i)))

        i = 96
        label = 'this is row #96'
        list_store.insert_before(treeiter, (i,
                                            label,
                                            TestGtk.TestClass(self, i, label),
                                            test_pyobj,
                                            test_pydict,
                                            test_pylist,
                                            0,
                                            False,
                                            TestPyGObject(i)))

        i = 98
        label = 'this is row #98'
        list_store.insert_after(treeiter, (i,
                                           label,
                                           TestGtk.TestClass(self, i, label),
                                           test_pyobj,
                                           test_pydict,
                                           test_pylist,
                                           0,
                                           False,
                                           TestPyGObject(i)))


        i = 95
        label = 'this is row #95'
        list_store.insert(95, (i,
                               label,
                               TestGtk.TestClass(self, i, label),
                               test_pyobj,
                               test_pydict,
                               test_pylist,
                               1,
                               True,
                               TestPyGObject(i)))

        self.assertEquals(len(list_store), 100)

        # walk the list to see if the values were stored correctly
        i = 0
        treeiter = list_store.get_iter_first()

        counter = 0
        while treeiter:
            i = list_store.get_value(treeiter, 0)
            self.assertEquals(i, counter)
            s = list_store.get_value(treeiter, 1)
            obj = list_store.get_value(treeiter, 2)
            obj.check(i, s)

            pyobj = list_store.get_value(treeiter, 3)
            self.assertEquals(pyobj, test_pyobj)
            pydict = list_store.get_value(treeiter, 4)
            self.assertEquals(pydict, test_pydict)
            pylist = list_store.get_value(treeiter, 5)
            self.assertEquals(pylist, test_pylist)

            bool_1 = list_store.get_value(treeiter, 6)
            bool_2 = list_store.get_value(treeiter, 7)
            self.assertEquals(bool_1, bool_2)
            self.assertTrue(isinstance(bool_1, bool))
            self.assertTrue(isinstance(bool_2, bool))

            pygobj = list_store.get_value(treeiter, 8)
            self.assertEquals(pygobj.sentinal, i + 5)

            treeiter = list_store.iter_next(treeiter)

            counter += 1

        self.assertEquals(i, 99)

    def test_tree_path(self):
        p1 = Gtk.TreePath()
        p2 = Gtk.TreePath.new_first()
        self.assertEqual(p1, p2)
        self.assertEqual(str(p1), '0')
        p1 = Gtk.TreePath(2)
        p2 = Gtk.TreePath.new_from_string('2')
        self.assertEqual(p1, p2)
        self.assertEqual(str(p1), '2')
        p1 = Gtk.TreePath('1:2:3')
        p2 = Gtk.TreePath.new_from_string('1:2:3')
        self.assertEqual(p1, p2)
        self.assertEqual(str(p1), '1:2:3')
        p1 = Gtk.TreePath((1,2,3))
        p2 = Gtk.TreePath.new_from_string('1:2:3')
        self.assertEqual(p1, p2)
        self.assertEqual(str(p1), '1:2:3')
        self.assertTrue(p1 != None)
        self.assertFalse(p1 == None)
        self.assertTrue(p1 > None)
        self.assertTrue(p1 >= None)
        self.assertFalse(p1 < None)
        self.assertFalse(p1 <= None)

    def test_tree_model(self):
        tree_store = Gtk.TreeStore(int, str)

        self.assertTrue(tree_store)
        self.assertEqual(len(tree_store), 0)
        self.assertEqual(tree_store.get_iter_first(), None)

        def get_by_index(row, col=None):
            if col:
                return tree_store[row][col]
            else:
                return tree_store[row]

        self.assertRaises(TypeError, get_by_index, None)
        self.assertRaises(TypeError, get_by_index, "")
        self.assertRaises(TypeError, get_by_index, ())

        self.assertRaises(IndexError, get_by_index, "0")
        self.assertRaises(IndexError, get_by_index, 0)
        self.assertRaises(IndexError, get_by_index, (0,))

        self.assertRaises(ValueError, tree_store.get_iter, "0")
        self.assertRaises(ValueError, tree_store.get_iter, 0)
        self.assertRaises(ValueError, tree_store.get_iter, (0,))

        self.assertRaises(ValueError, tree_store.get_iter_from_string, "0")

        for row in tree_store:
            self.fail("Should not be reached")

        class DerivedIntType(int):
            pass

        class DerivedStrType(str):
            pass

        for i in range(100):
            label = 'this is row #%d' % i
            parent = tree_store.append(None, (DerivedIntType(i), DerivedStrType(label),))
            self.assertNotEquals(parent, None)
            for j in range(20):
                label = 'this is child #%d of node #%d' % (j, i)
                child = tree_store.append(parent, (j, label,))
                self.assertNotEqual(child, None)

        self.assertTrue(tree_store)
        self.assertEqual(len(tree_store), 100)

        for i,row in enumerate(tree_store):
            self.assertEqual(row.model, tree_store)
            self.assertEqual(row.parent, None)

            self.assertEqual(tree_store[i].path, row.path)
            self.assertEqual(tree_store[str(i)].path, row.path)
            self.assertEqual(tree_store[(i,)].path, row.path)

            self.assertEqual(tree_store[i][0], i)
            self.assertEqual(tree_store[i][1], "this is row #%d" % i)

            aiter = tree_store.get_iter(i)
            self.assertEqual(tree_store.get_path(aiter), row.path)

            aiter = tree_store.get_iter(str(i))
            self.assertEqual(tree_store.get_path(aiter), row.path)

            aiter = tree_store.get_iter((i,))
            self.assertEqual(tree_store.get_path(aiter), row.path)

            self.assertEqual(tree_store.iter_parent(aiter), row.parent)

            next = tree_store.iter_next(aiter)
            if i < len(tree_store) - 1:
                self.assertEqual(tree_store.get_path(next), row.next.path)
            else:
                self.assertEqual(next, None)

            self.assertEqual(tree_store.iter_n_children(row.iter), 20)

            child = tree_store.iter_children(row.iter)
            for j,childrow in enumerate(row.iterchildren()):
                child_path = tree_store.get_path(child)
                self.assertEqual(childrow.path, child_path)
                self.assertEqual(childrow.parent.path, row.path)
                self.assertEqual(childrow.path, tree_store[child].path)
                self.assertEqual(childrow.path, tree_store[child_path].path)

                self.assertEqual(childrow[0], tree_store[child][0])
                self.assertEqual(childrow[0], j)
                self.assertEqual(childrow[1], tree_store[child][1])
                self.assertEqual(childrow[1], 'this is child #%d of node #%d' % (j, i))

                self.assertRaises(IndexError, get_by_index, child, 2)

                tree_store[child][1] = 'this was child #%d of node #%d' % (j, i)
                self.assertEqual(childrow[1], 'this was child #%d of node #%d' % (j, i))

                nth_child = tree_store.iter_nth_child(row.iter, j)
                self.assertEqual(childrow.path, tree_store.get_path(nth_child))

                childrow2 = tree_store["%d:%d" % (i, j)]
                self.assertEqual(childrow.path, childrow2.path)

                childrow2 = tree_store[(i, j,)]
                self.assertEqual(childrow.path, childrow2.path)

                child = tree_store.iter_next(child)
                if j < 19:
                    self.assertEqual(childrow.next.path, tree_store.get_path(child))
                else:
                    self.assertEqual(child, childrow.next)
                    self.assertEqual(child, None)

            self.assertEqual(j, 19)

        self.assertEqual(i, 99)

        # negative indices
        for i in range(-1,-100,-1):
            i_real = i + 100
            self.assertEqual(tree_store[i][0], i_real)

            row = tree_store[i]
            for j in range(-1, -20, -1):
                j_real = j + 20
                path = (i_real, j_real,)

                self.assertEqual(tree_store[path][-2], j_real)

                label = 'this was child #%d of node #%d' % (j_real, i_real)
                self.assertEqual(tree_store[path][-1], label)

                new_label = 'this still is child #%d of node #%d' % (j_real, i_real)
                tree_store[path][-1] = new_label
                self.assertEqual(tree_store[path][-1], new_label)

                self.assertRaises(IndexError, get_by_index, path, -3)

        self.assertRaises(IndexError, get_by_index, -101)

        last_row = tree_store[99]
        self.assertNotEqual(last_row, None)

        for i,childrow in enumerate(last_row.iterchildren()):
            if i < 19:
                self.assertTrue(tree_store.remove(childrow.iter))
            else:
                self.assertFalse(tree_store.remove(childrow.iter))

        self.assertEqual(i, 19)

        self.assertEqual(tree_store.iter_n_children(last_row.iter), 0)
        for childrow in last_row.iterchildren():
            self.fail("Should not be reached")

        aiter = tree_store.get_iter(10)
        self.assertRaises(TypeError, tree_store.get, aiter, 1, 'a')
        self.assertRaises(ValueError, tree_store.get, aiter, 1, -1)
        self.assertRaises(ValueError, tree_store.get, aiter, 1, 100)
        self.assertEqual(tree_store.get(aiter, 0, 1), (10, 'this is row #10'))

    def test_tree_view_column(self):
        cell = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(title='This is just a test',
                                    cell_renderer=cell,
                                    text=0,
                                    style=2)

    def test_tree_selection(self):
        store = Gtk.ListStore(int, str)
        for i in range(10):
            store.append((i, "foo"))
        view = Gtk.TreeView()
        view.set_model(store)
        firstpath = store.get_path(store.get_iter_first())
        sel = view.get_selection()

        sel.select_path(firstpath)
        (m, s) = sel.get_selected()
        self.assertEqual(m, store)
        self.assertEqual(store.get_path(s), firstpath)

        sel.select_path(0)
        (m, s) = sel.get_selected()
        self.assertEqual(m, store)
        self.assertEqual(store.get_path(s), firstpath)

        sel.select_path("0:0")
        (m, s) = sel.get_selected()
        self.assertEqual(m, store)
        self.assertEqual(store.get_path(s), firstpath)

        sel.select_path((0,0))
        (m, s) = sel.get_selected()
        self.assertEqual(m, store)
        self.assertEqual(store.get_path(s), firstpath)

    def test_text_buffer(self):
        self.assertEquals(Gtk.TextBuffer, overrides.Gtk.TextBuffer)
        buffer = Gtk.TextBuffer()
        tag = buffer.create_tag ('title', font = 'Sans 18')

        self.assertEquals(tag.props.name, 'title')
        self.assertEquals(tag.props.font, 'Sans 18')

        (start, end) = buffer.get_bounds()

        mark = buffer.create_mark(None, start)
        self.assertFalse(mark.get_left_gravity())

        buffer.set_text('Hello Jane Hello Bob')
        (start, end) = buffer.get_bounds()
        text = buffer.get_text(start, end, False)
        self.assertEquals(text, 'Hello Jane Hello Bob')

        buffer.set_text('')
        (start, end) = buffer.get_bounds()
        text = buffer.get_text(start, end, False)
        self.assertEquals(text, '')

        buffer.insert(end, 'HelloHello')
        buffer.insert(end, ' Bob')

        cursor_iter = end.copy()
        cursor_iter.backward_chars(9)
        buffer.place_cursor(cursor_iter)
        buffer.insert_at_cursor(' Jane ')

        (start, end) = buffer.get_bounds()
        text = buffer.get_text(start, end, False)
        self.assertEquals(text, 'Hello Jane Hello Bob')

        sel = buffer.get_selection_bounds()
        self.assertEquals(sel, ())
        buffer.select_range(start, end)
        sel = buffer.get_selection_bounds()
        self.assertTrue(sel[0].equal(start))
        self.assertTrue(sel[1].equal(end))

        buffer.set_text('')
        buffer.insert_with_tags(buffer.get_start_iter(), 'HelloHello', tag)
        (start, end) = buffer.get_bounds()
        self.assertTrue(start.begins_tag(tag))
        self.assertTrue(start.has_tag(tag))

        buffer.set_text('')
        buffer.insert_with_tags_by_name(buffer.get_start_iter(), 'HelloHello', 'title')
        (start, end) = buffer.get_bounds()
        self.assertTrue(start.begins_tag(tag))
        self.assertTrue(start.has_tag(tag))

        self.assertRaises(ValueError, buffer.insert_with_tags_by_name,
                buffer.get_start_iter(), 'HelloHello', 'unknowntag')

    def test_text_iter(self):
        self.assertEquals(Gtk.TextIter, overrides.Gtk.TextIter)
        buffer = Gtk.TextBuffer()
        buffer.set_text('Hello Jane Hello Bob')
        tag = buffer.create_tag ('title', font = 'Sans 18')
        (start, end) = buffer.get_bounds()
        start.forward_chars(10)
        buffer.apply_tag(tag, start, end)
        self.assertTrue(start.begins_tag())
        self.assertTrue(end.ends_tag())
        self.assertTrue(start.toggles_tag())
        self.assertTrue(end.toggles_tag())
        start.backward_chars(1)
        self.assertFalse(start.begins_tag())
        self.assertFalse(start.ends_tag())
        self.assertFalse(start.toggles_tag())

    def test_buttons(self):
        self.assertEquals(Gtk.Button, overrides.Gtk.Button)

        # test Gtk.Button
        button = Gtk.Button()
        button = Gtk.Button(stock=Gtk.STOCK_CLOSE)
        self.assertEquals(Gtk.STOCK_CLOSE, button.get_label())
        self.assertTrue(button.get_use_stock())
        self.assertTrue(button.get_use_underline())

        # test Gtk.LinkButton
        self.assertRaises(TypeError, Gtk.LinkButton)
        button = Gtk.LinkButton('http://www.gtk.org', 'Gtk')
        self.assertEquals('http://www.gtk.org', button.get_uri())
        self.assertEquals('Gtk', button.get_label())

    def test_inheritance(self):
        for name in overrides.Gtk.__all__:
            over = getattr(overrides.Gtk, name)
            for element in dir(Gtk):
                try:
                    klass = getattr(Gtk, element)
                    info = klass.__info__
                except (NotImplementedError, AttributeError):
                    continue

                # Get all parent classes and interfaces klass inherits from
                if isinstance(info, gi.types.ObjectInfo):
                    classes = list(info.get_interfaces())
                    parent = info.get_parent()
                    while parent.get_name() != "Object":
                        classes.append(parent)
                        parent = parent.get_parent()
                    classes = [kl for kl in classes if kl.get_namespace() == "Gtk"]
                else:
                    continue

                for kl in classes:
                    if kl.get_name() == name:
                        self.assertTrue(issubclass(klass, over,),
                            "%r does not inherit from override %r" % (klass, over,))

    def test_editable(self):
        self.assertEquals(Gtk.Editable, overrides.Gtk.Editable)

        # need to use Gtk.Entry because Editable is an interface
        entry=Gtk.Entry()
        pos = entry.insert_text('HeWorld', 0)
        self.assertEquals(pos, 7)
        pos = entry.insert_text('llo ', 2)
        self.assertEquals(pos, 6)
        text = entry.get_chars(0, 11)
        self.assertEquals('Hello World', text)

    def test_label(self):
        label = Gtk.Label('Hello')
        self.assertEquals(label.get_text(), 'Hello')

    def adjustment_check(self, adjustment, value=0.0, lower=0.0, upper=0.0,
                         step_increment=0.0, page_increment=0.0, page_size=0.0):
        self.assertEquals(adjustment.get_value(), value)
        self.assertEquals(adjustment.get_lower(), lower)
        self.assertEquals(adjustment.get_upper(), upper)
        self.assertEquals(adjustment.get_step_increment(), step_increment)
        self.assertEquals(adjustment.get_page_increment(), page_increment)
        self.assertEquals(adjustment.get_page_size(), page_size)

    def test_adjustment(self):
        adjustment =       Gtk.Adjustment(1, 0, 6, 4, 5, 3)
        self.adjustment_check(adjustment, 1, 0, 6, 4, 5, 3)

        adjustment =       Gtk.Adjustment(1, 0, 6, 4, 5)
        self.adjustment_check(adjustment, 1, 0, 6, 4, 5)

        adjustment =       Gtk.Adjustment(1, 0, 6, 4)
        self.adjustment_check(adjustment, 1, 0, 6, 4)

        adjustment =       Gtk.Adjustment(1, 0, 6)
        self.adjustment_check(adjustment, 1, 0, 6)

        adjustment = Gtk.Adjustment()
        self.adjustment_check(adjustment)

        adjustment = Gtk.Adjustment(value=1, lower=0, upper=6,
                                    step_increment=4, page_increment=5, page_size=3)
        self.adjustment_check(adjustment, 1, 0, 6, 4, 5, 3)

    def test_table(self):
        table = Gtk.Table()
        self.assertEquals(table.get_size(), (1,1))
        self.assertEquals(table.get_homogeneous(), False)
        table = Gtk.Table(2, 3)
        self.assertEquals(table.get_size(), (2,3))
        self.assertEquals(table.get_homogeneous(), False)
        table = Gtk.Table(2, 3, True)
        self.assertEquals(table.get_size(), (2,3))
        self.assertEquals(table.get_homogeneous(), True)

        # Test PyGTK interface
        table = Gtk.Table(rows=3, columns=2)
        self.assertEquals(table.get_size(), (3,2))
        # Test using the actual property names
        table = Gtk.Table(n_rows=2, n_columns=3, homogeneous=True)
        self.assertEquals(table.get_size(), (2,3))
        self.assertEquals(table.get_homogeneous(), True)

        label = Gtk.Label('Hello')
        table.attach(label, 0, 1, 0, 1)
        self.assertEquals(label, table.get_children()[0])

    def test_scrolledwindow(self):
        sw = Gtk.ScrolledWindow()
        sb = sw.get_hscrollbar()
        self.assertEquals(sw.get_hadjustment(), sb.get_adjustment())
        sb = sw.get_vscrollbar()
        self.assertEquals(sw.get_vadjustment(), sb.get_adjustment())

    def test_widget_drag_methods(self):
        widget = Gtk.Button()

        # here we are not checking functionality, only that the methods exist
        # and except the right number of arguments

        widget.drag_check_threshold(0, 0, 0, 0)

        # drag_dest_ methods
        widget.drag_dest_set(Gtk.DestDefaults.DROP, None, Gdk.DragAction.COPY)
        widget.drag_dest_add_image_targets()
        widget.drag_dest_add_text_targets()
        widget.drag_dest_add_uri_targets()
        widget.drag_dest_get_track_motion()
        widget.drag_dest_set_track_motion(True)
        widget.drag_dest_get_target_list()
        widget.drag_dest_set_target_list(Gtk.TargetList.new([Gtk.TargetEntry()]))
        widget.drag_dest_unset()

        widget.drag_highlight()
        widget.drag_unhighlight()

        # drag_source_ methods
        widget.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, None, Gdk.DragAction.MOVE)
        widget.drag_source_add_image_targets()
        widget.drag_source_add_text_targets()
        widget.drag_source_add_uri_targets()
        widget.drag_source_set_icon_name("")
        widget.drag_source_set_icon_pixbuf(GdkPixbuf.Pixbuf())
        widget.drag_source_set_icon_stock("")
        widget.drag_source_get_target_list()
        widget.drag_source_set_target_list(Gtk.TargetList.new([Gtk.TargetEntry()]))
        widget.drag_source_unset()

        # these methods cannot be called because they require a valid drag on
        # a real GdkWindow. So we only check that they exist and are callable.
        self.assertTrue(hasattr(widget.drag_dest_set_proxy, '__call__'))
        self.assertTrue(hasattr(widget.drag_get_data, '__call__'))

class TestGio(unittest.TestCase):
    def setUp(self):
        os.environ['GSETTINGS_BACKEND'] = 'memory'
        # support a separate build tree, so look in build dir first
        os.environ['GSETTINGS_SCHEMA_DIR'] = os.environ.get('TESTS_BUILDDIR', 
                os.path.dirname(__file__))
        self.settings = Gio.Settings('org.gnome.test')
        # we change the values in the tests, so set them to predictable start
        # value
        self.settings.reset('test-string')
        self.settings.reset('test-array')

    def test_file_enumerator(self):
        self.assertEquals(Gio.FileEnumerator, overrides.Gio.FileEnumerator)
        f = Gio.file_new_for_path("./")

        iter_info = []
        for info in f.enumerate_children("standard::*", 0, None):
            iter_info.append(info.get_name())

        next_info = []
        enumerator = f.enumerate_children("standard::*", 0, None)
        while True:
            info = enumerator.next_file(None)
            if info is None:
                break
            next_info.append(info.get_name())

        self.assertEquals(iter_info, next_info)

    def test_gsettings_native(self):
        self.assertTrue('test-array' in self.settings.list_keys())

        # get various types
        v = self.settings.get_value('test-boolean')
        self.assertEqual(v.get_boolean(), True)
        self.assertEqual(self.settings.get_boolean('test-boolean'), True)

        v = self.settings.get_value('test-string')
        self.assertEqual(v.get_string(), 'Hello')
        self.assertEqual(self.settings.get_string('test-string'), 'Hello')

        v = self.settings.get_value('test-array')
        self.assertEqual(v.unpack(), [1, 2])

        v = self.settings.get_value('test-tuple')
        self.assertEqual(v.unpack(), (1, 2))

        # set a value
        self.settings.set_string('test-string', 'World')
        self.assertEqual(self.settings.get_string('test-string'), 'World')

        self.settings.set_value('test-string', GLib.Variant('s', 'Goodbye'))
        self.assertEqual(self.settings.get_string('test-string'), 'Goodbye')

    def test_gsettings_constructor(self):
        # default constructor uses path from schema
        self.assertEqual(self.settings.get_property('path'), '/tests/')

        # optional constructor arguments
        with_path = Gio.Settings('org.gnome.nopathtest', path='/mypath/')
        self.assertEqual(with_path.get_property('path'), '/mypath/')
        self.assertEqual(with_path['np-int'], 42)

    def test_gsettings_override(self):
        # dictionary interface
        self.assertEqual(len(self.settings), 4)
        self.assertTrue('test-array' in self.settings)
        self.assertTrue('test-array' in self.settings.keys())
        self.failIf('nonexisting' in self.settings)
        self.failIf(4 in self.settings)
        self.assertEqual(bool(self.settings), True)

        # get various types
        self.assertEqual(self.settings['test-boolean'], True)
        self.assertEqual(self.settings['test-string'], 'Hello')
        self.assertEqual(self.settings['test-array'], [1, 2])
        self.assertEqual(self.settings['test-tuple'], (1, 2))

        self.assertRaises(KeyError, self.settings.__getitem__, 'unknown')
        self.assertRaises(KeyError, self.settings.__getitem__, 2)

        # set a value
        self.settings['test-string'] = 'Goodbye'
        self.assertEqual(self.settings['test-string'], 'Goodbye')
        self.settings['test-array'] = [3, 4, 5]
        self.assertEqual(self.settings['test-array'], [3, 4, 5])

        self.assertRaises(TypeError, self.settings.__setitem__, 'test-string', 1)
        self.assertRaises(KeyError, self.settings.__setitem__, 'unknown', 'moo')

    def test_gsettings_empty(self):
        empty = Gio.Settings('org.gnome.empty', path='/tests/')
        self.assertEqual(len(empty), 0)
        self.assertEqual(bool(empty), True)
        self.assertEqual(empty.keys(), [])

    def test_closures(self):
        # make sure this doesn't crash
        def fake_cb(*args):
            pass

        ag = Gtk.AccelGroup()
        ag.connect(Gdk.KEY_l, Gdk.ModifierType.CONTROL_MASK, 0, fake_cb)
