from PyQt6 import QtWidgets
from datetime import datetime
import os



def Add_Shadow(x=3, y=2, radius=10, op=160):
    from PyQt6.QtWidgets import QGraphicsDropShadowEffect
    from PyQt6.QtGui import QCursor, QColor
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(radius)
    shadow.setColor(QColor(0, 0, 0, op))
    shadow.setYOffset(x) 
    shadow.setXOffset(y) 
    # self.create_btn_dash.setGraphicsEffect(Add_Shadow())
    return shadow


def FrameLess(obj):
    from PyQt6.QtCore import Qt
    obj.setWindowFlags(Qt.WindowType.FramelessWindowHint) 


from PyQt6.QtWidgets import QLineEdit
class SingleLineLineEdit(QLineEdit):
    from PyQt6.QtCore import Qt
    from PyQt6.QtGui import QKeyEvent
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            event.ignore()  # Ignore Enter/Return key press
        else:
            super().keyPressEvent(event)


def New_Task_Screen():
    from _Create_Task_Screen import _New_Task
    from PyQt6.QtWidgets import QApplication, QMainWindow
    import sys
    class NewTask_Screen(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = _New_Task()
            self.ui.setupUi(self)
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
            FrameLess(self)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = _New_Task()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())


class Control_Buttons():
    def __init__(self, obj):
        self.app = obj

    def close_window(self):
        print("closing window")
        # self.is_running = False
        try: self.app.quit()
        except: self.app.close()

    def minimize_window(self):
        import win32gui
        import win32con
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


class Clock_DateTime():
    def __init__(self):
        pass

    def GET_CURRENT_DATE(instance=None):
        current_date = datetime.now()
        year = current_date.year
        day = current_date.day
        month = current_date.month
        date_obj = datetime(year, month, day)
        formatted_date = date_obj.strftime("%A, %b %d, %Y")
        return str(formatted_date)

    def GET_CURRENT_TIME(instance=None):
        current_datetime = datetime.now()
        current_hour = current_datetime.hour
        current_minute = current_datetime.minute
        current_second = current_datetime.second  # Add this line to get seconds
        am_pm = "AM" if current_hour < 12 else "PM"
        if current_hour == 0:
            current_hour = 12
        elif current_hour > 12:
            current_hour -= 12
        formatted_time = f"{current_hour}:{current_minute:02d}:{current_second:02d} {am_pm}"  # Include seconds
        return str(formatted_time)
    
    
