"""
create a combo box
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        combo_box = QComboBox()
        combo_box.addItems(("One", "Two", "Three"))
        combo_box.currentIndexChanged.connect(self.on_combo_box_index_changed)
        combo_box.currentTextChanged.connect(self.on_combo_box_text_changed)

        self.setWindowTitle("PyQt6 - QComboBox")
        self.setCentralWidget(combo_box)

    def on_combo_box_index_changed(self, index):
        print(index)

    def on_combo_box_text_changed(self, text):
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
