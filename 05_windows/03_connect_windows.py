"""
connect signal from one window to slot in another
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Another Window")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = AnotherWindow()
        self.button = QPushButton("Push For Window")
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def toggle_window(self, is_checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
