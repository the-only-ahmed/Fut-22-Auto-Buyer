#!/usr/bin/env python
import sys
import requests
# from termcolor import colored
from controller import PyController

from interface import PyUi
from PyQt5.QtWidgets import QApplication

# r = requests.get('https://www.ea.com/fifa/ultimate-team/web-app/content/22747632-e3df-4904-b3f6-bb0035736505/2022/fut/items/web/players.json')

# print (r.text)

__version__ = '0.1'
__author__ = 'El Kadhi Ahmed'

# Client code
def main():
    """Main function."""
    # data = loadPlayers()
    # id = 1
    # if id in data:
    #     player = data[id]
    #     print(player[0] + " --> " + colored(player[1], 'green'))
    # else:
    #     print(colored('player not found', 'red'))

    # Create an instance of QApplication
    pycalc = QApplication([])
    # Show the calculator's GUI
    view = PyUi()
    view.show()
    # Create instances of the model and the controller
    PyController(view)
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()