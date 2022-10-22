"""
create Context Menu (Menu Appears on Right Click) in the App
"""
import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/open.svg"),"Open", self))
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/save.svg"),"Save", self))
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/edit-copy.svg"),"Copy", self))
        context.addAction(QAction(QIcon("../03_toolbar_menu/icons/edit-cut.svg"),"Cut", self))
        context.exec(e.globalPos())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
