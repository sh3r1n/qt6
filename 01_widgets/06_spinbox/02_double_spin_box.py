"""
create a double spin box
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        double_spin = QDoubleSpinBox()
        double_spin.setMinimum(-10)
        double_spin.setMaximum(3)
        double_spin.setSingleStep(0.5)
        double_spin.setPrefix('$')
        double_spin.setSuffix('c')

        double_spin.valueChanged.connect(self.on_value_changed)
        double_spin.textChanged.connect(self.on_text_changed)

        self.setWindowTitle("PyQt6 - QDoubleSpinBox")
        self.setCentralWidget(double_spin)

    def on_value_changed(self, value):
        print(f"Value : {value}")

    def on_text_changed(self, text):
        print(f"Text : {text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
