"""
create a widget with line edit and checkbox
using the check box change the line edit's 'read-only' status
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QCheckBox
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)

        check_box = QCheckBox("Read Only")
        check_box.setCheckState(Qt.CheckState.Checked)
        check_box.stateChanged.connect(self.on_state_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(check_box)

        widget = QWidget()
        widget.setLayout(layout)

        self.setWindowTitle("PyQt6 - LineEdit Options")
        self.setCentralWidget(widget)

    def on_state_changed(self, state):
        if state == 0:
            self.line_edit.setReadOnly(False)
        elif state == 2:
            self.line_edit.setReadOnly(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
