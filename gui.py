import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os,sys
import time
from tkcalendar import *
from crypto_details import * 

root = tk.Tk()
coin_name = ""
def search_coin_clicked():
    if coin_text.get() == "":
        pass
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
root.geometry("1000x600")

#icon
root.iconphoto(False, tk.PhotoImage(file='icons\icon.png'))

#search bar for coin
l1 = tk.Label(root,text = "Search Coin",font=("bold", 18))
l1.grid(row=0,column=0)

coin_text = tk.StringVar()
coin_entry = tk.Entry(root, textvariable=coin_text)
coin_entry.grid(row=2, column=0, padx=3, pady=3)

#button search coin    
Search = tk.Button(root, text="Search Coin",command=search_coin_clicked)
Search.grid(row=3, column=0, padx = 0, pady = 0)

#text for coin name
Coin_Name = tk.Label(root,text = "",font=("bold", 18))
Coin_Name.grid(row=7,column=4)

#text for price
price = tk.Label(root,text = "",font=("bold", 12))
price.grid(row=8,column=4)

#date selection for price history
l2 = tk.Label(root,text = "Select date length for price and other history",font=("bold", 14))
l2.grid(row=100,column=0)

    #start date
l3 = tk.Label(root,text = "Start date & End Date",font=("bold", 14))
l3.grid(row=200,column=0)
mycal = Calendar(root,setmode="day", date_pattern = 'd/m/yy')
mycal.place(x=0, y=200)

    #end date
mycal2 = Calendar(root,setmode="day", date_pattern = 'd/m/yy')
mycal2.place(x=300, y=200)

#update the price every 5 seconds
def rep():
    search_coin_clicked()
    print(price["text"])
    root.after(5000, rep)
root.after(5000, rep)

root.mainloop()
