"""
create message dialog with specified buttons
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Press For Message")
        button.clicked.connect(self.on_button_clicked)

        self.setWindowTitle("PyQt6 - MessageBox")
        self.setCentralWidget(button)

    def on_button_clicked(self, is_checked):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I Have a Question")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setText("This is a QuestionDialog")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
