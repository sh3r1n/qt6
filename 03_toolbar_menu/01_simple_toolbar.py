"""
create toolbar 
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        toolbar = QToolBar('My Main Toolbar')

        self.setWindowTitle("PyQt6 - QToolBar")
        self.setCentralWidget(label)
        self.addToolBar(toolbar)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

