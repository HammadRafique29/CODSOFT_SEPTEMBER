import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import random
import string

def generate_password():
    password_length = int(length_entry.text())
    if password_length <= 0:
        result_label.setText("Please enter a valid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.setText(password)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Awesome Password Generator")
window.setGeometry(100, 100, 400, 300) 
window.setWindowOpacity(0.9)

title_label = QLabel("Password Generator", window)
title_label.setFont(QFont("Helvetica", 16))
title_label.setAlignment(Qt.AlignCenter)
title_label.setGeometry(100, 20, 200, 40)

length_label = QLabel("Password Length:", window)
length_label.setGeometry(20, 80, 120, 20)

length_entry = QLineEdit(window)
length_entry.setGeometry(160, 80, 120, 20)

generate_button = QPushButton("Generate Password", window)
generate_button.setGeometry(120, 120, 160, 30)
generate_button.clicked.connect(generate_password)

result_label = QLabel("", window)
result_label.setWordWrap(True)
result_label.setGeometry(20, 160, 360, 100)

window.show()
sys.exit(app.exec_())
