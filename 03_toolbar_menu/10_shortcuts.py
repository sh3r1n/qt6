"""
add shortcuts to actions
"""
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        open_action = QAction(QIcon("./icons/open.svg"), "Open", self)
        open_action.setStatusTip("Open File")
        open_action.setShortcut(QKeySequence("Ctrl+o"))
        open_action.triggered.connect(self.on_action_triggered)

        save_action = QAction(QIcon("./icons/save.svg"), "Save", self)
        save_action.setStatusTip("Save File")
        save_action.setShortcut(QKeySequence("Ctrl+s"))
        save_action.triggered.connect(self.on_action_triggered)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        toolbar = QToolBar("ToolBar")
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        label = QLabel("Menu + Shortcut")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setWindowTitle("PyQt - Action Shortcuts")
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
