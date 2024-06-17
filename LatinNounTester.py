import tkinter as tk
from window import Window


class MainApp(tk.Tk):

    def __init__(self):    
        tk.Tk.__init__(self)
        self.frame = HomePage(self)
        self.frame.pack()
        self.geometry("656x369")
        self.iconbitmap("images/SquareNounDeclension.ico")
        

    def change(self, frame):
        for widget in self.winfo_children():
            widget.destroy()
        self.frame = frame(self)
        self.frame.pack() # make new frame
   

class HomePage(Window):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        titleLabel = tk.Label(master.canvas, text="Welcome to the Latin Noun Tester",font=("Arial", 25))
        titleLabel.pack(anchor="center", expand=True)
               

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

