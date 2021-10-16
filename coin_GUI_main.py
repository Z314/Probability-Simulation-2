# The main function for the coin sim
# Tested with Python version 3.8
# Author: JP

# Imports module named coin_GUIClass.py (has the class definition)
import coin_GUIClass
import tkinter


def main():
    """
    Creates an instance of the coinGUI class located in coin_GUIClass.py. 
    The class contains a constructor which is automatically called when the below object is created.
    The mainloop() method which initiates the event loop, puts everything on the display, and responds to user input until the program terminates.
    """
    coinFlipper = coin_GUIClass.coinGUI()

    # Enter the tkinter main loop.
    tkinter.mainloop()


main()
