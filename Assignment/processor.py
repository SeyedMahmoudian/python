"""
File Name: processor.py
Author: Seyedamin Seyedmahmoudian
ID: 040813340
Course: CST8333 - Programming Language Research Project
Version : 4
Assignment:Final
Professor: Stanley Pieda
Since: 3.6
Date : 2017-12-017
"""
"""
This is class is responsible for all the work in the application
at first it will read the excel file and store it in panda, while it cleans up the data
it will make sure that each field in value contain a value and if not it will remove 
the row that have no value in value.
Then it will group all the GEO,VECTOR,COORDINATE,and EST
after insuring that all the data are being imported correctly and cleaned up it will
create a drop down menu base on the GEO of the file


NOTE: if you are going to change the data in excel you are more than welcome to do so
      but please make sure the headers of the file are matching otherwise it will fail
      also regex did not work for some reasons, so dummy inputs are also limited
      I spent lots of time trying to fix that but was not able to do so and had to move
      forward with the rest of the program
"""
try:
    import pandas as pd
except ImportError:
    print("You need panda please download from "
          "https://pandas.pydata.org/")
    exit(1)

try:
    from tkinter import StringVar
    from tkinter import Tk
    from tkinter import ttk
except ImportError:
    print("You need to have tkinter\n"
          "if you are seeing this error and panda error\n"
          "please make sure you are running python3")
    exit(1)

try:
    import numpy as np  # Object of numpy API

except ImportError:
    print("Pleas make sure to have numpy\n"
          "http://www.numpy.org/")
    exit(1)
try:
    import matplotlib.pyplot as plt  # Object of matplotlib API

except ImportError:
    print("Please download and install matplotlib"
          "https://matplotlib.org/users/installing.html")
    exit(1)

gui = Tk()
gui.title("Select the city")


def returnFile(name):
    """
    this function is only to demonstrate usage of unittest
    :return: file name
    """
    return name


class processor:
    filename = ""
    geo = ""
    refdate = ""
    value = ""
    table = ""
    df = ""
    selected = ""
    stringGeo = StringVar()

    def __init__(self, name):
        """
           initial constructor that will get the file fom main.py
           and call process for data manipulation
           :param: name:filename
        """
        self.fileName = name
        self.table = self.process()
        self.create()

    def process(self):
        """
        read the data from csv file make sure the header of the file match
        start processing the data remove .. and F from the file
        group GEO return the table
        :return: table
        """
        self.table = pd.read_csv(self.fileName, sep=',')
        self.df = pd.DataFrame(self.table, columns=['Ref_Date', 'GEO', 'EST', 'Vector', 'Coordinate', 'Value'])
        self.df = self.df[self.df['Value'] != 'F']  # remove row with F in it regex did not work
        self.df = self.df[self.df['Value'] != '..']  # remove row with .. in it regex did not work
        self.df = self.df.round(2)
        self.df['GEO'] = self.df['GEO'].str.replace("\s+", "-")  # replace the white space with dash
        self.df['GEO'] = self.df['GEO'].astype(str)  # convert the GEO from panda series to string
        self.geo = self.df['GEO'].unique()  # group all the GEO to remove redundant
        self.df['Ref_Date'] = self.df['Ref_Date'].astype(np.object)
        return self.table

    def create(self):
        """
        create drop down base on GEO
        :return:
        """
        strgeo = "\n".join(str(x) for x in self.geo)
        city = ttk.Combobox(gui, textvariable=self.stringGeo, state="readonly", width=30)
        city.config(values=strgeo)
        city.pack()
        city.bind("<<ComboboxSelected>>", self.selectedCity)

    def selectedCity(self, event):
        """
        drop down function handler, it also draw the plot and save the new excel
        file with name of the location+my student id 040813340
        containing all the information for that specific location.
        you would also find my name and student ID at the end of each file
        it get created by the app base on spec of the assignment.

        the program also print the Vector,Coordinate and Average of the Value  of the location to the terminal

        Once the new Excel file has been created and information displayed on command line or terminal
            a new picture will be saved with the name my student id which contains the plot that was created by
            python.
        :param event:
        :return:
        """
        self.selected = self.stringGeo.get()
        geo = self.df['GEO'] == self.selected
        values = self.df['Value']
        self.df = self.df[geo & values]
        vector = self.df['Vector'].unique()
        print("Vector:", vector)
        coordinate = self.df['Coordinate'].unique()
        print("Coordinate", coordinate)
        average = self.df['Value'].astype('float').mean()
        print("Average:", average)
        """
        create a snippet from the original file containing all the information of the selected city
        
        """
        self.df.to_csv(self.selected + '-040813340.csv', index=False)
        filename = self.selected + '-040813340.csv'
        file = open(filename, "a")
        file.write("**********************************************\n")
        file.write("CREATED BY SEYEDAMIN SEYEDMAHMOUDIAN-040813340\n")
        file.write("**********************************************\n")
        """
        end of saving the file
        
        """
        """
        Drop the extra columns
        """
        self.df = self.df.drop('GEO', axis=1)
        self.df = self.df.drop('EST', axis=1)
        self.df = self.df.drop('Vector', axis=1)
        self.df = self.df.drop('Coordinate', axis=1)
        """
        Draw the plot
        """
        #self.df.plot(x='Value', y='Ref_Date')
        x = self.df["Value"]
        y = self.df["Ref_Date"]
        plt.plot(y,x,kind='bar')
        plt.title(self.selected + "-040813340")
        """
        Save the jpg version of the plot in case it did not show on screen or required for future reference.
        """
        plt.savefig(self.selected + '-040813340.png')
        """
        Now show the plot
        """
        plt.show()
        plt.draw()
