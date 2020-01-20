import tkinter as tk
import playsound
from tkinter import *
from PIL import Image, ImageTk

# Globals
WIDTH = 394
HEIGHT = 525
FILENAME = 'bass_guitar.PNG'

# Change these depending on system location.
Efile = "../Samples/4E.wav"
Afile = "../Samples/3A.wav"
Dfile = "../Samples/2D.wav"
Gfile = "../Samples/1G.wav"

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


def updateDropD():
    E_string.set("D")
    global Efile
    Efile = "../Samples/4D.wav"

    A_string.set("A")
    global Afile
    Afile = "../Samples/3A.wav"

    D_string.set("D")
    global Dfile
    Dfile = "../Samples/2D.wav"

    G_string.set("G")
    global Gfile
    Gfile = "../Samples/1G.wav"

    print("Updated to Drop D")

def updateDropC():
    E_string.set("C")
    global Efile
    Efile = "../Samples/4C.wav"

    A_string.set("A")
    global Afile
    Afile = "../Samples/3A.wav"

    D_string.set("D")
    global Dfile
    Dfile = "../Samples/2D.wav"

    G_string.set("G")
    global Gfile
    Gfile = "../Samples/1G.wav"

    print("Updated to Drop C")


def updateFullStep():
    E_string.set("D")
    global Efile
    Efile = "../Samples/4D.wav"

    A_string.set("G")
    global Afile
    Afile = "../Samples/3G.wav"

    D_string.set("C")
    global Dfile
    Dfile = "../Samples/2C.wav"

    G_string.set("F")
    global Gfile
    Gfile = "../Samples/1F.wav"

    print("Updated to Full Step")


def updateFullStepDropC():
    E_string.set("C")
    global Efile
    Efile = "../Samples/4C.wav"

    A_string.set("G")
    global Afile
    Afile = "../Samples/3G.wav"

    D_string.set("C")
    global Dfile
    Dfile = "../Samples/2C.wav"

    G_string.set("F")
    global Gfile
    Gfile = "../Samples/1F.wav"

    print("Updated to Full Step (Drop C)")


def updateStd():
    E_string.set("E")
    global Efile
    Efile = "../Samples/4E.wav"

    A_string.set("A")
    global Afile
    Afile = "../Samples/3A.wav"

    D_string.set("D")
    global Dfile
    Dfile = "../Samples/2D.wav"

    G_string.set("G")
    global Gfile
    Gfile = "../Samples/1G.wav"

    print("Updated to Standard Tuning")



root = tk.Tk()
root.title("Bass Guitar Tuner by Brian Sukhnandan")
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

E_string = tk.StringVar()
E_string.set("E")

A_string = tk.StringVar()
A_string.set("A")

D_string = tk.StringVar()
D_string.set("D")

G_string = tk.StringVar()
G_string.set("G")

bass_guitar = ImageTk.PhotoImage(bass_guitar_image)
canvas.create_image(263, 202, image=bass_guitar)

topFrame = Frame(root)
topFrame.pack(side=TOP)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Change Tuning', menu=filemenu)
filemenu.add_command(label='Standard Tuning', command=updateStd)
filemenu.add_command(label='Drop D', command=updateDropD)
filemenu.add_command(label='Drop C', command=updateDropC)
filemenu.add_command(label='Full Step', command=updateFullStep)
filemenu.add_command(label='Full Step (Drop C)', command=updateFullStepDropC)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

buttonE = Button(bottomFrame, textvariable=E_string, command=playE, height = 5, width = 5)
buttonA = Button(bottomFrame, textvariable=A_string, command=playA, height = 5, width = 5)
buttonD = Button(bottomFrame, textvariable=D_string, command=playD, height = 5, width = 5)
buttonG = Button(bottomFrame, textvariable=G_string, command=playG, height = 5, width = 5)

buttonE.grid(column=0, row=1)
buttonA.grid(column=1, row=1)
buttonD.grid(column=2, row=1)
buttonG.grid(column=3, row=1)

root.configure(background='black')
canvas.configure(background='black')

root.mainloop()
