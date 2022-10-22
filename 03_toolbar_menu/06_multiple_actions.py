"""
create toolbar with 2 actions, label and a checkbox
"""
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        copy_action = QAction(QIcon("./icons/edit-copy.svg"), "Copy Action", self)
        copy_action.setCheckable(True)
        copy_action.setStatusTip("Your Copy Button")
        copy_action.triggered.connect(self.on_action_triggered)

        cut_action = QAction(QIcon("./icons/edit-cut.svg"), "Cut Action", self)
        cut_action.setCheckable(True)
        cut_action.setStatusTip("Your Cut Button")
        cut_action.triggered.connect(self.on_action_triggered)

        toolbar = QToolBar("My Main Toolbar")
        toolbar.addAction(copy_action)
        toolbar.addAction(cut_action)
        toolbar.addSeparator()
        toolbar.addWidget(QLabel("Hello!  "))
        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox("Activate"))

        label = QLabel("Hello, Multiple Buttons")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setWindowTitle("PyQt6 - Multiple Toolbar Buttons")
        self.addToolBar(toolbar)
        self.setCentralWidget(label)
        self.setStatusBar(QStatusBar(self))


    def on_action_triggered(self, is_checked):
        print(f"Checked : {is_checked}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
