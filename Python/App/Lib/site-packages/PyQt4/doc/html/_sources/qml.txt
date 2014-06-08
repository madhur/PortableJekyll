Integrating Python and QML
==========================

Qt v4.7 introduced QML as a means of declaratively describing a user interface
and using JavaScript as a scripting language within QML.  It is possible to
write complete standalone QML applications, or to combine them with C++.

PyQt4 supports the integration of Python and QML as far as it can - given the
limitations of the QML implementation.

There are three types of QML application:

- *Pure* applications that are written entirely in QML and can be run using the
  :program:`qmlviewer` tool provided with Qt.  PyQt4 fully supports this type
  of application.  The examples provided by :program:`qtdemo.py` under the *Qt
  Declarative Examples* heading are all of this type.

- QML allows ``QObject`` instances to be used in QML applications.  QML code is
  able to call an object's slots and has read and write access to the object's
  properties.  QML code can also respond to changes to the value of a property.
  PyQt4 fully supports the use objects created in Python in this way.  The
  :program:`minehunt.py` example under the *Demonstrations* heading of
  :program:`qtdemo.py` is an example of this type of application.

- QML also allows ``QObject`` sub-classes to be used in QML applications so
  that new instances are created from QML.  PyQt4 does not support this.  The
  reason is that QML uses information generated at compile time (specifically
  it uses ``QObject::staticMetaObject``) rather than information created
  dynamically at run time (i.e. ``QObject::metaObject()``).  This approach is
  fine for a static language like C++ but causes problems for languages such as
  Python that allow types to created dynamically.  This limitation doesn't
  place any restriction on the functionality of a Python/QML application, it
  only places restrictions on how that application is written.


QML can implement JavaScript functions and define signals.  PyQt4 allows both
of these to be accessed transparently from Python.  The following is a simple
example application that displays the current date and time when the user
clicks on it.

The following is the QML (in the :file:`message.qml`) that defines the user
interface::

    import Qt 4.7
 
    Rectangle {
        signal messageRequired;
 
        function updateMessage(text) {
            messageText.text = text
        }
 
        anchors.fill: parent; color: "black"
 
        Text {
            id: messageText
            anchors.centerIn: parent; color: "white"
        }
 
        MouseArea {
            anchors.fill: parent
            onClicked: messageRequired()
        }
    }

This defines a signal ``messageRequired`` which is emitted when the user clicks
on the mouse area.  It also implements a function ``updateMessage()`` which
updates the message being displayed.

The following is the Python code that implements the application logic::

    import sys

    from PyQt4.QtCore import QDateTime, QObject, QUrl, pyqtSignal
    from PyQt4.QtGui import QApplication
    from PyQt4.QtDeclarative import QDeclarativeView


    # This class will emit the current date and time as a signal when
    # requested.
    class Now(QObject):

        now = pyqtSignal(str)

        def emit_now(self):
            formatted_date = QDateTime.currentDateTime().toString()
            self.now.emit(formatted_date)


    app = QApplication(sys.argv)

    now = Now()

    # Create the QML user interface.
    view = QDeclarativeView()
    view.setSource(QUrl('message.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

    # Get the root object of the user interface.  It defines a
    # 'messageRequired' signal and JavaScript 'updateMessage' function.  Both
    # can be accessed transparently from Python.
    rootObject = view.rootObject()

    # Provide the current date and time when requested by the user interface.
    rootObject.messageRequired.connect(now.emit_now)

    # Update the user interface with the current date and time.
    now.now.connect(rootObject.updateMessage)

    # Provide an initial message as a prompt.
    rootObject.updateMessage("Click to get the current date and time")

    # Display the user interface and allow the user to interact with it.
    view.setGeometry(100, 100, 400, 240)
    view.show()

    app.exec_()

Hopefully the comments in the code are sufficient explanation.  The important
things to note are that the signal and JavaScript function appear as
appropriate attributes of the root object ``QDeclarativeItem`` returned by the
``rootObject()`` method of ``QDeclarativeView`` and can be connected to and
called respectively.
