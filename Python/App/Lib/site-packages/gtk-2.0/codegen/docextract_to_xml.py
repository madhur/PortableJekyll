#!/usr/bin/env python
# -*- Mode: Python; py-indent-offset: 4 -*-
#
# This litte script outputs the C doc comments to an XML format.
# So far it's only used by gtkmm (The C++ bindings). Murray Cumming.
# Usage example:
# # ./docextract_to_xml.py -s /gnome/head/cvs/gtk+/gtk/ -s /gnome/head/cvs/gtk+/docs/reference/gtk/tmpl/ > gtk_docs.xml

import getopt
import re
import string
import sys

import docextract

def usage():
    sys.stderr.write('usage: docextract_to_xml.py ' +
        '[-s /src/dir | --source-dir=/src/dir] ' +
        '[-a | --with-annotations] [-p | --with-properties] ' +
        '[-i | --with-signals ]\n')
    sys.exit(1)

# Translates special texts to &... HTML acceptable format.  Also replace
# occurrences of '/*' and '*/' with '/ *' and '* /' respectively to avoid
# comment errors (note the spaces).  Some function descriptions include C++
# multi-line comments which cause errors when the description is included in a
# C++ Doxygen comment block.
def escape_text(unescaped_text):
    # Escape every "&" not part of an entity reference
    escaped_text = re.sub(r'&(?![A-Za-z]+;)', '&amp;', unescaped_text)

    # These weird entities turn up in the output...
    escaped_text = string.replace(escaped_text, '&mdash;', '&#8212;')
    escaped_text = string.replace(escaped_text, '&ast;', '*')
    escaped_text = string.replace(escaped_text, '&percnt;', '%')
    escaped_text = string.replace(escaped_text, '&commat;', '@')
    escaped_text = string.replace(escaped_text, '&num;', '&#35;')
    escaped_text = string.replace(escaped_text, '&nbsp;', '&#160;')
    # This represents a '/' before or after an '*' so replace with slash but
    # with spaces.
    escaped_text = string.replace(escaped_text, '&sol;', ' / ')

    # Escape for both tag contents and attribute values
    escaped_text = string.replace(escaped_text, '<', '&lt;')
    escaped_text = string.replace(escaped_text, '>', '&gt;')
    escaped_text = string.replace(escaped_text, '"', '&quot;')

    # Replace C++ comment begin and ends to ones that don't affect Doxygen.
    escaped_text = string.replace(escaped_text, '/*', '/ *')
    escaped_text = string.replace(escaped_text, '*/', '* /')

    return escaped_text

def print_annotations(annotations):
    for annotation in annotations:
        print "<annotation name=" + annotation[0] +  ">" + \
                escape_text(annotation[1]) + "</annotation>"

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:s:o:api",
                                   ["source-dir=", "with-annotations",
                                     "with-properties", "with-signals"])
    except getopt.error, e:
        sys.stderr.write('docextract_to_xml.py: %s\n' % e)
        usage()
    source_dirs = []
    with_annotations = False
    with_signals = False
    with_properties = False
    for opt, arg in opts:
        if opt in ('-s', '--source-dir'):
            source_dirs.append(arg)
        if opt in ('-a', '--with-annotations'):
            with_annotations = True
        if opt in ('-p', '--with-properties'):
            with_properties = True
        if opt in ('-i', '--with-signals'):
            with_signals = True
    if len(args) != 0:
        usage()

    docs = docextract.extract(source_dirs);
    docextract.extract_tmpl(source_dirs, docs); #Try the tmpl sgml files too.

    # print d.docs

    if docs:

        print "<root>"

        for name, value in sorted(docs.items()):
            # Get the type of comment block ('function', 'signal' or
            # 'property') (the value is a GtkDoc).
            block_type = value.get_type()

            # Skip signals if the option was not specified.
            if block_type == 'signal' and not with_signals:
                continue
            # Likewise for properties.
            elif block_type == 'property' and not with_properties:
                continue

            print "<" + block_type + " name=\"" + escape_text(name) + "\">"

            print "<description>"
            print escape_text(value.get_description())
            print "</description>"

            # Loop through the parameters if not dealing with a property:
            if block_type != 'property':
                print "<parameters>"
                for name, description, annotations in value.params:
                        print "<parameter name=\"" + escape_text(name) + "\">"
                        print "<parameter_description>" + escape_text(description) + "</parameter_description>"

                        if with_annotations:
                            print_annotations(annotations)

                        print "</parameter>"

                print "</parameters>"

                # Show the return-type (also if not dealing with a property):
                if with_annotations:
                    print "<return>"
                    print "<return_description>" + escape_text(value.ret[0]) + \
                            "</return_description>"
                    print_annotations(value.ret[1])
                    print "</return>"
                else:
                    print "<return>" + escape_text(value.ret[0]) + "</return>"

            if with_annotations:
                print_annotations(value.get_annotations())

            print "</" + block_type + ">\n"

        print "</root>"
