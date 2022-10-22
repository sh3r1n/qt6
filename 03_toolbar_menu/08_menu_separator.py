"""
create a 'File' menu with separator
"""
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        open_action = QAction(QIcon("./icons/open.svg"), "Open File", self)
        open_action.setCheckable(True)
        open_action.setStatusTip("Open File For Editing")
        open_action.triggered.connect(self.on_action_triggered)

        save_action = QAction(QIcon("./icons/save.svg"), "Save File", self)
        save_action.setCheckable(True)
        save_action.setStatusTip("Save File")
        save_action.triggered.connect(self.on_action_triggered)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(save_action)
        
        toolbar = QToolBar("ToolBar")
        toolbar.setIconSize(QSize(24, 24))
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        label = QLabel("Hello, Menu Separator")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setWindowTitle("PyQt6 - Menu Separator")
        self.addToolBar(toolbar)
        self.setCentralWidget(label)
        self.setStatusBar(QStatusBar(self))

    def on_action_triggered(self, is_checked):
        print(f"Checked {is_checked}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
