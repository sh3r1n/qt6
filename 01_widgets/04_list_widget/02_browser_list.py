"""
add list widget items with icons
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        chrome = QListWidgetItem(QIcon("./icons/chrome.png"), "Google Chrome")
        firefox = QListWidgetItem(QIcon("./icons/firefox.png"), "Mozilla Firefox")
        edge = QListWidgetItem(QIcon("./icons/edge.png"), "Microsoft Edge")
        safari = QListWidgetItem(QIcon("./icons/safari.png"), "Apple Safari")

        list_widget = QListWidget()
        list_widget.addItem(chrome)
        list_widget.addItem(firefox)
        list_widget.addItem(edge)
        list_widget.addItem(safari)

        list_widget.currentItemChanged.connect(self.on_current_item_changed)  
        list_widget.currentTextChanged.connect(self.on_current_text_changed)

        self.setWindowTitle("PyQt6 - QListWidget - QListWidgetItem")
        self.setCentralWidget(list_widget)

    def on_current_text_changed(self, text):
        print(text)

    def on_current_item_changed(self, item):
        print(item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
