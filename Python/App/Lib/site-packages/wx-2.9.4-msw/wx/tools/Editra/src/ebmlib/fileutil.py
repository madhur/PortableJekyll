###############################################################################
# Name: fileutil.py                                                           #
# Purpose: File Management Utilities.                                         #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2009 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows Licence                                                  #
###############################################################################

"""
Editra Business Model Library: File Utilities

Utility functions for managing and working with files.

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: fileutil.py 71689 2012-06-07 18:55:45Z CJP $"
__revision__ = "$Revision: 71689 $"

__all__ = [ 'GetAbsPath', 'GetFileExtension', 'GetFileModTime', 'GetFileName',
            'GetFileSize', 'GetPathName', 'GetPathFromURI', 'GetUniqueName', 
            'IsLink', 'MakeNewFile', 'MakeNewFolder', 'PathExists',
            'ResolveRealPath', 'IsExecutable', 'Which', 'ComparePaths',
            'AddFileExtension', 'GetDirectoryObject', 'File', 'Directory',
            'GetFileManagerCmd', 'OpenWithFileManager', 'IsHidden', 'IsSubPath' ]

#-----------------------------------------------------------------------------#
# Imports
import wx
import ctypes
import os
import platform
import urllib2
import stat
import subprocess

UNIX = WIN = False
if wx.Platform == '__WXMSW__':
    WIN = True
    try:
        # Check for if win32 extensions are available
        import win32com.client as win32client
    except ImportError:
        win32client = None

    try:
        # Check for win32api
        import win32api
    except ImportError:
        win32api = None
else:
    UNIX = True

#-----------------------------------------------------------------------------#

def uri2path(func):
    """Decorator method to convert path arguments that may be uri's to
    real file system paths. Arg 0 must be a file path or uri.

    """
    def WrapURI(*args, **kwargs):
        args = list(args)
        args[0] = GetPathFromURI(args[0])
        return func(*args, **kwargs)

    WrapURI.__name__ = func.__name__
    WrapURI.__doc__ = func.__doc__
    return WrapURI

#-----------------------------------------------------------------------------#

def AddFileExtension(path, ext):
    """Add a file extension to a path if it doesn't already exist
    @param path: file path
    @param ext: file extension

    """
    assert isinstance(ext, basestring)
    if not ext.startswith('.'):
        ext = '.' + ext
    if not path.endswith(ext):
        path = path + ext
    return path

def ComparePaths(path1, path2):
    """Determine whether the two given paths are equivalent
    @param path1: unicode
    @param path2: unicode
    @return: bool

    """
    path1 = GetAbsPath(path1)
    path2 = GetAbsPath(path2)
    if WIN:
        path1 = path1.lower()
        path2 = path2.lower()
    return path1 == path2

def CopyFile(orig, dest):
    """Copy the given file to the destination
    @param orig: file to copy (full path)
    @param dest: where to copy to

    """
    raise NotImplementedError

@uri2path
def GetAbsPath(path):
    """Get the absolute path of a file of a file.
    @param path: string
    @return: string
    @note: on windows if win32api is available short notation paths will be
           converted to the proper long name.
    
    """
    rpath = os.path.abspath(path)
    # Resolve short path notation on Windows when possible
    if WIN and win32api is not None and u"~" in rpath:
        try:
            rpath = win32api.GetLongPathNameW(rpath)
        except Exception:
            # Ignore errors from win32api calls
            pass
    return rpath

def GetFileExtension(file_str):
    """Gets last atom at end of string as extension if
    no extension whole string is returned
    @param file_str: path or file name to get extension from

    """
    return file_str.split('.')[-1]

def GetFileModTime(file_name):
    """Returns the time that the given file was last modified on
    @param file_name: path of file to get mtime of

    """
    try:
        mod_time = os.path.getmtime(file_name)
    except (OSError, EnvironmentError):
        mod_time = 0
    return mod_time

def GetFileName(path):
    """Gets last atom on end of string as filename
    @param path: full path to get filename from

    """
    return os.path.split(path)[-1]

@uri2path
def GetFileSize(path):
    """Get the size of the file at a given path
    @param path: Path to file
    @return: long

    """
    try:
        return os.stat(path)[stat.ST_SIZE]
    except:
        return 0

def GetPathFromURI(path):
    """Get a local path from a file:// uri
    @return: normalized path

    """
    if path.startswith(u"file:"):
        path = path.replace(u"file:", u"")
        path = path.lstrip(u"/")
        if platform.system().lower() in ('windows', 'microsoft'):
            path = path.replace(u"/", u"\\")
            if len(path) >= 2 and path[1] != u':':
                # A valid windows file uri should start with the drive
                # letter. If not make the assumption that it should be
                # the C: drive.
                path = u"C:\\\\" + path
        else:
            path = u"/" + path
        path = urllib2.unquote(path)

    return path

@uri2path
def GetPathName(path):
    """Gets the path minus filename
    @param path: full path to get base of

    """
    return os.path.split(path)[0]

@uri2path
def IsLink(path):
    """Is the file a link
    @return: bool

    """
    if WIN:
        return path.endswith(".lnk") or os.path.islink(path)
    else:
        return os.path.islink(path)

def IsSubPath(path1, path2):
    """Is path1 a subpath of path2
    i.e) /usr/bin/foo is a subpath of /usr/bin
    @return: bool

    """
    if WIN:
        path1 = path1.lower()
        path2 = path2.lower()
    path1 = GetAbsPath(path1)
    path2 = GetAbsPath(path2)
    return path1.startswith(path2)

@uri2path
def IsHidden(path):
    """Is the path a hidden path
    @param path: path to check
    @return: bool

    """
    bHidden = False
    if PathExists(path):
        if WIN:
            try:
                attrs = ctypes.windll.kernel32.GetFileAttributesW(path)
                assert attrs != -1
                bHidden = bool(attrs & 2)
            except (AttributeError, AssertionError):
                bHidden = False
        else:
            dname = GetFileName(path)
            bHidden = dname.startswith('.')
    return bHidden

@uri2path
def PathExists(path):
    """Does the path exist.
    @param path: file path or uri
    @return: bool

    """
    return os.path.exists(path)

@uri2path
def IsExecutable(path):
    """Is the file at the given path an executable file
    @param path: file path
    @return: bool

    """
    return os.path.isfile(path) and os.access(path, os.X_OK)

@uri2path
def ResolveRealPath(link):
    """Return the real path of the link file
    @param link: path of link file
    @return: string

    """
    assert IsLink(link), "ResolveRealPath expects a link file!"
    realpath = link
    if WIN and win32client is not None:
        shell = win32client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(link)
        realpath = shortcut.Targetpath
    else:
        realpath = os.path.realpath(link)
    return realpath

def GetFileManagerCmd():
    """Get the file manager open command for the current os. Under linux
    it will check for xdg-open, nautilus, konqueror, and Thunar, it will then
    return which one it finds first or 'nautilus' it finds nothing.
    @return: string

    """
    if wx.Platform == '__WXMAC__':
        return 'open'
    elif wx.Platform == '__WXMSW__':
        return 'explorer'
    else:
        # Check for common linux filemanagers returning first one found
        #          Gnome/ubuntu KDE/kubuntu  xubuntu
        for cmd in ('xdg-open', 'nautilus', 'konqueror', 'Thunar'):
            result = os.system("which %s > /dev/null" % cmd)
            if result == 0:
                return cmd
        else:
            return 'nautilus'

def OpenWithFileManager(path):
    """Open the given path with the systems file manager
    @param path: file/directory path

    """
    cmd = GetFileManagerCmd()
    subprocess.call([cmd, path])

def Which(program):
    """Find the path of the given executable
    @param program: executable name (i.e 'python')
    @return: executable path or None

    """
    # Check local directory first
    if IsExecutable(program):
        return program
    else:
        # Start looking on the $PATH
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if IsExecutable(exe_file):
                return exe_file        
    return None

def GetDirectoryObject(path, recurse=True, includedot=False):
    """Gets a L{Directory} object representing the filesystem of the
    given path.
    @param path: base path to list
    @keyword recurse: recurse into subdirectories
    @keyword includedot: include '.' files
    @return: L{Directory} object instance

    """
    assert os.path.isdir(path)
    def _BuildDir(thedir):
        dirAddFile = thedir.Files.append
        isdir = os.path.isdir
        pjoin = os.path.join
        for fname in os.listdir(thedir.Path):
            if not includedot and fname.startswith('.'):
                continue
            fpath = pjoin(thedir.Path, fname)
            if isdir(fpath):
                newobj = Directory(fpath)
                if recurse:
                    _BuildDir(newobj)
            else:
                newobj = File(fpath)
            dirAddFile(newobj)

    dobj = Directory(path)
    _BuildDir(dobj)
    return dobj

#-----------------------------------------------------------------------------#

class File(object):
    """Basic file data structure"""
    __slots__ = ('path', 'modtime')
    def __init__(self, path):
        super(File, self).__init__()

        self.path = path
        self.modtime = GetFileModTime(self.path)

    Path = property(lambda self: self.path)
    Name = property(lambda self: os.path.basename(self.Path))
    ModTime = property(lambda self: self.modtime,
                       lambda self, mod: setattr(self, 'modtime', mod))

    def __str__(self):
        return self.Path

    def __eq__(self, other):
        assert isinstance(other, File)
        return ComparePaths(self.Path, other.Path)

class Directory(File):
    """Basic directory data structure.
    Is a container class that provides a simple in memory representation of
    a file system.

    """
    __slots__ = ('files',)
    def __init__(self, path):
        super(Directory, self).__init__(path)

        self.files = list()

    Files = property(lambda self: self.files)

#-----------------------------------------------------------------------------#

def GetUniqueName(path, name):
    """Make a file name that will be unique in case a file of the
    same name already exists at that path.
    @param path: Root path to folder of files destination
    @param name: desired file name base
    @return: string

    """
    tmpname = os.path.join(path, name)
    if os.path.exists(tmpname):
        if '.' not in name:
            ext = ''
            fbase = name
        else:
            ext = '.' + name.split('.')[-1]
            fbase = name[:-1 * len(ext)]

        inc = len([x for x in os.listdir(path) if x.startswith(fbase)])
        tmpname = os.path.join(path, "%s-%d%s" % (fbase, inc, ext))
        while os.path.exists(tmpname):
            inc = inc + 1
            tmpname = os.path.join(path, "%s-%d%s" % (fbase, inc, ext))

    return tmpname


#-----------------------------------------------------------------------------#

def MakeNewFile(path, name):
    """Make a new file at the given path with the given name.
    If the file already exists, the given name will be changed to
    a unique name in the form of name + -NUMBER + .extension
    @param path: path to directory to create file in
    @param name: desired name of file
    @return: Tuple of (success?, Path of new file OR Error message)

    """
    if not os.path.isdir(path):
        path = os.path.dirname(path)
    fname = GetUniqueName(path, name)

    try:
        open(fname, 'w').close()
    except (IOError, OSError), msg:
        return (False, str(msg))

    return (True, fname)

def MakeNewFolder(path, name):
    """Make a new folder at the given path with the given name.
    If the folder already exists, the given name will be changed to
    a unique name in the form of name + -NUMBER.
    @param path: path to create folder on
    @param name: desired name for folder
    @return: Tuple of (success?, new dirname OR Error message)

    """
    if not os.path.isdir(path):
        path = os.path.dirname(path)
    folder = GetUniqueName(path, name)
    try:
        os.mkdir(folder)
    except (OSError, IOError), msg:
        return (False, str(msg))

    return (True, folder)
