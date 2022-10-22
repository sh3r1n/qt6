"""
create a list of browsers with icons and names
with placeholder text
"""
import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        combo_box = QComboBox()
        combo_box.setPlaceholderText("Browser List")
        combo_box.addItem(QIcon("./icons/chrome.png"), "Google Chrome")
        combo_box.addItem(QIcon("./icons/firefox.png"), "Mozilla Firefox")
        combo_box.addItem(QIcon("./icons/safari.png"), "Apple Safari")
        combo_box.addItem(QIcon("./icons/edge.png"), "Microsoft Edge")
        combo_box.currentTextChanged.connect(self.on_current_text_changed)

        self.setWindowTitle("PyQt6 - QComboBox - Browser List")
        self.setCentralWidget(combo_box)

    def on_current_text_changed(self, text):
        print(f"Your Choice : {text}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
