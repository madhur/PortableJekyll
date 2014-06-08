// This is the SIP interface definition for QAxWidget.
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

class QAxWidget : QWidget, QAxBase /PyQt4NoQMetaObject/
{
%TypeHeaderCode
#include <qaxwidget.h>
%End

public:
    QAxWidget(QWidget *parent /TransferThis/ = 0, Qt::WFlags flags = 0);
    QAxWidget(const QString &, QWidget *parent /TransferThis/ = 0,
            Qt::WFlags flags = 0);
    //QAxWidget(IUnknown *, QWidget *parent /TransferThis/ = 0, Qt::WFlags flags = 0);
    ~QAxWidget();

    void clear();
    bool doVerb(const QString &);

    QSize sizeHint() const;
    QSize minimumSizeHint() const;

    //virtual QaxAggregated *createAggregate();

protected:
    //bool initialize(IUnknown **);
    virtual bool createHostWindow(bool);

    void changeEvent(QEvent *);
    void resizeEvent(QResizeEvent *);

    virtual bool translateKeyEvent(int,int) const;

%If (Qt_5_0_0 -)
    void connectNotify(const QMetaMethod &);
%End
%If (- Qt_5_0_0)
    void connectNotify(const char *);
%End
};

%End
