// This is the SIP interface definition for QAxObject.
//
// Copyright (c) 2013 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt.
// 
// This file may be used under the terms of the GNU General Public
// License versions 2.0 or 3.0 as published by the Free Software
// Foundation and appearing in the files LICENSE.GPL2 and LICENSE.GPL3
// included in the packaging of this file.  Alternatively you may (at
// your option) use any later version of the GNU General Public
// License if such license has been publicly approved by Riverbank
// Computing Limited (or its successors, if any) and the KDE Free Qt
// Foundation. In addition, as a special exception, Riverbank gives you
// certain additional rights. These rights are described in the Riverbank
// GPL Exception version 1.1, which can be found in the file
// GPL_EXCEPTION.txt in this package.
// 
// If you are unsure which license is appropriate for your use, please
// contact the sales department at sales@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


%If (WS_WIN)

class QAxObject : QObject, QAxBase /PyQt4NoQMetaObject/
{
%TypeHeaderCode
#include <qaxobject.h>
%End

public:
    QAxObject(QObject *parent /TransferThis/ = 0);
    QAxObject(const QString &, QObject *parent /TransferThis/ = 0);
    //QAxObject(IUnknown *, QObject *parent /TransferThis/ = 0);
    ~QAxObject();

%ConvertToSubClassCode
    static struct class_graph {
        const char *name;
        sipWrapperType **type;
        int yes, no;
    } graph[] = {
        {sipName_QAxObject, &sipClass_QAxObject,    1, -1},
        {sipName_QAxWidget, &sipClass_QAxWidget,    -1, -1},
    };

    int i = 0;

    sipClass = NULL;

    do
    {
        struct class_graph *cg = &graph[i];

        if (cg->name != NULL && sipCpp->inherits(cg->name))
        {
            sipClass = *cg->type;
            i = cg->yes;
        }
        else
            i = cg->no;
    }
    while (i >= 0);
%End

    bool doVerb(const QString &);

protected:
%If (Qt_5_0_0 -)
    void connectNotify(const QMetaMethod &);
%End
%If (- Qt_5_0_0)
    void connectNotify(const char *);
%End
};

%End
