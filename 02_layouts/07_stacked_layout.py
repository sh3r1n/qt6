"""
create stacked layout
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(3)

        widget.setLayout(layout)

        self.setWindowTitle("PyQt6 - QStackedLayout")
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
