import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os,sys
import time


root = tk.Tk()

def search_coin_clicked():
    if not coin_text.get():
        messagebox.showerror("Error", "Empty Search")
    else:
        coin = coin_text.get()
        Coin_Name["text"] = coin
#title
root.title("CPNDC")
root.geometry("700x400")

#icon
root.iconphoto(False, tk.PhotoImage(file='icons\icon.png'))

#background
# filename = ImageTk.PhotoImage(Image.open("./icons/backgroud.jpg"))
# background_label = tk.Label(root, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

#search bar for coin
coin_text = tk.StringVar()
coin_entry = tk.Entry(root, textvariable=coin_text)
coin_entry.grid(row=0, column=0, padx=3, pady=3)

#button search coin
Search = tk.Button(root, text="Search Coin",command=search_coin_clicked)
Search.grid(row=1, column=0, padx = 0, pady = 0)

#text for coin name
Coin_Name = tk.Label(root,text = "",font=("bold", 18))
Coin_Name.grid(row=7,column=2)

root.mainloop()
