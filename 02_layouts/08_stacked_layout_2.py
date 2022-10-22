"""
change visible stacked layout using buttons
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QHBoxLayout, QPushButton

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button_1 = QPushButton("red")
        button_2 = QPushButton("green")
        button_3 = QPushButton("blue")

        button_1.pressed.connect(self.activate_tab_1)
        button_2.pressed.connect(self.activate_tab_2)
        button_3.pressed.connect(self.activate_tab_3)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(Color("red"))
        self.stacked_layout.addWidget(Color("green"))
        self.stacked_layout.addWidget(Color("blue"))

        button_box = QHBoxLayout()
        button_box.addWidget(button_1)
        button_box.addWidget(button_2)
        button_box.addWidget(button_3)

        widget_layout = QVBoxLayout()
        widget_layout.addLayout(self.stacked_layout)
        widget_layout.addLayout(button_box)

        widget = QWidget()
        widget.setLayout(widget_layout)

        self.setWindowTitle("PyQt6 - StackedLayout")
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacked_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacked_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacked_layout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
