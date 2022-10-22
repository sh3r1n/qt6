"""
nesting vbox layouts inside a hbox
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(Color("red"))
        vbox_1.addWidget(Color("yellow"))
        vbox_1.addWidget(Color("blue"))

        vbox_2 = QVBoxLayout()
        vbox_2.addWidget(Color("green"))
        vbox_2.addWidget(Color("purple"))

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_1)
        hbox.addWidget(Color("orange"))
        hbox.addLayout(vbox_2)

        widget = QWidget()
        widget.setLayout(hbox)

        self.setWindowTitle("PyQt6 - Nested Layout")
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
