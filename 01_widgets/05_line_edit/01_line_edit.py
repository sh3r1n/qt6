"""
create an input wiget -> QLineEdit
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        line_edit = QLineEdit()
        line_edit.setMaxLength(10)
        line_edit.setPlaceholderText("Enter Your Text")

        line_edit.returnPressed.connect(self.on_return_pressed)
        line_edit.selectionChanged.connect(self.on_selection_changed)
        line_edit.textChanged.connect(self.on_text_changed)
        line_edit.textEdited.connect(self.on_text_edited)

        self.setWindowTitle("PyQt6 - QLineEdit")
        self.setCentralWidget(line_edit)

    def on_return_pressed(self):
        print("Return Pressed")
        self.centralWidget().setText("BOOM!")

    def on_selection_changed(self):
        print("Selection Changed")
        print(self.centralWidget().selectedText())

    def on_text_edited(self, text):
        print("Text Edited")
        print(text)

    def on_text_changed(self, text):
        print("Text Changed")
        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
