"""
create fontComboBox
"""
import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QFontComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        font_combo_box = QFontComboBox()
        font_combo_box.currentFontChanged.connect(self.on_font_changed)

        self.setWindowTitle("PyQt6 - QFontComboBox")
        self.setCentralWidget(font_combo_box)

    def on_font_changed(self, font):
        font_selected = QFont(font)
        #print(dir(fontx))
        print(font_selected.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
