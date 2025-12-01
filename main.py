import tkinter
from tkinter import Label

from tkinter import *

root = tkinter.Tk()

root.title("Hello world")
root.geometry("300x250")
root.iconbitmap(default="icon1.ico")

label_1_Hello_world = tkinter.Label(text = "Hello world!!!")
label_1_Hello_world.pack()

root.mainloop()