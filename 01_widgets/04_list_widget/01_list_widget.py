"""
creata list widget
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        list_widget = QListWidget()
        list_widget.addItems(("One", "Two", "Three"))
        list_widget.currentItemChanged.connect(self.on_current_item_changed)
        list_widget.currentTextChanged.connect(self.on_current_text_changed)

        self.setWindowTitle("PyQt6 - QListWidget")
        self.setCentralWidget(list_widget)

    def on_current_item_changed(self, item):
        print(dir(item))
        print(item)

    def on_current_text_changed(self, text):
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
