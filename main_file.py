# Importing the needed libraries
import sys
import os

# Opening the file with the codes
f = open('codes.txt', 'r+')

# Reserving a meal for every code given from terminal
for code in f:
    print('Trying to reserve a meal for: ' + code)
    os.system('python magic_script.py ' + code)