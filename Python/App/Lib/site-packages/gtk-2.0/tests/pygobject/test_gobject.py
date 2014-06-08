# -*- Mode: Python -*-

import unittest

import gobject
import sys
import testhelper


class TestGObjectAPI(unittest.TestCase):
    def testGObjectModule(self):
        obj = gobject.GObject()
        self.assertEquals(obj.__module__,
                          'gobject._gobject')


class TestReferenceCounting(unittest.TestCase):
    def testRegularObject(self):
        obj = gobject.GObject()
        self.assertEquals(obj.__grefcount__, 1)

        obj = gobject.new(gobject.GObject)
        self.assertEquals(obj.__grefcount__, 1)

    def testFloatingWithSinkFunc(self):
        obj = testhelper.FloatingWithSinkFunc()
        self.assertEquals(obj.__grefcount__, 1)

        obj = gobject.new(testhelper.FloatingWithSinkFunc)
        self.assertEquals(obj.__grefcount__, 1)

    def testFloatingWithoutSinkFunc(self):
        obj = testhelper.FloatingWithoutSinkFunc()
        self.assertEquals(obj.__grefcount__, 1)

        obj = gobject.new(testhelper.FloatingWithoutSinkFunc)
        self.assertEquals(obj.__grefcount__, 1)

    def testOwnedByLibrary(self):
        # Upon creation, the refcount of the object should be 2:
        # - someone already has a reference on the new object.
        # - the python wrapper should hold its own reference.
        obj = testhelper.OwnedByLibrary()
        self.assertEquals(obj.__grefcount__, 2)

        # We ask the library to release its reference, so the only
        # remaining ref should be our wrapper's. Once the wrapper
        # will run out of scope, the object will get finalized.
        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

    def testOwnedByLibraryOutOfScope(self):
        obj = testhelper.OwnedByLibrary()
        self.assertEquals(obj.__grefcount__, 2)

        # We are manually taking the object out of scope. This means
        # that our wrapper has been freed, and its reference dropped. We
        # cannot check it but the refcount should now be 1 (the ref held
        # by the library is still there, we didn't call release()
        obj = None

        # When we get the object back from the lib, the wrapper is
        # re-created, so our refcount will be 2 once again.
        obj = testhelper.owned_by_library_get_instance_list()[0]
        self.assertEquals(obj.__grefcount__, 2)

        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

    def testOwnedByLibraryUsingGObjectNew(self):
        # Upon creation, the refcount of the object should be 2:
        # - someone already has a reference on the new object.
        # - the python wrapper should hold its own reference.
        obj = gobject.new(testhelper.OwnedByLibrary)
        self.assertEquals(obj.__grefcount__, 2)

        # We ask the library to release its reference, so the only
        # remaining ref should be our wrapper's. Once the wrapper
        # will run out of scope, the object will get finalized.
        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

    def testOwnedByLibraryOutOfScopeUsingGobjectNew(self):
        obj = gobject.new(testhelper.OwnedByLibrary)
        self.assertEquals(obj.__grefcount__, 2)

        # We are manually taking the object out of scope. This means
        # that our wrapper has been freed, and its reference dropped. We
        # cannot check it but the refcount should now be 1 (the ref held
        # by the library is still there, we didn't call release()
        obj = None

        # When we get the object back from the lib, the wrapper is
        # re-created, so our refcount will be 2 once again.
        obj = testhelper.owned_by_library_get_instance_list()[0]
        self.assertEquals(obj.__grefcount__, 2)

        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

    def testFloatingAndSunk(self):
        # Upon creation, the refcount of the object should be 2:
        # - someone already has a reference on the new object.
        # - the python wrapper should hold its own reference.
        obj = testhelper.FloatingAndSunk()
        self.assertEquals(obj.__grefcount__, 2)

        # We ask the library to release its reference, so the only
        # remaining ref should be our wrapper's. Once the wrapper
        # will run out of scope, the object will get finalized.
        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

    def testFloatingAndSunkOutOfScope(self):
        obj = testhelper.FloatingAndSunk()
        self.assertEquals(obj.__grefcount__, 2)

        # We are manually taking the object out of scope. This means
        # that our wrapper has been freed, and its reference dropped. We
        # cannot check it but the refcount should now be 1 (the ref held
        # by the library is still there, we didn't call release()
        obj = None

        # When we get the object back from the lib, the wrapper is
        # re-created, so our refcount will be 2 once again.
        obj = testhelper.floating_and_sunk_get_instance_list()[0]
        self.assertEquals(obj.__grefcount__, 2)

        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

 
    def testFloatingAndSunkUsingGObjectNew(self):
        # Upon creation, the refcount of the object should be 2:
        # - someone already has a reference on the new object.
        # - the python wrapper should hold its own reference.
        obj = gobject.new(testhelper.FloatingAndSunk)
        self.assertEquals(obj.__grefcount__, 2)

        # We ask the library to release its reference, so the only
        # remaining ref should be our wrapper's. Once the wrapper
        # will run out of scope, the object will get finalized.
        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

    def testFloatingAndSunkOutOfScopeUsingGObjectNew(self):
        obj = gobject.new(testhelper.FloatingAndSunk)
        self.assertEquals(obj.__grefcount__, 2)

        # We are manually taking the object out of scope. This means
        # that our wrapper has been freed, and its reference dropped. We
        # cannot check it but the refcount should now be 1 (the ref held
        # by the library is still there, we didn't call release()
        obj = None

        # When we get the object back from the lib, the wrapper is
        # re-created, so our refcount will be 2 once again.
        obj = testhelper.floating_and_sunk_get_instance_list()[0]
        self.assertEquals(obj.__grefcount__, 2)

        obj.release()
        self.assertEquals(obj.__grefcount__, 1)

class A(gobject.GObject):
    def __init__(self):
        super(A, self).__init__()

class TestPythonReferenceCounting(unittest.TestCase):
    # Newly created instances should alwayshave two references: one for
    # the GC, and one for the bound variable in the local scope.

    def testNewInstanceHasTwoRefs(self):
        obj = gobject.GObject()
        self.assertEquals(sys.getrefcount(obj), 2)

    def testNewInstanceHasTwoRefsUsingGObjectNew(self):
        obj = gobject.new(gobject.GObject)
        self.assertEquals(sys.getrefcount(obj), 2)

    def testNewSubclassInstanceHasTwoRefs(self):
        obj = A()
        self.assertEquals(sys.getrefcount(obj), 2)

    def testNewSubclassInstanceHasTwoRefsUsingGObjectNew(self):
        obj = gobject.new(A)
        self.assertEquals(sys.getrefcount(obj), 2)
