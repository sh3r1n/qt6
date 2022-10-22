"""
create grid layout
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        grid = QGridLayout()

        grid.addWidget(Color("red"), 0, 0)
        grid.addWidget(Color("blue"), 1, 0)
        grid.addWidget(Color("green"), 1, 1)
        grid.addWidget(Color("purple"), 2, 1)

        widget.setLayout(grid)

        self.setWindowTitle("PyQt6 - GridLayout")
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
