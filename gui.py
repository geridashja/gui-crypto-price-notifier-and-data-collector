import tkinter as tk
from PIL import Image, ImageTk
import os,sys
import time


root = tk.Tk()

#title
blank_space = " "
root.title(90*blank_space+"CPNDC")
root.geometry("700x400")

#backgroud
backgroud = ImageTk.PhotoImage(Image.open("./icons/backgroud.jpg"))  
l= tk.Label(image=backgroud)
l.pack()

root.mainloop()
