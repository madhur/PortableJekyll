import sys

if sys.version_info >= (3, 0):
    '''
    for tests that need to test long values in python 2

    python 3 does not differentiate between long and int
    and does not supply a long keyword

    instead of testing longs by using values such as 10L
    test writters should do this:

    from compathelper import _long
    _long(10)
    '''
    _long = int

    '''
    for tests that need to test string values in python 2

    python 3 does differentiate between str and bytes
    and does not supply a basestring keyword

    any tests that use basestring should do this:

    from compathelper import _basestring
    isinstance(_basestring, "hello")
    '''
    _basestring = str

    '''
    for tests that need to write to intefaces that take bytes in
    python 3

    python 3 has a seperate bytes type for low level functions like os.write

    python 2 treats these as strings

    any tests that need to write a string of bytes should do something like
    this:

    from compathelper import _bytes
    os.write(_bytes("hello"))
    '''

    _bytes = lambda s: s.encode()

    '''
    for tests that need to write to intefaces that take unicode in
    python 2

    python 3 strings are unicode encoded as UTF-8 so the unicode object 
    doesn't exist

    python 2 differs between a string an unicode string and you must specify
    an encoding.  This macro will specify UTF-8 in python 2

    any tests that need to use unicode should do this

    from compathelper import _unicode
    unicode_string = _unicode('this is a unicode string')
    '''

    _unicode = lambda s: str(s)
else:
    _long = long
    _basestring = basestring
    _bytes = str
    _unicode = lambda s: unicode(s, 'UTF-8')
