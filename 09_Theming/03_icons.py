"""
set a system icon for the button
"""
import sys
from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6.QtGui import QIcon


app = QApplication(sys.argv)
button = QPushButton("Hello")
icon = QIcon.fromTheme("document-new")
button.setIcon(icon)
button.show()
app.exec()
