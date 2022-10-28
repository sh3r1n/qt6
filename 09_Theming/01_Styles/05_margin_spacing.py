"""
give margin and spacing
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        hbox = QHBoxLayout()
        vbox_1 = QVBoxLayout()
        vbox_2 = QVBoxLayout()

        vbox_1.addWidget(Color("red"))
        vbox_1.addWidget(Color("yellow"))
        vbox_1.addWidget(Color("orange"))

        vbox_2.addWidget(Color("pink"))
        vbox_2.addWidget(Color("purple"))

        hbox.addLayout(vbox_1)
        hbox.addWidget(Color("blue"))
        hbox.addLayout(vbox_2)
        hbox.setContentsMargins(0,0,0,0)
        hbox.setSpacing(20)

        widget.setLayout(hbox)

        self.setWindowTitle("PyQt6 - Margin & Spacing")
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()
