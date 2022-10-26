"""
load 'MainWindow.py' window and add logic to window
"""
import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        font = self.label.font()
        font.setPointSize(25)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(font)

        self.pushButton.pressed.connect(self.on_button_pressed)
    
    def on_button_pressed(self):
        self.label.setText(f"{random.randint(0, 100)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

