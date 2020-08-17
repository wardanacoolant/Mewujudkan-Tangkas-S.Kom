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

class home:
    def __init__(self, my_home):
        self.my_home = my_home
        self.file_name = ''

        # Creating label widgets
        self.label_1 = Label(self.my_home,
                                    text = 'Klasifikasi Musik Berdasarkan Genre pada Layanan\nStreaming Musik Spotify Menggunakan algoritma\nK–Nearest Neighbor dan Modified K–Nearest Neighbor',
                                    font = 'times 20 underline',
                                    height=3,
                                    relief="groove",
                                    bd=16,
                                    padx=20,
                                    bg="white")

        # Buttons
        self.open_file_button = Button(self.my_home,
                                        text = 'Open File',
                                        font = 'Arial, 14',
                                        bg = 'Green',
                                        fg = 'Black')
        self.analisis_data_button = Button(self.my_home,
                                        text = 'Analisis Plot Data Atribut Fitur Pada Lagu',
                                        font = 'Arial, 14',
                                        bg = 'Orange',
                                        fg = 'Black')
        self.transformasi_data_button = Button(self.my_home,
                                        text = 'Transformasi Data',
                                        font = 'Arial, 14',
                                        bg = 'Orange',
                                        fg = 'Black')
        self.pca_button = Button(self.my_home,
                                        text = 'Klasifikasi KNN dan MKNN dengan PCA',
                                        font = 'Arial, 14',
                                        bg = 'Orange',
                                        fg = 'Black')
        self.tanpa_pca_button = Button(self.my_home,
                                        text = 'Klasifikasi KNN dan MKNN tanpa PCA',
                                        font = 'Arial, 14',
                                        bg = 'Orange',
                                        fg = 'Black')
        self.exit_button = Button(self.my_home,
                                    text = 'Exit',
                                    font = 'Arial, 14',
                                    bg = 'Red',
                                    fg = 'Black',
                                    command = my_home.destroy)

        # Placing the widgets using grid manager
        self.label_1.grid(row = 1, column = 1)
        self.open_file_button.grid(row = 3, column = 0,
                                    padx = 10, pady = 15)
        self.analisis_data_button.grid(row = 3, column = 1,
                                    padx = 0, pady = 15)
        self.transformasi_data_button.grid(row = 3, column = 2,
                                    padx = 0, pady = 15)
        self.pca_button.grid(row = 4, column = 0,
                                    padx = 0, pady = 15)
        self.tanpa_pca_button.grid(row = 4, column = 1,
                                    padx = 0, pady = 15)
        self.exit_button.grid(row = 4, column = 2,
                                padx = 10, pady = 15)



# Process Method tkinter window
my_home = Tk() # Method window
obj = home(my_home)

width_window = 800 # Set size width x window
height_window = 600 # Set size height y window
screen_width = my_home.winfo_screenwidth()
screen_height = my_home.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_window/2) # Set position window center
y_coordinate = (screen_height/2) - (height_window/2) # Set position window center

my_home.geometry("%dx%d+%d+%d" % (width_window, height_window, x_coordinate, y_coordinate))
my_home.title("KLASIFIKASI MUSIK BERDASARKAN GENRE PADA LAYANAN STREAMING MUSIK SPOTIFY MENGGUNAKAN ALGORITMA K–NEAREST NEIGHBOR DAN Modified K–NEAREST NEIGHBOR") # Tittle window
my_home.configure(bg = "#ADD8E6") # Background
# my_home.iconbitmap()

my_home.mainloop()