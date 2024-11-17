from tkinter import *
from PIL import Image, ImageTk
from Customers import Customers

class SMS :
    def __init__(self, root) :
        self.root = root
        self.root.geometry("1360x700+0+0")
        self.root.config(bg = "palegreen")
        self.root.title("Shop Management System | Developed by Vedant")
        
        self.root.icon_image = PhotoImage(file = "images/logo1.png")

        title = Label(
                      self.root,
                      text = "Shop Management System",
                      font = ("times of now", 20, "bold"),
                      fg = "White",
                      bg = "darkBlue",
                      pady = 20,
                      image = self.root.icon_image,
                      padx = 20,
                      compound = LEFT,
                      anchor = "w"
                      ).place(x = 0, y = 0, relwidth = 1, height = 70)
        logout_button = Button(
                               self.root,
                               text = "Logout",
                               bg = "yellow",
                               font = ("times of now", 15, "bold"),
                               anchor = "w",
                               cursor = "hand2"
                               ).place(x = 1200, y = 20, height = 30, width = 80)

        self.label_clock = Label(
                                text = "\t\t\tWelcome to Shop Management System\t\t\t\tDate : DD/MM/YYYY\t\t\t\tTime : HH : MM : SS",
                                bg = "grey",
                                fg = "white",
                                anchor = "w",
                                font = ("times of now", 10),                                
                                ).place(x = 0, y = 70, relwidth = 1, height = 30)
        

        LeftMenu = Frame(
                        self.root,
                         bg = "white",
                         bd = 2,
                         relief = RIDGE
                         )
        LeftMenu.place(x = 0, y = 100, width = 200, height = 535)

        self.menu_icon = Image.open("images/menu_im.png")
        self.menu_icon = self.menu_icon.resize((200, 300))
        self.menu_icon = ImageTk.PhotoImage(self.menu_icon)

        lbl_menu_icon = Label(
                              LeftMenu,
                              image = self.menu_icon
                              )
        lbl_menu_icon.pack(side = TOP, fill = X)

        Menu = Label(
                     LeftMenu,
                     text = "Menu",
                     font = ("times of now", 15, "bold"),
                     bg = "darkBlue",
                     fg = "white"
                     ).pack(side = TOP, fill = X)

        self.btn_logo = PhotoImage(file = "images/side.png")

        Customer_btn = Button(
                              LeftMenu,
                              text = "Customers",
                              bg = "white",
                              image = self.btn_logo,
                              font = ("times of now", 15, "bold"),
                              bd = 2,
                              command = self.AddCustomers,
                              padx = 5,
                              anchor = "w",
                              relief = RIDGE,
                              compound = LEFT,
                              cursor = "hand2",
                              width = 250
                              ).pack()

        Products_btn = Button(
                              LeftMenu,
                              text = "Products",
                              bg = "white",
                              image = self.btn_logo,
                              font = ("times of now", 15, "bold"),
                              bd = 2,
                              relief = RIDGE,
                              cursor = "hand2",
                              width = 250,
                              padx = 5,
                              anchor = "w",
                              compound = LEFT,
                              ).pack()
        
        catogry_btn = Button(
                              LeftMenu,
                              text = "Category",
                              bg = "white",
                              image = self.btn_logo,
                              font = ("times of now", 15, "bold"),
                              bd = 2,
                              compound = LEFT,
                              relief = RIDGE,
                              cursor = "hand2",
                              padx = 5,
                              anchor = "w",
                              width = 250
                              ).pack()

        Sales_btn = Button(
                              LeftMenu,
                              text = "Sales",
                              bg = "white",
                              image = self.btn_logo,
                              compound = LEFT,
                              font = ("times of now", 15, "bold"),
                              bd = 2,
                              width = 250,
                              relief = RIDGE,
                              padx = 5,
                              anchor = "w",
                              cursor = "hand2"
                              ).pack()

        exit_btn = Button(
                              LeftMenu,
                              text = "Exit",
                              bg = "white",
                              image = self.btn_logo,
                              font = ("times of now", 15, "bold"),
                              bd = 2,
                              padx = 5,
                              anchor = "w",
                              relief = RIDGE,
                              compound = LEFT,
                              cursor = "hand2",
                              width = 250
                              ).pack()

        footer = Label(
                       self.root,
                       text = "Shop Mangement System | Developed by Vedant\nFor any Technical Queries Contact :- 9767133965",
                       bg = "gray"
                       ).pack(side = BOTTOM, fill = X)
        
        Total_CS = Button(
                        self.root,
                        text = "Total Customers",
                        bg = "orange",
                        fg = "white",
                        width = 15,
                        bd = 2,
                        relief = RIDGE,                        
                        height = 5,
                        cursor = "hand2",
                        font = ("goundy old style", 15, "bold")
                        ).place(x = 300, y = 170)

        Products = Button(
                        self.root,
                        text = "Products",
                        bg = "yellow",
                        fg = "white",
                        width = 15,
                        height = 5,
                        cursor = "hand2",
                        bd = 2,
                        relief = RIDGE,
                        font = ("goundy old style", 15, "bold")
                        ).place(x = 900, y = 170)

        Sales = Button(
                        self.root,
                        text = "Sales",
                        bg = "blue",
                        fg = "white",
                        width = 15,
                        height = 5,
                        cursor = "hand2",
                        bd = 2,
                        relief = RIDGE,
                        font = ("goundy old style", 15, "bold")
                        ).place(x = 300, y = 470)

        category = Button(
                        self.root,
                        text = "Category",
                        bg = "red",
                        fg = "white",
                        width = 15,
                        height = 5,
                        cursor = "hand2",
                        bd = 2,
                        relief = RIDGE,
                        font = ("goundy old style", 15, "bold")
                        ).place(x = 900, y = 470)

    def AddCustomers(self) :
        self.new_win = Toplevel(self.root)
        self.new_obj = Customers(self.new_win)


if __name__ == "__main__" :
    root = Tk()
    ob1 = SMS(root)
    root.mainloop()