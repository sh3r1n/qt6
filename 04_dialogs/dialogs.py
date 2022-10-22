"""
create custom dialog classes
"""
from PyQt6.QtWidgets import QDialog, QLabel, QDialogButtonBox, QVBoxLayout


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        label_message = QLabel("Something Happend, Is That Ok ?")

        buttons = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        button_box = QDialogButtonBox(buttons)
        button_box.accepted.connect(self.on_accept)
        button_box.rejected.connect(self.on_reject)

        layout = QVBoxLayout()
        layout.addWidget(label_message)
        layout.addWidget(button_box)

        self.setWindowTitle("PyQt6 - CustomDialog")
        self.setLayout(layout)

    def on_accept(self):
        print("Accepted")

    def on_reject(self):
        print("Rejected")


class ParentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        label = QLabel("Something Happened, Is That Ok?")

        buttons = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        button_box = QDialogButtonBox(buttons)
        button_box.accepted.connect(self.on_accepted)
        button_box.rejected.connect(self.on_rejected)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def on_accepted(self):
        print("Accepted")
        self.hide()

    def on_rejected(self):
        print("Rejected")
        self.hide()
