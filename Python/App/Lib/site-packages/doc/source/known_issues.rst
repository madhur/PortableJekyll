
Known issues
============

 * If you do not want pyreadline at the standard windows prompt. Delete readline.py
   from the install directory. This will not interfere with ipython usage, but you will
   not be able to use the rlcompleter module which requires the readline.py module.

 * Forward incremental search using ctrl-s is flaky because no keyrelease events are generated for ctrl-s
   we use keypress events instead. As a work around ctrl-shift-r is also bound to forward incremental search.

 * #488177 exceptions occur when using pyreadline on windows 2008 r2

 * #526850 pyreadline causes conhost.exe to crash on windows 7. When pasting long text (>230 characters)
   python crashes. Has been observed on Windows 7 with pyreadline 1.5, not a confirmed problem with pyreadline 1.6 series.
   Workaround is to use the pyreadline paste instead i.e. ctrl-v.
