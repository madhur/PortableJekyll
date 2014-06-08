###############################################################################
# Name: _dirmon.py                                                            #
# Purpose: Directory monitor object.                                          #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2011 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows Licence                                                  #
###############################################################################

"""
Editra Business Model Library: DirectoryMonitor


"""

__author__ = "Cody Precord <cprecord@editra.org>"
__cvsid__ = "$Id: _dirmon.py 71949 2012-07-03 13:41:15Z CJP $"
__revision__ = "$Revision: 71949 $"

__all__ = ['DirectoryMonitor',]

#-----------------------------------------------------------------------------#
# Imports
import wx
import os
import time
import threading

# Local imports
import fileutil

#-----------------------------------------------------------------------------#

class DirectoryMonitor(object):
    """Object to manage monitoring file system changes"""
    def __init__(self, checkFreq=1000.0):
        """@keyword checkFreq: check frequency in milliseconds"""
        super(DirectoryMonitor, self).__init__()

        # Attributes
        self._watcher = WatcherThread(self._ThreadNotifier, checkFreq=checkFreq)
        self._callbacks = list()
        self._cbackLock = threading.Lock()
        self._running = False

    def __del__(self):
        if self._running:
            self._watcher.Shutdown()
            self._watcher.join()

    def _ThreadNotifier(self, added, deleted, modified):
        """Notifier callback from background L{WatcherThread}
        to call notifiers on main thread.
        @note: this method is invoked from a background thread and
               is not safe to make direct UI calls from.

        """
        with self._cbackLock:
            for cback in self._callbacks:
                wx.CallAfter(cback, added, deleted, modified)

    #---- Properties ----#

    # Is the monitor currently watching any directories
    Monitoring = property(lambda self: self._running)
    Frequency = property(lambda self: self._watcher.GetFrequency(),
                         lambda self, freq: self._watcher.SetFrequency(freq))

    #---- End Properties ----#

    def AddDirectory(self, dname):
        """Add a directory to the monitor
        @param dname: directory path
        @return: bool - True if added, False if failed to add

        """
        return self._watcher.AddWatchDirectory(dname)

    def SubscribeCallback(self, callback):
        """Subscribe a callback method to be called when changes are
        detected in one of the watched directories.
        @param callback: callable([added,], [deleted,], [modified,])

        """
        with self._cbackLock:
            if callback not in self._callbacks:
                self._callbacks.append(callback)

    def UnsubscribeCallback(self, callback):
        """Remove a callback method from the monitor"""
        with self._cbackLock:
            if callback in self._callbacks:
                self._callbacks.remove(callback)

    def RemoveDirectory(self, dname):
        """Remove a directory from the watch list
        @param dname: directory path

        """
        self._watcher.RemoveWatchDirectory(dname)

    def StartMonitoring(self):
        """Start monitoring the directories in the watch list and
        notifying target of changes.

        """
        self._running = True
        self._watcher.start()

    def Suspend(self, pause=True):
        """Suspend background processing
        @keyword pause: True (suspend) False (resume)

        """
        if pause:
            self._watcher.Suspend()
        else:
            self._watcher.Continue()

    def Refresh(self):
        """Force a recheck of the monitored directories. This method
        is useful for doing manual control of the refresh cycle. It is
        ignored and does nothing when WatcherThread is set up for automatic
        refresh cycles.

        """
        self._watcher.Refresh()

#-----------------------------------------------------------------------------#
    
class WatcherThread(threading.Thread):
    """Background thread to monitor a directory"""
    def __init__(self, notifier, checkFreq=1000.0):
        """Create the WatcherThread. Provide a callback notifier method
        that will be called when changes are detected in the directory.
        The notifier will be called in the context of this thread. Notifier
        will be called with three lists of ebmlib.File objects to indicate
        the changes that have occurred.
        @param notifier: callable([added,], [deleted,], [modified,])
        @keyword checkFreq: check frequency in milliseconds. If value is set
                            to zero or less update checks must be manually
                            controlled via the Refresh interface.

        """
        super(WatcherThread, self).__init__()

        # Attributes
        assert callable(notifier)
        self._notifier = notifier
        self._dirs = list() # Directories being monitored

        self._freq = checkFreq # Monitoring frequency in milliseconds
        self._continue = True
        self._changePending = False
        self._lock = threading.Lock()
        self._suspend = False
        self._suspendcond = threading.Condition()
        self._listEmptyCond = threading.Condition()
        self._refreshCond = threading.Condition()

    def run(self):
        """Run the watcher"""
        while self._continue:
            deleted = list()
            added = list()
            modified = list()

            # Watch is empty so wait on things to monitor before continuing
            if not self._dirs:
                with self._listEmptyCond:
                    self._listEmptyCond.wait()

            # Suspend processing if requested
            if self._suspend:
                with self._suspendcond:
                    self._suspendcond.wait()

            with self._lock:
                for dobj in self._dirs:
                    if not self._continue:
                        return
                    elif self._changePending:
                        break

                    # Check if a watched directory has been deleted
                    if not os.path.exists(dobj.Path):
                        deleted.append(dobj)
                        self._dirs.remove(dobj)
                        continue

                    snapshot = fileutil.GetDirectoryObject(dobj.Path, 
                                                           False, True)

                    # Check for deletions
                    dobjFiles = dobj.Files # optimization
                    dobjIndex = dobjFiles.index # optimization
                    snapFiles = snapshot.Files
                    for tobj in dobjFiles:
                        if not self._continue:
                            return
                        elif self._changePending:
                            break
                        if tobj not in snapFiles:
                            deleted.append(tobj)
                            dobjFiles.remove(tobj)

                    # Check for additions and modifications
                    for tobj in snapFiles:
                        if not self._continue:
                            return
                        elif self._changePending:
                            break
                        if tobj not in dobjFiles:
                            # new object was added
                            added.append(tobj)
                            dobjFiles.append(tobj)
                        else:
                            idx = dobjIndex(tobj)
                            existing = dobjFiles[idx]
                            # object was modified
                            if existing.ModTime < tobj.ModTime:
                                modified.append(tobj)
                                existing.ModTime = tobj.ModTime

            # Call Notifier if anything changed
            if any((added, deleted, modified)):
                self._notifier(added, deleted, modified)

            # Wait till next check
            if self._freq > 0:
                # Automatic updates
                time.sleep(self._freq / 1000.0)
            else:
                # Manually controlled updates
                with self._refreshCond:
                    self._refreshCond.wait()

    #---- Implementation ----#

    def AddWatchDirectory(self, dpath):
        """Add a directory to the watch list
        @param dpath: directory path (unicode)
        @return: bool - True means watch was added, False means unable to list directory

        """
        assert os.path.isdir(dpath)
        dobj = fileutil.Directory(dpath)
        self._changePending = True
        with self._lock:
            if dobj not in self._dirs and os.access(dobj.Path, os.R_OK):
                # Get current snapshot of the directory
                try:
                    dobj = fileutil.GetDirectoryObject(dpath, False, True)
                except OSError:
                    self._changePending = False
                    return False
                self._dirs.append(dobj)
                with self._listEmptyCond:
                    self._listEmptyCond.notify()
        self._changePending = False
        return True

    def RemoveWatchDirectory(self, dpath):
        """Remove a directory from the watch
        @param dpath: directory path to remove (unicode)

        """
        dobj = fileutil.Directory(dpath)
        self._changePending = True
        with self._lock:
            if dobj in self._dirs:
                self._dirs.remove(dobj)
            # Also remove any subpaths of dpath
            toremove = list()
            for d in self._dirs:
                if fileutil.IsSubPath(d.Path, dpath):
                    toremove.append(d)
            for todel in toremove:
                self._dirs.remove(todel)
        self._changePending = False

    def GetFrequency(self):
        """Get the update frequency
        @return: int (milliseconds)

        """
        return self._freq

    def SetFrequency(self, milli):
        """Set the update frequency
        @param milli: int (milliseconds)

        """
        self._freq = float(milli)

    def Refresh(self):
        """Recheck the monitored directories
        only useful when manually controlling refresh cycle of the monitor.

        """
        with self._refreshCond:
            self._refreshCond.notify()

    def Shutdown(self):
        """Shut the thread down"""
        self._continue = False

    def Suspend(self):
        """Suspend the thread"""
        self._suspend = True

    def Continue(self):
        """Continue the thread"""
        self._suspend = False
        with self._suspendcond:
            self._suspendcond.notify()
