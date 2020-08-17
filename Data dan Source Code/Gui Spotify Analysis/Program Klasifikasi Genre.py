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

class program:
    def __init__(self, my_program):
        self.my_program = my_program
        self.file_name = ''

        # Creating label widgets
        self.label_1 = Label(self.my_program,
                                    text = 'Klasifikasi Musik Berdasarkan Genre pada Layanan\nStreaming Musik Spotify Menggunakan algoritma\nK–Nearest Neighbor dan Modified K–Nearest Neighbor',
                                    font = 'times 20 underline',
                                    height=3,
                                    relief="groove",
                                    bd=16,
                                    padx=20,
                                    bg="white")

        # Buttons
        self.start_program_button = Button(self.my_program,
                                        text = 'Start Program',
                                        font = 'Arial, 14',
                                        bg = 'Green',
                                        fg = 'Black')
        self.tentang_program_button = Button(self.my_program,
                                        text = 'Tentang Program Ini',
                                        font = 'Arial, 14',
                                        bg = 'Orange',
                                        fg = 'Black')
        self.exit_button = Button(self.my_program,
                                    text = 'Exit',
                                    font = 'Arial, 14',
                                    bg = 'Red',
                                    fg = 'Black',
                                    command = my_program.destroy)

        # Placing the widgets using grid manager
        self.label_1.grid(row = 1, column = 1)
        self.startprogram_button.grid(row = 3, column = 0,
                                    padx = 10, pady = 15)
        self.tentangprogram_button.grid(row = 3, column = 1,
                                    padx = 0, pady = 15)
        self.exit_button.grid(row = 3, column = 2,
                                padx = 10, pady = 15)

    def start_program(self):
        try:



    def tentang_program(self):
        try:



# Process Method tkinter window
my_program = Tk() # Method window
obj = program(my_program)

width_window = 800 # Set size width x window
height_window = 600 # Set size height y window
screen_width = my_program.winfo_screenwidth()
screen_height = my_program.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_window/2) # Set position window center
y_coordinate = (screen_height/2) - (height_window/2) # Set position window center

my_program.geometry("%dx%d+%d+%d" % (width_window, height_window, x_coordinate, y_coordinate))

my_program.title("KLASIFIKASI MUSIK BERDASARKAN GENRE PADA LAYANAN STREAMING MUSIK SPOTIFY MENGGUNAKAN ALGORITMA K–NEAREST NEIGHBOR DAN Modified K–NEAREST NEIGHBOR") # Tittle window
my_program.configure(bg = "#ADD8E6") # Background
# my_program.iconbitmap()

my_program.mainloop()