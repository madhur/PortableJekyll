# -*- Mode: Python; py-indent-offset: 4 -*-
# coding=utf-8
# vim: tabstop=4 shiftwidth=4 expandtab

import sys

import unittest
from gi.repository import GObject

import gobject
from gi.repository import GIMarshallingTests

from compathelper import _bytes

if sys.version_info < (3, 0):
    CONSTANT_UTF8 = "const \xe2\x99\xa5 utf8"
    PY2_UNICODE_UTF8 = unicode(CONSTANT_UTF8, 'UTF-8')
    CHAR_255='\xff'
else:
    CONSTANT_UTF8 = "const ♥ utf8"
    CHAR_255=bytes([255])

CONSTANT_NUMBER = 42


class Number(object):

    def __init__(self, value):
        self.value = value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)


class Sequence(object):

    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[key]


class TestConstant(unittest.TestCase):

# Blocked by https://bugzilla.gnome.org/show_bug.cgi?id=595773
#    def test_constant_utf8(self):
#        self.assertEquals(CONSTANT_UTF8, GIMarshallingTests.CONSTANT_UTF8)

    def test_constant_number(self):
        self.assertEquals(CONSTANT_NUMBER, GIMarshallingTests.CONSTANT_NUMBER)


class TestBoolean(unittest.TestCase):

    def test_boolean_return(self):
        self.assertEquals(True, GIMarshallingTests.boolean_return_true())
        self.assertEquals(False, GIMarshallingTests.boolean_return_false())

    def test_boolean_in(self):
        GIMarshallingTests.boolean_in_true(True)
        GIMarshallingTests.boolean_in_false(False)

        GIMarshallingTests.boolean_in_true(1)
        GIMarshallingTests.boolean_in_false(0)

    def test_boolean_out(self):
        self.assertEquals(True, GIMarshallingTests.boolean_out_true())
        self.assertEquals(False, GIMarshallingTests.boolean_out_false())

    def test_boolean_inout(self):
        self.assertEquals(False, GIMarshallingTests.boolean_inout_true_false(True))
        self.assertEquals(True, GIMarshallingTests.boolean_inout_false_true(False))


class TestInt8(unittest.TestCase):

    MAX = GObject.G_MAXINT8
    MIN = GObject.G_MININT8

    def test_int8_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int8_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int8_return_min())

    def test_int8_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.int8_in_max(max)
        GIMarshallingTests.int8_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.int8_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.int8_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.int8_in_max, "self.MAX")

    def test_int8_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int8_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int8_out_min())

    def test_int8_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.int8_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.int8_inout_min_max(Number(self.MIN)))


class TestUInt8(unittest.TestCase):

    MAX = GObject.G_MAXUINT8

    def test_uint8_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint8_return())

    def test_uint8_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.uint8_in(number)
        GIMarshallingTests.uint8_in(CHAR_255)

        number.value += 1
        self.assertRaises(ValueError, GIMarshallingTests.uint8_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.uint8_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.uint8_in, "self.MAX")

    def test_uint8_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint8_out())

    def test_uint8_inout(self):
        self.assertEquals(0, GIMarshallingTests.uint8_inout(Number(self.MAX)))


class TestInt16(unittest.TestCase):

    MAX = GObject.G_MAXINT16
    MIN = GObject.G_MININT16

    def test_int16_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int16_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int16_return_min())

    def test_int16_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.int16_in_max(max)
        GIMarshallingTests.int16_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.int16_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.int16_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.int16_in_max, "self.MAX")

    def test_int16_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int16_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int16_out_min())

    def test_int16_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.int16_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.int16_inout_min_max(Number(self.MIN)))


class TestUInt16(unittest.TestCase):

    MAX = GObject.G_MAXUINT16

    def test_uint16_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint16_return())

    def test_uint16_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.uint16_in(number)

        number.value += 1

        self.assertRaises(ValueError, GIMarshallingTests.uint16_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.uint16_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.uint16_in, "self.MAX")

    def test_uint16_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint16_out())

    def test_uint16_inout(self):
        self.assertEquals(0, GIMarshallingTests.uint16_inout(Number(self.MAX)))


class TestInt32(unittest.TestCase):

    MAX = GObject.G_MAXINT32
    MIN = GObject.G_MININT32

    def test_int32_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int32_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int32_return_min())

    def test_int32_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.int32_in_max(max)
        GIMarshallingTests.int32_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.int32_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.int32_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.int32_in_max, "self.MAX")

    def test_int32_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int32_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int32_out_min())

    def test_int32_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.int32_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.int32_inout_min_max(Number(self.MIN)))


class TestUInt32(unittest.TestCase):

    MAX = GObject.G_MAXUINT32

    def test_uint32_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint32_return())

    def test_uint32_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.uint32_in(number)

        number.value += 1

        self.assertRaises(ValueError, GIMarshallingTests.uint32_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.uint32_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.uint32_in, "self.MAX")

    def test_uint32_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint32_out())

    def test_uint32_inout(self):
        self.assertEquals(0, GIMarshallingTests.uint32_inout(Number(self.MAX)))


class TestInt64(unittest.TestCase):

    MAX = 2 ** 63 - 1
    MIN = - (2 ** 63)

    def test_int64_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int64_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int64_return_min())

    def test_int64_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.int64_in_max(max)
        GIMarshallingTests.int64_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.int64_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.int64_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.int64_in_max, "self.MAX")

    def test_int64_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int64_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int64_out_min())

    def test_int64_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.int64_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.int64_inout_min_max(Number(self.MIN)))


class TestUInt64(unittest.TestCase):

    MAX = 2 ** 64 - 1

    def test_uint64_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint64_return())

    def test_uint64_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.uint64_in(number)

        number.value += 1

        self.assertRaises(ValueError, GIMarshallingTests.uint64_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.uint64_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.uint64_in, "self.MAX")

    def test_uint64_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint64_out())

    def test_uint64_inout(self):
        self.assertEquals(0, GIMarshallingTests.uint64_inout(Number(self.MAX)))


class TestShort(unittest.TestCase):

    MAX = GObject.constants.G_MAXSHORT
    MIN = GObject.constants.G_MINSHORT

    def test_short_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.short_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.short_return_min())

    def test_short_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.short_in_max(max)
        GIMarshallingTests.short_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.short_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.short_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.short_in_max, "self.MAX")

    def test_short_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.short_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.short_out_min())

    def test_short_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.short_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.short_inout_min_max(Number(self.MIN)))


class TestUShort(unittest.TestCase):

    MAX = GObject.constants.G_MAXUSHORT

    def test_ushort_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.ushort_return())

    def test_ushort_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.ushort_in(number)

        number.value += 1

        self.assertRaises(ValueError, GIMarshallingTests.ushort_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.ushort_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.ushort_in, "self.MAX")

    def test_ushort_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.ushort_out())

    def test_ushort_inout(self):
        self.assertEquals(0, GIMarshallingTests.ushort_inout(Number(self.MAX)))


class TestInt(unittest.TestCase):

    MAX = GObject.constants.G_MAXINT
    MIN = GObject.constants.G_MININT

    def test_int_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int_return_min())

    def test_int_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.int_in_max(max)
        GIMarshallingTests.int_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.int_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.int_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.int_in_max, "self.MAX")

    def test_int_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.int_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.int_out_min())

    def test_int_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.int_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.int_inout_min_max(Number(self.MIN)))
        self.assertRaises(TypeError, GIMarshallingTests.int_inout_min_max, Number(self.MIN), CONSTANT_NUMBER)


class TestUInt(unittest.TestCase):

    MAX = GObject.constants.G_MAXUINT

    def test_uint_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint_return())

    def test_uint_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.uint_in(number)

        number.value += 1

        self.assertRaises(ValueError, GIMarshallingTests.uint_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.uint_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.uint_in, "self.MAX")

    def test_uint_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.uint_out())

    def test_uint_inout(self):
        self.assertEquals(0, GIMarshallingTests.uint_inout(Number(self.MAX)))


class TestLong(unittest.TestCase):

    MAX = GObject.constants.G_MAXLONG
    MIN = GObject.constants.G_MINLONG

    def test_long_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.long_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.long_return_min())

    def test_long_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.long_in_max(max)
        GIMarshallingTests.long_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.long_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.long_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.long_in_max, "self.MAX")

    def test_long_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.long_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.long_out_min())

    def test_long_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.long_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.long_inout_min_max(Number(self.MIN)))


class TestULong(unittest.TestCase):

    MAX = GObject.constants.G_MAXULONG

    def test_ulong_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.ulong_return())

    def test_ulong_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.ulong_in(number)

        number.value += 1

        self.assertRaises(ValueError, GIMarshallingTests.ulong_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.ulong_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.ulong_in, "self.MAX")

    def test_ulong_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.ulong_out())

    def test_ulong_inout(self):
        self.assertEquals(0, GIMarshallingTests.ulong_inout(Number(self.MAX)))


class TestSSize(unittest.TestCase):

    MAX = GObject.constants.G_MAXLONG
    MIN = GObject.constants.G_MINLONG

    def test_ssize_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.ssize_return_max())
        self.assertEquals(self.MIN, GIMarshallingTests.ssize_return_min())

    def test_ssize_in(self):
        max = Number(self.MAX)
        min = Number(self.MIN)

        GIMarshallingTests.ssize_in_max(max)
        GIMarshallingTests.ssize_in_min(min)

        max.value += 1
        min.value -= 1

        self.assertRaises(ValueError, GIMarshallingTests.ssize_in_max, max)
        self.assertRaises(ValueError, GIMarshallingTests.ssize_in_min, min)

        self.assertRaises(TypeError, GIMarshallingTests.ssize_in_max, "self.MAX")

    def test_ssize_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.ssize_out_max())
        self.assertEquals(self.MIN, GIMarshallingTests.ssize_out_min())

    def test_ssize_inout(self):
        self.assertEquals(self.MIN, GIMarshallingTests.ssize_inout_max_min(Number(self.MAX)))
        self.assertEquals(self.MAX, GIMarshallingTests.ssize_inout_min_max(Number(self.MIN)))


class TestSize(unittest.TestCase):

    MAX = GObject.constants.G_MAXULONG

    def test_size_return(self):
        self.assertEquals(self.MAX, GIMarshallingTests.size_return())

    def test_size_in(self):
        number = Number(self.MAX)

        GIMarshallingTests.size_in(number)

        number.value += 1

        self.assertRaises(ValueError, GIMarshallingTests.size_in, number)
        self.assertRaises(ValueError, GIMarshallingTests.size_in, Number(-1))

        self.assertRaises(TypeError, GIMarshallingTests.size_in, "self.MAX")

    def test_size_out(self):
        self.assertEquals(self.MAX, GIMarshallingTests.size_out())

    def test_size_inout(self):
        self.assertEquals(0, GIMarshallingTests.size_inout(Number(self.MAX)))


class TestFloat(unittest.TestCase):

    MAX = GObject.constants.G_MAXFLOAT
    MIN = GObject.constants.G_MINFLOAT

    def test_float_return(self):
        self.assertAlmostEquals(self.MAX, GIMarshallingTests.float_return())

    def test_float_in(self):
        GIMarshallingTests.float_in(Number(self.MAX))

        self.assertRaises(TypeError, GIMarshallingTests.float_in, "self.MAX")

    def test_float_out(self):
        self.assertAlmostEquals(self.MAX, GIMarshallingTests.float_out())

    def test_float_inout(self):
        self.assertAlmostEquals(self.MIN, GIMarshallingTests.float_inout(Number(self.MAX)))


class TestDouble(unittest.TestCase):

    MAX = GObject.constants.G_MAXDOUBLE
    MIN = GObject.constants.G_MINDOUBLE

    def test_double_return(self):
        self.assertAlmostEquals(self.MAX, GIMarshallingTests.double_return())

    def test_double_in(self):
        GIMarshallingTests.double_in(Number(self.MAX))

        self.assertRaises(TypeError, GIMarshallingTests.double_in, "self.MAX")

    def test_double_out(self):
        self.assertAlmostEquals(self.MAX, GIMarshallingTests.double_out())

    def test_double_inout(self):
        self.assertAlmostEquals(self.MIN, GIMarshallingTests.double_inout(Number(self.MAX)))


class TestGType(unittest.TestCase):

    def test_gtype_return(self):
        self.assertEquals(GObject.TYPE_NONE, GIMarshallingTests.gtype_return())

    def test_gtype_in(self):
        GIMarshallingTests.gtype_in(GObject.TYPE_NONE)

        self.assertRaises(TypeError, GIMarshallingTests.gtype_in, "GObject.TYPE_NONE")

    def test_gtype_out(self):
        self.assertEquals(GObject.TYPE_NONE, GIMarshallingTests.gtype_out())

    def test_gtype_inout(self):
        self.assertEquals(GObject.TYPE_INT, GIMarshallingTests.gtype_inout(GObject.TYPE_NONE))


class TestUtf8(unittest.TestCase):

    def test_utf8_none_return(self):
        self.assertEquals(CONSTANT_UTF8, GIMarshallingTests.utf8_none_return())

    def test_utf8_full_return(self):
        self.assertEquals(CONSTANT_UTF8, GIMarshallingTests.utf8_full_return())

    def test_utf8_none_in(self):
        GIMarshallingTests.utf8_none_in(CONSTANT_UTF8)
        if sys.version_info < (3, 0):
            GIMarshallingTests.utf8_none_in(PY2_UNICODE_UTF8)

        self.assertRaises(TypeError, GIMarshallingTests.utf8_none_in, CONSTANT_NUMBER)
        self.assertRaises(TypeError, GIMarshallingTests.utf8_none_in, None)

    def test_utf8_none_out(self):
        self.assertEquals(CONSTANT_UTF8, GIMarshallingTests.utf8_none_out())

    def test_utf8_full_out(self):
        self.assertEquals(CONSTANT_UTF8, GIMarshallingTests.utf8_full_out())

    def test_utf8_dangling_out(self):
        GIMarshallingTests.utf8_dangling_out()

    def test_utf8_none_inout(self):
        self.assertEquals("", GIMarshallingTests.utf8_none_inout(CONSTANT_UTF8))

    def test_utf8_full_inout(self):
        self.assertEquals("", GIMarshallingTests.utf8_full_inout(CONSTANT_UTF8))


class TestArray(unittest.TestCase):

    def test_array_fixed_int_return(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.array_fixed_int_return())

    def test_array_fixed_short_return(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.array_fixed_short_return())

    def test_array_fixed_int_in(self):
        GIMarshallingTests.array_fixed_int_in(Sequence([-1, 0, 1, 2]))

        self.assertRaises(TypeError, GIMarshallingTests.array_fixed_int_in, Sequence([-1, '0', 1, 2]))

        self.assertRaises(TypeError, GIMarshallingTests.array_fixed_int_in, 42)
        self.assertRaises(TypeError, GIMarshallingTests.array_fixed_int_in, None)

    def test_array_fixed_short_in(self):
        GIMarshallingTests.array_fixed_short_in(Sequence([-1, 0, 1, 2]))

    def test_array_fixed_out(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.array_fixed_out())

    def test_array_fixed_inout(self):
        self.assertEquals([2, 1, 0, -1], GIMarshallingTests.array_fixed_inout([-1, 0, 1, 2]))


    def test_array_return(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.array_return())

    def test_array_in(self):
        GIMarshallingTests.array_in(Sequence([-1, 0, 1, 2]))

    def test_array_uint8_in(self):
        GIMarshallingTests.array_uint8_in(Sequence([97, 98, 99, 100]))
        GIMarshallingTests.array_uint8_in(_bytes("abcd"))

    def test_array_out(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.array_out())

    def test_array_inout(self):
        self.assertEquals([-2, -1, 0, 1, 2], GIMarshallingTests.array_inout(Sequence([-1, 0, 1, 2])))

    def test_method_array_in(self):
        object_ = GIMarshallingTests.Object()
        object_.method_array_in(Sequence([-1, 0, 1, 2]))

    def test_method_array_out(self):
        object_ = GIMarshallingTests.Object()
        self.assertEquals([-1, 0, 1, 2], object_.method_array_out())

    def test_method_array_inout(self):
        object_ = GIMarshallingTests.Object()
        self.assertEquals([-2, -1, 0, 1, 2], object_.method_array_inout(Sequence([-1, 0, 1, 2])))

    def test_method_array_return(self):
        object_ = GIMarshallingTests.Object()
        self.assertEquals([-1, 0, 1, 2], object_.method_array_return())

    def test_array_fixed_out_struct(self):
        struct1, struct2 = GIMarshallingTests.array_fixed_out_struct()

        self.assertEquals(7, struct1.long_)
        self.assertEquals(6, struct1.int8)
        self.assertEquals(6, struct2.long_)
        self.assertEquals(7, struct2.int8)

    def test_array_zero_terminated_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.array_zero_terminated_return())

    def test_array_zero_terminated_in(self):
        GIMarshallingTests.array_zero_terminated_in(Sequence(['0', '1', '2']))

    def test_array_zero_terminated_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.array_zero_terminated_out())

    def test_array_zero_terminated_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.array_zero_terminated_out())

    def test_array_zero_terminated_inout(self):
        self.assertEquals(['-1', '0', '1', '2'], GIMarshallingTests.array_zero_terminated_inout(['0', '1', '2']))

    def test_gstrv_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gstrv_return())

    def test_gstrv_in(self):
        GIMarshallingTests.gstrv_in(Sequence(['0', '1', '2']))

    def test_gstrv_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gstrv_out())

    def test_gstrv_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gstrv_out())

    def test_gstrv_inout(self):
        self.assertEquals(['-1', '0', '1', '2'], GIMarshallingTests.gstrv_inout(['0', '1', '2']))


class TestGArray(unittest.TestCase):

    def test_garray_int_none_return(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.garray_int_none_return())

    def test_garray_utf8_none_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.garray_utf8_none_return())

    def test_garray_utf8_container_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.garray_utf8_container_return())

    def test_garray_utf8_full_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.garray_utf8_full_return())

    def test_garray_int_none_in(self):
        GIMarshallingTests.garray_int_none_in(Sequence([-1, 0, 1, 2]))

        self.assertRaises(TypeError, GIMarshallingTests.garray_int_none_in, Sequence([-1, '0', 1, 2]))

        self.assertRaises(TypeError, GIMarshallingTests.garray_int_none_in, 42)
        self.assertRaises(TypeError, GIMarshallingTests.garray_int_none_in, None)

    def test_garray_utf8_none_in(self):
        GIMarshallingTests.garray_utf8_none_in(Sequence(['0', '1', '2']))

    def test_garray_utf8_none_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.garray_utf8_none_out())

    def test_garray_utf8_container_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.garray_utf8_container_out())

    def test_garray_utf8_full_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.garray_utf8_full_out())

    def test_garray_utf8_none_inout(self):
        self.assertEquals(['-2', '-1', '0', '1'], GIMarshallingTests.garray_utf8_none_inout(Sequence(('0', '1', '2'))))

    def test_garray_utf8_container_inout(self):
        self.assertEquals(['-2', '-1','0', '1'], GIMarshallingTests.garray_utf8_container_inout(['0', '1', '2']))

    def test_garray_utf8_full_inout(self):
        self.assertEquals(['-2', '-1','0', '1'], GIMarshallingTests.garray_utf8_full_inout(['0', '1', '2']))


class TestGList(unittest.TestCase):

    def test_glist_int_none_return(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.glist_int_none_return())

    def test_glist_utf8_none_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.glist_utf8_none_return())

    def test_glist_utf8_container_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.glist_utf8_container_return())

    def test_glist_utf8_full_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.glist_utf8_full_return())

    def test_glist_int_none_in(self):
        GIMarshallingTests.glist_int_none_in(Sequence((-1, 0, 1, 2)))

        self.assertRaises(TypeError, GIMarshallingTests.glist_int_none_in, Sequence((-1, '0', 1, 2)))

        self.assertRaises(TypeError, GIMarshallingTests.glist_int_none_in, 42)
        self.assertRaises(TypeError, GIMarshallingTests.glist_int_none_in, None)

    def test_glist_utf8_none_in(self):
        GIMarshallingTests.glist_utf8_none_in(Sequence(('0', '1', '2')))

    def test_glist_utf8_none_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.glist_utf8_none_out())

    def test_glist_utf8_container_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.glist_utf8_container_out())

    def test_glist_utf8_full_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.glist_utf8_full_out())

    def test_glist_utf8_none_inout(self):
        self.assertEquals(['-2', '-1', '0', '1'], GIMarshallingTests.glist_utf8_none_inout(Sequence(('0', '1', '2'))))

    def test_glist_utf8_container_inout(self):
        self.assertEquals(['-2', '-1','0', '1'], GIMarshallingTests.glist_utf8_container_inout(('0', '1', '2')))

    def test_glist_utf8_full_inout(self):
        self.assertEquals(['-2', '-1','0', '1'], GIMarshallingTests.glist_utf8_full_inout(('0', '1', '2')))


class TestGSList(unittest.TestCase):

    def test_gslist_int_none_return(self):
        self.assertEquals([-1, 0, 1, 2], GIMarshallingTests.gslist_int_none_return())

    def test_gslist_utf8_none_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gslist_utf8_none_return())

    def test_gslist_utf8_container_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gslist_utf8_container_return())

    def test_gslist_utf8_full_return(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gslist_utf8_full_return())

    def test_gslist_int_none_in(self):
        GIMarshallingTests.gslist_int_none_in(Sequence((-1, 0, 1, 2)))

        self.assertRaises(TypeError, GIMarshallingTests.gslist_int_none_in, Sequence((-1, '0', 1, 2)))

        self.assertRaises(TypeError, GIMarshallingTests.gslist_int_none_in, 42)
        self.assertRaises(TypeError, GIMarshallingTests.gslist_int_none_in, None)

    def test_gslist_utf8_none_in(self):
        GIMarshallingTests.gslist_utf8_none_in(Sequence(('0', '1', '2')))

    def test_gslist_utf8_none_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gslist_utf8_none_out())

    def test_gslist_utf8_container_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gslist_utf8_container_out())

    def test_gslist_utf8_full_out(self):
        self.assertEquals(['0', '1', '2'], GIMarshallingTests.gslist_utf8_full_out())

    def test_gslist_utf8_none_inout(self):
        self.assertEquals(['-2', '-1', '0', '1'], GIMarshallingTests.gslist_utf8_none_inout(Sequence(('0', '1', '2'))))

    def test_gslist_utf8_container_inout(self):
        self.assertEquals(['-2', '-1','0', '1'], GIMarshallingTests.gslist_utf8_container_inout(('0', '1', '2')))

    def test_gslist_utf8_full_inout(self):
        self.assertEquals(['-2', '-1','0', '1'], GIMarshallingTests.gslist_utf8_full_inout(('0', '1', '2')))


class TestGHashTable(unittest.TestCase):

    def test_ghashtable_int_none_return(self):
        self.assertEquals({-1: 1, 0: 0, 1: -1, 2: -2}, GIMarshallingTests.ghashtable_int_none_return())

    def test_ghashtable_int_none_return(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '-1', '2': '-2'}, GIMarshallingTests.ghashtable_utf8_none_return())

    def test_ghashtable_int_container_return(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '-1', '2': '-2'}, GIMarshallingTests.ghashtable_utf8_container_return())

    def test_ghashtable_int_full_return(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '-1', '2': '-2'}, GIMarshallingTests.ghashtable_utf8_full_return())

    def test_ghashtable_int_none_in(self):
        GIMarshallingTests.ghashtable_int_none_in({-1: 1, 0: 0, 1: -1, 2: -2})

        self.assertRaises(TypeError, GIMarshallingTests.ghashtable_int_none_in, {-1: 1, '0': 0, 1: -1, 2: -2})
        self.assertRaises(TypeError, GIMarshallingTests.ghashtable_int_none_in, {-1: 1, 0: '0', 1: -1, 2: -2})

        self.assertRaises(TypeError, GIMarshallingTests.ghashtable_int_none_in, '{-1: 1, 0: 0, 1: -1, 2: -2}')
        self.assertRaises(TypeError, GIMarshallingTests.ghashtable_int_none_in, None)

    def test_ghashtable_utf8_none_in(self):
        GIMarshallingTests.ghashtable_utf8_none_in({'-1': '1', '0': '0', '1': '-1', '2': '-2'})

    def test_ghashtable_utf8_none_out(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '-1', '2': '-2'}, GIMarshallingTests.ghashtable_utf8_none_out())

    def test_ghashtable_utf8_container_out(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '-1', '2': '-2'}, GIMarshallingTests.ghashtable_utf8_container_out())

    def test_ghashtable_utf8_full_out(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '-1', '2': '-2'}, GIMarshallingTests.ghashtable_utf8_full_out())

    def test_ghashtable_utf8_none_inout(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '1'},
            GIMarshallingTests.ghashtable_utf8_none_inout({'-1': '1', '0': '0', '1': '-1', '2': '-2'}))

    def test_ghashtable_utf8_container_inout(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '1'},
            GIMarshallingTests.ghashtable_utf8_container_inout({'-1': '1', '0': '0', '1': '-1', '2': '-2'}))

    def test_ghashtable_utf8_full_inout(self):
        self.assertEquals({'-1': '1', '0': '0', '1': '1'},
            GIMarshallingTests.ghashtable_utf8_full_inout({'-1': '1', '0': '0', '1': '-1', '2': '-2'}))


class TestGValue(unittest.TestCase):

    def test_gvalue_return(self):
        self.assertEquals(42, GIMarshallingTests.gvalue_return())

    def test_gvalue_in(self):
        GIMarshallingTests.gvalue_in(42)
        value = GObject.Value()
        value.init(GObject.TYPE_INT)
        value.set_int(42)
        GIMarshallingTests.gvalue_in(value)

    def test_gvalue_out(self):
        self.assertEquals(42, GIMarshallingTests.gvalue_out())

    def test_gvalue_inout(self):
        self.assertEquals('42', GIMarshallingTests.gvalue_inout(42))
        value = GObject.Value()
        value.init(GObject.TYPE_INT)
        value.set_int(42)
        self.assertEquals('42', GIMarshallingTests.gvalue_inout(value))

class TestGClosure(unittest.TestCase):

    def test_gclosure_in(self):
        GIMarshallingTests.gclosure_in(lambda: 42)

        # test passing a closure between two C calls
        closure = GIMarshallingTests.gclosure_return()
        GIMarshallingTests.gclosure_in(closure)

        self.assertRaises(TypeError, GIMarshallingTests.gclosure_in, 42)
        self.assertRaises(TypeError, GIMarshallingTests.gclosure_in, None)


class TestPointer(unittest.TestCase):
    def test_pointer_in_return(self):
        self.assertEquals(GIMarshallingTests.pointer_in_return(42), 42)


class TestEnum(unittest.TestCase):

    def test_enum(self):
        self.assertTrue(issubclass(GIMarshallingTests.Enum, int))
        self.assertTrue(isinstance(GIMarshallingTests.Enum.VALUE1, GIMarshallingTests.Enum))
        self.assertTrue(isinstance(GIMarshallingTests.Enum.VALUE2, GIMarshallingTests.Enum))
        self.assertTrue(isinstance(GIMarshallingTests.Enum.VALUE3, GIMarshallingTests.Enum))
        self.assertEquals(42, GIMarshallingTests.Enum.VALUE3)

    def test_value_nick_and_name(self):
        self.assertEqual(GIMarshallingTests.Enum.VALUE1.value_nick, 'value1')
        self.assertEqual(GIMarshallingTests.Enum.VALUE2.value_nick, 'value2')
        self.assertEqual(GIMarshallingTests.Enum.VALUE3.value_nick, 'value3')

        self.assertEqual(GIMarshallingTests.Enum.VALUE1.value_name, 'GI_MARSHALLING_TESTS_ENUM_VALUE1')
        self.assertEqual(GIMarshallingTests.Enum.VALUE2.value_name, 'GI_MARSHALLING_TESTS_ENUM_VALUE2')
        self.assertEqual(GIMarshallingTests.Enum.VALUE3.value_name, 'GI_MARSHALLING_TESTS_ENUM_VALUE3')

    def test_enum_in(self):
        GIMarshallingTests.enum_in(GIMarshallingTests.Enum.VALUE3)
        GIMarshallingTests.enum_in(42)

        self.assertRaises(TypeError, GIMarshallingTests.enum_in, 43)
        self.assertRaises(TypeError, GIMarshallingTests.enum_in, 'GIMarshallingTests.Enum.VALUE3')

    def test_enum_out(self):
        enum = GIMarshallingTests.enum_out()
        self.assertTrue(isinstance(enum, GIMarshallingTests.Enum))
        self.assertEquals(enum, GIMarshallingTests.Enum.VALUE3)

    def test_enum_inout(self):
        enum = GIMarshallingTests.enum_inout(GIMarshallingTests.Enum.VALUE3)
        self.assertTrue(isinstance(enum, GIMarshallingTests.Enum))
        self.assertEquals(enum, GIMarshallingTests.Enum.VALUE1)

    def test_enum_second(self):
        # check for the bug where different non-gtype enums share the same class
        self.assertNotEqual(GIMarshallingTests.Enum, GIMarshallingTests.SecondEnum)

        # check that values are not being shared between different enums
        self.assertTrue(hasattr(GIMarshallingTests.SecondEnum, "SECONDVALUE1"))
        self.assertRaises(AttributeError, getattr, GIMarshallingTests.Enum, "SECONDVALUE1")
        self.assertTrue(hasattr(GIMarshallingTests.Enum, "VALUE1"))
        self.assertRaises(AttributeError, getattr, GIMarshallingTests.SecondEnum, "VALUE1")


class TestGEnum(unittest.TestCase):

    def test_genum(self):
        self.assertTrue(issubclass(GIMarshallingTests.GEnum, GObject.GEnum))
        self.assertTrue(isinstance(GIMarshallingTests.GEnum.VALUE1, GIMarshallingTests.GEnum))
        self.assertTrue(isinstance(GIMarshallingTests.GEnum.VALUE2, GIMarshallingTests.GEnum))
        self.assertTrue(isinstance(GIMarshallingTests.GEnum.VALUE3, GIMarshallingTests.GEnum))
        self.assertEquals(42, GIMarshallingTests.GEnum.VALUE3)

    def test_value_nick_and_name(self):
        self.assertEqual(GIMarshallingTests.GEnum.VALUE1.value_nick, 'value1')
        self.assertEqual(GIMarshallingTests.GEnum.VALUE2.value_nick, 'value2')
        self.assertEqual(GIMarshallingTests.GEnum.VALUE3.value_nick, 'value3')

        self.assertEqual(GIMarshallingTests.GEnum.VALUE1.value_name, 'GI_MARSHALLING_TESTS_GENUM_VALUE1')
        self.assertEqual(GIMarshallingTests.GEnum.VALUE2.value_name, 'GI_MARSHALLING_TESTS_GENUM_VALUE2')
        self.assertEqual(GIMarshallingTests.GEnum.VALUE3.value_name, 'GI_MARSHALLING_TESTS_GENUM_VALUE3')

    def test_genum_in(self):
        GIMarshallingTests.genum_in(GIMarshallingTests.GEnum.VALUE3)
        GIMarshallingTests.genum_in(42)

        self.assertRaises(TypeError, GIMarshallingTests.genum_in, 43)
        self.assertRaises(TypeError, GIMarshallingTests.genum_in, 'GIMarshallingTests.GEnum.VALUE3')

    def test_genum_out(self):
        genum = GIMarshallingTests.genum_out()
        self.assertTrue(isinstance(genum, GIMarshallingTests.GEnum))
        self.assertEquals(genum, GIMarshallingTests.GEnum.VALUE3)

    def test_genum_inout(self):
        genum = GIMarshallingTests.genum_inout(GIMarshallingTests.GEnum.VALUE3)
        self.assertTrue(isinstance(genum, GIMarshallingTests.GEnum))
        self.assertEquals(genum, GIMarshallingTests.GEnum.VALUE1)


class TestGFlags(unittest.TestCase):

    def test_flags(self):
        self.assertTrue(issubclass(GIMarshallingTests.Flags, GObject.GFlags))
        self.assertTrue(isinstance(GIMarshallingTests.Flags.VALUE1, GIMarshallingTests.Flags))
        self.assertTrue(isinstance(GIMarshallingTests.Flags.VALUE2, GIMarshallingTests.Flags))
        self.assertTrue(isinstance(GIMarshallingTests.Flags.VALUE3, GIMarshallingTests.Flags))
        # __or__() operation should still return an instance, not an int.
        self.assertTrue(isinstance(GIMarshallingTests.Flags.VALUE1 | GIMarshallingTests.Flags.VALUE2,
                                   GIMarshallingTests.Flags))
        self.assertEquals(1 << 1, GIMarshallingTests.Flags.VALUE2)

    def test_value_nick_and_name(self):
        self.assertEqual(GIMarshallingTests.Flags.VALUE1.first_value_nick, 'value1')
        self.assertEqual(GIMarshallingTests.Flags.VALUE2.first_value_nick, 'value2')
        self.assertEqual(GIMarshallingTests.Flags.VALUE3.first_value_nick, 'value3')

        self.assertEqual(GIMarshallingTests.Flags.VALUE1.first_value_name, 'GI_MARSHALLING_TESTS_FLAGS_VALUE1')
        self.assertEqual(GIMarshallingTests.Flags.VALUE2.first_value_name, 'GI_MARSHALLING_TESTS_FLAGS_VALUE2')
        self.assertEqual(GIMarshallingTests.Flags.VALUE3.first_value_name, 'GI_MARSHALLING_TESTS_FLAGS_VALUE3')

    def test_flags_in(self):
        GIMarshallingTests.flags_in(GIMarshallingTests.Flags.VALUE2)
        # result of __or__() operation should still be valid instance, not an int.
        GIMarshallingTests.flags_in(GIMarshallingTests.Flags.VALUE2 | GIMarshallingTests.Flags.VALUE2)
        GIMarshallingTests.flags_in_zero(Number(0))

        self.assertRaises(TypeError, GIMarshallingTests.flags_in, 1 << 1)
        self.assertRaises(TypeError, GIMarshallingTests.flags_in, 'GIMarshallingTests.Flags.VALUE2')

    def test_flags_out(self):
        flags = GIMarshallingTests.flags_out()
        self.assertTrue(isinstance(flags, GIMarshallingTests.Flags))
        self.assertEquals(flags, GIMarshallingTests.Flags.VALUE2)

    def test_flags_inout(self):
        flags = GIMarshallingTests.flags_inout(GIMarshallingTests.Flags.VALUE2)
        self.assertTrue(isinstance(flags, GIMarshallingTests.Flags))
        self.assertEquals(flags, GIMarshallingTests.Flags.VALUE1)

class TestNoTypeFlags(unittest.TestCase):

    def test_flags(self):
        self.assertTrue(issubclass(GIMarshallingTests.NoTypeFlags, GObject.GFlags))
        self.assertTrue(isinstance(GIMarshallingTests.NoTypeFlags.VALUE1, GIMarshallingTests.NoTypeFlags))
        self.assertTrue(isinstance(GIMarshallingTests.NoTypeFlags.VALUE2, GIMarshallingTests.NoTypeFlags))
        self.assertTrue(isinstance(GIMarshallingTests.NoTypeFlags.VALUE3, GIMarshallingTests.NoTypeFlags))
        # __or__() operation should still return an instance, not an int.
        self.assertTrue(isinstance(GIMarshallingTests.NoTypeFlags.VALUE1 | GIMarshallingTests.NoTypeFlags.VALUE2,
                                   GIMarshallingTests.NoTypeFlags))
        self.assertEquals(1 << 1, GIMarshallingTests.NoTypeFlags.VALUE2)

    def test_value_nick_and_name(self):
        self.assertEqual(GIMarshallingTests.NoTypeFlags.VALUE1.first_value_nick, 'value1')
        self.assertEqual(GIMarshallingTests.NoTypeFlags.VALUE2.first_value_nick, 'value2')
        self.assertEqual(GIMarshallingTests.NoTypeFlags.VALUE3.first_value_nick, 'value3')

        self.assertEqual(GIMarshallingTests.NoTypeFlags.VALUE1.first_value_name, 'GI_MARSHALLING_TESTS_NO_TYPE_FLAGS_VALUE1')
        self.assertEqual(GIMarshallingTests.NoTypeFlags.VALUE2.first_value_name, 'GI_MARSHALLING_TESTS_NO_TYPE_FLAGS_VALUE2')
        self.assertEqual(GIMarshallingTests.NoTypeFlags.VALUE3.first_value_name, 'GI_MARSHALLING_TESTS_NO_TYPE_FLAGS_VALUE3')

    def test_flags_in(self):
        GIMarshallingTests.no_type_flags_in(GIMarshallingTests.NoTypeFlags.VALUE2)
        GIMarshallingTests.no_type_flags_in(GIMarshallingTests.NoTypeFlags.VALUE2 | GIMarshallingTests.NoTypeFlags.VALUE2)
        GIMarshallingTests.no_type_flags_in_zero(Number(0))

        self.assertRaises(TypeError, GIMarshallingTests.no_type_flags_in, 1 << 1)
        self.assertRaises(TypeError, GIMarshallingTests.no_type_flags_in, 'GIMarshallingTests.NoTypeFlags.VALUE2')

    def test_flags_out(self):
        flags = GIMarshallingTests.no_type_flags_out()
        self.assertTrue(isinstance(flags, GIMarshallingTests.NoTypeFlags))
        self.assertEquals(flags, GIMarshallingTests.NoTypeFlags.VALUE2)

    def test_flags_inout(self):
        flags = GIMarshallingTests.no_type_flags_inout(GIMarshallingTests.NoTypeFlags.VALUE2)
        self.assertTrue(isinstance(flags, GIMarshallingTests.NoTypeFlags))
        self.assertEquals(flags, GIMarshallingTests.NoTypeFlags.VALUE1)


class TestStructure(unittest.TestCase):

    def test_simple_struct(self):
        self.assertTrue(issubclass(GIMarshallingTests.SimpleStruct, GObject.GPointer))

        struct = GIMarshallingTests.SimpleStruct()
        self.assertTrue(isinstance(struct, GIMarshallingTests.SimpleStruct))

        self.assertEquals(0, struct.long_)
        self.assertEquals(0, struct.int8)

        struct.long_ = 6
        struct.int8 = 7

        self.assertEquals(6, struct.long_)
        self.assertEquals(7, struct.int8)

        del struct

    def test_nested_struct(self):
        struct = GIMarshallingTests.NestedStruct()

        self.assertTrue(isinstance(struct.simple_struct, GIMarshallingTests.SimpleStruct))

        struct.simple_struct.long_ = 42
        self.assertEquals(42, struct.simple_struct.long_)

        del struct

    def test_not_simple_struct(self):
        struct = GIMarshallingTests.NotSimpleStruct()
        self.assertEquals(None, struct.pointer)

    def test_simple_struct_return(self):
        struct = GIMarshallingTests.simple_struct_returnv()

        self.assertTrue(isinstance(struct, GIMarshallingTests.SimpleStruct))
        self.assertEquals(6, struct.long_)
        self.assertEquals(7, struct.int8)

        del struct

    def test_simple_struct_in(self):
        struct = GIMarshallingTests.SimpleStruct()
        struct.long_ = 6
        struct.int8 = 7

        GIMarshallingTests.SimpleStruct.inv(struct)

        del struct

        struct = GIMarshallingTests.NestedStruct()

        self.assertRaises(TypeError, GIMarshallingTests.SimpleStruct.inv, struct)

        del struct

        self.assertRaises(TypeError, GIMarshallingTests.SimpleStruct.inv, None)

    def test_simple_struct_method(self):
        struct = GIMarshallingTests.SimpleStruct()
        struct.long_ = 6
        struct.int8 = 7

        struct.method()

        del struct

        self.assertRaises(TypeError, GIMarshallingTests.SimpleStruct.method)


    def test_pointer_struct(self):
        self.assertTrue(issubclass(GIMarshallingTests.PointerStruct, GObject.GPointer))

        struct = GIMarshallingTests.PointerStruct()
        self.assertTrue(isinstance(struct, GIMarshallingTests.PointerStruct))

        del struct

    def test_pointer_struct_return(self):
        struct = GIMarshallingTests.pointer_struct_returnv()

        self.assertTrue(isinstance(struct, GIMarshallingTests.PointerStruct))
        self.assertEquals(42, struct.long_)

        del struct

    def test_pointer_struct_in(self):
        struct = GIMarshallingTests.PointerStruct()
        struct.long_ = 42

        struct.inv()

        del struct

    def test_boxed_struct(self):
        self.assertTrue(issubclass(GIMarshallingTests.BoxedStruct, GObject.GBoxed))

        struct = GIMarshallingTests.BoxedStruct()
        self.assertTrue(isinstance(struct, GIMarshallingTests.BoxedStruct))

        self.assertEquals(0, struct.long_)
        self.assertEquals([], struct.g_strv)

        del struct

    def test_boxed_struct_new(self):
        struct = GIMarshallingTests.BoxedStruct.new()
        self.assertTrue(isinstance(struct, GIMarshallingTests.BoxedStruct))

        del struct

    def test_boxed_struct_copy(self):
        struct = GIMarshallingTests.BoxedStruct()

        new_struct = struct.copy()
        self.assertTrue(isinstance(new_struct, GIMarshallingTests.BoxedStruct))

        del new_struct
        del struct

    def test_boxed_struct_return(self):
        struct = GIMarshallingTests.boxed_struct_returnv()

        self.assertTrue(isinstance(struct, GIMarshallingTests.BoxedStruct))
        self.assertEquals(42, struct.long_)
        self.assertEquals(['0', '1', '2'], struct.g_strv)

        del struct

    def test_boxed_struct_in(self):
        struct = GIMarshallingTests.BoxedStruct()
        struct.long_ = 42

        struct.inv()

        del struct

    def test_boxed_struct_out(self):
        struct = GIMarshallingTests.boxed_struct_out()

        self.assertTrue(isinstance(struct, GIMarshallingTests.BoxedStruct))
        self.assertEquals(42, struct.long_)

        del struct

    def test_boxed_struct_inout(self):
        in_struct = GIMarshallingTests.BoxedStruct()
        in_struct.long_ = 42

        out_struct = GIMarshallingTests.boxed_struct_inout(in_struct)

        self.assertTrue(isinstance(out_struct, GIMarshallingTests.BoxedStruct))
        self.assertEquals(0, out_struct.long_)

        del in_struct
        del out_struct

    def test_union(self):
        union = GIMarshallingTests.Union()

        self.assertTrue(isinstance(union, GIMarshallingTests.Union))

        new_union = union.copy()
        self.assertTrue(isinstance(new_union, GIMarshallingTests.Union))

        del union
        del new_union

    def test_union_return(self):
        union = GIMarshallingTests.union_returnv()

        self.assertTrue(isinstance(union, GIMarshallingTests.Union))
        self.assertEquals(42, union.long_)

        del union

    def test_union_in(self):
        union = GIMarshallingTests.Union()
        union.long_ = 42

        union.inv()

        del union

    def test_union_method(self):
        union = GIMarshallingTests.Union()
        union.long_ = 42

        union.method()

        del union

        self.assertRaises(TypeError, GIMarshallingTests.Union.method)

class TestGObject(unittest.TestCase):

    def test_object(self):
        self.assertTrue(issubclass(GIMarshallingTests.Object, GObject.GObject))

        object_ = GIMarshallingTests.Object()
        self.assertTrue(isinstance(object_, GIMarshallingTests.Object))
        self.assertEquals(object_.__grefcount__, 1)

    def test_object_new(self):
        object_ = GIMarshallingTests.Object.new(42)
        self.assertTrue(isinstance(object_, GIMarshallingTests.Object))
        self.assertEquals(object_.__grefcount__, 1)

    def test_object_int(self):
        object_ = GIMarshallingTests.Object(int = 42)
        self.assertEquals(object_.int_, 42)
# FIXME: Don't work yet.
#        object_.int_ = 0
#        self.assertEquals(object_.int_, 0)

    def test_object_static_method(self):
        GIMarshallingTests.Object.static_method()

    def test_object_method(self):
        GIMarshallingTests.Object(int = 42).method()
        self.assertRaises(TypeError, GIMarshallingTests.Object.method, GObject.GObject())
        self.assertRaises(TypeError, GIMarshallingTests.Object.method)


    def test_sub_object(self):
        self.assertTrue(issubclass(GIMarshallingTests.SubObject, GIMarshallingTests.Object))

        object_ = GIMarshallingTests.SubObject()
        self.assertTrue(isinstance(object_, GIMarshallingTests.SubObject))

    def test_sub_object_new(self):
        self.assertRaises(TypeError, GIMarshallingTests.SubObject.new, 42)

    def test_sub_object_static_method(self):
        object_ = GIMarshallingTests.SubObject()
        object_.static_method()

    def test_sub_object_method(self):
        object_ = GIMarshallingTests.SubObject(int = 42)
        object_.method()

    def test_sub_object_sub_method(self):
        object_ = GIMarshallingTests.SubObject()
        object_.sub_method()

    def test_sub_object_overwritten_method(self):
        object_ = GIMarshallingTests.SubObject()
        object_.overwritten_method()

        self.assertRaises(TypeError, GIMarshallingTests.SubObject.overwritten_method, GIMarshallingTests.Object())

    def test_sub_object_int(self):
        object_ = GIMarshallingTests.SubObject()
        self.assertEquals(object_.int_, 0)
# FIXME: Don't work yet.
#        object_.int_ = 42
#        self.assertEquals(object_.int_, 42)

    def test_object_none_return(self):
        object_ = GIMarshallingTests.Object.none_return()
        self.assertTrue(isinstance(object_, GIMarshallingTests.Object))
        self.assertEquals(object_.__grefcount__, 2)

    def test_object_full_return(self):
        object_ = GIMarshallingTests.Object.full_return()
        self.assertTrue(isinstance(object_, GIMarshallingTests.Object))
        self.assertEquals(object_.__grefcount__, 1)

    def test_object_none_in(self):
        object_ = GIMarshallingTests.Object(int = 42)
        GIMarshallingTests.Object.none_in(object_)
        self.assertEquals(object_.__grefcount__, 1)

        object_ = GIMarshallingTests.SubObject(int = 42)
        GIMarshallingTests.Object.none_in(object_)

        object_ = GObject.GObject()
        self.assertRaises(TypeError, GIMarshallingTests.Object.none_in, object_)

        self.assertRaises(TypeError, GIMarshallingTests.Object.none_in, None)

    def test_object_none_out(self):
        object_ = GIMarshallingTests.Object.none_out()
        self.assertTrue(isinstance(object_, GIMarshallingTests.Object))
        self.assertEquals(object_.__grefcount__, 2)

        new_object = GIMarshallingTests.Object.none_out()
        self.assertTrue(new_object is object_)

    def test_object_full_out(self):
        object_ = GIMarshallingTests.Object.full_out()
        self.assertTrue(isinstance(object_, GIMarshallingTests.Object))
        self.assertEquals(object_.__grefcount__, 1)

    def test_object_none_inout(self):
        object_ = GIMarshallingTests.Object(int = 42)
        new_object = GIMarshallingTests.Object.none_inout(object_)

        self.assertTrue(isinstance(new_object, GIMarshallingTests.Object))

        self.assertFalse(object_ is new_object)

        self.assertEquals(object_.__grefcount__, 1)
        self.assertEquals(new_object.__grefcount__, 2)

        new_new_object = GIMarshallingTests.Object.none_inout(object_)
        self.assertTrue(new_new_object is new_object)

        GIMarshallingTests.Object.none_inout(GIMarshallingTests.SubObject(int = 42))

    def test_object_full_inout(self):
        object_ = GIMarshallingTests.Object(int = 42)
        new_object = GIMarshallingTests.Object.full_inout(object_)

        self.assertTrue(isinstance(new_object, GIMarshallingTests.Object))

        self.assertFalse(object_ is new_object)

        self.assertEquals(object_.__grefcount__, 2)
        self.assertEquals(new_object.__grefcount__, 1)

# FIXME: Doesn't actually return the same object.
#    def test_object_inout_same(self):
#        object_ = GIMarshallingTests.Object()
#        new_object = GIMarshallingTests.object_full_inout(object_)
#        self.assertTrue(object_ is new_object)
#        self.assertEquals(object_.__grefcount__, 1)


class TestPythonGObject(unittest.TestCase):

    class Object(GIMarshallingTests.Object):
        def __init__(self, int):
            GIMarshallingTests.Object.__init__(self)
            self.val = None

        def method(self):
            # Don't call super, which asserts that self.int == 42.
            pass

        def do_method_int8_in(self, int8):
            self.val = int8

        def do_method_int8_out(self):
            return 42

        def do_method_with_default_implementation(self, int8):
            GIMarshallingTests.Object.do_method_with_default_implementation(self, int8)
            self.props.int += int8

    class SubObject(GIMarshallingTests.SubObject):
        def __init__(self, int):
            GIMarshallingTests.SubObject.__init__(self)
            self.val = None

        def do_method_with_default_implementation(self, int8):
            self.val = int8

    def test_object(self):
        self.assertTrue(issubclass(self.Object, GIMarshallingTests.Object))

        object_ = self.Object(int = 42)
        self.assertTrue(isinstance(object_, self.Object))

    def test_object_method(self):
        self.Object(int = 0).method()

    def test_object_vfuncs(self):
        object_ = self.Object(int = 42)
        object_.method_int8_in(84)
        self.assertEqual(object_.val, 84)
        self.assertEqual(object_.method_int8_out(), 42)

        object_.method_with_default_implementation(42)
        self.assertEqual(object_.props.int, 84)

        class ObjectWithoutVFunc(GIMarshallingTests.Object):
            def __init__(self, int):
                GIMarshallingTests.Object.__init__(self)

        object_ = ObjectWithoutVFunc(int = 42)
        object_.method_with_default_implementation(84)
        self.assertEqual(object_.props.int, 84)

    def test_subobject_parent_vfunc(self):
        object_ = self.SubObject(int = 81)
        object_.method_with_default_implementation(87)
        self.assertEquals(object_.val, 87)

    def test_dynamic_module(self):
        from gi.module import DynamicGObjectModule
        self.assertTrue(isinstance(GObject, DynamicGObjectModule))
        # compare the same enum from both the pygobject attrs and gi GObject attrs
        self.assertEquals(GObject.SIGNAL_ACTION, GObject.SignalFlags.ACTION)
        # compare a static gobject attr with a dynamic GObject attr
        self.assertEquals(GObject.GObject, gobject.GObject)

    def test_subobject_non_vfunc_do_method(self):
        class PythonObjectWithNonVFuncDoMethod:
            def do_not_a_vfunc(self):
                return 5

        class ObjectOverrideNonVFuncDoMethod(GIMarshallingTests.Object, PythonObjectWithNonVFuncDoMethod):
            def do_not_a_vfunc(self):
                value = super(ObjectOverrideNonVFuncDoMethod, self).do_not_a_vfunc()
                return 13 + value

        object_ = ObjectOverrideNonVFuncDoMethod()
        self.assertEquals(18, object_.do_not_a_vfunc())

    def test_native_function_not_set_in_subclass_dict(self):
        # Previously, GI was setting virtual functions on the class as well
        # as any *native* class that subclasses it. Here we check that it is only
        # set on the class that the method is originally from.
        self.assertTrue('do_method_with_default_implementation' in GIMarshallingTests.Object.__dict__)
        self.assertTrue('do_method_with_default_implementation' not in GIMarshallingTests.SubObject.__dict__)

        # Here we check that accessing a vfunc from the subclass returns the same wrapper object,
        # meaning that multiple wrapper objects have not been created for the same vfunc.
        func1 = GIMarshallingTests.Object.do_method_with_default_implementation
        func2 = GIMarshallingTests.SubObject.do_method_with_default_implementation
        if sys.version_info < (3,0):
            func1 = func1.im_func
            func2 = func2.im_func
            
        self.assertTrue(func1 is func2)

    def test_subobject_with_interface_and_non_vfunc_do_method(self):
        # There was a bug for searching for vfuncs in interfaces. It was
        # triggered by having a do_* method that wasn't overriding
        # a native vfunc, as well as inheriting from an interface.
        class GObjectSubclassWithInterface(GObject.GObject, GIMarshallingTests.Interface):
            def do_method_not_a_vfunc(self):
                pass

class TestMultiOutputArgs(unittest.TestCase):

    def test_int_out_out(self):
        self.assertEquals((6, 7), GIMarshallingTests.int_out_out())

    def test_int_return_out(self):
        self.assertEquals((6, 7), GIMarshallingTests.int_return_out())

class TestGErrorException(unittest.TestCase):
    def test_gerror_exception(self):
        self.assertRaises(GObject.GError, GIMarshallingTests.gerror)
        try:
            GIMarshallingTests.gerror()
        except Exception:
            etype, e = sys.exc_info()[:2]
            self.assertEquals(e.domain, GIMarshallingTests.CONSTANT_GERROR_DOMAIN)
            self.assertEquals(e.code, GIMarshallingTests.CONSTANT_GERROR_CODE)
            self.assertEquals(e.message, GIMarshallingTests.CONSTANT_GERROR_MESSAGE)


# Interface

class TestInterfaces(unittest.TestCase):

    def test_wrapper(self):
        self.assertTrue(issubclass(GIMarshallingTests.Interface, GObject.GInterface))
        self.assertEquals(GIMarshallingTests.Interface.__gtype__.name, 'GIMarshallingTestsInterface')
        self.assertRaises(NotImplementedError, GIMarshallingTests.Interface)

    def test_implementation(self):

        class TestInterfaceImpl(GObject.GObject, GIMarshallingTests.Interface):
            def __init__(self):
                GObject.GObject.__init__(self)
                self.val = None

            def do_test_int8_in(self, int8):
                self.val = int8

        self.assertTrue(issubclass(TestInterfaceImpl, GIMarshallingTests.Interface))

        instance = TestInterfaceImpl()
        self.assertTrue(isinstance(instance, GIMarshallingTests.Interface))

        GIMarshallingTests.test_interface_test_int8_in(instance, 42)
        self.assertEquals(instance.val, 42)

        class TestInterfaceImplA(TestInterfaceImpl):
            pass

        class TestInterfaceImplB(TestInterfaceImplA):
            pass

        instance = TestInterfaceImplA()
        GIMarshallingTests.test_interface_test_int8_in(instance, 42)
        self.assertEquals(instance.val, 42)

    def test_mro(self):
        # there was a problem with Python bailing out because of
        # http://en.wikipedia.org/wiki/Diamond_problem with interfaces,
        # which shouldn't really be a problem.

        class TestInterfaceImpl(GObject.GObject, GIMarshallingTests.Interface):
            pass

        class TestInterfaceImpl2(GIMarshallingTests.Interface,
                                 TestInterfaceImpl):
            pass

        class TestInterfaceImpl3(TestInterfaceImpl,
                                 GIMarshallingTests.Interface2):
            pass


class TestInterfaceClash(unittest.TestCase):

    def test_clash(self):
        def create_clash():
            class TestClash(GObject.GObject, GIMarshallingTests.Interface, GIMarshallingTests.Interface2):
                def do_test_int8_in(self, int8):
                    pass
            TestClash()

        self.assertRaises(TypeError, create_clash)


class TestOverrides(unittest.TestCase):

    def test_constant(self):
        self.assertEquals(GIMarshallingTests.OVERRIDES_CONSTANT, 7)

    def test_struct(self):
        # Test that the constructor has been overridden.
        struct = GIMarshallingTests.OverridesStruct(42)

        self.assertTrue(isinstance(struct, GIMarshallingTests.OverridesStruct))

        # Test that the method has been overridden.
        self.assertEquals(6, struct.method())

        del struct

        # Test that the overrides wrapper has been registered.
        struct = GIMarshallingTests.overrides_struct_returnv()

        self.assertTrue(isinstance(struct, GIMarshallingTests.OverridesStruct))

        del struct

    def test_object(self):
        # Test that the constructor has been overridden.
        object_ = GIMarshallingTests.OverridesObject(42)

        self.assertTrue(isinstance(object_, GIMarshallingTests.OverridesObject))

        # Test that the alternate constructor has been overridden.
        object_ = GIMarshallingTests.OverridesObject.new(42)

        self.assertTrue(isinstance(object_, GIMarshallingTests.OverridesObject))

        # Test that the method has been overridden.
        self.assertEquals(6, object_.method())

        # Test that the overrides wrapper has been registered.
        object_ = GIMarshallingTests.OverridesObject.returnv()

        self.assertTrue(isinstance(object_, GIMarshallingTests.OverridesObject))

    def test_module_name(self):
        self.assertEquals(GIMarshallingTests.OverridesStruct.__module__, 'gi.overrides.GIMarshallingTests')
        self.assertEquals(GObject.InitiallyUnowned.__module__, 'gi.repository.GObject')

class TestDir(unittest.TestCase):
    def test_members_list(self):
        list = dir(GIMarshallingTests)
        self.assertTrue('OverridesStruct' in list)
        self.assertTrue('BoxedStruct' in list)
        self.assertTrue('OVERRIDES_CONSTANT' in list)
        self.assertTrue('GEnum' in list)
        self.assertTrue('int32_return_max' in list)

    def test_modules_list(self):
        import gi.repository
        list = dir(gi.repository)
        self.assertTrue('GIMarshallingTests' in list)

        # FIXME: test to see if a module which was not imported is in the list
        #        we should be listing every typelib we find, not just the ones
        #        which are imported
        #
        #        to test this I recommend we compile a fake module which
        #        our tests would never import and check to see if it is
        #        in the list:
        #
        # self.assertTrue('DoNotImportDummyTests' in list)

class TestGErrorArrayInCrash(unittest.TestCase):
    # Previously there was a bug in invoke, in which C arrays were unwrapped
    # from inside GArrays to be passed to the C function. But when a GError was
    # set, invoke would attempt to free the C array as if it were a GArray.
    # This crash is only for C arrays. It does not happen for C functions which
    # take in GArrays. See https://bugzilla.gnome.org/show_bug.cgi?id=642708
    def test_gerror_array_in_crash(self):
        self.assertRaises(GObject.GError, GIMarshallingTests.gerror_array_in, [1, 2, 3])
