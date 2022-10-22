"""
create skeleton app to launch a dialog
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Press For a Button")
        button.clicked.connect(self.on_button_clicked)

        self.setWindowTitle("PyQt6 - QDialog")
        self.setCentralWidget(button)

    def on_button_clicked(self, is_checked):
        print(f"Clicked, checked : {is_checked}")

        dialog = QDialog(self)
        dialog.setWindowTitle("QDialog")
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
