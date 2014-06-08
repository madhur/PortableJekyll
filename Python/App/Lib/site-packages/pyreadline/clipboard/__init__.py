import sys
success = True
in_ironpython = u"IronPython" in sys.version
if in_ironpython:
    try:
        from ironpython_clipboard import GetClipboardText, SetClipboardText
    except ImportError:
        from no_clipboard import GetClipboardText, SetClipboardText

else:
    try:
        from win32_clipboard import GetClipboardText, SetClipboardText
    except ImportError:
        from no_clipboard import GetClipboardText, SetClipboardText
    

def send_data(lists):
    SetClipboardText(make_tab(lists))
    

def set_clipboard_text(toclipboard):
    SetClipboardText(str(toclipboard))

def make_tab(lists):
    if hasattr(lists, u"tolist"):
        lists = lists.tolist()
    ut = []
    for rad in lists:
        if type(rad) in [list, tuple]:
            ut.append(u"\t".join([u"%s"%x for x in rad]))
        else:
            ut.append(u"%s"%rad)
    return u"\n".join(ut)            
    
def make_list_of_list(txt):
    def make_num(x):
        try:
            return int(x)
        except ValueError:
            try:
                return float(x)
            except ValueError:
                try:
                    return complex(x)
                except ValueError:
                    return x
        return x                
    ut = []
    flag = False
    for rad in [x for x in txt.split(u"\r\n") if x != u""]:
        raden=[make_num(x) for x in rad.split(u"\t")]
        if str in map(type,raden):
            flag = True
        ut.append(raden)
    return ut, flag


def get_clipboard_text_and_convert(paste_list=False):
    u"""Get txt from clipboard. if paste_list==True the convert tab separated 
    data to list of lists. Enclose list of list in array() if all elements are 
    numeric"""
    txt = GetClipboardText()
    if txt:
        if paste_list and u"\t" in txt:
            array, flag = make_list_of_list(txt)
            if flag:
                txt = repr(array)
            else:
                txt = u"array(%s)"%repr(array)
            txt = u"".join([c for c in txt if c not in u" \t\r\n"])
    return txt

