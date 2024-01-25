import platform
import sys
import os
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QTabWidget, QApplication, QMainWindow, QWidget, QPushButton
import json


app = QApplication(sys.argv)

# import and check status code from api key via gui window. give user an error and option
# input new api key if this is errored. also give user option to change or delete it in
# settings. consider using hash storage of some kind

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #initial window settings
        self.setWindowTitle('Weatherboy')
        self.setFixedSize(QSize(600,400))
        
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        
        #init tab widget
        tab = QTabWidget(self)

        #1 day forecast tab
        oneDay = QWidget(self)
        oneDayLayout = QGridLayout()
        

        #5 day forecast tab
        fiveDayLayout = QHBoxLayout()


        #settings tab
        settingsLayout = QGridLayout()


        #tab placement
        main_layout.addWidget(tab, 0, 3, 2, 1)


            

window = Window()
window.show()

app.exec()

