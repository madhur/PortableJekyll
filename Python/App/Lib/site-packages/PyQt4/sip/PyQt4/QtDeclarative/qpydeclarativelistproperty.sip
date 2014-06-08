// This is the SIP specification of the QDeclarativeListProperty mapped type.
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


%MappedType QDeclarativeListProperty<QObject> /DocType="QPyDeclarativeListProperty"/
{
%TypeHeaderCode
#include <QDeclarativeListProperty>
%End

%TypeCode
#if defined(SIP_USE_PYCAPSULE)
extern "C" {
static void qpydeclarative_QPyDeclarativeListProperty_delete(PyObject *capsule)
{
    delete reinterpret_cast<QDeclarativeListProperty<QObject> *>(PyCapsule_GetPointer(capsule, 0));
}
}
#else
extern "C" {
static void qpydeclarative_QPyDeclarativeListProperty_delete(void *ptr)
{
    delete reinterpret_cast<QDeclarativeListProperty<QObject> *>(ptr);
}
}
#endif
%End

%ConvertFromTypeCode
#if defined(SIP_USE_PYCAPSULE)
    return PyCapsule_New(sipCpp, 0,
            qpydeclarative_QPyDeclarativeListProperty_delete);
#else
    return PyCObject_FromVoidPtr(sipCpp,
            qpydeclarative_QPyDeclarativeListProperty_delete);
#endif
%End

%ConvertToTypeCode
    if (sipIsErr == NULL)
    {
#if defined(SIP_USE_PYCAPSULE)
        return PyCapsule_CheckExact(sipPy);
#else
        return PyCObject_Check(sipPy);
#endif
    }

#if defined(SIP_USE_PYCAPSULE)
    *sipCppPtr = reinterpret_cast<QDeclarativeListProperty<QObject> *>(
            PyCapsule_GetPointer(sipPy, 0));
#else
    *sipCppPtr = reinterpret_cast<QDeclarativeListProperty<QObject> *>(
            PyCObject_AsVoidPtr(sipPy));
#endif

    // It isn't a temporary copy.
    return 0;
%End
};
