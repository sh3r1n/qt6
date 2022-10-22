"""
show custom dialogs
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from dialogs import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Press For Dialog")
        button.clicked.connect(self.on_button_clicked)

        self.setWindowTitle("PyQt6 - CustomDialog")
        self.setCentralWidget(button)

    def on_button_clicked(self, on_checked):
        dialog = CustomDialog()
        dialog.exec()

if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

