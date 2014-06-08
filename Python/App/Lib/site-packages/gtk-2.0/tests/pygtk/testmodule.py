import gtk

class PyLabel(gtk.Label):
    __gtype_name__ = 'PyLabel'

    def __init__(self):
        gtk.Label.__init__(self, "hello")
