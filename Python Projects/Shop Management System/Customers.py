from tkinter import *
from PIL import Image, ImageTk

class Customers :
    def __init__(self, root) :
        self.root = root
        self.root.geometry("1120x530+210+130")
        self.root.config(bg = "orange")
        self.root.title("Shop Management System | Developed by Vedant")
        self.root.focus_force()

        title = Label(
                      self.root,
                      text = "Search Customer",
                      font = ("goundy old style", 15, "bold"),
                      bg = "Blue",
                      fg = "white",
                      height = 2
                      ).pack(side = TOP, fill = X)
        
        name_lbl = Label(
                         self.root,
                         text = "Name",
                         font = ("goundy old style", 10, "bold"),
                         bg = "orange"
                         ).place(x = 330, y = 80, width = 50,height = 30)
                        

        Name = Entry(
                     self.root,
                     bg = "white",
                     font = ("goundy old style", 10, "bold")
                     ).place(x = 330, y = 110, width = 330, height = 50)

        Save_btn = Button(
                         self.root,
                         text = "Search",
                         cursor = "hand2",
                         fg = "white",
                         bg = "green",
                         bd = 2,
                         relief = RIDGE,
                         font = ("goundy old style", 10, "bold")
                         ).place(x = 680, y = 120, width = 100, height = 30)

        New_customer = Label(
                            self.root,
                            text = "Add New Customer",
                            fg = "white",
                            bg = "red",
                            font = ("goundy old style", 20, "bold")
                             ).place(x = 0, y = 200, height = 50, relwidth = 1) 

        new_Name = Entry(
                     self.root,
                     bg = "white",
                     font = ("goundy old style", 10, "bold")
                     ).place(x = 330, y = 300, width = 330, height = 50)

        Add_btn = Button(
                         self.root,
                         text = "Add",
                         cursor = "hand2",
                         fg = "white",
                         bg = "green",
                         bd = 2,
                         relief = RIDGE,
                         font = ("goundy old style", 10, "bold")
                         ).place(x = 680, y = 310, width = 100, height = 30)

        add_lbl = Label(
                         self.root,
                         text = "Name",
                         font = ("goundy old style", 10, "bold"),
                         bg = "orange"
                         ).place(x = 330, y = 270, width = 50,height = 30)
             

if __name__ == "__main__" :
    root = Tk()
    ob1 = Customers(root)
    root.mainloop()