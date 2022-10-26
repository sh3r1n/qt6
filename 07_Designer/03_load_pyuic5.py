"""
import 'Ui_MainWindow' from 'MainWindow.py' that created using
$ pyuic6 ./ui_files/01_main_window.ui -o MainWindow.py
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
