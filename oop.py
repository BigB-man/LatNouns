import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os
import random
import shutil
from functools import partial
from window import Window

initImage = True

class MainApp(tk.Tk):

    def __init__(self):    
        tk.Tk.__init__(self)
        self.frame = HomePage(self)
        self.frame.pack()
        self.geometry("680x380")
        

    def change(self, frame):
        for widget in self.winfo_children():
            widget.destroy()
        self.frame = frame(self)
        self.frame.pack() # make new frame

    

class HomePage(Window):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        master.title("Home Page")
        print(str(master.winfo_height())+"HHI")
        titleLabel = tk.Label(master.canvas, text="Welcome to the Latin Noun Tester",font=("Arial", 25))
        titleLabel.pack(anchor="center", expand=True)

           
        
            


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()