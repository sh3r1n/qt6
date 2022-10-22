"""
show/hide new window when button is pressed
"""
import sys
from random import randint

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel(f"Another Window {randint(0, 100)}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(label)

        self.setLayout(vbox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.new_window = AnotherWindow()
        button = QPushButton("Press For Window")
        button.clicked.connect(self.on_button_clicked)

        self.setWindowTitle("PyQt6 - 2 Windows")
        self.setCentralWidget(button)

    def on_button_clicked(self, is_checked):
        if self.new_window.isVisible():
            self.new_window.hide()
        else:
            self.new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

