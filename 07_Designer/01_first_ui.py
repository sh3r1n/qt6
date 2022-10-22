"""
load window form "*.ui" file created using Qt Designer
"""
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
window = uic.loadUi("./ui_files/01_main_window.ui")
window.show()
app.exec()
