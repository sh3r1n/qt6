"""
play video in a label 
using setMovie(QMovie(file))
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QMovie


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel()
        movie = QMovie('giphy.gif')
        label.setMovie(movie)
        movie.start()

        self.setWindowTitle("PyQt6 - QLabel => setMovie()")
        self.setCentralWidget(label)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

