"""
create a checkable action button
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("Hello, Checkable Action")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_action = QAction("Your Button", self)
        button_action.setStatusTip("This is your Button")
        button_action.setCheckable(True)
        button_action.triggered.connect(self.on_action_button_triggerd)
        
        toolbar = QToolBar("My Main Toolbar")
        toolbar.addAction(button_action)

        self.setWindowTitle("PyQt6 - Checkable Action Button")
        self.setCentralWidget(label)
        self.setStatusBar(QStatusBar(self))
        self.addToolBar(toolbar)

    def on_action_button_triggerd(self, is_checked):
        print(f"Checked : {is_checked}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

