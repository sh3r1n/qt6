"""
create a spin box
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        spin_box = QSpinBox()
        spin_box.setMinimum(-10)
        spin_box.setMaximum(3)
        spin_box.setSingleStep(3)
        spin_box.setPrefix('$')
        spin_box.setSuffix('c')
        spin_box.valueChanged.connect(self.on_value_changed)
        spin_box.textChanged.connect(self.on_text_changed)

        self.setWindowTitle("PyQt6 - QSpinBox")
        self.setCentralWidget(spin_box)

    def on_value_changed(self, value):
        print(f"Value : {value}")

    def on_text_changed(self, text):
        print(f"String value : {text}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

