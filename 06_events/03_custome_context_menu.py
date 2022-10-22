"""
create a context menu appears based on signal from 'QWidget'
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/open.svg"), "Open", self))
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/save.svg"), "Save", self))
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/edit-copy.svg"), "Copy", self))
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/edit-cut.svg"), "Cut", self))
        context.exec(self.mapToGlobal(pos))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
