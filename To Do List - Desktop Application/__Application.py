import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from _Dashboard_Screen import Ui_MainWindow 
from _Date_Screen import _Date
from PyQt6.QtCore import Qt
from __supporting_func import FrameLess
from PyQt6 import QtCore, QtGui, QtWidgets

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        FrameLess(self)

    def open_second_window(self):
        self.second_window = NewTask_Screen()
        self.second_window.show()
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
