#!/usr/bin/env python
import sys
import requests
# from termcolor import colored
from controller import PyController

from interface import PyUi
from PyQt5.QtWidgets import QApplication

__version__ = '0.1'
__author__ = 'El Kadhi Ahmed'

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication([])
    # Show the calculator's GUI
    view = PyUi()
    view.show()
    # Create instances of the model and the controller
    PyController(view=view)
    
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()