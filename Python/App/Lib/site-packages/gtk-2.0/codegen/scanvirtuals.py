#!/usr/bin/env python
import re
import sys


def main():
    rx = re.compile(r'^\s*([\w\s\*]+)\(\s*\*\s*(\w+)\s*\)\s*\(([^()]*)\);',
                    re.DOTALL|re.MULTILINE)
    for f in sys.argv[1:]:
        #print ";; From", f
        buf = file(f).read()
        for m in rx.findall(buf):
            return_type =  m[0].strip()
            if 'typedef' in return_type:
                continue
            if return_type == 'void':
                return_type = 'none'
            return_type = return_type.replace(' ', '')
            virtual_name =  m[1]
            if 'reserved' in virtual_name:
                continue
            params = []
            if not m[2]:
                print >> sys.stderr, repr(m)
                continue
            for param in map(str.strip, m[2].split(',')):
                if '*' in param:
                    tokens = param.split('*')
                    ptype = tokens[0].strip() + '*'*(len(tokens) - 1)
                    pname = tokens[-1].strip()
                else:
                    if param == 'void':
                        continue
                    ptype, pname = map(str.strip, param.split())
                ptype = ptype.replace('const ', 'const-')
                while '[]' in pname:
                    pname = pname.replace('[]', '')
                    ptype += '[]'
                params.append((ptype, pname))
            if not params:
                continue
            objname = params[0][0].replace('*', '')
            print '(define-virtual', virtual_name
            print '  (of-object "%s")' % objname
            print '  (return-type "%s")' % return_type
            if len(params) > 1:
                print '  (parameters'
                for param in params[1:]:
                    print '    \'("%s" "%s")' % param
                print '  )'
            print ')'

if __name__ == '__main__':
    main()
