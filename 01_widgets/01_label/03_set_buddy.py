"""
setbuddy() 
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        name_ledit = QLineEdit()
        name_label = QLabel("&Name")
        name_label.setIndent(20)
        name_label.setBuddy(name_ledit)

        phone_ledit = QLineEdit()
        phone_label = QLabel("&Phone")
        phone_label.setBuddy(phone_ledit)
        phone_label.setMargin(20)

        grid_layout = QGridLayout()
        grid_layout.addWidget(name_label, 0, 0)
        grid_layout.addWidget(name_ledit, 0, 1)
        grid_layout.addWidget(phone_label, 1, 0)
        grid_layout.addWidget(phone_ledit, 1, 1)

        widget = QWidget()
        widget.setLayout(grid_layout)

        self.setWindowTitle("PyQt6 - QLabel => setBuddy()")
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
