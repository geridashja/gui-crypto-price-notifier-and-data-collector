from tkinter.constants import N
from tkinter.messagebox import NO
from pycoingecko import CoinGeckoAPI
import pandas as pd
import threading
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

