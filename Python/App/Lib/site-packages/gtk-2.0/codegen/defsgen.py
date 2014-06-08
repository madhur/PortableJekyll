#!/usr/bin/env python
# -*- Mode: Python; py-indent-offset: 4 -*-
#
# Copyright (C) 2006-2009 John Finlay.
#
# Scan the given public .h files of a GTK module (or module using
# GTK object conventions) and generates a set of scheme defs.
#
# defsgen uses the ctypes module to extract information from the installed
# module library (or libraries) to generate the object, interface, function,
# method, virtual, enum and flags defs. defsgen uses the gobject library
# g_type_* functions. defsgen will try to open the "libgobject-2.0.so" library
# if one is not specified on the command line.
#
# Basically the operation of defsgen is:
#
# - open and initialize the gobject and module libraries
# - read each .h file into a buffer which is scrubbed of extraneous data
# - find all *_get_type() functions prototypes
# - look in the module libraries for the get_type symbols
# - if found run the get_type() function to retrieve the GType
# - find the parent type name and save the object info
# - find each function prototypes in the file and check if it has a symbol in
#   the module libraries - save the info if found
# - extract the virtual prototypes from the Class or Iface structs and save
# - write out the various defs.
#
# The command line options are:
#
#   -l --modulelib   Adds the given module library name to the list to be used
#                    for finding symbols. Mor ethan one modulefile may be
#                    specified. (required)
#   -L --libgobject  Specifies the name of the gobject library (optional but
#                    must be specified if "libgobject-2.0.so" is not availble)
#   -s --separate    Create separate files for objects and function/method defs
#                    using the given name as the base name (optional). If this
#                    is not specified the combined object and function defs
#                    will be output to sys.stdout.
#   -f --defsfile    Extract defs from the given file to filter the output defs
#                    that is don't output defs that are defined in the
#                    defsfile. More than one deffile may be specified.
#   -D --defines     Include portions of the defsfile defs that are conditional
#                    on the given define, for example GDK_TARGET_X11. Only
#                    useful with the --defsfile option
#   -m --modulename  The prefix to be stripped from the front of function names
#                    for the given module
#   -p --useprefix   Use the modulename prefix as a hint to split names into
#                    module and name for object and enum defs. Also used for
#                    generating type codes.
#   --onlyenums      Only produce defs for enums and flags
#   --onlyobjdefs    Only produce defs for objects
#   --onlyvirtuals   Only produce defs for virtuals
#   --genpropgetsets Experimental option to generate prop-getset annotations.
#                    Not supported by codegen.py and friends.
#
# Examples:
#
# python defsgen.py -m pango -l libpango-1.0.so \
#            /usr/local/include/pango-1.0/pango/*.h >/tmp/pango.defs
#
# - Outputs all defs for the pango module.using the library module
#   libpango-1.0.so.
#
# python defsgen.py -m gdk -DGDK_TARGET_X11 -l libgdk-x11-2.0.so \
#            -l libgdk_pixbuf-2.0.so -s /tmp/gdk-2.10 \
#            -f /usr/tmp/pygtk/gtk/gdk-base.defs \
#            /usr/local/include/gtk-2.0/gdk/*.h \
#            /usr/local/include/gtk-2.0/gdk-pixbuf/*.h
#
# - Outputs the gdk module defs that are not contained in the defs file
#   /usr/tmp/pygtk/gtk/gdk-base.defs. Two output files are created:
#   /tmp/gdk-2.10-types.defs and /tmp/gdk-2.10.defs.
#
# Based on the original h2def.py program by
# Toby D. Reeves <toby@max.rl.plh.af.mil> and
# modified by James Henstridge <james@daa.com.au> to output stuff in
# Havoc's new defs format.  Info on this format can be seen at:
# http://www.gnome.org/mailing-lists/archives/gtk-devel-list/2000-January/0085.shtml
# Updated to be PEP-8 compatible and refactored to use OOP
# Extensively modified by John Finlay to use ctypes module to extract GType
# info from the given library and to create virtual defines.
#

import getopt
import os
import re, string
import sys
import ctypes
import defsparser

#------------------ utility defs -----------------

_upperstr_pat1 = re.compile(r'([^A-Z])([A-Z])')
_upperstr_pat2 = re.compile(r'([A-Z][A-Z])([A-Z][0-9a-z])')
_upperstr_pat3 = re.compile(r'^([A-Z])([A-Z])')

def to_upper_str(name):
    """Converts a typename to the equivalent uppercase and underscores
    name.  This is used to form the type conversion macros and enum/flag
    name variables"""
    name = _upperstr_pat1.sub(r'\1_\2', name)
    name = _upperstr_pat2.sub(r'\1_\2', name)
    name = _upperstr_pat3.sub(r'\1_\2', name, count=1)
    return name.upper()

def typecode(typename, prefix, use_prefix):
    """create a typecode (eg. GTK_TYPE_WIDGET) from a typename"""
    tcode = to_upper_str(typename)
    if (use_prefix and prefix and tcode.lower() != prefix
        and tcode.lower().startswith(prefix)):
        l = len(prefix)
        tcode = tcode[:l] + '_TYPE' + tcode[l:]
    else:
        tcode = tcode.replace('_', '_TYPE_', 1)
    return tcode

_class_iface_pat = re.compile(r'\w+(Class|Iface)')

def class_iface_sub(mobj):
    '''Returns matched string if it matches a Class or Iface struct
    otherwise returns the empty string'''
    if not _class_iface_pat.match(mobj.group(1)):
        return ''
    return mobj.group(0)

clean_patterns = [
    # strip comments
    (re.compile(r'/\*.*?\*/', re.DOTALL), ''),
    # compact continued lines
    (re.compile(r"\\\n", re.MULTILINE), ''),
    # remove preprocess directives
    (re.compile(r"""^[#].*?$""", re.MULTILINE), ''),
    # strip DECLS macros and Windows DLL API macros
    (re.compile(r"""G_BEGIN_DECLS|BEGIN_LIBGTOP_DECLS|G_END_DECLS|[A-Z]+_API """,
                re.MULTILINE), ''),
    # remove extern "C"
    (re.compile(r'^\s*(extern)\s+"C"\s+{', re.MULTILINE), ''),
    # remove singleline typedefs of stucts
    (re.compile(r'^typedef\s+struct\s*[^{;\n]*;\s*$', re.MULTILINE), ''),
    # remove all struct definitons but those for object classes and interfaces
    (re.compile(r'^struct\s+(\w+)\s+{[^}]+}\s*;\s*$', re.MULTILINE),
     class_iface_sub),
    # compress multiple whitespace
    (re.compile(r'\s+', re.MULTILINE), ' '),
    # clean up line ends
    (re.compile(r';\s*', re.MULTILINE), '\n'),
    (re.compile(r'^\s*', re.MULTILINE), ''),
    # associate *, &, and [] with type instead of variable
    (re.compile(r' \s* ([*|&]+) \s* ([(\w]+)', re.VERBOSE), r'\1 \2'),
    (re.compile(r'\s+ (\w+) \[ \s* \]', re.VERBOSE), r'[] \1'),
    # make return types that are const work.
    (re.compile(r'\s*\*\s*G_CONST_RETURN\s*\*\s*'), '** '),
    (re.compile(r'G_CONST_RETURN |const '), 'const-'),
    # remove typedefs of callback types
    (re.compile(r'^typedef\s+\w+\s*\*?\s*\(\s*\*\s*\w+\)\s*\([^(]*\)\n',
                re.MULTILINE), ''),
    #strip GSEAL macros from the middle of function declarations:
    (re.compile(r"""GSEAL""", re.VERBOSE), '')
    ]

def clean_buffer(buf):
    """Cleans out extraneous data leaving function prototypes, Class and Iface
    structs."""
    for pat, subst in clean_patterns:
        buf = pat.sub(subst, buf)
    return buf

# ------------------ utility classes -------------------------

class ObjDef(object):
    def __init__(self, name, type_id, parent_name, parent_type, base_name):
        self.name = name
        self.type = type_id
        self.parent_name = parent_name
        self.parent_type = parent_type
        self.base_name = base_name
        self.props = []
        return
    def __cmp__(self, other):
        try:
            res = cmp(self.name, other.name)
        except AttributeError:
            res = cmp(id(self), id(other))
        return res
    def set_properties(self, gobj):
        if self.base_name == 'GObject':
            self.props = self._get_gobject_properties(gobj)
        elif self.base_name == 'GInterface':
            self.props = self._get_ginterface_properties(gobj)

    def _get_gobject_properties(self, gobj):
        klass = gobj.g_type_class_ref(self.type)
        num = ctypes.c_uint()
        plist = gobj.g_object_class_list_properties(klass, ctypes.byref(num))
        props = [plist[i][0].name for i in range(num.value)
                 if self.name == gobj.g_type_name(plist[i][0].owner_type)]
        return props
    def _get_ginterface_properties(self, gobj):
        iface = gobj.g_type_default_interface_ref(self.type)
        num = ctypes.c_uint()
        plist = gobj.g_object_interface_list_properties(iface,
                                                        ctypes.byref(num))
        props = [plist[i][0].name for i in range(num.value)]
        return props

# ------------------ Find object definitions -----------------

split_prefix_pat = re.compile('([A-Z]+[a-z]*)([A-Za-z0-9]+)')

get_type_pat = re.compile(r'''^\s*(GType|GtkType)\s+
([a-z]\w+_get_type)\s*(\(void\)|\(\)).*$''', re.VERBOSE | re.MULTILINE)

defkeys = 'GBoxed GInterface GObject gpointer GEnum GFlags'

def find_defs(buf, gobj, modlib, defs):
    """Find possible gobject, gboxed, interface, gpointer, enum and flags
    definitions in header files.and find parent type."""
    #  find all *_get_type() functions that may represent a GObject
    for m in get_type_pat.findall(buf):
        func_name = m[1]
        for lib in modlib:
            if hasattr(lib, func_name):
                objtype = apply(getattr(lib, func_name))
                obj_name = gobj.g_type_name(objtype)
                parent = gobj.g_type_parent(objtype)
                parent_name = gobj.g_type_name(parent)
                base_name = gobj.g_type_name(gobj.g_type_fundamental(parent))
                #if gobj.g_type_is_a(parent, gobj.GObject):
                #    base_name = 'GObject'
                if base_name in defkeys:
                    obj = ObjDef(obj_name, objtype, parent_name, parent,
                                 base_name)
                    obj.set_properties(gobj)
                    defs[obj.base_name].append(obj)
                break
    return

# ------------------ Find function definitions -----------------

arg_split_pat = re.compile("\s*,\s*")

proto_pat=re.compile(r"""^
\s*((?:-|\w|\&|\*)+)  # return type
\s+                   # skip whitespace
([a-z]\w+)\s*[(]      # match the function name until the opening (
\s*(.*?)\s*[)].*      # group the function arguments
$""", re.IGNORECASE|re.VERBOSE|re.MULTILINE)

def find_func_defs(buf, modlib, deffile, defs, verbose):
    '''Find function prototypes in buf that have symbols in modlib
    and save in defs.'''
    funcs = defs['funcs'][deffile] = []
    for m in proto_pat.findall(buf):
        ret, func, args = m
        if not True in [hasattr(lib, func) for lib in modlib]:
            if verbose:
                sys.stderr.write('no symbol for function: ' + func
                                 + ' from file' + deffile + '\n')
        else:
            args = arg_split_pat.split(args)
            args = [a.replace(' ','-', a.count(' ')-1) for a in args]
            funcs.append((func, ret, args))
    return

virtual_pat = re.compile(r'''^
\s*((?:-|\w|\&|\*)+)   # return type
\s*                    # skip whitespace
\(\s*\*\s*             # opening (
([a-z]\w+)\)           # match the function name until the closing )
\s*\(\s*([^)]*)\).*      # group the function arguments
$''', re.VERBOSE|re.MULTILINE)

class_iface_struct_pat = re.compile(
    r'^struct\s+_(\w+)(?:Class|Iface)\s+{([^}]+)}\s*$', re.MULTILINE)

def find_virt_defs(buf, deffile, defs):
    '''Find virtual function prototypes in buf and save in defs.'''
    virts = defs['virts'][deffile] = []
    # get the Class or Iface structs
    for m in class_iface_struct_pat.findall(buf):
        objname, virtuals  = m
        for v in virtual_pat.findall(virtuals):
            ret, func, args = v
            if 'reserved' in func or args == 'void':
                continue
            args = arg_split_pat.split(args)
            args = [a.replace(' ','-', a.count(' ')-1) for a in args]
            virts.append((func, ret, args, objname))
    return

enum_pat = re.compile(r'^\s*typedef enum\s+{\s*([^}]*)}\s*([^\s]*)$',
                      re.MULTILINE)
values_splitter = re.compile(r'\s*,\s', re.MULTILINE)

def find_enums(buf, defs):
    for vals, name in enum_pat.findall(buf):
        if name != 'GdkCursorType':
            isflags = '<<' in vals
            entries = [val.split()[0] for val in values_splitter.split(vals)
                       if val.strip()]
            if entries:
                defs['untypedenums'][name] = (isflags, entries)
    return

# ------------------ write definitions -----------------

type_pat = re.compile(r'(?:const-)?([A-Za-z0-9]+)\*?\s+')
pointer_pat = re.compile('(.*)\*$')
func_new_pat = re.compile('(\w+)_new$')
getset_pat = re.compile(r'^(?:get|set)_(.*)$')

def split_prefix(cname, prefix, use_prefix):
    # use the module prefix to split the cname
    pre = prefix.replace('_', '')
    if use_prefix and cname.lower().startswith(pre):
        l = len(pre)
        module = cname[:l]
        name = cname[l:]
    else:
        m = split_prefix_pat.match(cname)
        if m:
            module = m.group(1)
            name = m.group(2)
    return module, name

class DefsWriter:
    def __init__(self, defs, fp=None, prefix=None, verbose=False,
                 defsfiles=None, defines={}, genpropgetsets=False,
                 useprefix=False):
        self.defs = defs
        self.use_prefix = useprefix
        self.objnames = reduce(list.__add__,
                               [[o.name for o in defs[base]]
                                for base in defkeys.split()[:3]])
        self.othernames = reduce(list.__add__,
                                 [[o.name for o in defs[base]]
                                  for base in defkeys.split()[3:]])
        self.objifacedefs = dict(reduce(list.__add__,
                                       [[(o.name, o) for o in defs[base]]
                                        for base in defkeys.split()[1:3]]))
        self.fp = (fp, sys.stdout)[not fp]
        self.prefix = prefix
        self.verbose = verbose
        self.genpropgetsets = genpropgetsets
        self._c_names={}
        for defsfile in defsfiles:
            filter = defsparser.DefsParser(defsfile, defines)
            filter.startParsing()
            self._c_names.update(filter.c_name)
            for vdef in filter.virtuals:
                self._c_names[vdef.of_object + '.' + vdef.name] = None
        return

    def write_func_defs(self, deffiles, onlyvirts=False):
        filter = self._c_names
        for deffile in deffiles:
            self.fp.write('\n;; From %s\n\n' % os.path.basename(deffile))
            if not onlyvirts:
                for func, ret, args in self.defs['funcs'][deffile]:
                    if not func in filter:
                        self._write_func(func, ret, args)
            for virt, ret, args, objname in self.defs['virts'][deffile]:
                if not objname + '.' + virt in filter:
                    self._write_virt(objname, virt, ret, args)
            self.fp.write('\n')
        return

    def write_enum_defs(self, fp=None):
        fp = (fp, self.fp)[not fp]
        klassptrs = {'GEnum':ctypes.POINTER(EnumClass),
                    'GFlags':ctypes.POINTER(FlagsClass)}
        filter = self._c_names
        objs = self.defs['GEnum'] + self.defs ['GFlags']
        #objs.sort()
        fp.write(';; Enumerations and Flags ...\n\n')
        for obj in objs:
            cname = name = obj.name
            tcode = typecode(cname, self.prefix, self.use_prefix)
            if cname in filter:
                continue
            if cname in self.defs['untypedenums']:
                if tcode not in self.defs['typedefines']:
                    # no type define so skip and print as untyped enum
                    continue
                self.defs['untypedenums'].pop(cname, None)
            parent_name = obj.parent_name
            klassptr = klassptrs[parent_name]
            typename = parent_name.lower()[1:]
            module = None
            module, name = split_prefix(cname, self.prefix, self.use_prefix)
            fp.write('(define-' + typename + ' ' + name + '\n')
            if module:
                fp.write('  (in-module "' + module + '")\n')
            fp.write('  (c-name "' + cname + '")\n')
            fp.write('  (gtype-id "' + tcode + '")\n')
            fp.write('  (values\n')
            classref = self.gobj.g_type_class_ref(obj.type)
            itemclass = ctypes.cast(classref, klassptr).contents
            for i in range(itemclass.n_values):
                val = itemclass.values[i]
                fp.write('    \'("%s" "%s")\n' % (val.value_nick,
                                                  val.value_name))
            fp.write('  )\n')
            fp.write(')\n\n')
        if self.defs['untypedenums']:
            self.write_untyped_enum_defs(fp)
        return

    def write_untyped_enum_defs(self, fp):
        fp.write(';; Untyped enumerations and flags ...\n\n')
        filter = self._c_names
        for cname, (isflags, entries) in self.defs['untypedenums'].items():
            if filter and cname in filter: continue
            module, name = split_prefix(cname, self.prefix, self.use_prefix)
            if isflags:
                fp.write('(define-flags ' + name + '\n')
            else:
                fp.write('(define-enum ' + name + '\n')
            if module:
                fp.write('  (in-module "' + module + '")\n')
            fp.write('  (c-name "' + cname + '")\n')
            preindex = entries[0].rfind('_')
            for ent in entries[1:]:
                while (preindex > 0
                       and ent[:preindex] != entries[0][:preindex]):
                    preindex = ent[:preindex].rfind('_')
            fp.write('  (values\n')
            for ent in entries:
                fp.write('    \'("%s" "%s")\n' %
                         (ent[preindex+1:].lower().replace('_', '-'), ent))
            fp.write('  )\n')
            fp.write(')\n\n')
        

    def _write_obj_helper(self, obj, fp):
        base_name = obj.base_name.lower()[1:]
        cmodule = None
        cname = name = obj.name
        type_id = obj.type
        parent_name = obj.parent_name
        cmodule, name = split_prefix(cname, self.prefix, self.use_prefix)
        fp.write('(define-' + base_name + ' ' + name + '\n')
        if cmodule:
            fp.write('  (in-module "' + cmodule + '")\n')
        if base_name == 'object':
            fp.write('  (parent "' + parent_name + '")\n')
        fp.write('  (c-name "' + cname + '")\n')
        fp.write('  (gtype-id "'
                 + typecode(cname, self.prefix, self.use_prefix) + '")\n')
        n = ctypes.c_uint()
        ifaces = self.gobj.g_type_interfaces(type_id, ctypes.byref(n))
        for i in range(n.value):
            iface_name = self.gobj.g_type_name(ifaces[i])
            if iface_name in self.interfaces:
                fp.write('  (implements "%s")\n' % iface_name)
        if base_name == 'interface':
            prereq = self.gobj.g_type_interface_prerequisites(type_id,
                                                              ctypes.byref(n))
            for i in range(n.value):
                fp.write('  (prerequisite "%s")\n'
                         % self.gobj.g_type_name(prereq[i]))
        # should do something about accessible fields
        fp.write(')\n\n')
        return

    def write_obj_defs(self, fp=None):
        fp = (fp, self.fp)[not fp]
        fp.write(';; -*- scheme -*-\n')
        filter = self._c_names
        for base in defkeys.split()[:4]:
            base_name = base.lower()[1:]
            fp.write('; %s definitions ...\n\n' % base_name)
            for obj in self.defs[base]:
                if not obj.name in filter:
                    self._write_obj_helper(obj, fp)
        return

    def _write_func(self, name, ret, args):
        if len(args) >= 1:
            # methods must have at least one argument
            munged_name = name.replace('_', '')
            m = type_pat.match(args[0])
            if m:
                obj = m.group(1)
                if munged_name.startswith(obj.lower()):
                    if obj not in self.othernames:
                        self._write_method(obj, name, ret, args)
                        return
        fname = name
        if self.prefix:
            fname = re.sub('^'+self.prefix+'_', '', fname)

        # it is either a constructor or normal function
        self.fp.write('(define-function ' + fname + '\n')
        self.fp.write('  (c-name "' + name + '")\n')

        # Asume that a constructor function name
        # ends with '_new' and it returns an object pointer.
        m = func_new_pat.match(name)
        r = pointer_pat.match(ret)
        if m and r:
            cname = ''
            # get the type name by using the _get_type function
            func = m.group(1) + '_get_type'
            lib = [l for l in self.modlib if hasattr(l, func)]
            if lib:
                cname = self.gobj.g_type_name(apply(getattr(lib[0], func)))
            if cname and self.gobj.g_type_from_name(r.group(1)):
                self.fp.write('  (is-constructor-of "' + cname + '")\n')
        self._write_return(ret)
        self._write_arguments(args)
        return

    def _write_method(self, obj, name, ret, args):
        regex = ''.join([c+'_?' for c in obj.lower()])
        mname, count = re.subn(regex, '', name, 1)
        if not count and self.prefix:
            mname = re.sub('^'+self.prefix+'_', '', mname)
        self.fp.write('(define-method ' + mname + '\n')
        self.fp.write('  (of-object "' + obj + '")\n')
        self.fp.write('  (c-name "' + name + '")\n')
        m = getset_pat.match(mname)
        if self.genpropgetsets and m and len(args[1:]) <= 1:
            prop = m.group(1)
            if obj in self.objifacedefs:
                oidef = self.objifacedefs[obj]
                if prop.replace('_', '-') in oidef.props:
                    self.fp.write('  (prop-getset "' + prop + '")\n')
        self._write_return(ret)
        self._write_arguments(args[1:])
        return

    def _write_virt(self, obj, name, ret, args):
        self.fp.write('(define-virtual ' + name + '\n')
        self.fp.write('  (of-object "' + obj + '")\n')
        self._write_return(ret)
        self._write_arguments(args[1:])
        return

    def _write_return(self, ret):
        if ret == 'void':
            ret = 'none'
        self.fp.write('  (return-type "' + ret + '")\n')
        return

    def _write_arguments(self, args):
        if args and not 'void' in args:
            varargs = ''
            self.fp.write('  (parameters\n')
            for arg in args:
                if arg == '...':
                    varargs = '  (varargs #t)\n'
                else:
                    tupleArg = tuple(arg.split())
                    if len(tupleArg) == 2:
                        self.fp.write('    \'("%s" "%s")\n' % tupleArg)
            self.fp.write('  )\n' + varargs)
        self.fp.write(')\n\n')

# ---------- ctypes support classes for gobject library functions ----------

GType = ctypes.c_uint

class GTypeClass(ctypes.Structure):
    _fields_ = [('g_type', GType)]

class GTypeInstance(ctypes.Structure):
    _fields_ = [('g_class', ctypes.POINTER(GTypeClass))]

class EnumValue(ctypes.Structure):
    _fields_ = [('value', ctypes.c_int),
                ('value_name', ctypes.c_char_p),
                ('value_nick', ctypes.c_char_p)]

class FlagsValue(ctypes.Structure):
    _fields_ = [('value', ctypes.c_uint),
                ('value_name', ctypes.c_char_p),
                ('value_nick', ctypes.c_char_p)]

class EnumClass(ctypes.Structure):
    _fields_ = [('g_type_class',  GTypeClass),
                ('minimum', ctypes.c_int),
                ('maximum', ctypes.c_int),
                ('n_values', ctypes.c_uint),
                ('values', ctypes.POINTER(EnumValue))]

class FlagsClass(ctypes.Structure):
    _fields_ = [('g_type_class', GTypeClass),
               ('mask', ctypes.c_uint),
               ('n_values', ctypes.c_uint),
               ('values', ctypes.POINTER(FlagsValue))]

class GTypeInterface(ctypes.Structure):
    _fields_ = [('g_type', GType),
                ('g_instance_type', GType)]

class GParamSpec(ctypes.Structure):
    _fields_ = [('g_type_instance', GTypeInstance),
                ('name', ctypes.c_char_p),
                ('flags', ctypes.c_uint),
                ('value_type', GType),
                ('owner_type', GType)]

# ------------------ Main function -----------------

def main(args):
    verbose = False
    all = True
    onlyenums = False
    onlyobjdefs = False
    onlyvirtuals = False
    separate = False
    modulename = None
    defsfiles = []
    libgobject = None
    modulelibs = []
    defines = {}
    genpropgetsets = False
    use_prefix = False
    opts, args = getopt.getopt(args[1:], 'vs:m:f:D:L:l:p',
                               ['onlyenums', 'onlyobjdefs', 'onlyvirtuals',
                                'modulename=', 'separate=',
                                'defsfile=', 'defines=', 'genpropgetsets',
                                'libgobject-', 'modulelib=', 'useprefix'])
    for o, v in opts:
        if o == '-v':
            verbose = True
        if o == '--onlyenums':
            onlyenums = True
            all = False
        if o == '--onlyvirtuals':
            onlyvirtuals = True
            all = False
        if o == '--onlyobjdefs':
            onlyobjdefs = True
            all = False
        if o in ('-p', '--useprefix'):
            use_prefix = True
        if o == '--genpropgetsets':
            genpropgetsets = True
        if o in ('-s', '--separate'):
            separate = v
        if o in ('-m', '--modulename'):
            modulename = v
        if o in ('-L', '--libgobject'):
            libgobject = v
        if o in ('-l', '--modulelib'):
            modulelibs.append(v)
        if o in ('-f', '--defsfile'):
            defsfiles.append(v)
        if o in ('-D', '--defines'):
            nameval = v.split('=')
            try:
                defines[nameval[0]] = nameval[1]
            except IndexError:
                defines[nameval[0]] = None

    if not args[0:1]:
        print 'Must specify at least one input file name'
        return -1
    if not modulelibs:
        print 'Must specify one or more modulelib names'
        return -1

    # load the gobject and module libraries and init the gtype system
    if not libgobject:
        if verbose:
            sys.stderr.write('Using "libgobject-2.0.so" as the libobject' \
                             'library name by default\n')
        gobj = ctypes.cdll.LoadLibrary('libgobject-2.0.so')
    else:
        gobj = ctypes.cdll.LoadLibrary(libgobject)

    modlib = [ctypes.cdll.LoadLibrary(lib) for lib in modulelibs]

    gobj.g_type_init()
    gobj.g_type_name.restype = ctypes.c_char_p
    gobj.g_type_from_name.argtypes = [ctypes.c_char_p]
    gobj.g_type_interfaces.restype = ctypes.POINTER(ctypes.c_int)
    gobj.g_type_interface_prerequisites.restype = ctypes.POINTER(ctypes.c_int)
    gobj.g_object_class_list_properties.restype = ctypes.POINTER(ctypes.POINTER(GParamSpec))
    gobj.g_object_interface_list_properties.restype = ctypes.POINTER(ctypes.POINTER(GParamSpec))
    gobj.GObject = gobj.g_type_from_name('GObject')
    gobj.g_object_new(gobj.GObject, None)

    defs = {}
    for key in defkeys.split():
        defs[key] = []
    defs['funcs'] = {}
    defs['virts'] = {}
    defs['untypedenums'] = {}
    defs['typedefines'] = []

    # read in all the object and function definitions
    args.sort()
    type_define_pat = re.compile(
        r'^#define\s+([A-Z]\S+_TYPE_\S+)\s+.*[a-z]\w+_get_type.*$',
        re.MULTILINE)
    for filename in args:
        buf = open(filename).read()
        defs['typedefines'] += type_define_pat.findall(buf)
        buf = clean_buffer(buf)
        find_enums(buf, defs)
        find_defs(buf, gobj, modlib, defs)
        find_func_defs(buf, modlib, filename, defs, verbose)
        find_virt_defs(buf, filename, defs)

    for key in defkeys.split():
        defs[key].sort()

    methods = types = None
    if separate:
        methods = file(separate + '.defs', 'w')
        types = file(separate + '-types.defs', 'w')

    dw = DefsWriter(defs, methods, prefix=modulename, verbose=verbose,
                    defsfiles=defsfiles, defines=defines,
                    genpropgetsets=genpropgetsets, useprefix=use_prefix)
    dw.interfaces = [i.name for i in defs['GInterface']]
    dw.gobj = gobj
    dw.modlib = modlib

    if onlyobjdefs or all:
        dw.write_obj_defs(types)
        if separate:
            print "Wrote object defs to %s-types.defs" % separate
    if onlyenums or all:
        dw.write_enum_defs(types)
        if separate:
            print "Wrote enum and flags defs to %s-types.defs" % separate
    if onlyvirtuals or all:
        dw.write_func_defs(args, onlyvirtuals)
        if separate:
            print "Wrote function and virtual defs to %s.defs" % separate

if __name__ == '__main__':
    sys.exit(main(sys.argv))
