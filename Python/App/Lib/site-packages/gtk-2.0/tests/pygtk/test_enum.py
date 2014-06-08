import unittest
import warnings

from gobject import GEnum, GFlags, GObject, GType, PARAM_READWRITE
from common import gobject, atk, gtk

class PObject(GObject):
    __gproperties__ = {
        'enum': (gtk.WindowType, 'blurb', 'description',
                 gtk.WINDOW_TOPLEVEL, PARAM_READWRITE),
        'enum2': (gtk.WindowType, 'blurb', 'description',
                  int(gtk.WINDOW_TOPLEVEL), PARAM_READWRITE),
        'flags': (gtk.AttachOptions, 'blurb', 'description',
                  gtk.EXPAND, PARAM_READWRITE),
        'flags2': (gtk.AttachOptions, 'blurb', 'description',
                   int(gtk.EXPAND), PARAM_READWRITE),
    }

class EnumTest(unittest.TestCase):
    def testEnums(self):
        self.assertTrue(issubclass(GEnum, int))
        self.assertTrue(isinstance(atk.LAYER_OVERLAY, atk.Layer))
        self.assertTrue(isinstance(atk.LAYER_OVERLAY, int))
        self.assertTrue('LAYER_OVERLAY' in repr(atk.LAYER_OVERLAY))
        self.assertTrue(int(atk.LAYER_OVERLAY))
        self.assertEquals(atk.LAYER_INVALID, 0)
        self.assertNotEquals(atk.LAYER_INVALID, 1)
        self.assertNotEquals(atk.LAYER_INVALID, -1)
        self.assertNotEquals(atk.LAYER_INVALID, atk.LAYER_BACKGROUND)

    def testComparisionWarning(self):
        warnings.filterwarnings("error", "", Warning, "", 0)
        try:
            self.assertNotEquals(atk.LAYER_INVALID, atk.RELATION_NULL)
        except Warning:
            pass
        else:
            raise AssertionError
        warnings.resetwarnings()

    def testWindowGetState(self):
        win = gtk.Window()
        win.realize()

        state = win.window.get_state()
        self.assertEquals(state, gtk.gdk.WINDOW_STATE_WITHDRAWN)
        self.assertTrue(isinstance(state, gtk.gdk.WindowState))
        self.assertTrue('WINDOW_STATE_WITHDRAWN' in repr(state))

    def testProperty(self):
        win = gtk.Window()

        wtype = win.get_property('type')
        self.assertEquals(wtype, gtk.WINDOW_TOPLEVEL)
        self.assertTrue(isinstance(wtype, gtk.WindowType))
        self.assertTrue('WINDOW_TOPLEVEL' in repr(wtype))

    def testAtkObj(self):
        obj = atk.NoOpObject(GObject())
        self.assertEquals(obj.get_role(), atk.ROLE_INVALID)

    def testGParam(self):
        win = gtk.Window()
        enums = filter(lambda x: GType.is_a(x.value_type, GEnum),
                       gobject.list_properties(win))
        self.assertTrue(enums)
        enum = enums[0]
        self.assertTrue(hasattr(enum, 'enum_class'))
        self.assertTrue(issubclass(enum.enum_class, GEnum))

    def testWeirdEnumValues(self):
        self.assertEquals(int(gtk.gdk.NOTHING), -1)
        self.assertEquals(int(gtk.gdk.BUTTON_PRESS), 4)

    def testParamSpec(self):
        props = filter(lambda prop: GType.is_a(prop.value_type, GEnum),
                       gobject.list_properties(gtk.Window))
        self.assertTrue(len(props)>= 6)
        props = filter(lambda prop: prop.name == 'type', props)
        self.assertTrue(props)
        pspec = props[0]
        klass = pspec.enum_class
        self.assertEquals(klass, gtk.WindowType)
        self.assertTrue(hasattr(klass, '__enum_values__'))
        self.assertTrue(isinstance(klass.__enum_values__, dict))
        self.assertTrue(len(klass.__enum_values__) >= 2)
        self.assertTrue(isinstance(pspec.default_value, gtk.WindowType))

    def testOutofBounds(self):
        val = gtk.icon_size_register('fake', 24, 24)
        self.assertTrue(isinstance(val, gobject.GEnum))
        self.assertEquals(int(val), 7)
        self.assertTrue('7' in repr(val))
        self.assertTrue('GtkIconSize' in repr(val))

    def testEnumProperty(self):
        default = PObject.props.enum.default_value
        self.assertTrue(isinstance(default, gtk.WindowType))
        self.assertEqual(default, gtk.WINDOW_TOPLEVEL)
        default = PObject.props.enum2.default_value
        self.assertTrue(isinstance(default, gtk.WindowType))
        self.assertEqual(default, gtk.WINDOW_TOPLEVEL)

class FlagsTest(unittest.TestCase):
    def testFlags(self):
        self.assertTrue(issubclass(GFlags, int))
        self.assertTrue(isinstance(gtk.gdk.BUTTON_PRESS_MASK, gtk.gdk.EventMask))
        self.assertTrue(isinstance(gtk.gdk.BUTTON_PRESS_MASK, int))
        self.assertEquals(gtk.gdk.BUTTON_PRESS_MASK, 256)
        self.assertNotEquals(gtk.gdk.BUTTON_PRESS_MASK, 0)
        self.assertNotEquals(gtk.gdk.BUTTON_PRESS_MASK, -256)
        self.assertNotEquals(gtk.gdk.BUTTON_PRESS_MASK, gtk.gdk.BUTTON_RELEASE_MASK)

        self.assertEquals(gtk.gdk.EventMask.__bases__[0], GFlags)
        self.assertEquals(len(gtk.gdk.EventMask.__flags_values__), 22)

    def testComparisionWarning(self):
        warnings.filterwarnings("error", "", Warning, "", 0)
        try:
            self.assertNotEquals(gtk.ACCEL_VISIBLE, gtk.EXPAND)
        except Warning:
            pass
        else:
            raise AssertionError
        warnings.resetwarnings()

    def testFlagOperations(self):
        a = gtk.gdk.BUTTON_PRESS_MASK
        self.assertTrue(isinstance(a, GFlags))
        self.assertEquals(a.first_value_name, 'GDK_BUTTON_PRESS_MASK')
        self.assertEquals(a.first_value_nick, 'button-press-mask')
        self.assertEquals(a.value_names, ['GDK_BUTTON_PRESS_MASK'],
                          a.value_names)
        self.assertEquals(a.value_nicks, ['button-press-mask'],
                          a.value_names)
        b = gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.BUTTON_RELEASE_MASK
        self.assertTrue(isinstance(b, GFlags))
        self.assertEquals(b.first_value_name, 'GDK_BUTTON_PRESS_MASK')
        self.assertEquals(b.first_value_nick, 'button-press-mask')
        self.assertEquals(b.value_names, ['GDK_BUTTON_PRESS_MASK',
                                          'GDK_BUTTON_RELEASE_MASK'])
        self.assertEquals(b.value_nicks, ['button-press-mask',
                                          'button-release-mask'])
        c = (gtk.gdk.BUTTON_PRESS_MASK |
             gtk.gdk.BUTTON_RELEASE_MASK |
             gtk.gdk.ENTER_NOTIFY_MASK)
        self.assertTrue(isinstance(c, GFlags))
        self.assertEquals(c.first_value_name, 'GDK_BUTTON_PRESS_MASK')
        self.assertEquals(c.first_value_nick, 'button-press-mask')
        self.assertEquals(c.value_names,
                          ['GDK_BUTTON_PRESS_MASK',
                           'GDK_BUTTON_RELEASE_MASK',
                           'GDK_ENTER_NOTIFY_MASK'])
        self.assertEquals(c.value_nicks,
                          ['button-press-mask',
                           'button-release-mask',
                           'enter-notify-mask'])
        self.assertTrue(int(a))
        self.assertEquals(int(a), int(gtk.gdk.BUTTON_PRESS_MASK))
        self.assertTrue(int(b))
        self.assertEquals(int(b), (int(gtk.gdk.BUTTON_PRESS_MASK) |
                                   int(gtk.gdk.BUTTON_RELEASE_MASK)))
        self.assertTrue(int(c))
        self.assertEquals(int(c), (int(gtk.gdk.BUTTON_PRESS_MASK) |
                                   int(gtk.gdk.BUTTON_RELEASE_MASK) |
                                   int(gtk.gdk.ENTER_NOTIFY_MASK)))

    def testUnsupportedOpertionWarning(self):
        warnings.filterwarnings("error", "", Warning, "", 0)
        try:
            value = gtk.gdk.BUTTON_PRESS_MASK + gtk.gdk.BUTTON_RELEASE_MASK
        except Warning:
            pass
        else:
            raise AssertionError
        warnings.resetwarnings()

    def testParamSpec(self):
        props = filter(lambda x: GType.is_a(x.value_type, GFlags),
                       gtk.Table.list_child_properties())
        self.assertTrue(len(props) >= 2)
        pspec = props[0]
        klass = pspec.flags_class
        self.assertEquals(klass, gtk.AttachOptions)
        self.assertTrue(hasattr(klass, '__flags_values__'))
        self.assertTrue(isinstance(klass.__flags_values__, dict))
        self.assertTrue(len(klass.__flags_values__) >= 3)
        self.assertTrue(isinstance(pspec.default_value, gtk.AttachOptions))

    def testEnumComparision(self):
        enum = gtk.TREE_VIEW_DROP_BEFORE
        self.assertEquals(enum, 0)
        self.assertTrue(not enum == 10)
        self.assertTrue(not enum != 0)
        self.assertNotEquals(enum, 10)
        self.assertTrue(not enum < 0)
        self.assertTrue(enum < 10)
        self.assertTrue(not enum > 0)
        self.assertTrue(not enum > 10)
        self.assertTrue(enum >= 0)
        self.assertTrue(not enum >= 10)
        self.assertTrue(enum <= 0)
        self.assertTrue(enum <= 10)

    def testFlagComparision(self):
        flag = gtk.gdk.EXPOSURE_MASK
        self.assertEquals(flag, 2)
        self.assertTrue(not flag == 10)
        self.assertTrue(not flag != 2)
        self.assertNotEquals(flag, 10)
        self.assertTrue(not flag < 2)
        self.assertTrue(flag < 10)
        self.assertTrue(not flag > 2)
        self.assertTrue(not flag > 10)
        self.assertTrue(flag >= 2)
        self.assertTrue(not flag >= 10)
        self.assertTrue(flag <= 2)
        self.assertTrue(flag <= 10)

    def testFlagsProperty(self):
        default = PObject.props.flags.default_value
        self.assertTrue(isinstance(default, gtk.AttachOptions))
        self.assertEqual(default, gtk.EXPAND)
        default = PObject.props.flags2.default_value
        self.assertTrue(isinstance(default, gtk.AttachOptions))
        self.assertEqual(default, gtk.EXPAND)

if __name__ == '__main__':
    unittest.main()
