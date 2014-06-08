
Usage
=====

The purpose of readline is to improve the interactive experience with the
python interpreter by improving the line editing facilities. The most important
being tab completion and copy and paste.

Configuration file
------------------

The configuration file is read from the users home directory and is named
pyreadlineconfig.ini. The files syntax is not the same as for GNU readline but
a python syntax is used instead. The available commands are:


    bind_exit_key
      is used to bind the keys that are used to exit the interpreter. (Ctrl-d,
      ctrl-z)

    bind_key
      is used to bind keys to editor functions

    un_bind_key
      is used to unbind keys can be useful to unbind default bindings the user
      does not like

    bell_style
      is used to set bell style. (none|visible|audible)

    show_all_if_ambiguous
      is used to enable the showing of a list of all alternative for tab
      completion (on|off)

    mark_directories
      show directories (on|off)

    completer_delims
      Which delimeters should be used to separate words for tab completion

    debug_output
      Turn on debug output (on|off). Not implemented yet.

    disable_readline
      Disable pyreadline completely (True|False).

    allow_ctrl_c
      Allows use of ctrl-c as copy key, still propagate keyboardinterrupt when not waiting for input.

    ctrl_c_tap_time_interval
      Set the ctrl-c double tap time interval to be used before issuing a KeyboadInterupt. Used
      to be able to have ctrl-c bound to copy.

    history_filename
      Set name of history file. Default is %USERPROFILE%/.pythonhistory

    history_length
      Set max length of history file default 200
      
      
    

Here is the example config file shipped with pyreadline:

.. literalinclude:: ../../pyreadline/configuration/pyreadlineconfig.ini

pyreadline with python interpreter
----------------------------------

In your startup file (pointed to by environment variable PYTHONSTARTUP) add:

.. literalinclude:: ../../pyreadline/configuration/startup.py

This file is included in the doc directory of the distribution.

pyreadline with IronPython
--------------------------

*THIS HAS NOT BEEN TESTED FOR A WHILE*

Pyreadline can be used together with IronPython. Unfortunately the binary
installs of IronPython can not run pyreadline directly. You need to patch the
source code to make PythonCommandLine a public class that we can override.

* In PythonCommandLine.cs you need to change class PythonCommandLine to public class PythonCommandLine and recompile.

* Copy rlcompleter.py from a standard python install to your ironpython path (this file is not included with fepy).


pyreadline with IPython
-----------------------

In IPython pyreadline is automatically used if available.

Clipboard
---------

Pyreadline can do copy/paste using the clipboard. Selections can be done using
shift and arrowkeys as in most windows programs.

There are three different paste functions that can be bound.


    paste
      Paste windows clipboard. Assume single line strip other lines and end of
      line markers and trailing spaces

    paste_mulitline_code
      Paste windows clipboard as multiline code. Removes any empty lines in the
      code

    ipython_paste
      Paste windows clipboard. If enable_ipython_paste_list_of_lists is True
      then try to convert tabseparated data to repr of list of lists or repr of
      array. If enable_ipython_paste_for_paths==True then change \\\\ to / and
      spaces to \\space.


International characters
------------------------

The pyreadline package now supports international characters. However using
international characters in the interactive prompt can be annoying on windows
since the default codepage for the terminal is an ascii codepage (850 on
swedish systems) but the filesystem often uses some other codepage (1252 on
swedish systems). This means the filenames containing internationl characters
entered on interactive prompt will not work. The workaround here is to change
the codepage of your terminal to a more suitable one using the :command:`chcp`
command. For swedish systems :command:`chcp 1252` does the trick but you also
have to change the terminal font to `lucida console` using the properties
dialog for the console.



