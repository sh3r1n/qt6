"""
create a vertical slider with label to display its value
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSlider, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        slider = QSlider()
        slider.setMinimum(0)
        slider.setMaximum(50)
        slider.setValue(0)

        slider.valueChanged.connect(self.on_value_changed)

        self.label = QLabel("0")

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(slider)

        widget = QWidget()
        widget.setLayout(vbox)

        self.setWindowTitle("PyQt6 - QSlider")
        self.setCentralWidget(widget)

    def on_value_changed(self, value):
        self.label.setText(str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
