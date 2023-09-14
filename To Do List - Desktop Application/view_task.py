# Form implementation generated from reading ui file 'view_task.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from __supporting_func import FrameLess
from PyQt6.QtCore import Qt
from _Date_Screen import _Date
from PyQt6.QtCore import Qt, pyqtSignal, QDate
import time
from threading import Thread



        
              
class _View_Task(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(770, 502)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 770, 502))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/View_Task2.png"))
        self.label.setObjectName("label")
        self.Input_User_Task = QtWidgets.QTextEdit(parent=Form)
        self.Input_User_Task.setGeometry(QtCore.QRect(90, 128, 390, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_User_Task.sizePolicy().hasHeightForWidth())
        self.Input_User_Task.setSizePolicy(sizePolicy)
        self.Input_User_Task.setMinimumSize(QtCore.QSize(390, 25))
        self.Input_User_Task.setMaximumSize(QtCore.QSize(390, 25))
        self.Input_User_Task.setStyleSheet("background-color:transparent;\n"
        "outline:none;\n"
        "border:none;\n"
        "font-size:10pt")
        self.Input_User_Task.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Input_User_Task.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Input_User_Task.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Input_User_Task.setTabChangesFocus(False)
        self.Input_User_Task.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.Input_User_Task.setLineWrapColumnOrWidth(0)
        self.Input_User_Task.setObjectName("Input_User_Task")
        self.select_date_btn = QtWidgets.QPushButton(parent=Form)
        self.select_date_btn.setGeometry(QtCore.QRect(530, 126, 75, 23))
        self.select_date_btn.setStyleSheet("background-color:transparent;\n"
"color:gray;\n"
"font-size:10pt;\n"
"")
        self.select_date_btn.setObjectName("select_date_btn")
        self.timeEdit = QtWidgets.QTimeEdit(parent=Form)
        self.timeEdit.setGeometry(QtCore.QRect(530, 180, 151, 22))
        self.timeEdit.setStyleSheet("background-color:transparent;\n"
"color:gray;\n"
"font-size:10pt;\n"
"border:none;")
        self.timeEdit.setObjectName("timeEdit")
        self.Input_url = QtWidgets.QTextEdit(parent=Form)
        self.Input_url.setGeometry(QtCore.QRect(530, 240, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_url.sizePolicy().hasHeightForWidth())
        self.Input_url.setSizePolicy(sizePolicy)
        self.Input_url.setMinimumSize(QtCore.QSize(150, 25))
        self.Input_url.setMaximumSize(QtCore.QSize(150, 25))
        self.Input_url.setStyleSheet("background-color:transparent;\n"
"outline:none;\n"
"border:none;\n"
"font-size:10pt")
        self.Input_url.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Input_url.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Input_url.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Input_url.setTabChangesFocus(False)
        self.Input_url.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.Input_url.setLineWrapColumnOrWidth(0)
        self.Input_url.setObjectName("Input_url")
        self.cancel_tak_btn_2 = QtWidgets.QPushButton(parent=Form)
        self.cancel_tak_btn_2.setGeometry(QtCore.QRect(307, 437, 91, 30))
        self.cancel_tak_btn_2.setMinimumSize(QtCore.QSize(0, 30))
        self.cancel_tak_btn_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cancel_tak_btn_2.setStyleSheet("background-color:transparent;\n"
"font-size:11pt;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"border-radius:10px;\n"
"\n"
"")
        self.cancel_tak_btn_2.setObjectName("cancel_tak_btn_2")
        self.update_task_btn = QtWidgets.QPushButton(parent=Form)
        self.update_task_btn.setGeometry(QtCore.QRect(423, 437, 91, 30))
        self.update_task_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.update_task_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.update_task_btn.setStyleSheet("background-color:transparent;\n"
"font-size:11pt;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"border-radius:10px;\n"
"\n"
"")
        self.update_task_btn.setObjectName("update_task_btn")
        self.del_task_btn = QtWidgets.QPushButton(parent=Form)
        self.del_task_btn.setGeometry(QtCore.QRect(537, 437, 91, 30))
        self.del_task_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.del_task_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.del_task_btn.setStyleSheet("background-color:transparent;\n"
"font-size:11pt;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"border-radius:10px;\n"
"\n"
"")
        self.del_task_btn.setObjectName("del_task_btn")
        self.complete_task_btn = QtWidgets.QPushButton(parent=Form)
        self.complete_task_btn.setGeometry(QtCore.QRect(653, 437, 91, 30))
        self.complete_task_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.complete_task_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.complete_task_btn.setStyleSheet("background-color:transparent;\n"
"font-size:11pt;\n"
"font-weight:bold;\n"
"font-family:Arial;\n"
"border-radius:10px;\n"
"border: 2px solid transparent;\n"
"    border-image: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"              stop:0 rgba(166, 80, 207, 1),\n"
"              stop:0.25 rgba(255, 71, 79, 1),\n"
"              stop:0.75 rgba(255, 221, 149, 1),\n"
"              stop:1 rgba(90, 208, 251, 1));\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"")
        self.complete_task_btn.setObjectName("complete_task_btn")
        self.Input_User_Task_Des = QtWidgets.QPlainTextEdit(parent=Form)
        self.Input_User_Task_Des.setGeometry(QtCore.QRect(90, 210, 391, 171))
        self.Input_User_Task_Des.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"font-size:9pt")
        self.Input_User_Task_Des.setObjectName("Input_User_Task_Des")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Input_User_Task.setPlaceholderText(_translate("Form", "Enter your task name ..."))
        self.select_date_btn.setText(_translate("Form", "Select Date"))
        self.Input_url.setPlaceholderText(_translate("Form", "Enter your task name ..."))
        self.cancel_tak_btn_2.setText(_translate("Form", "Cancel"))
        self.update_task_btn.setText(_translate("Form", "Update"))
        self.del_task_btn.setText(_translate("Form", "Delete"))
        self.complete_task_btn.setText(_translate("Form", "Complete"))
        self.Input_User_Task_Des.setPlaceholderText(_translate("Form", "Type your task info ..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = _View_Task()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
