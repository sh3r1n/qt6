"""
create a dial and display its value in  a label
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDial, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        dial = QDial()
        dial.setRange(-10, 100)
        dial.setSingleStep(1)
        dial.setValue(0)

        dial.valueChanged.connect(self.on_value_changed)

        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(dial)
        vbox.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(vbox)

        self.setWindowTitle("PyQt6 - QDial")
        self.setCentralWidget(widget)

    def on_value_changed(self, value):
        self.label.setText(str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
