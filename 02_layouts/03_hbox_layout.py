"""
create hbox layout
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout()
        hbox.addWidget(Color("blue"))
        hbox.addWidget(Color("green"))
        hbox.addWidget(Color("red"))

        widget = QWidget()
        widget.setLayout(hbox)

        self.setWindowTitle("PyQt6 - QHBoxLayout")
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
