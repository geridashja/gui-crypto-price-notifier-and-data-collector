import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os,sys
import time
import threading
from crypto_details import * 

root = tk.Tk()

coin_name = ""
def search_coin_clicked():
    if not coin_text.get():
        messagebox.showerror("Error", "Empty Search")
    else:
        coin = coin_text.get()
        coin_name = coin
        kot = Crypto_Details(coin.lower())
        if kot.find_crypto_price(coin.lower()) == None:
            messagebox.showerror("Error", "Your coin does not exist")
        else:
            Coin_Name["text"] = coin.upper()
            price["text"] = kot.find_crypto_price(coin.lower())[coin.lower()]['usd']
            
#title
root.title("CPNDC")
root.geometry("700x400")

#icon
root.iconphoto(False, tk.PhotoImage(file='icons\icon.png'))

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

#text for price
price = tk.Label(root,text = "",font=("bold", 12))
price.grid(row=8,column=2)

def rep():
    search_coin_clicked()
    print(price["text"])
    root.after(5000, rep)
root.after(5000, rep)
root.mainloop()
