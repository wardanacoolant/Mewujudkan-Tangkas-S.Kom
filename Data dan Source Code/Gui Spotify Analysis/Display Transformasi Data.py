# Import libraries attributes
from tkinter import *
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox as msg
from pandastable import Table
from tkintertable import TableCanvas

import seaborn as sns # untuk visualization Data
import matplotlib.pyplot as plt # untuk visualization Data
import pandas as pd # analysis data
import math # analysis math
import operator
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

class transformasi_data:
    def __init__(self, my_transformasi):
        self.my_transformasi = my_transformasi
        self.file_name = ''

        # Buttons
        self.convert_button = Button(self.my_transformasi,
                                        text = 'Convert',
                                        font = 'Arial, 14',
                                        bg = 'Green',
                                        fg = 'Black')
        self.display_button = Button(self.my_transformasi,
                                        text = 'Display',
                                        font = 'Arial, 14',
                                        bg = 'Orange',
                                        fg = 'Black')
        self.exit_button = Button(self.my_transformasi,
                                    text = 'Exit',
                                    font = 'Arial, 14',
                                    bg = 'Red',
                                    fg = 'Black',
                                    command = my_transformasi.destroy)

        # Placing the widgets using grid manager
        self.convert_button.grid(row = 3, column = 0,
                                    padx = 10, pady = 15)
        self.display_button.grid(row = 3, column = 1,
                                    padx = 0, pady = 15)
        self.exit_button.grid(row = 3, column = 2,
                                padx = 10, pady = 15)

    def display_csv_file(self):
        try:
            self.file_name = filedialog.askopenfilename(initialdir = '/',
                                                        title = 'Select a excel file',
                                                        filetypes = (('excel file','*.csv'),
                                                                    ('excel file','*.csv')))
            df = pd.read_excel(self.file_name)

            if (len(df)== 0):
                msg.showinfo('No records', 'No records')
            else:
                pass

            # Now display the DF in 'Table' object
            # under'pandastable' module
            self.my_home = Frame(self.my_home, height=200, width=300)
            self.my_home.pack(fill=BOTH,expand=1)
            self.table=Table(self.my_home, dataframe=df,read_only=True)
            self.table.show()

        except FileNotFoundError as e:
            print(e)
            msg.showerror('Error in opening file',e)






# Process Method tkinter window
my_transformasi = Tk() # Method window
obj = transformasi_data(my_transformasi)

width_window = 800 # Set size width x window
height_window = 600 # Set size height y window
screen_width = my_transformasi.winfo_screenwidth()
screen_height = my_transformasi.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_window/2) # Set position window center
y_coordinate = (screen_height/2) - (height_window/2) # Set position window center

my_transformasi.geometry("%dx%d+%d+%d" % (width_window, height_window, x_coordinate, y_coordinate))
my_transformasi.title("KLASIFIKASI MUSIK BERDASARKAN GENRE PADA LAYANAN STREAMING MUSIK SPOTIFY MENGGUNAKAN ALGORITMA K–NEAREST NEIGHBOR DAN Modified K–NEAREST NEIGHBOR") # Tittle window
my_transformasi.configure(bg = "#ADD8E6") # Background
# my_transformasi.iconbitmap()

my_transformasi.mainloop()