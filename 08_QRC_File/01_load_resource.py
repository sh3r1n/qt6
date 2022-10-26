"""
load icon from 'resources.qrc' through 'resources.py'
"""
import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import resources

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("My Button")
        button.setIcon(QIcon(":/icons/chrome.png"))

        self.setWindowTitle("PyQt6 - QRC File")
        self.setCentralWidget(button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
