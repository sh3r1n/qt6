"""
lauch a dialog with current window as the parent
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from dialogs import ParentDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Push For a Dialog")
        button.clicked.connect(self.on_button_clicked)

        self.setWindowTitle("PyQt6 - QDialog")
        self.setCentralWidget(button)
        
    def on_button_clicked(self, is_checked):
        dlg = ParentDialog(self)
        dlg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
