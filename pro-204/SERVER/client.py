import socket
from threading import Thread
from tkinter import *
import random
from PIL import ImageTk,Image

screen_width=None
screen_height=None

SERVER=None
PORT=None
IP_ADDRESS=None

canvas1=None

playerName=None
nameEntry=None
nameWindow=None

def saveName():
    global SERVER
    global playerName
    global nameEntry
    global nameWindow
    playerName=nameEntry.get()
    nameEntry.delete(0,END)
    SERVER.send(playerName.encode('utf-8'))


def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow =Tk()
    nameWindow.title("TAMBOLA")
    nameWindow.geometry("800x600")
    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./assets/background.png")

    canvas1=Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)

    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/4.5,screen_height/8,text="Enter Name",font=("Chalkboard SE",50),fill="black")

    nameEntry=Entry(nameWindow,width=15,justify="center",font=("Chalkboard SE",30),BD=5,BG="WHITE")

    button=Button(nameWindow,text="Save",font=("Chalkboard SE",30),width=11,command=saveName,height=2,bg="#80deea",bd=3)
    button.place(x=screen_width/6,y=screen_height/4)

    nameWindow.resizable(True,True)
    nameWindow.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT=6000
    IP_ADDRESS='127.0.0.1'

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    askPlayerName()

setup()