import platform
import sys
import os
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import(
    QGridLayout, 
    QHBoxLayout,
    QTabWidget,
    QApplication,
    QMainWindow,
    QWidget, 
    QPushButton
    )

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
        
        mainLayout = QGridLayout(self)
        self.setLayout(mainLayout)
        mainLayout.setSpacing(20)
        #init tab widget
        tabs = QTabWidget(self)

        #1 day forecast tab
        oneDay = QWidget(self)
        oneDayLayout = QGridLayout()
        oneDay.setLayout(oneDayLayout)
        

        #5 day forecast tab
        fiveDay = QWidget(self)
        fiveDayLayout = QHBoxLayout()
        fiveDay.setLayout(fiveDayLayout)

        #settings tab
        settings = QWidget(self)
        settingsLayout = QGridLayout()
        settings.setLayout(settingsLayout)

        #add the three tabs
        tabs.addTab(oneDay, "Today")
        tabs.addTab(fiveDay, "5 day forecast")
        tabs.addTab(settings, "Settings")

        #tab placement
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.setCentralWidget(tabs)
        tabs.setMovable(False)
        #mainLayout.addWidget(tabs, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        


            

window = Window()
window.show()

app.exec()

