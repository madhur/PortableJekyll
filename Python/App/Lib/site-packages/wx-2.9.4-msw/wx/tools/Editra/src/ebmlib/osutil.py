###############################################################################
# Name: osutil.py                                                             #
# Purpose: Text Utilities.                                                    #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2010 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows Licence                                                  #
###############################################################################

"""
Editra Business Model Library: Operating System Utilities

Utilities for handling OS related interactions.

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: $"
__revision__ = "$Revision: $"

__all__ = ['InstallTermHandler',
           'GetWindowsDrives', 'GetWindowsDriveType',
           'GenericDrive', 'FixedDrive', 'CDROMDrive', 'RamDiskDrive', 'RemoteDrive',
           'RemovableDrive' ]

#-----------------------------------------------------------------------------#
# Imports
import wx
import ctypes
import signal
import collections

HASWIN32 = False
if wx.Platform == '__WXMSW__':
    try:
        import win32api
    except ImportError:
        HASWIN32 = False
    else:
        HASWIN32 = True

#-----------------------------------------------------------------------------#
# Windows Drive Utilities

class GenericDrive(object):
    def __init__(self, name):
        super(GenericDrive, self).__init__()

        # Attributes
        self._name = name

    Name = property(lambda self: self._name,
                    lambda self, v: setattr(self, '_name', v))

class RemovableDrive(GenericDrive):
    pass
class FixedDrive(GenericDrive):
    pass
class RemoteDrive(GenericDrive):
    pass
class CDROMDrive(GenericDrive):
    pass
class RamDiskDrive(GenericDrive):
    pass

def GetWindowsDrives():
    """Get a list of all available windows drives
    @return: list of strings

    """
    assert wx.Platform == '__WXMSW__', "Windows Only API Method"
    drives = list()
    try:
        dletters = list()
        bmask = ctypes.windll.kernel32.GetLogicalDrives()
        for dletter in u"ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if bmask & 1:
                dletters.append(dletter)
            bmask >>= 1

        for dletter in dletters:
            dname = dletter + u":\\"
            dtype = GetWindowsDriveType(dname)
            if type(dtype) != GenericDrive:
                drives.append(dtype)
    except Exception, err:
        pass
    return drives

def GetWindowsDriveType(dname):
    """Get the drive type for the given letter"""
    assert wx.Platform == '__WXMSW__', "Windows Only API Method"
    dtype = GenericDrive(dname)
    try:
        dtypes = [None, None, RemovableDrive, FixedDrive, RemoteDrive, CDROMDrive, RamDiskDrive]
        idx = ctypes.windll.kernel32.GetDriveTypeW(dname)
        if idx < len(dtypes):
            drive = dtypes[idx]
            if drive:
                dtype = drive(dname)
    except:
        pass
    return dtype

#-----------------------------------------------------------------------------#

def InstallTermHandler(callback, *args, **kwargs):
    """Install exit app handler for sigterm (unix/linux)
    and uses SetConsoleCtrlHandler on Windows.
    @param callback: callable(*args, **kwargs)
    @param args: positional arguments to pass to callback
    @param kwargs: keyword arguments to pass to callback
    @return: bool (installed or not)

    """
    assert isinstance(callback, collections.Callable), "callback must be callable!"

    installed = True
    if wx.Platform == '__WXMSW__':
        if HASWIN32:
            win32api.SetConsoleCtrlHandler(lambda dummy : callback(*args, **kwargs),
                                           True)
        else:
            installed = False
    else:
        signal.signal(signal.SIGTERM,
                      lambda signum, frame : callback(*args, **kwargs))

    return installed

