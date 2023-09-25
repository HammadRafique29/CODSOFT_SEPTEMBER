import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QLinearGradient

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.input_display = QLineEdit(self)
        self.input_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_display.setPlaceholderText("0")
        layout.addWidget(self.input_display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        grid_row, grid_col = 4, 4

        grid_layout = QGridLayout()

        for i in range(grid_row):
            for j in range(grid_col):
                button_text = buttons[i * grid_col + j]
                button = QPushButton(button_text, self)
                grid_layout.addWidget(button, i, j)

                # Apply styling to buttons
                self.style_button(button)

                button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))

        layout.addLayout(grid_layout)
        self.setLayout(layout)

        self.current_input = ''
        self.result_shown = False

        # Set dark gradient background
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(0, 0, 0))  # Start color
        gradient.setColorAt(1.0, QColor(30, 30, 30))  # End color
        palette = self.palette()
        palette.setBrush(QPalette.ColorRole.Window, gradient)
        self.setPalette(palette)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.current_input))
                self.input_display.setText(result)
                self.current_input = result
                self.result_shown = True
            except Exception as e:
                self.input_display.setText("Error")
                self.current_input = ""
        else:
            if self.result_shown:
                self.input_display.setText("")
                self.current_input = ""
                self.result_shown = False

            self.current_input += text
            self.input_display.setText(self.current_input)

    def style_button(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #555;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                padding: 10px;
            }

            QPushButton:pressed {
                background-color: white;
                color: #555;
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
