# imports 
import requests as r 
import json
import csv
import pyqt6 as qt
import sys
import platform

#define arrays as setup for zipcodes
ziparray = ['00000']
latarray = ['0.00']
lngarray = ['0.00']

#load api key (impliment user entered api key with saving and loading)
wkey = open('api.key', 'r').read().splitlines()[0]

#zip parsing and loading arrays
with open('zip.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ziparray.append(row['ZIP'])
        latarray.append(row['LAT'])
        lngarray.append(row['LNG'])


class Window = 
#Window
while True:

