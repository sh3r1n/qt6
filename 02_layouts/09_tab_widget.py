"""
create tab widget contains color widget
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tab_widget = QTabWidget()
        tab_widget.setTabPosition(QTabWidget.TabPosition.West)
        tab_widget.setMovable(True)

        colors = ["red", "green", "blue", "yellow"]
        
        for color in colors:
            tab_widget.addTab(Color(color), color)

        self.setWindowTitle("PyQt6 - QTabWidget")
        self.setCentralWidget(tab_widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
