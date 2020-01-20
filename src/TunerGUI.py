import tkinter as tk
import playsound
from tkinter import *
from PIL import Image, ImageTk

# Globals
WIDTH = 394
HEIGHT = 525
FILENAME = 'bass_guitar.PNG'

# Change these depending on system location.
Efile = "../Samples/E.wav"
Afile = "../Samples/A.wav"
Dfile = "../Samples/D.wav"
Gfile = "../Samples/G.wav"

A_string = 'A'
D_string = 'D'
G_string = 'G'

# Open the file and resize
bass_guitar_image = Image.open("../images/bass_guitar.PNG")
bass_guitar_image = bass_guitar_image.resize((HEIGHT, WIDTH), Image.ANTIALIAS)

# TODO: Import WAV files


def playE():
    playsound.playsound(Efile)
    print("Played an E")


def playA():
    playsound.playsound(Afile)
    print("Played an A")


def playD():
    playsound.playsound(Dfile)
    print("Played a D")


def playG():
    playsound.playsound(Gfile)
    print("Played a G")


def updateDropD(string):
    string.set("D")
    print("Updated to Drop D")


class GUI:
    root = tk.Tk()
    root.title("Bass Guitar Tuner")
    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack()

    E_string = tk.StringVar()

    bass_guitar = ImageTk.PhotoImage(bass_guitar_image)
    canvas.create_image(263, 202, image=bass_guitar)

    topFrame = Frame(root)
    topFrame.pack(side=TOP)

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='Change Tuning', menu=filemenu)
    filemenu.add_command(label='Drop D', command=updateDropD(E_string))
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)


    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    rightFrame = Frame(root)
    rightFrame.pack(side=RIGHT)

    buttonE = Button(bottomFrame, textvariable=E_string, command=playE, height = 5, width = 5)
    E_string.set("Test")

    buttonA = Button(bottomFrame, text=A_string, command=playA, height = 5, width = 5)
    buttonD = Button(bottomFrame, text=D_string, command=playD, height = 5, width = 5)
    buttonG = Button(bottomFrame, text=G_string, command=playG, height = 5, width = 5)

    buttonE.grid(column=0, row=1)
    buttonA.grid(column=1, row=1)
    buttonD.grid(column=2, row=1)
    buttonG.grid(column=3, row=1)

    root.configure(background='black')
    canvas.configure(background='black')
