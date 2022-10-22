"""
create a window using  'layout_colorwidget'
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        window = Color("red")

        self.setWindowTitle("PyQt6 - Layout")
        self.setCentralWidget(window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
