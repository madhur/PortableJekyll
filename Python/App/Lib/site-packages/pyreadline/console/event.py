class Event(object):
    u'''Represent events from the console.'''
    def __init__(self, console, input):
        pass

    def __repr__(self):
        u'''Display an event for debugging.'''
        if self.type in [u'KeyPress', u'KeyRelease']:
            chr = self.char
            if ord(chr)<ord(u"A"):
                chr = u"?"
            s = u"%s char='%s'%d keysym='%s' keycode=%d:%x state=%x keyinfo=%s" % \
                   (self.type, chr, ord(self.char), self.keysym, self.keycode, self.keycode,
                     self.state, self.keyinfo)
        elif self.type in [u'Motion', u'Button']:
            s = u'%s x=%d y=%d state=%x' % (self.type, self.x, self.y, self.state)
        elif self.type == u'Configure':
            s = u'%s w=%d h=%d' % (self.type, self.width, self.height)
        elif self.type in [u'FocusIn', u'FocusOut']:
            s = self.type
        elif self.type == u'Menu':
            s = u'%s state=%x' % (self.type, self.state)
        else:
            s = u'unknown event type'
        return s


#    def __str__(self):
#        return "('%s',%s,%s,%s)"%(self.char,self.key,self.state,self.keyinfo)