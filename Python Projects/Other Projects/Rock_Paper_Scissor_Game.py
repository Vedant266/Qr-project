from tkinter import *
from PIL import Image, ImageTk
import random

class Game : 
    def __init__(self, root) :
        self.root = root
        self.root.geometry("1360x730")
        self.root.maxsize(1360, 730)
        self.root.config(bg = "violet")
        self.root.title("Rock Paper Scissor Game Developed By Vedant")
        self.computerChoice = None

        uI1 = Image.open("Rock.jpeg")
        uI2 = Image.open("Paper.jpeg")
        uI3 = Image.open("Scissor.jpeg")
        
        u_1 = uI1.resize((300, 300), Image.Resampling.LANCZOS)
        u_2 = uI2.resize((300, 300), Image.Resampling.LANCZOS)
        u_3 = uI3.resize((300, 300), Image.Resampling.LANCZOS)

        userImage1 = ImageTk.PhotoImage(u_1)
        userImage2 = ImageTk.PhotoImage(u_2)
        userImage3 = ImageTk.PhotoImage(u_3)

        title = Label(
                      self.root,
                      text = "Rock Paper Scisssor Game",
                      font = ("times new roman", 20, "bold"),
                      bg = "darkblue",
                      fg = "white" 
                      ).pack(fill = X)
        
        youLabel = LabelFrame(
                             self.root,
                             width = 300,
                             height = 300
                             ).place(x = 150, y = 200)
        
        comLabel = LabelFrame(
                             self.root,
                             width = 300,
                             height = 300
                            ).place(x = 900, y = 200)
        
        showScore = Label(
                         self.root,
                         text = 0,
                         font = ("times new roman", 50, "bold"),
                         bg = "violet"
                          )
        showScore.place(x = 600, y = 300)
        
        Column = Label(
                         self.root,
                         text = ":",
                         font = ("times new roman", 50, "bold"),
                         bg = "violet"
                          ).place(x = 675, y = 295)        

        showComScore = Label(
                         self.root,
                         text = 0,
                         font = ("times new roman", 50, "bold"),
                         bg = "violet"
                          )
        showComScore.place(x = 730, y = 300)

        rock_btn = Button(
                        self.root,
                        text = "Rock",
                        font = ("times new roman", 15, "bold"),
                        bg = "skyblue",
                        bd = 2,
                        command =  lambda : self.Rock(self.computerChoice, userImage1, userImage2, userImage3, rock_btn, paper_btn, scissor_btn, showScore, showComScore), 
                        relief = "ridge",
                        cursor = "hand2",
                        height = 1,
                        width = 15
                        )
        rock_btn.place(x = 400, y = 550)

        paper_btn = Button(
                        self.root,
                        command =  lambda : self.Paper(self.computerChoice, userImage1, userImage2, userImage3, rock_btn, paper_btn, scissor_btn, showScore, showComScore),
                        text = "Paper",
                        font = ("times new roman", 15, "bold"),
                        bg = "yellow",
                        bd = 2,
                        relief = "ridge",
                        cursor = "hand2",
                        height = 1,
                        width = 15
                        )
        paper_btn.place(x = 590, y = 550)

        scissor_btn = Button(
                        self.root,
                        text = "Scissor",
                        font = ("times new roman", 15, "bold"),
                        bg = "orange",
                        command = lambda : self.Scissor(self.computerChoice, userImage1, userImage2, userImage3, rock_btn, paper_btn, scissor_btn, showScore, showComScore),
                        bd = 2,
                        relief = "ridge",
                        height = 1,
                        width = 15,
                        cursor = "hand2"
                        )
        scissor_btn.place(x = 780, y = 550)
        
        reset_btn = Button(
                            self.root,
                            text = "Restart",
                            font = ("times new roman", 15, "bold"),
                            bg = "white",
                            cursor = "hand2",
                            command = lambda : self.reset(showComScore, showScore, self.com_lbl, self.user_lbl, self.winlbl, userImage1)
                            )
        reset_btn.place(x = 1150, y = 60)

        quit_btn = Button(
                            self.root,
                            text = "Quit",
                            font = ("times new roman", 15, "bold"),
                            bg = "red",
                            width = 7,
                            cursor = "hand2",
                            fg = "white",
                            command = self.Quit
                            )
        quit_btn.place(x = 1250, y = 60)

        com_lbl = Label(
                        image = userImage1
                        )
        com_lbl.place(x = 900, y = 200)

        user_lbl = Label(
                        image = userImage1,
                         )
        user_lbl.place(x = 150, y = 200)

    def Rock(self, computerChoice, userImage1, userImage2, userImage3, rock_btn, paper_btn, scissor_btn, showScore, showComScore) :

        computerChoice = self.updateImages() 

        self.user_lbl = Label(
                        image = userImage1,
                         )
        self.user_lbl.place(x = 150, y = 200)

        if(computerChoice == "Rock") : 
            self.com_lbl = Label(
                            image = userImage1
                            )
            self.com_lbl.place(x = 900, y = 200)
            
            self.winlbl = Label(
                self.root,
                text = "Game Tie",
                font = ("times new roman", 30, "bold"),
                bg = "white",
                padx = 5
                )
            self.winlbl.place(x = 600, y = 80)

        elif(computerChoice == "Paper") : 
            self.com_lbl = Label(
                            image = userImage2
                            )
            self.com_lbl.place(x = 900, y = 200)
            
            self.winlbl = Label(
                self.root,
                text = "You Lose",
                font = ("times new roman", 30, "bold"),
                bg = "Red",
                fg = "white",
                padx = 10
                )
            self.winlbl.place(x = 600, y = 80)

            self.updateComScore(showComScore)

        elif(computerChoice == "Scissor") : 
            self.com_lbl = Label(
                            image = userImage3
                            )
            self.com_lbl.place(x = 900, y = 200)
            
            self.winlbl = Label(
                self.root,
                text = "You Won",
                font = ("times new roman", 30, "bold"),
                bg = "yellow",
                padx = 10
                )
            self.winlbl.place(x = 600, y = 80)
            
            self.updateUserScore(showScore)



    def Paper(self, computerChoice, userImage1, userImage2, userImage3, rock_btn, paper_btn, scissor_btn, showScore, showComScore) :

        computerChoice = self.updateImages()

        self.user_lbl = Label(
                        image = userImage2,
                         )
        self.user_lbl.place(x = 150, y = 200)

        if(computerChoice == "Rock") : 
            self.com_lbl = Label(
                            image = userImage1
                            )
            self.com_lbl.place(x = 900, y = 200)
            
            self.winlbl = Label(
                self.root,
                text = "You Won",
                font = ("times new roman", 30, "bold"),
                bg = "yellow",
                padx = 10
                )
            self.winlbl.place(x = 600, y = 80)
            
            self.updateUserScore(showScore )

        elif(computerChoice == "Paper") : 
            self.com_lbl = Label(
                            image = userImage2
                            )
            self.com_lbl.place(x = 900, y = 200)
            
            self.winlbl = Label(
                self.root,
                text = "Game Tie",
                font = ("times new roman", 30, "bold"),
                bg = "white",
                padx = 5
                )
            self.winlbl.place(x = 600, y = 80)
            
        elif(computerChoice == "Scissor") : 
            self.com_lbl = Label(
                            image = userImage3
                            )
            self.com_lbl.place(x = 900, y = 200)
            
            self.winlbl = Label(
                self.root,
                text = "You Lose",
                font = ("times new roman", 30, "bold"),
                bg = "red",
                fg = "white",
                padx = 10
                )
            self.winlbl.place(x = 600, y = 80)

            self.updateComScore(showComScore)

    def Scissor(self, computerChoice, userImage1, userImage2, userImage3, rock_btn, paper_btn, scissor_btn, showScore, showComScore) :

            computerChoice = self.updateImages()

            self.user_lbl = Label(
                            image = userImage3,
                            )
            self.user_lbl.place(x = 150, y = 200)
            
            if(computerChoice == "Rock") : 
                self.com_lbl = Label(
                                image = userImage1
                                )
                self.com_lbl.place(x = 900, y = 200)
                
                self.winlbl = Label(
                    self.root,
                    text = "You Lose",
                    font = ("times new roman", 30, "bold"),
                    bg = "red",
                    fg = "white",
                    padx = 10
                    )
                self.winlbl.place(x = 600, y = 80)
                
                self.updateComScore(showComScore)

            elif(computerChoice == "Paper") : 
                self.com_lbl = Label(
                                image = userImage2
                                )
                self.com_lbl.place(x = 900, y = 200)
                
                self.winlbl = Label(
                    self.root,
                    text = "You Won",
                    font = ("times new roman", 30, "bold"),
                    bg = "yellow",
                    padx = 10
                    )
                self.winlbl.place(x = 600, y = 80)
                
                self.updateUserScore(showScore)

            elif(computerChoice == "Scissor") : 
                self.com_lbl = Label(
                                image = userImage3
                                )
                self.com_lbl.place(x = 900, y = 200)

                self.winlbl = Label(
                    self.root,
                    text = "Game Tie",
                    font = ("times new roman", 30, "bold"),
                    bg = "white",
                    padx = 5
                    )
                self.winlbl.place(x = 600, y = 80)

    def updateUserScore(self, showUserScore) :

        showUserScore['text'] += 1
        
    def updateComScore(self, showComScore) :

        showComScore['text'] += 1

    def updateImages(self) :
            options = ["Rock", "Paper", "Scissor"]

            cChoice = random.choice(options)
            return cChoice

    def Quit(self) : 
        exit()
                       
    def reset(self, showComScore, showUserScore, user_lbl, com_lbl, winlbl, userImage3) :
        showUserScore['text'] = 0
        showComScore['text'] = 0
        user_lbl['image'] = userImage3
        com_lbl['image'] = userImage3
        winlbl['text'] = None
        winlbl['bg'] = "violet"
        winlbl['fg'] = "violet"
        reset_lb =Label(self.root,
                        bg = "violet",
                        width = 50,
                        height = 3)
        reset_lb.place(x = 595, y = 80)

root = Tk() 
obj = Game(root)
root.mainloop()