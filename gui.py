import platform
import sys
import os
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import json


app = QApplication(sys.argv)

# import and check status code from api key via gui window. give user an error and option
# input new api key if this is errored. also give user option to change or delete it in
# settings. consider using hash storage of some kind

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GUI TEST')
        button = QPushButton("test")
        self.setCentralWidget(button)
        self.setFixedSize(QSize(600,400))

window = Window()
window.show()

app.exec()

