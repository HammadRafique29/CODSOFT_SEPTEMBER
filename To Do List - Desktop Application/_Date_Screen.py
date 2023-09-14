# Form implementation generated from reading ui file 'date.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt, pyqtSignal, QDate

data = ""

class _Date(object):
    def __init__(self):
        self.date = {"Result":[False, None]}

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(333, 246)
        Form.setStyleSheet("background-color:white;\n"
        "border-radius:10px;\n"
        "border:none;"
        "background-color: transparent;")

        def Date_Selected():
            selected_date = self.calendarWidget.selectedDate()
            selected_date = selected_date.toString(Qt.DateFormat.ISODate)
            print("Inside:" + selected_date)
            self.date = {"Result":[True,selected_date]}
            Form.close()

        self.select_date_btn = QtWidgets.QPushButton(parent=Form)
        self.select_date_btn.setGeometry(QtCore.QRect(180, 210, 101, 31))
        self.select_date_btn.setObjectName("select_date_btn")
        self.select_date_btn.clicked.connect(lambda: Date_Selected())
        self.select_date_btn.setStyleSheet("\n"
        "QPushButton{\n"
        "background-color:#FE603E;\n"
        "border-radius:6px;\n"
        "font-size:11pt;\n"
        "}\n"
        "QPushButton:hover{\n"
        "font-size:13pt;\n"
        "\n"
        "}")
        

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 201))
        self.frame.setStyleSheet("background-color:black;\n"
        "border-radius:10px")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setStyleSheet("border-radius:20px;\n"
        "color:#FE603E;\n"
        "background-color:white;\n"
        "")
        
        def Cancel_date():
            self.date = {"Result":[False, 0]}
            Form.close()

        self.cancel_date_btn = QtWidgets.QPushButton(parent=Form)
        self.cancel_date_btn.setGeometry(QtCore.QRect(70, 210, 101, 31))
        self.cancel_date_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.cancel_date_btn.clicked.connect(lambda: Cancel_date())
        self.cancel_date_btn.setStyleSheet("\n"
        "QPushButton{\n"
        "background-color:#FE603E;\n"
        "border-radius:6px;\n"
        "font-size:11pt;\n"
        "}\n"
        "QPushButton:hover{\n"
        "font-size:13pt;\n"
        "\n"
        "}")
        self.cancel_date_btn.setObjectName("cancel_date_btn")
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 30, 311, 21))
        self.frame_2.setStyleSheet("b")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame.raise_()
        self.select_date_btn.raise_()
        self.cancel_date_btn.raise_()
        self.frame_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.select_date_btn.setText(_translate("Form", "Select"))
        self.cancel_date_btn.setText(_translate("Form", "Cencel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = _Date()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())