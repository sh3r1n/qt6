"""
create a slider and display its value in 
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QSlider, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(-10)
        slider.setMaximum(3)
        slider.setSingleStep(1)
        slider.setValue(0)

        slider.valueChanged.connect(self.on_value_changed)
        slider.sliderMoved.connect(self.on_slider_moved)
        slider.sliderPressed.connect(self.on_slider_pressed)
        slider.sliderReleased.connect(self.on_slider_released)

        self.label = QLabel("0")
        hbox = QHBoxLayout()
        hbox.addWidget(slider)
        hbox.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(hbox)

        self.setWindowTitle("PyQt6 - QSlider")
        self.setCentralWidget(widget)


    def on_slider_moved(self, position):
        print(f"Slider Moved, Position: {position}")

    def on_value_changed(self, value):
        print(f"Slider Value : {value}")
        self.label.setText(str(value))

    def on_slider_pressed(self):
        print("Slider Pressed")

    def on_slider_released(self):
        print("Slider Released")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
