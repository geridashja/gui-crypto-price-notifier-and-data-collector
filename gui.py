import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os,sys
import time
from tkcalendar import *
from crypto_details import * 

root = tk.Tk()
# coin_name = ""
def search_coin_clicked():
    if coin_text.get() == "":
        pass
    else:
        coin = coin_text.get()
        # coin_name = coin
        kot = Crypto_Details(coin.lower())
        if kot.find_crypto_price(coin.lower()) == None:
            messagebox.showerror("Error", "Your coin does not exist")
        else:
            Coin_Name["text"] = coin.upper()
            price["text"] = kot.find_crypto_price(coin.lower())[coin.lower()]['usd']
            
def generate_data():
    date = mycal1.get_date()
    kot = Crypto_Details(coin_text.get().lower())
    data = kot.generate_data(date,coin_text.get().lower())
    print(data)

def notify():
    price = price_text.get()
    print(price)
    
#title
root.title("CPNDC")
root.geometry("1000x600")

#icon
root.iconphoto(False, tk.PhotoImage(file='icons\icon.png'))

#search bar for coin
l1 = tk.Label(root,text = "Search Coin",font=("bold", 18))
l1.grid(row=0,column=0, padx=0, pady=0)

coin_text = tk.StringVar()
coin_entry = tk.Entry(root, textvariable=coin_text)
coin_entry.grid(row=1, column=0, padx=0, pady=0)

#button search coin    
Search = tk.Button(root, text="Search Coin",command=search_coin_clicked)
Search.grid(row=2, column=0, padx = 0, pady = 0)

#text for coin name
Coin_Name = tk.Label(root,text = "",font=("bold", 18))
Coin_Name.grid(row=0,column=90,padx = 100)

#text for price
price = tk.Label(root,text = "",font=("bold", 12))
price.grid(row=1,column=90,padx = 100)

#date selection for price history
# l2 = tk.Label(root,text = "Select date for price and other history",font=("bold", 14))
# l2.grid(row=100,column=0)
# mycal1 = Calendar(root,setmode="day", date_pattern = 'd/m/yy')
# mycal1.place(x=220, y=200)
# Generate_Data = tk.Button(root, text="Generate Data",command=generate_data)
# Generate_Data.grid(row=4000, column=0)


# #price you want to get notified
# l3 = tk.Label(root,text = "Price to get notified",font=("bold", 14))
# l3.grid(row=0,column=70)

l2 = tk.Label(root,text = "Enter Price",font=("bold", 18))
l2.grid(row=60,column=0)

price_text = tk.StringVar()
price_entry = tk.Entry(root, textvariable=price_text)
price_entry.grid(row=70, column=0, padx=0, pady=0)

Set_Notifier = tk.Button(root, text="Set Notifier",command=notify)
Set_Notifier.grid(row=80, column=0)
#update the price every 5 seconds
def rep():
    search_coin_clicked()
    print(price["text"])
    root.after(5000, rep)
root.after(5000, rep)


#new window for adding sender, password of sender and your main email

root.mainloop()
