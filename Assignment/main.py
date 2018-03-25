"""
File Name: Main.py
Author: Seyedamin Seyedmahmoudian
ID: 040813340
Course: CST8333 - Programming Language Research Project
Version : 4
Assignment:Final
Professor: Stanley Pieda
Since: 3.6
Date : 2017-12-17
"""
"""
This is the main class of the program from here the application starts
it will create a TK based file browser and get the file path for 
processing to the processor.py
"""

try:
    import processor as processor  # object of processor
except ImportError:
    import processor as processor # in case first import failed
from tkinter import Tk, filedialog
import sys


class Main:
    def __init__(self, master):
        """
        initial constructor to start the program
        :param master:
        """
        # Master attribute needed for the python to work
        self.master = master
        # call create gui function to start the program
        self._creategui()
        # make sure the gui windows get closed when user close them
        self.master.protocol("WM_DELETE_WINDOW", self._safe_close)

    def _creategui(self):
        """
        :param: self
        create a gui for file dialog and get path of the file
        send it to processor, filter files to only accept csv Excel file

        """
        try:
            filename = filedialog.askopenfilename(initialdir="/", title="Select the Excel file",
                                              filetypes=[("Excel file", "*csv")])
        except FileNotFoundError:
            print ("File not found")
            exit(1)

        processor.processor(filename)  # send file path to processor

    def _safe_close(self):
        """
        close the application when use close the app
        :param:self
        """
        self.master.destroy()


if __name__ == "__main__":

    if sys.version_info[0] < 3:
        print("Must run on python3\n"
              "if you have python 3 and seeing this error\n"
              "check if IDE is correctly working with python3\n"
              "or visit https://www.python.org/")
    else:
        root = Tk()
        root.withdraw()
        app = Main(root)
        root.mainloop()
