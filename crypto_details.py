from tkinter.constants import N
from tkinter.messagebox import NO
from pycoingecko import CoinGeckoAPI
import pandas as pd
import json
import time
import re

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
    
    def generate_data(self,data,crypto_name):
        #fixing data format getted from user on gui
        new_date = re.sub('/', '-', data)
        print(crypto_name)
        print(new_date)
        print(type(new_date))
        # cg_hist = cg.get_coin_history_by_id(id="bitcoin",date=new_data,localization='false')
        coin_hist = cg.get_coin_history_by_id(id=crypto_name,date=new_date,localization=False,vs_currency="usd")
        #converting json to string in order to normalise
        str_coin_hist = json.dumps(coin_hist)
        data = json.loads(str_coin_hist)
        return data
        # time.sleep(2)
        # print(str_coin_hist)
        # df = pd.json_normalize(data['market_data'])
        # new_df = df.transpose()
        # new_df.insert(0, 'Coin_name', crypto_name)
        # new_df.to_csv(crypto_name+new_date+'.csv')

