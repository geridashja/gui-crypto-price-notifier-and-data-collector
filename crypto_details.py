from tkinter.constants import N
from tkinter.messagebox import NO
from pycoingecko import CoinGeckoAPI
import pandas as pd
import json
import time
import re
import requests 
# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
# result = requests.get(url.format(city, get_api()))

url = "https://alpha-vantage.p.rapidapi.com/query"
querystring = {"market":"USD","symbol":"btc","function":"DIGITAL_CURRENCY_MONTHLY"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "30462a1579mshdd8d5a103d6c66bp16425djsnb3fddb396e98"
    }


cg = CoinGeckoAPI()

class Crypto_Details:
    def __init__(self,crypto_name):
        self.crypto_name = crypto_name
    def get_all_crypto(self):
        all_cryptos = cg.get_coins_list()
        return all_cryptos
    
    def find_crypto_price(self,crypto_name):     
        price = cg.get_price(ids=crypto_name, vs_currencies='usd')
        if price:
            return price
        else:
            return None
    
    def generate_data(self,data,symbol):
        if data == "Daily Data":
            data = "DIGITAL_CURRENCY_DAILY"
        if data == "Weekly Data":
            data = "DIGITAL_CURRENCY_WEEKLY"
        if data == "Monthly Data":
            data = "DIGITAL_CURRENCY_MONTHLY"

        # querystring['symbol'] = symbol
        # querystring['function'] = data
        response = requests.request("GET", url, headers=headers, params=querystring)
        if(response):
            print(response.text)
        else:
            print("No response")

