"""
create a vbox layout
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        vbox.addWidget(Color("red"))
        vbox.addWidget(Color("green"))
        vbox.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(vbox)

        self.setWindowTitle("PyQt6 - QVBoxLayout")
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
