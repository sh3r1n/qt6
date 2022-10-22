"""
handle all mouse events
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Event Reports")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setWindowTitle("PyQt6 - QMouseEvents")
        self.setCentralWidget(self.label)

    def eventButtons(self, text, e):
        button = ""
        if e.button() == Qt.MouseButton.LeftButton:
            button = "LEFT"
        elif e.button() == Qt.MouseButton.MiddleButton:
            button = "MIDDLE"
        elif e.button() == Qt.MouseButton.RightButton:
            button = "RIGHT"
        self.label.setText(f"mouse{text}Event {button}")

    def mouseMoveEvent(self, e):
        self.label.setText("Mouse Moved")

    def mousePressEvent(self, e):
        self.eventButtons("Press", e)

    def mouseReleaseEvent(self, e):
        self.eventButtons("Release", e)

    def mouseDoubleClickEvent(self, e):
        self.eventButtons("DoubleClick", e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
