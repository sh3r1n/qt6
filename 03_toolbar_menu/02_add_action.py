"""
create an QAction and add it to Toolbar
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_action = QAction("Your Button", self)
        button_action.setStatusTip("This is your action")
        button_action.triggered.connect(self.on_action_button_click)

        toolbar = QToolBar("My Toolbar")
        toolbar.addAction(button_action)

        self.setWindowTitle("PyQt6 - QAction")
        self.setCentralWidget(label)
        self.addToolBar(toolbar)

    def on_action_button_click(self, s):
        print(f"click {s}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
