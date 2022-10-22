"""
create a message box dialog
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Push for Message")
        button.clicked.connect(self.on_button_clicked)

        self.setWindowTitle("PyQt6 - QMessageBox")
        self.setCentralWidget(button)

    def on_button_clicked(self, is_checked):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I Have a Question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("Ok")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
