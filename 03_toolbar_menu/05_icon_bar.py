"""
create toolbar with icon action button
"""
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("Hello, Icon ToolBar")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_action = QAction(QIcon("./icons/edit-copy.svg"), "Your Button", self)
        button_action.setStatusTip("This is Your Button")
        button_action.setCheckable(True)
        button_action.triggered.connect(self.on_action_button_clicked)

        toolbar = QToolBar("My Main ToolBar")
        toolbar.setIconSize(QSize(32, 32))
        toolbar.addAction(button_action)

        self.setWindowTitle("PyQt6 - QIcon Button")
        self.addToolBar(toolbar)
        self.setCentralWidget(label)
        self.setStatusBar(QStatusBar(self))

    def on_action_button_clicked(self, is_checked):
        print(f"Checked : {is_checked}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
