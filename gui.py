import tkinter as tk
from tkinter import mainloop, messagebox
import re
import time
from tkcalendar import *
from crypto_details import * 
from send_mail import *


root = tk.Tk()
def search_coin_clicked():
    if coin_text.get() == "":
        pass
    else:
        coin = coin_text.get()
        kot = Crypto_Details(coin.lower())
        if kot.find_crypto_price(coin.lower()) == None:
            messagebox.showerror("Error", "Your coin does not exist")
        else:
            Coin_Name["text"] = coin.upper()
            price["text"] = kot.find_crypto_price(coin.lower())[coin.lower()]['usd']
            
def generate_data():
    date = date_duration.get()
    # kot = Crypto_Details(coin_text.get().lower())
    # data = kot.generate_data(date,coin_text.get().lower())
    print(date)

def add_emails_window():
    print("New Window Button Opened")
    global newWindow
    newWindow = tk.Toplevel(root)
    newWindow.title("Add Emails for Notifications")
    newWindow.geometry("400x400")
    newWindow.iconphoto(False, tk.PhotoImage(file='icons\icon.png'))
    tk.Label(newWindow).grid()

    global email_text
    global password_text
    global main_email_text
    #1
    l1 = tk.Label(newWindow,text = "Sender Email",font=("bold", 18))
    l1.grid(row=0,column=0, padx=0, pady=0)
    email_text = tk.StringVar()
    email_entry = tk.Entry(newWindow, textvariable=email_text)
    email_entry.grid(row=1, column=0, padx=0, pady=(10,0))
    #2
    l2 = tk.Label(newWindow,text = "Password of Sender",font=("bold", 18))
    l2.grid(row=3,column=0, padx=0, pady=0)
    password_text = tk.StringVar()
    password_entry = tk.Entry(newWindow, textvariable=password_text)
    password_entry.grid(row=4, column=0, padx=0, pady=(10,0))
    #3
    l3 = tk.Label(newWindow,text = "Main Email",font=("bold", 18))
    l3.grid(row=5,column=0, padx=0, pady=0)
    main_email_text = tk.StringVar()
    main_email_entry = tk.Entry(newWindow, textvariable=main_email_text)
    main_email_entry.grid(row=6, column=0, padx=0, pady=(10,0))
    #button
    Add = tk.Button(newWindow, text="Add",command=get_emails)
    Add.grid(row=8, column=0, padx = 0, pady = 10)

credentials = []
def get_emails():
    global sender_email,sender_password,main_email
    sender_email = email_text.get()
    sender_password = password_text.get()
    main_email = main_email_text.get()
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if (sender_email == "") or (sender_password == "") or (main_email == ""):
        messagebox.showerror("Error", "You must fill all the fields")
    else:
        if email_regex.match(sender_email) == False:
            messagebox.showerror("Error", "Please enter a valid email")
        elif email_regex.match(sender_email) == False:
            messagebox.showerror("Error", "Please enter a valid email")
        else:
            newWindow.destroy()
    credentials.append(sender_email)
    credentials.append(sender_password)
    credentials.append(main_email)

def notify():
    if credentials == []:
        pass
    else:
        sender_email = credentials[0]
        sender_password = credentials[1]
        main_email = credentials[2]
        notify = Send_Mail(sender_email,sender_password,main_email)
        if(float(price_text.get()) == float(price["text"])):
            print("EQUAL")
            notify.send_main()
            tk.messagebox.showinfo("BUY IT", "EMAIL SENT")
            time.sleep(2)
            root.destroy()
        else:
            print("Waiting desired price!")
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
Coin_Name = tk.Label(root,text = "",font=("bold", 18),fg ="green")
Coin_Name.grid(row=3,column=0,pady=(20,0))

#text for price
price = tk.Label(root,text = "",font=("bold", 12),fg ="green")
price.grid(row=4,column=0)

# #price you want to get notified
l2 = tk.Label(root,text = "Enter Price",font=("bold", 18))
l2.grid(row=100,pady=(20,0))

price_text = tk.StringVar()
price_entry = tk.Entry(root, textvariable=price_text)
price_entry.grid(row=110, column=0, padx=0, pady=0)

Set_Notifier = tk.Button(root, text="Set Notifier",command=notify)
Set_Notifier.grid(row=120, column=0,pady=0)

#date selection for price history
l3 = tk.Label(root,text = "Select Historical Data Duration",font=("bold", 14))
l3.grid(row=0,column=100,padx=(300,0))

date_duration = tk.StringVar()
date_duration.set("Daily Data")
drop = tk.OptionMenu(root,date_duration,"Daily Data", "Weekly Data","Monthly Data")
drop.grid(row=1, column=100,padx=(300,0))

Generate_Data = tk.Button(root, text="Generate Data",command=generate_data)
Generate_Data.grid(row=4, column=100,padx=(300,0))

# new window button
New_Window = tk.Button(root, text="Add Emails for Notifications",command=add_emails_window)
New_Window.grid(row=400, column=0,pady=(20,0))

#update the price every 5 seconds
def rep():
    search_coin_clicked()
    notify()
    print(price["text"])
    root.after(5000, rep)

root.after(5000, rep)

root.mainloop()
