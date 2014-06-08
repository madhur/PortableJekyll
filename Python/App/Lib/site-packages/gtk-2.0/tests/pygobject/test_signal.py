# -*- Mode: Python -*-

import gc
import unittest
import sys

import gobject
import testhelper
from compathelper import _long

class C(gobject.GObject):
    __gsignals__ = { 'my_signal': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,
                                   (gobject.TYPE_INT,)) }
    def do_my_signal(self, arg):
        self.arg = arg

class D(C):
    def do_my_signal(self, arg2):
        self.arg2 = arg2
        C.do_my_signal(self, arg2)

class TestSignalCreation(unittest.TestCase):
    # Bug 540376.
    def test_illegals(self):
        self.assertRaises(TypeError, lambda: gobject.signal_new('test',
                                                                None,
                                                                0,
                                                                gobject.TYPE_NONE,
                                                                (gobject.TYPE_LONG,)))


class TestChaining(unittest.TestCase):
    def setUp(self):
        self.inst = C()
        self.inst.connect("my_signal", self.my_signal_handler_cb, 1, 2, 3)

    def my_signal_handler_cb(self, *args):
        assert len(args) == 5
        assert isinstance(args[0], C)
        assert args[0] == self.inst

        assert isinstance(args[1], int)
        assert args[1] == 42

        assert args[2:] == (1, 2, 3)

    def testChaining(self):
        self.inst.emit("my_signal", 42)
        assert self.inst.arg == 42

    def testChaining(self):
        inst2 = D()
        inst2.emit("my_signal", 44)
        assert inst2.arg == 44
        assert inst2.arg2 == 44

# This is for bug 153718
class TestGSignalsError(unittest.TestCase):
    def testInvalidType(self, *args):
        def foo():
            class Foo(gobject.GObject):
                __gsignals__ = None
        self.assertRaises(TypeError, foo)
        gc.collect()

    def testInvalidName(self, *args):
        def foo():
            class Foo(gobject.GObject):
                __gsignals__ = {'not-exists' : 'override'}
        self.assertRaises(TypeError, foo)
        gc.collect()

class TestGPropertyError(unittest.TestCase):
    def testInvalidType(self, *args):
        def foo():
            class Foo(gobject.GObject):
                __gproperties__ = None
        self.assertRaises(TypeError, foo)
        gc.collect()

    def testInvalidName(self, *args):
        def foo():
            class Foo(gobject.GObject):
                __gproperties__ = { None: None }

        self.assertRaises(TypeError, foo)
        gc.collect()

class TestList(unittest.TestCase):
    def testListObject(self):
        self.assertEqual(gobject.signal_list_names(C), ('my-signal',))


def my_accumulator(ihint, return_accu, handler_return, user_data):
    """An accumulator that stops emission when the sum of handler
    returned values reaches 3"""
    assert user_data == "accum data"
    if return_accu >= 3:
        return False, return_accu
    return True, return_accu + handler_return

class Foo(gobject.GObject):
    __gsignals__ = {
        'my-acc-signal': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_INT,
                                   (), my_accumulator, "accum data"),
        'my-other-acc-signal': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_BOOLEAN,
                                (), gobject.signal_accumulator_true_handled)
        }

class TestAccumulator(unittest.TestCase):

    def testAccumulator(self):
        inst = Foo()
        inst.connect("my-acc-signal", lambda obj: 1)
        inst.connect("my-acc-signal", lambda obj: 2)
        ## the value returned in the following handler will not be
        ## considered, because at this point the accumulator already
        ## reached its limit.
        inst.connect("my-acc-signal", lambda obj: 3)
        retval = inst.emit("my-acc-signal")
        self.assertEqual(retval, 3)

    def testAccumulatorTrueHandled(self):
        inst = Foo()
        inst.connect("my-other-acc-signal", self._true_handler1)
        inst.connect("my-other-acc-signal", self._true_handler2)
        ## the following handler will not be called because handler2
        ## returns True, so it should stop the emission.
        inst.connect("my-other-acc-signal", self._true_handler3)
        self.__true_val = None
        inst.emit("my-other-acc-signal")
        self.assertEqual(self.__true_val, 2)

    def _true_handler1(self, obj):
        self.__true_val = 1
        return False
    def _true_handler2(self, obj):
        self.__true_val = 2
        return True
    def _true_handler3(self, obj):
        self.__true_val = 3
        return False

class E(gobject.GObject):
    __gsignals__ = { 'signal': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,
                                ()) }
    def __init__(self):
        gobject.GObject.__init__(self)
        self.status = 0

    def do_signal(self):
        assert self.status == 0
        self.status = 1

class F(gobject.GObject):
    __gsignals__ = { 'signal': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,
                                ()) }
    def __init__(self):
        gobject.GObject.__init__(self)
        self.status = 0

    def do_signal(self):
        self.status += 1

class TestEmissionHook(unittest.TestCase):
    def testAdd(self):
        self.hook = True
        e = E()
        e.connect('signal', self._callback)
        gobject.add_emission_hook(E, "signal", self._emission_hook)
        e.emit('signal')
        self.assertEqual(e.status, 3)

    def testRemove(self):
        self.hook = False
        e = E()
        e.connect('signal', self._callback)
        hook_id = gobject.add_emission_hook(E, "signal", self._emission_hook)
        gobject.remove_emission_hook(E, "signal", hook_id)
        e.emit('signal')
        self.assertEqual(e.status, 3)

    def _emission_hook(self, e):
        self.assertEqual(e.status, 1)
        e.status = 2

    def _callback(self, e):
        if self.hook:
            self.assertEqual(e.status, 2)
        else:
            self.assertEqual(e.status, 1)
        e.status = 3

    def testCallbackReturnFalse(self):
        self.hook = False
        obj = F()
        def _emission_hook(obj):
            obj.status += 1
            return False
        hook_id = gobject.add_emission_hook(obj, "signal", _emission_hook)
        obj.emit('signal')
        obj.emit('signal')
        self.assertEqual(obj.status, 3)

    def testCallbackReturnTrue(self):
        self.hook = False
        obj = F()
        def _emission_hook(obj):
            obj.status += 1
            return True
        hook_id = gobject.add_emission_hook(obj, "signal", _emission_hook)
        obj.emit('signal')
        obj.emit('signal')
        gobject.remove_emission_hook(obj, "signal", hook_id)
        self.assertEqual(obj.status, 4)

    def testCallbackReturnTrueButRemove(self):
        self.hook = False
        obj = F()
        def _emission_hook(obj):
            obj.status += 1
            return True
        hook_id = gobject.add_emission_hook(obj, "signal", _emission_hook)
        obj.emit('signal')
        gobject.remove_emission_hook(obj, "signal", hook_id)
        obj.emit('signal')
        self.assertEqual(obj.status, 3)

class TestClosures(unittest.TestCase):
    def setUp(self):
        self.count = 0

    def _callback(self, e):
        self.count += 1

    def testDisconnect(self):
        e = E()
        e.connect('signal', self._callback)
        e.disconnect_by_func(self._callback)
        e.emit('signal')
        self.assertEqual(self.count, 0)

    def testHandlerBlock(self):
        e = E()
        e.connect('signal', self._callback)
        e.handler_block_by_func(self._callback)
        e.emit('signal')
        self.assertEqual(self.count, 0)

    def testHandlerUnBlock(self):
        e = E()
        signal_id = e.connect('signal', self._callback)
        e.handler_block(signal_id)
        e.handler_unblock_by_func(self._callback)
        e.emit('signal')
        self.assertEqual(self.count, 1)

    def testHandlerBlockMethod(self):
        # Filed as #375589
        class A:
            def __init__(self):
                self.a = 0

            def callback(self, o):
                self.a = 1
                o.handler_block_by_func(self.callback)

        inst = A()
        e = E()
        e.connect("signal", inst.callback)
        e.emit('signal')
        self.assertEqual(inst.a, 1)
        gc.collect()

    def testGString(self):
        class C(gobject.GObject):
            __gsignals__ = { 'my_signal': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_GSTRING,
                                           (gobject.TYPE_GSTRING,)) }
            def __init__(self, test):
                gobject.GObject.__init__(self)
                self.test = test
            def do_my_signal(self, data):
                self.data = data
                self.test.assertEqual(len(data), 3)
                return ''.join([data[2], data[1], data[0]])
        c = C(self)
        data = c.emit("my_signal", "\01\00\02")
        self.assertEqual(data, "\02\00\01")

class SigPropClass(gobject.GObject):
    __gsignals__ = { 'my_signal': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,
                                   (gobject.TYPE_INT,)) }

    __gproperties__ = {
        'foo': (str, None, None, '', gobject.PARAM_WRITABLE|gobject.PARAM_CONSTRUCT),
        }

    signal_emission_failed = False

    def do_my_signal(self, arg):
        self.arg = arg

    def do_set_property(self, pspec, value):
        if pspec.name == 'foo':
            self._foo = value
        else:
            raise AttributeError('unknown property %s' % pspec.name)
        try:
            self.emit("my-signal", 1)
        except TypeError:
            self.signal_emission_failed = True


class TestSigProp(unittest.TestCase):
    def testEmitInPropertySetter(self):
        obj = SigPropClass()
        self.failIf(obj.signal_emission_failed)

f = gobject.SIGNAL_RUN_FIRST
l = gobject.SIGNAL_RUN_LAST
float = gobject.TYPE_FLOAT
double = gobject.TYPE_DOUBLE
uint = gobject.TYPE_UINT
ulong = gobject.TYPE_ULONG

class CM(gobject.GObject):
    __gsignals__ = dict(
        test1=(f, None, ()),
        test2=(l, None, (str,)),
        test3=(l, int, (double,)),
        test4=(f, None, (bool, _long, float, double, int, uint, ulong)),
        test_float=(l, float, (float,)),
        test_double=(l, double, (double, )),
        test_string=(l, str, (str, )),
        test_object=(l, object, (object, )),
    )

class _TestCMarshaller:
    def setUp(self):
        self.obj = CM()
        testhelper.connectcallbacks(self.obj)

    def testTest1(self):
        self.obj.emit("test1")

    def testTest2(self):
        self.obj.emit("test2", "string")

    def testTest3(self):
        rv = self.obj.emit("test3", 42.0)
        self.assertEqual(rv, 20)

    def testTest4(self):
        self.obj.emit("test4", True, _long(10), 3.14, 1.78, 20, _long(30), _long(31))

    def testTestReturnFloat(self):
        rv = self.obj.emit("test-float", 1.234)
        self.failUnless(rv >= 1.233999 and rv <= 1.2400001, rv)

    def testTestReturnDouble(self):
        rv = self.obj.emit("test-double", 1.234)
        self.assertEqual(rv, 1.234)

    def testTestReturnString(self):
        rv = self.obj.emit("test-string", "str")
        self.assertEqual(rv, "str")

    def testTestReturnObject(self):
        rv = self.obj.emit("test-object", self)
        self.assertEqual(rv, self)

if 'generic-c-marshaller' in gobject.features:
    class TestCMarshaller(_TestCMarshaller, unittest.TestCase):
        pass
else:
    print()
    print('** WARNING: LIBFFI disabled, not testing')
    print()

# Test for 374653
class TestPyGValue(unittest.TestCase):
    def testNoneNULLBoxedConversion(self):
        class C(gobject.GObject):
            __gsignals__ = dict(my_boxed_signal=(
                gobject.SIGNAL_RUN_LAST,
                gobject.type_from_name('GStrv'), ()))

        obj = C()
        obj.connect('my-boxed-signal', lambda obj: None)
        sys.last_type = None
        obj.emit('my-boxed-signal')
        assert not sys.last_type

if __name__ == '__main__':
    unittest.main()
