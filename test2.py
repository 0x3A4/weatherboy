import platform
import sys
import os
import requests
import tempfile
import json
from functools import cached_property
from PyQt6.QtCore import QSize, Qt, QObject, pyqtSignal, QUrl
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt6.QtWidgets import(
    QGridLayout, 
    QHBoxLayout,
    QTabWidget,
    QApplication,
    QMainWindow,
    QWidget, 
    QLabel
    )


# import and check status code from api key via gui window. give user an error and option
# input new api key if this is errored. also give user option to change or delete it in
# settings. consider using hash storage of some kind


#Image downloader. Used to pass images into widgets.
class ImageDownloader(QObject):
    finished = pyqtSignal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager.finished.connect(self.handle_finished)

    @cached_property
    def manager(self):
        return QNetworkAccessManager()

    def start_download(self, url):
        self.manager.get(QNetworkRequest(url))

    def handle_finished(self, reply):
        if reply.error() == QNetworkReply.error:
            print("error: ", reply.errorString())
            return
        image = QImage()
        image.loadFromData(reply.readAll())
        self.finished.emit(image)




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #initial window settings
        self.setWindowTitle('Weatherboy')
        self.setFixedSize(QSize(640,480))
        mainLayout = QGridLayout(self)
        self.setLayout(mainLayout)
        mainLayout.setSpacing(20)


        #downloader
        self.downloader = ImageDownloader()

        self.downloader.finished.connect(self.handle_finished)
        self.download()
        
        #init tab widget
        tabs = QTabWidget(self)

        #1 day forecast tab
        oneDay = QWidget(self)
        oneDayLayout = QGridLayout()
        oneDay.setLayout(oneDayLayout)


        #5 day forecast tab
        fiveDay = QWidget(self)
        fiveDayLayout = QHBoxLayout(self)
        fiveDay.setLayout(fiveDayLayout)
        
        #init days for 5 day forecast
        #dayOne   = QWidget(self)
        #dayTwo   = QWidget(self)
        #dayThree = QWidget(self)
        #dayFour  = QWidget(self)
        #dayFive  = QWidget(self)

        #grab images as icons for each day
        self.dayOnePNG   = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.dayTwoPNG   = QLabel()
        self.dayThreePNG = QLabel()
        self.dayFourPNG  = QLabel()
        self.dayFivePNG  = QLabel()
        
        #self.dayOnePNG.resize(120, 120)
        self.dayTwoPNG.resize(120, 120)
        self.dayThreePNG.resize(120, 120)
        self.dayFourPNG.resize(120, 120)
        self.dayFivePNG.resize(120, 120)

        #self.dayOnePNG.setStyleSheet('border:1px solid black;')
        self.dayTwoPNG.setStyleSheet('border:1px solid black;')
        self.dayThreePNG.setStyleSheet('border:1px solid black;')
        self.dayFourPNG.setStyleSheet('border:1px solid black;')
        self.dayFivePNG.setStyleSheet('border:1px solid black;')\
        


        #place days 1-5
        fiveDayLayout.addWidget(self.dayOnePNG)

        #settings tab
        settings = QWidget(self)
        settingsLayout = QGridLayout()
        settings.setLayout(settingsLayout)

        #add the three tabs
        tabs.addTab(oneDay, "Today")
        tabs.addTab(fiveDay, "5 Day Forecast")
        tabs.addTab(settings, "Settings")

        #tab placement
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.setCentralWidget(tabs)
        tabs.setMovable(False)

        
        #mainLayout.addWidget(tabs, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
    def handle_finished(self, image):
        pixmap = QPixmap.fromImage(image)
        self.dayOnePNG.setPixmap(pixmap)
    def download(self):
        url = QUrl('http://openweathermap.org/img/wn/01d@2x.png')  
        self.downloader.start_download(url)
         


            
app = QApplication(sys.argv)
w = Window()
w.show()

app.exec()

