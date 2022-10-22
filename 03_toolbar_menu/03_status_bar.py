"""
create a status bar and add it to QMainWindow
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("Hello, StatusBar")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_action = QAction("Your Button", self)
        button_action.setStatusTip("This is Your Button")
        button_action.triggered.connect(self.on_action_button_triggered)

        toolbar = QToolBar("My Main Toolbar")
        toolbar.addAction(button_action)

        self.setWindowTitle("PyQt6 - QStatusBar")
        self.setCentralWidget(label)
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

    def on_action_button_triggered(self, is_checked):
        print(f"Clicked, Checked : {is_checked}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
