# Import libraries attributes
from tkinter import *
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox as msg
from pandastable import Table
from tkintertable import TableCanvas

# Proses Class
class csv_to_excel:
   
    def __init__(self, my_window2): 
   
        self.my_window2 = my_window2
        self.file_name = ''
        self.f = Frame(self.my_window2,
                       height = 200,
                       width = 300)

        # Place the frame on my_window2
        self.f.pack()
           
        # Creating label widgets
        self.message_label = Label(self.f,
                                   text = 'GeeksForGeeks',
                                   font = ('Arial', 19,'underline'), 
                                   fg = 'Green')
        self.message_label2 = Label(self.f,
                                    text = 'Converter of CSV to Excel file', 
                                    font = ('Arial', 14,'underline'), 
                                    fg = 'Red')
   
        # Buttons
        self.convert_button = Button(self.f,
                                     text = 'Convert',
                                     font = ('Arial', 14),
                                     bg = 'Orange',
                                     fg = 'Black',
                                     command = self.convert_csv_to_xls) 
        self.display_button = Button(self.f,
                                     text = 'Display',
                                     font = ('Arial', 14),
                                     bg = 'Green',
                                     fg = 'Black',
                                     command = self.display_xls_file) 
        self.exit_button = Button(self.f,
                                  text = 'Exit',
                                  font = ('Arial', 14),
                                  bg = 'Red',
                                  fg = 'Black',
                                  command = my_window2.destroy)
   
        # Placing the widgets using grid manager
        self.message_label.grid(row = 1, column = 1)
        self.message_label2.grid(row = 2, column = 1) 
        self.convert_button.grid(row = 3, column = 0, 
                                 padx = 0, pady = 15) 
        self.display_button.grid(row = 3, column = 1,  
                                 padx = 10, pady = 15) 
        self.exit_button.grid(row = 3, column = 2, 
                              padx = 10, pady = 15) 
   
    def convert_csv_to_xls(self): 
        try: 
            self.file_name = filedialog.askopenfilename(initialdir = '/Desktop', 
                                                        title = 'Select a CSV file', 
                                                        filetypes = (('csv file','*.csv'), 
                                                                     ('csv file','*.csv'))) 
               
            df = pd.read_csv(self.file_name) 
              
            # Next - Pandas DF to Excel file on disk 
            if(len(df) == 0):       
                msg.showinfo('No Rows Selected', 'CSV has no rows') 
            else: 
                  
                # saves in the current directory 
                with pd.ExcelWriter('GeeksForGeeks.xls') as writer: 
                        df.to_excel(writer,'GFGSheet') 
                        writer.save() 
                        msg.showinfo('Excel file ceated', 'Excel File created')      
               
        except FileNotFoundError as e: 
                msg.showerror('Error in opening file', e) 
   
    def display_xls_file(self): 
        try: 
            self.file_name = filedialog.askopenfilename(initialdir = '/Desktop', 
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
            self.f2 = Frame(self.my_window2, height=200, width=300)  
            self.f2.pack(fill=BOTH,expand=1) 
            self.table = Table(self.f2, dataframe=df,read_only=True) 
            self.table.show() 
          
        except FileNotFoundError as e: 
            print(e) 
            msg.showerror('Error in opening file',e) 

# tkinter window
my_window2 = Tk() # Method window

obj = csv_to_excel(my_window2)

width_window = 800 # Set size width x window
height_window = 600 # Set size height y window
screen_width = my_window2.winfo_screenwidth()
screen_height = my_window2.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_window/2) # Set position window center
y_coordinate = (screen_height/2) - (height_window/2) # Set position window center

my_window2.geometry("%dx%d+%d+%d" % (width_window, height_window, x_coordinate, y_coordinate))
my_window2.title("KLASIFIKASI MUSIK BERDASARKAN GENRE PADA LAYANAN STREAMING MUSIK SPOTIFY MENGGUNAKAN ALGORITMA K–NEAREST NEIGHBOR DAN Modified K–NEAREST NEIGHBOR") # Tittle window
my_window2.configure(bg = "#ADD8E6") # Background
#my_window2.iconbitmap()

my_window2.mainloop()



# Label widgets
judul_1 = Label(my_window1,
                text="Klasifikasi Musik Berdasarkan Genre pada Layanan\nStreaming Musik Spotify Menggunakan algoritma\nK–Nearest Neighbor dan Modified K–Nearest Neighbor",
                bg="#ADD8E6",
                font="times 25 bold italic",
                height=3,
                relief="groove",
                bd=16,
                padx=20)

# Button
button_1 = Button(my_window1,
                    text="Start Program",
                    relief="ridge",
                    bd=10,
                    padx=20)


judul_1.pack() # Set label_1
button_1.pack() # Set Button_1