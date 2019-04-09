import tkinter as tk
import playsound
from tkinter import Button, Frame, BOTTOM, RIGHT, TOP
from PIL import Image, ImageTk

# Globals
WIDTH = 394
HEIGHT = 525
FILENAME = 'bass guitar.PNG'

Efile = "C:\\Users\\dbz0w\\PycharmProjects\\Bass-Tuner\\Samples\\E.wav"
Afile = "C:\\Users\\dbz0w\\PycharmProjects\\Bass-Tuner\\Samples\\A.wav"
Dfile = "C:\\Users\\dbz0w\\PycharmProjects\\Bass-Tuner\\Samples\\D.wav"
Gfile = "C:\\Users\\dbz0w\\PycharmProjects\\Bass-Tuner\\Samples\\G.wav"

E = 'E'
A = 'A'
D = 'D'
G = 'G'

# Open the file and resize
bass_guitar_image = Image.open("bass guitar.PNG")
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


"""
def create_configure_window():

    print("Opened Second window")

    new_window = tk.Toplevel()
    new_window.title("String Menu")
    label = tk.Label(new_window, text="Configure")
    label.pack()

    buttonDADG = Button(new_window, text="Set configuration to Drop D (D A D G).", command=set_drop_D)
    buttonDADG.pack()
"""


class GUI:

    root = tk.Tk()
    root.title("Bass Guitar Tuner")
    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack()

    bass_guitar = ImageTk.PhotoImage(bass_guitar_image)
    canvas.create_image(263, 202, image=bass_guitar)

    topFrame = Frame(root)
    topFrame.pack(side=TOP)

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    rightFrame = Frame(root)
    rightFrame.pack(side=RIGHT)

    buttonE = Button(bottomFrame, text=E, command=playE, height = 5, width = 5)
    buttonA = Button(bottomFrame, text=A, command=playA, height = 5, width = 5)
    buttonD = Button(bottomFrame, text=D, command=playD, height = 5, width = 5)
    buttonG = Button(bottomFrame, text=G, command=playG, height = 5, width = 5)

    buttonE.grid(column=0, row=1)
    buttonA.grid(column=1, row=1)
    buttonD.grid(column=2, row=1)
    buttonG.grid(column=3, row=1)

    root.configure(background='black')
    canvas.configure(background='black')

