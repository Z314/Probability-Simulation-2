# Coin flipping simulation class
# Tested with Python version 3.8
# Author: JP

import tkinter
import tkinter.messagebox
import random


class coinGUI:
    """
    coinGUI class simulates a coin being flipped
    """

    def __init__(self):
        """
        Constructor __init__ method is called when the object is created in coin_GUI_main.py from the coinGUI class
        Creates the GUI interface
        """

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(
            self.top_frame, text='Enter the number of coin flips:')
        self.flip_entry = tkinter.Entry(self.top_frame, width=10)
        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.flip_entry.pack(side='left')

        # Create the button widgets for the bottom frame and get user input from entry field in widget
        self.flip_button = tkinter.Button(
            self.bottom_frame, text='Flip', command=lambda: self.toss(int(self.flip_entry.get())))
        self.quit_button = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)
        # Pack the buttons.
        self.flip_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

    def toss(self, flips):
        """
        Simulates a coin being flipped
        Arguments: 
        self -- Default required. Represents the instance of the class. 
        The first parameter of methods is the instance the method is called on.
        flips -- Integer. Determines the loop count
        Variables:
        sideUp -- Dictionary that stores the number of heads and tails that occur in simulation
        percentHeads -- String. Calculates the percentage of heads that occur
        percentTails --  String. Calculates the percentage of tails that occur
        """
        # Dictionary stores results
        sideUp = {"heads": 0, "tails": 0}
        # Simulate coin flips
        for i in range(flips):
            if random.randint(0, 1) == 0:
                sideUp["heads"] = sideUp["heads"] + 1

            else:
                sideUp["tails"] = sideUp["tails"] + 1

            percentHeads = str(round((sideUp['heads']/flips)*100, 1))
            percentTails = str(round((sideUp['tails']/flips)*100, 1))

        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo('Results ', str(flips) + " coin flips, produced " +
                                    str(sideUp['heads']) + " " + "(" + percentHeads + "%)" +
                                    " heads and " +
                                    str(sideUp['tails']) + " " + "(" + percentTails + "%)" +
                                    " tails.")
