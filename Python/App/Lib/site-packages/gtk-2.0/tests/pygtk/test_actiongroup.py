# Test for Bug #162874

import gc
import unittest

from common import gtk, gobject


class ActionGroupTest(unittest.TestCase):
    ui0 = '''<ui>
    <menubar name="MenuBar">
      <menu action="File">
        <menuitem action="Quit"/>
      </menu>
      <menu action="Sound">
        <menuitem action="Mute"/>
      </menu>
      <menu action="RadioBand">
        <menuitem action="AM"/>
        <menuitem action="FM"/>
        <menuitem action="SSB"/>
      </menu>
    </menubar>
    <toolbar name="Toolbar">
      <toolitem action="Quit"/>
      <separator/>
      <toolitem action="Mute"/>
      <separator name="sep1"/>
      <placeholder name="RadioBandItems">
        <toolitem action="AM"/>
        <toolitem action="FM"/>
        <toolitem action="SSB"/>
      </placeholder>
    </toolbar>
    </ui>'''

    def build_gui(self):
        # Create the toplevel window
        window = gtk.Window()
        vbox = gtk.VBox()
        window.add(vbox)

        # Create a UIManager instance
        uimanager = gtk.UIManager()
        self.uimanager = uimanager

        # Create the base ActionGroup
        actiongroup = gtk.ActionGroup('UIMergeExampleBase')

        actiongroup.add_actions([('File', None, '_File'),
                                  ('Sound', None, '_Sound'),
                                  ('RadioBand', None, '_Radio Band')])
        uimanager.insert_action_group(actiongroup, 0)

        # Create an ActionGroup
        actiongroup0 = gtk.ActionGroup('UIMergeExample0')

        # Create a ToggleAction, etc.
        actiongroup0.add_toggle_actions([('Mute', None, '_Mute', '<Control>m',
                                          'Mute the volume', self.cb)])

        # Create actions
        actiongroup0.add_actions([('Quit', gtk.STOCK_QUIT, '_Quit me!', None,
                                   'Quit the Program', self.cb)])

        # Create some RadioActions
        actiongroup0.add_radio_actions([('AM', None, '_AM', '<Control>a',
                                         'AM Radio', 0),
                                        ('FM', None, '_FM', '<Control>f',
                                         'FM Radio', 1),
                                        ('SSB', None, '_SSB', '<Control>b',
                                         'SSB Radio', 2),
                                        ], 0, self.cb)

        # Add the actiongroup to the uimanager
        uimanager.insert_action_group(actiongroup0, 1)

        self.ag0 = actiongroup0
        del actiongroup0

        # Add a UI description
        self.merge_id0 = uimanager.add_ui_from_string(self.ui0)

        # Create a MenuBar
        menubar = uimanager.get_widget('/MenuBar')
        vbox.pack_start(menubar, False)

        # Create a Toolbar
        toolbar = uimanager.get_widget('/Toolbar')
        vbox.pack_start(toolbar, False)

        gobject.timeout_add(50, self.timeout_cb)

        gtk.main()
        return

    def timeout_cb(self):
        ag0 = self.ag0
        uimanager = self.uimanager
        del self.ag0, self.uimanager

        uimanager.remove_ui(self.merge_id0)
        uimanager.remove_action_group(ag0)

        if gobject.pygobject_version >= (2,13):
            ag0ref = ag0.weak_ref()
            del ag0
            self.assertEqual(ag0ref(), None)
        else:
            gc.collect()             # Clean out unreachable objects

            del ag0
            self.assertEqual(gc.collect(), 1) # Collect just the ActionGroup

            uimanager.ensure_update()
            self.assertEqual(gc.collect(), 6) # Now the GtkActions have lost their last
                                     # GObject reference; they should be collected.
                                     # We have a ToggleAction, an Action and a
                                     # RadioAction, plus self.cb is bound in three
                                     # closures.

        gtk.main_quit()

    def setUp(self):
        gc.collect()

    def testActionGroups(self):
        self.build_gui()

    def cb(self, action):
        return


class ActionTest(unittest.TestCase):
    def testActionSubclass(self):

        class MyAction(gtk.Action):
            __gtype_name__ = 'MyAction'
            def __init__(self):
                self._activated = False
                gtk.Action.__init__(self, "name", "label", "tooltip", "stock_id")
            def do_activate(self):
                self._activated = True
        
        myaction = MyAction()
        myaction.activate()
        self.assertEqual(myaction._activated, True)

    def testSetItemClasses(self):

        class MyAction(gtk.Action):
            def __init__(self):
                gtk.Action.__init__(self, 'name', 'label', None, None)

        def set_menu_item_type(type):
            MyAction.set_menu_item_type(type)

        def set_tool_item_type(type):
            MyAction.set_tool_item_type(type)

        self.assertRaises(TypeError, lambda: set_menu_item_type(None))
        self.assertRaises(TypeError, lambda: set_menu_item_type(gtk.Button))
        set_menu_item_type(gtk.ImageMenuItem)
        self.assert_(isinstance(MyAction().create_menu_item(), gtk.ImageMenuItem))

        self.assertRaises(TypeError, lambda: set_tool_item_type(None))
        self.assertRaises(TypeError, lambda: set_tool_item_type(gtk.Button))
        set_tool_item_type(gtk.SeparatorToolItem)
        self.assert_(isinstance(MyAction().create_tool_item(), gtk.SeparatorToolItem))
        

if __name__ == '__main__':
    unittest.main()
