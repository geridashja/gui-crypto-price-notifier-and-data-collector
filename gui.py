import tkinter as tk
from PIL import Image, ImageTk
import os,sys
import time


root = tk.Tk()

#title
blank_space = " "
root.title(90*blank_space+"CPNDC")
root.geometry("700x400")

#background
filename = ImageTk.PhotoImage(Image.open("./icons/backgroud.jpg"))
background_label = tk.Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#search bar
city_text = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.pack()

Search = tk.Button(root, text="Search Weather")
Search.pack()

root.mainloop()
