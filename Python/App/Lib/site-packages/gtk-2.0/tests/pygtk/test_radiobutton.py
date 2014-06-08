import unittest

from common import gtk

class RadioTest(unittest.TestCase):
    widget_type = None
    constructor_args = ()

    def new(self):
        return self.widget_type(*self.constructor_args)

    def newLabel(self, label):
        return self.widget_type(None, label)

    def newGroup(self, group):
        return self.widget_type(group)

    def getLabel(self, obj):
        return obj.get_property('label')

    def compareGroups(self, group1, group2):
        return self.assertEqual(group1, group2)

    def testCreate(self):
        if self.widget_type is None:
            return
        radio = self.new()
        self.assert_(isinstance(radio, self.widget_type))

    def testLabel(self):
        if self.widget_type is None:
            return
        radio = self.newLabel('test-radio')
        self.assertEqual(self.getLabel(radio), 'test-radio')

    def testGroup(self):
        if self.widget_type is None:
            return
        radio = self.new()
        radio2 = self.newGroup(radio)
        self.compareGroups(radio.get_group(), radio2.get_group())
        self.compareGroups(radio2.get_group(), radio.get_group())

    def testEmptyGroup(self):
        if self.widget_type is None:
            return
        radio = self.new()
        radio2 = self.new()
        self.compareGroups(radio.get_group(), [radio])
        self.compareGroups(radio2.get_group(), [radio2])
        radio2.set_group(radio)
        self.compareGroups(radio.get_group(), radio2.get_group())
        self.compareGroups(radio2.get_group(), radio.get_group())
        radio2.set_group(None)
        self.compareGroups(radio.get_group(), [radio])
        self.compareGroups(radio2.get_group(), [radio2])

class RadioButtonTest(RadioTest):
    widget_type = gtk.RadioButton

class RadioActionTest(RadioTest):
    widget_type = gtk.RadioAction
    constructor_args = ('RadioAction', 'test-radio-action', '', '', 0)

    def newGroup(self, radio):
        # No constructor, so set it manually
        obj = self.new()
        obj.set_group(radio)
        return obj

    def newLabel(self, label):
        return gtk.RadioAction('RadioAction', label, '', '', 0)

class RadioToolButtonTest(RadioTest):
    widget_type = gtk.RadioToolButton

    def compareGroups(self, group1, group2):
        # GtkRadioToolButton.set/get_groups return GtkRadioButtons,
        # so instead of doing a normal cmp, compare ids
        return cmp(map(id, group1), map(id, group2))

    def newLabel(self, label):
        # We don't have a constructor for which we can pass in a label
        # for, so just call set_label instead
        radio = gtk.RadioToolButton(None)
        radio.set_label(label)
        return radio

class RadioMenuItem(RadioTest):
    widget_type = gtk.RadioMenuItem

    def getLabel(self, obj):
        # The label is stored in a gtk.AccelLabel, which is the only
        # child of the RadioMenuItem.
        return obj.get_child().get_text()

if __name__ == '__main__':
    unittest.main()
