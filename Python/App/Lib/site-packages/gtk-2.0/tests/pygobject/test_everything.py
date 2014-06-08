# -*- Mode: Python; py-indent-offset: 4 -*-
# coding=utf-8
# vim: tabstop=4 shiftwidth=4 expandtab

import unittest

import sys
sys.path.insert(0, "../")
from sys import getrefcount

import cairo

from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Regress as Everything

if sys.version_info < (3, 0):
    UNICHAR = "\xe2\x99\xa5"
    PY2_UNICODE_UNICHAR = unicode(UNICHAR, 'UTF-8')
else:
    UNICHAR = "♥"


class TestEverything(unittest.TestCase):

    def test_cairo_context(self):
        context = Everything.test_cairo_context_full_return()
        self.assertTrue(isinstance(context, cairo.Context))

        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 10, 10)
        context = cairo.Context(surface)
        Everything.test_cairo_context_none_in(context)

    def test_cairo_surface(self):
        surface = Everything.test_cairo_surface_none_return()
        self.assertTrue(isinstance(surface, cairo.ImageSurface))
        self.assertTrue(isinstance(surface, cairo.Surface))
        self.assertEquals(surface.get_format(), cairo.FORMAT_ARGB32)
        self.assertEquals(surface.get_width(), 10)
        self.assertEquals(surface.get_height(), 10)

        surface = Everything.test_cairo_surface_full_return()
        self.assertTrue(isinstance(surface, cairo.ImageSurface))
        self.assertTrue(isinstance(surface, cairo.Surface))
        self.assertEquals(surface.get_format(), cairo.FORMAT_ARGB32)
        self.assertEquals(surface.get_width(), 10)
        self.assertEquals(surface.get_height(), 10)

        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 10, 10)
        Everything.test_cairo_surface_none_in(surface)

        surface = Everything.test_cairo_surface_full_out()
        self.assertTrue(isinstance(surface, cairo.ImageSurface))
        self.assertTrue(isinstance(surface, cairo.Surface))
        self.assertEquals(surface.get_format(), cairo.FORMAT_ARGB32)
        self.assertEquals(surface.get_width(), 10)
        self.assertEquals(surface.get_height(), 10)

    def test_unichar(self):
        self.assertEquals("c", Everything.test_unichar("c"))

        if sys.version_info < (3, 0):
            self.assertEquals(UNICHAR, Everything.test_unichar(PY2_UNICODE_UNICHAR))
        self.assertEquals(UNICHAR, Everything.test_unichar(UNICHAR))
        self.assertRaises(TypeError, Everything.test_unichar, "")
        self.assertRaises(TypeError, Everything.test_unichar, "morethanonechar")
        

    def test_floating(self):
        e = Everything.TestFloating()
        self.assertEquals(e.__grefcount__, 1)

        e = GObject.new(Everything.TestFloating)
        self.assertEquals(e.__grefcount__, 1)

        e = Everything.TestFloating.new()
        self.assertEquals(e.__grefcount__, 1)

    def test_caller_allocates(self):
        struct_a = Everything.TestStructA()
        struct_a.some_int = 10
        struct_a.some_int8 = 21
        struct_a.some_double = 3.14
        struct_a.some_enum = Everything.TestEnum.VALUE3

        struct_a_clone = struct_a.clone()
        self.assertTrue(struct_a != struct_a_clone)
        self.assertEquals(struct_a.some_int, struct_a_clone.some_int)
        self.assertEquals(struct_a.some_int8, struct_a_clone.some_int8)
        self.assertEquals(struct_a.some_double, struct_a_clone.some_double)
        self.assertEquals(struct_a.some_enum, struct_a_clone.some_enum)

        struct_b = Everything.TestStructB()
        struct_b.some_int8 = 8
        struct_b.nested_a.some_int = 20
        struct_b.nested_a.some_int8 = 12
        struct_b.nested_a.some_double = 333.3333
        struct_b.nested_a.some_enum = Everything.TestEnum.VALUE2

        struct_b_clone = struct_b.clone()
        self.assertTrue(struct_b != struct_b_clone)
        self.assertEquals(struct_b.some_int8, struct_b_clone.some_int8)
        self.assertEquals(struct_b.nested_a.some_int, struct_b_clone.nested_a.some_int)
        self.assertEquals(struct_b.nested_a.some_int8, struct_b_clone.nested_a.some_int8)
        self.assertEquals(struct_b.nested_a.some_double, struct_b_clone.nested_a.some_double)
        self.assertEquals(struct_b.nested_a.some_enum, struct_b_clone.nested_a.some_enum)

    def test_wrong_type_of_arguments(self):
        try:
            Everything.test_int8()
        except TypeError:
            (e_type, e) = sys.exc_info()[:2]
            self.assertEquals(e.args, ("test_int8() takes exactly 1 argument(s) (0 given)",))

    def test_gtypes(self):
        gchararray_gtype = GObject.type_from_name('gchararray')
        gtype = Everything.test_gtype(str)
        self.assertEquals(gchararray_gtype, gtype)
        gtype = Everything.test_gtype('gchararray')
        self.assertEquals(gchararray_gtype, gtype)
        gobject_gtype = GObject.GObject.__gtype__
        gtype = Everything.test_gtype(GObject.GObject)
        self.assertEquals(gobject_gtype, gtype)
        gtype = Everything.test_gtype('GObject')
        self.assertEquals(gobject_gtype, gtype)
        self.assertRaises(TypeError, Everything.test_gtype, 'invalidgtype')

        class NotARegisteredClass(object):
            pass

        self.assertRaises(TypeError, Everything.test_gtype, NotARegisteredClass)

        class ARegisteredClass(GObject.GObject):
            __gtype_name__ = 'EverythingTestsARegisteredClass'

        gtype = Everything.test_gtype('EverythingTestsARegisteredClass')
        self.assertEquals(ARegisteredClass.__gtype__, gtype)
        gtype = Everything.test_gtype(ARegisteredClass)
        self.assertEquals(ARegisteredClass.__gtype__, gtype)
        self.assertRaises(TypeError, Everything.test_gtype, 'ARegisteredClass')
        
    def test_dir(self):
        attr_list = dir(Everything)
        
        # test that typelib attributes are listed
        self.assertTrue('TestStructA' in attr_list)
        
        # test that class attributes and methods are listed
        self.assertTrue('__class__' in attr_list)
        self.assertTrue('__dir__' in attr_list)
        self.assertTrue('__repr__' in attr_list)
        
        # test that instance members are listed
        self.assertTrue('_namespace' in attr_list)
        self.assertTrue('_version' in attr_list)
        
        # test that there are no duplicates returned
        self.assertEqual(len(attr_list), len(set(attr_list)))

class TestNullableArgs(unittest.TestCase):
    def test_in_nullable_hash(self):
        Everything.test_ghash_null_in(None)

    def test_in_nullable_list(self):
        Everything.test_gslist_null_in(None)
        Everything.test_glist_null_in(None)
        Everything.test_gslist_null_in([])
        Everything.test_glist_null_in([])

    def test_in_nullable_array(self):
        Everything.test_array_int_null_in(None)
        Everything.test_array_int_null_in([])

    def test_in_nullable_string(self):
        Everything.test_utf8_null_in(None)

    def test_in_nullable_object(self):
        Everything.func_obj_null_in(None)

    def test_out_nullable_hash(self):
        self.assertEqual(None, Everything.test_ghash_null_out())

    def test_out_nullable_list(self):
        self.assertEqual([], Everything.test_gslist_null_out())
        self.assertEqual([], Everything.test_glist_null_out())

    def test_out_nullable_array(self):
        self.assertEqual([], Everything.test_array_int_null_out())

    def test_out_nullable_string(self):
        self.assertEqual(None, Everything.test_utf8_null_out())

    def test_out_nullable_object(self):
        self.assertEqual(None, Everything.TestObj.null_out())


class TestCallbacks(unittest.TestCase):
    called = False
    main_loop = GObject.MainLoop()

    def testCallback(self):
        TestCallbacks.called = False
        def callback():
            TestCallbacks.called = True
        
        Everything.test_simple_callback(callback)
        self.assertTrue(TestCallbacks.called)

    def testCallbackException(self):
        """
        This test ensures that we get errors from callbacks correctly
        and in particular that we do not segv when callbacks fail
        """
        def callback():
            x = 1 / 0
            
        try:
            Everything.test_simple_callback(callback)
        except ZeroDivisionError:
            pass

    def testDoubleCallbackException(self):
        """
        This test ensures that we get errors from callbacks correctly
        and in particular that we do not segv when callbacks fail
        """
        def badcallback():
            x = 1 / 0

        def callback():
            Everything.test_boolean(True)
            Everything.test_boolean(False)
            Everything.test_simple_callback(badcallback())

        try:
            Everything.test_simple_callback(callback)
        except ZeroDivisionError:
            pass

    def testReturnValueCallback(self):
        TestCallbacks.called = False
        def callback():
            TestCallbacks.called = True
            return 44

        self.assertEquals(Everything.test_callback(callback), 44)
        self.assertTrue(TestCallbacks.called)
    
    def testCallbackAsync(self):
        TestCallbacks.called = False
        def callback(foo):
            TestCallbacks.called = True
            return foo

        Everything.test_callback_async(callback, 44);
        i = Everything.test_callback_thaw_async();
        self.assertEquals(44, i);
        self.assertTrue(TestCallbacks.called)

    def testCallbackScopeCall(self):
        TestCallbacks.called = 0
        def callback():
            TestCallbacks.called += 1
            return 0

        Everything.test_multi_callback(callback)
        self.assertEquals(TestCallbacks.called, 2)

    def testCallbackUserdata(self):
        TestCallbacks.called = 0
        def callback(userdata):
            self.assertEquals(userdata, "Test%d" % TestCallbacks.called)
            TestCallbacks.called += 1
            return TestCallbacks.called
        
        for i in range(100):
            val = Everything.test_callback_user_data(callback, "Test%d" % i)
            self.assertEquals(val, i+1)
            
        self.assertEquals(TestCallbacks.called, 100)

    def testCallbackUserdataRefCount(self):
        TestCallbacks.called = False
        def callback(userdata):
            TestCallbacks.called = True
            return 1

        ud = "Test User Data"

        start_ref_count = getrefcount(ud)
        for i in range(100):
            Everything.test_callback_destroy_notify(callback, ud)
            
        Everything.test_callback_thaw_notifications()
        end_ref_count = getrefcount(ud)

        self.assertEquals(start_ref_count, end_ref_count)

    def testAsyncReadyCallback(self):
        TestCallbacks.called = False
        TestCallbacks.main_loop = GObject.MainLoop()

        def callback(obj, result, user_data):
            TestCallbacks.main_loop.quit()
            TestCallbacks.called = True

        Everything.test_async_ready_callback(callback)

        TestCallbacks.main_loop.run()

        self.assertTrue(TestCallbacks.called)

    def testCallbackDestroyNotify(self):
        def callback(user_data):
            TestCallbacks.called = True
            return 42

        TestCallbacks.called = False
        self.assertEquals(Everything.test_callback_destroy_notify(callback, 42), 42)
        self.assertTrue(TestCallbacks.called)
        self.assertEquals(Everything.test_callback_thaw_notifications(), 42)

    def testCallbackInMethods(self):
        object_ = Everything.TestObj()

        def callback():
            TestCallbacks.called = True
            return 42

        TestCallbacks.called = False
        object_.instance_method_callback(callback)
        self.assertTrue(TestCallbacks.called)

        TestCallbacks.called = False
        Everything.TestObj.static_method_callback(callback)
        self.assertTrue(TestCallbacks.called)

        def callbackWithUserData(user_data):
            TestCallbacks.called = True
            return 42

        TestCallbacks.called = False
        obj_ = Everything.TestObj.new_callback(callbackWithUserData, None)
        self.assertTrue(TestCallbacks.called)

    def testCallbackNone(self):
        # make sure this doesn't assert or crash
        Everything.test_simple_callback(None)


class TestProperties(unittest.TestCase):

    def test_basic(self):
        object_ = Everything.TestObj()

        self.assertEquals(object_.props.int, 0)
        object_.props.int = 42
        self.assertTrue(isinstance(object_.props.int, int))
        self.assertEquals(object_.props.int, 42)

        self.assertEquals(object_.props.float, 0.0)
        object_.props.float = 42.42
        self.assertTrue(isinstance(object_.props.float, float))
        self.assertAlmostEquals(object_.props.float, 42.42, places=5)

        self.assertEquals(object_.props.double, 0.0)
        object_.props.double = 42.42
        self.assertTrue(isinstance(object_.props.double, float))
        self.assertAlmostEquals(object_.props.double, 42.42, places=5)

        self.assertEquals(object_.props.string, None)
        object_.props.string = 'mec'
        self.assertTrue(isinstance(object_.props.string, str))
        self.assertEquals(object_.props.string, 'mec')

    def test_hash_table(self):
        object_ = Everything.TestObj()
        self.assertEquals(object_.props.hash_table, None)

        object_.props.hash_table = {'mec': 56}
        self.assertTrue(isinstance(object_.props.hash_table, dict))
        self.assertEquals(list(object_.props.hash_table.items())[0], ('mec', 56))

    def test_list(self):
        object_ = Everything.TestObj()
        self.assertEquals(object_.props.list, [])

        object_.props.list = ['1', '2', '3']
        self.assertTrue(isinstance(object_.props.list, list))
        self.assertEquals(object_.props.list, ['1', '2', '3'])

    def test_boxed(self):
        object_ = Everything.TestObj()
        self.assertEquals(object_.props.boxed, None)

        boxed = Everything.TestBoxed()
        boxed.some_int8 = 42
        object_.props.boxed = boxed

        self.assertTrue(isinstance(object_.props.boxed, Everything.TestBoxed))
        self.assertEquals(object_.props.boxed.some_int8, 42)

class TestTortureProfile(unittest.TestCase):
    def test_torture_profile(self):
        import time
        total_time = 0
        print("")
        object_ = Everything.TestObj()
        sys.stdout.write("\ttorture test 1 (10000 iterations): ")

        start_time = time.clock()
        for i in range(10000):
            (y,z,q) = object_.torture_signature_0(5000,
                                                  "Torture Test 1",
                                                  12345)

        end_time = time.clock()
        delta_time = end_time - start_time
        total_time += delta_time
        print("%f secs" % delta_time)

        sys.stdout.write("\ttorture test 2 (10000 iterations): ")

        start_time = time.clock()
        for i in range(10000):
            (y,z,q) = Everything.TestObj().torture_signature_0(5000,
                                                               "Torture Test 2",
                                                               12345)

        end_time = time.clock()
        delta_time = end_time - start_time
        total_time += delta_time
        print("%f secs" % delta_time)


        sys.stdout.write("\ttorture test 3 (10000 iterations): ")
        start_time = time.clock()
        for i in range(10000):
            try:
                (y,z,q) = object_.torture_signature_1(5000,
                                                      "Torture Test 3",
                                                      12345)
            except:
                pass
        end_time = time.clock()
        delta_time = end_time - start_time
        total_time += delta_time
        print("%f secs" % delta_time)

        sys.stdout.write("\ttorture test 4 (10000 iterations): ")
        def callback(userdata):
            pass

        userdata = [1,2,3,4]
        start_time = time.clock()
        for i in range(10000):
            (y,z,q) = Everything.test_torture_signature_2(5000,
                                                          callback,
                                                          userdata,
                                                          "Torture Test 4",
                                                          12345)
        end_time = time.clock()
        delta_time = end_time - start_time
        total_time += delta_time
        print("%f secs" % delta_time)
        print("\t====")
        print("\tTotal: %f sec" % total_time)

