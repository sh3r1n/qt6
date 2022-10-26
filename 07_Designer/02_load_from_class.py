"""
load the .ui file from 'MainWindow' class
"""
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui_files/01_main_window.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
