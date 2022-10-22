"""
create checkbox and add stateChanged Event
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        checkbox = QCheckBox("This is a Checkbox")
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.stateChanged.connect(self.on_cbox_state_changed)

        self.setWindowTitle("PyQt6 - QCheckBox")
        self.setCentralWidget(checkbox)

    def on_cbox_state_changed(self, state):
        print(state == int(Qt.CheckState.Checked))
        print(type(Qt.CheckState.Checked))
        print(state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
