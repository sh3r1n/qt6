"""
create different type of message boxes
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn_question = QPushButton("Question")
        btn_question.clicked.connect(self.on_question_button_clicked)

        btn_info = QPushButton("Information")
        btn_info.clicked.connect(self.on_info_button_clicked)

        btn_about = QPushButton("About")
        btn_about.clicked.connect(self.on_about_button_clicked)

        btn_critical = QPushButton("Critical")
        btn_critical.clicked.connect(self.on_critical_button_clicked)

        btn_warning = QPushButton("Warning")
        btn_warning.clicked.connect(self.on_warning_button_clicked)

        hbox = QHBoxLayout()
        hbox.addWidget(btn_question)
        hbox.addWidget(btn_info)
        hbox.addWidget(btn_about)
        hbox.addWidget(btn_critical)
        hbox.addWidget(btn_warning)

        widget = QWidget()
        widget.setLayout(hbox)

        self.setWindowTitle("PyQt6 - Built-In Message Boxes")
        self.setCentralWidget(widget)
    def on_warning_button_clicked(self, is_checked):
        button = QMessageBox.warning(self, "Warning Message", "You Should be Careful")

    def on_critical_button_clicked(self, is_checked):
        Buttons = QMessageBox.StandardButton
        button = QMessageBox.critical(self,
                                      "Oh Dear!", 
                                      "Something Went Very Wrong!!",
                                      buttons= Buttons.Discard | Buttons.NoToAll | Buttons.Ignore,
                                      defaultButton=Buttons.Discard
                                    )

    def on_about_button_clicked(self, is_checked):
        button  = QMessageBox.about(self, "About Message", "About the Application")

    def on_info_button_clicked(self, is_checked):
        button = QMessageBox.information(self, "Information Message", "This is Just an Intel")

    def on_question_button_clicked(self, is_checked):
        button = QMessageBox.question(self, "Question Message", "The Longer Message")
        if button == QMessageBox.StandardButton.Yes:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
