# -*- coding: utf-8 -*-
#*****************************************************************************
#       Copyright (C) 2003-2006 Jack Trainor.
#       Copyright (C) 2006  Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#*****************************************************************************
###################################
#
# Based on recipe posted to ctypes-users
# see archive
# http://aspn.activestate.com/ASPN/Mail/Message/ctypes-users/1771866
#
#

###################################################################################
#
# The Python win32clipboard lib functions work well enough ... except that they
# can only cut and paste items from within one application, not across
# applications or processes.
#
# I've written a number of Python text filters I like to run on the contents of
# the clipboard so I need to call the Windows clipboard API with global memory
# for my filters to work properly.
#
# Here's some sample code solving this problem using ctypes.
#
# This is my first work with ctypes.  It's powerful stuff, but passing arguments
# in and out of functions is tricky.  More sample code would have been helpful,
# hence this contribution.
#
###################################################################################

from ctypes import *
from pyreadline.keysyms.winconstants import CF_TEXT, GHND
from pyreadline.unicode_helper import ensure_unicode,ensure_str

OpenClipboard = windll.user32.OpenClipboard
OpenClipboard.argtypes = [c_int]

EmptyClipboard = windll.user32.EmptyClipboard

GetClipboardData = windll.user32.GetClipboardData
GetClipboardData.argtypes = [c_int]

GetClipboardFormatName = windll.user32.GetClipboardFormatNameA
GetClipboardFormatName.argtypes = [c_uint,c_char_p,c_int]

SetClipboardData = windll.user32.SetClipboardData
SetClipboardData.argtypes = [c_int,c_int]

EnumClipboardFormats = windll.user32.EnumClipboardFormats
EnumClipboardFormats.argtypes = [c_int]

CloseClipboard = windll.user32.CloseClipboard
CloseClipboard.argtypes = []


GlobalAlloc = windll.kernel32.GlobalAlloc
GlobalLock = windll.kernel32.GlobalLock
GlobalLock.argtypes = [c_int]
GlobalUnlock = windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = [c_int]
memcpy = cdll.msvcrt.memcpy

def enum():
    OpenClipboard(0)
    q = EnumClipboardFormats(0)
    while q:
        q = EnumClipboardFormats(q)
    CloseClipboard()

def getformatname(format):
    buffer = c_buffer(" "*100)
    bufferSize = sizeof(buffer)
    OpenClipboard(0)
    GetClipboardFormatName(format, buffer, bufferSize)
    CloseClipboard()
    return buffer.value

def GetClipboardText():
    text = u""
    if OpenClipboard(0):
        hClipMem = GetClipboardData(CF_TEXT)
        if hClipMem:        
            GlobalLock.restype = c_char_p
            text = GlobalLock(hClipMem)
            GlobalUnlock(hClipMem)
        CloseClipboard()
    return ensure_unicode(text)

def SetClipboardText(text):
    buffer = c_buffer(ensure_str(text))
    bufferSize = sizeof(buffer)
    hGlobalMem = GlobalAlloc(c_int(GHND), c_int(bufferSize))
    GlobalLock.restype = c_void_p
    lpGlobalMem = GlobalLock(c_int(hGlobalMem))
    memcpy(lpGlobalMem, addressof(buffer), c_int(bufferSize))
    GlobalUnlock(c_int(hGlobalMem))
    if OpenClipboard(0):
        EmptyClipboard()
        SetClipboardData(c_int(CF_TEXT), c_int(hGlobalMem))
        CloseClipboard()

if __name__ == u'__main__':
    txt = GetClipboardText()                            # display last text clipped
    print txt
