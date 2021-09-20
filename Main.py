from tkinter import *
import requests
import socket
from discord_webhook import DiscordWebhook, DiscordEmbed
import os


# Login Window
def loginwin():
    # Window Settings
    window = Tk()
    Icon = PhotoImage(file="C:\\Users\\Windows\\Desktop\\BadPiggies beta 0.1\\Icon.png")
    window.title("BadPiggies Beta 0.1 - Login")
    window.iconphoto(False, Icon)
    window.geometry("350x500")
    window.resizable(0,0)

    j = 0
    r = 0
    for i in range(100):
        c=str(222222+r)
        Frame(window,width=10,height=500,bg="#"+c).place(x=j,y=0)
        j=j+10
        r=r+1
    Frame(window,width=250,height=400,bg="white").place(x=50,y=50)

    # Login Lables
    UsernameLable = Label(window, text="Username", bg="white")
    UsernameLable.config(font=1)
    UsernameLable.place(x=135,y=125)

    PasswordLable = Label(window, text="Password", bg="white")
    PasswordLable.config(font=1)
    PasswordLable.place(x=135,y=250)

    # Login Entries
    UsernameEntry = Entry(window, width=8, border=0)
    UsernameEntry.config(font=1)
    UsernameEntry.place(x=135, y=165)

    PasswordEntry = Entry(window, width=8, border=0)
    PasswordEntry.config(font=1)
    PasswordEntry.place(x=135, y=285)

    # Form Decoration
    Frame(window, width=75, height=2, bg="#141414").place(x=135, y=185)
    Frame(window, width=75, height=2, bg="#141414").place(x=135, y=305)

    # Login Button
    def login():
        if UsernameEntry.get()=="QuePenaHermano!" and PasswordEntry.get()=="DeVerdad":
            window.destroy()
            botwin()


    Button(window, width=20, height=2, fg="white", bg="#994422", border=0, command=login, text="Login!").place(x=100, y=365)

    # Start
    window.mainloop()



def botwin():
    # Window Settings
    window = Tk()
    Icon = PhotoImage(file="C:\\Users\\Windows\\Desktop\\BadPiggies beta 0.1\\Icon.png")
    window.title("BadPiggies Beta 0.1 - Bot")
    window.iconphoto(False, Icon)
    window.geometry("1280x720")
    window.config(bg="gray")



    # Start
    window.mainloop()



