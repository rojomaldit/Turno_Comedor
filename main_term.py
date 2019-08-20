# Importing the needed libraries
import sys
import os

# Reserving a meal for every code given from terminal
for code in sys.argv[1:]:
    print('Trying to reserve a meal for: ' + code)
    os.system('python magic_script.py ' + code)
