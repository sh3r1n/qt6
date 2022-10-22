"""
create a check box with 3 states (tristate)
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        checkbox = QCheckBox("This is a TriState Checkbox")
        checkbox.setTristate(True)
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.stateChanged.connect(self.on_cbox_state_changed)

        self.setWindowTitle("PyQt6 - QtCheckBox - TriState")
        self.setCentralWidget(checkbox)

    def on_cbox_state_changed(self, state):
        states = ('Unchecked', 'PartiallyChecked', 'Checked')
        print(f"state : {states[state]}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
