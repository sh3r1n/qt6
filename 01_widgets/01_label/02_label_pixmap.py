"""
we can show picture in a label
set picture on label using
setPixmap(QPixmap('image.jpg'))
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel()
        label.setPixmap(QPixmap('./python_2.jpg'))
        label.setScaledContents(True)

        self.setWindowTitle("PyQt6 - QLabel + Picture")
        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

         

