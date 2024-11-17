from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("700x700")


userImage = PhotoImage(file = "rock.png")

user_lbl = Label(
                        image = userImage,
                         )
user_lbl.pack()


root.mainloop()