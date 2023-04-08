# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:57:20 2023

@author: HP
"""

import requests
import datetime
import pandas as pd

url1 = "https://realstonks.p.rapidapi.com/AAPL"
url2 = "https://realstonks.p.rapidapi.com/NFLX"
url3 = "https://realstonks.p.rapidapi.com/GOOG"
url4 = "https://realstonks.p.rapidapi.com/AMZN"


headers = {
	"X-RapidAPI-Key": "d559911da8msh459bc68cbab598bp1ac69bjsnaf7d7204d005",
	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
}

for step in range(1,101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    col = [time_stamp]
    response_aapl = requests.request("GET", url1, headers=headers)
    response_nflx = requests.request("GET", url2, headers=headers)
    response_goog = requests.request("GET", url3, headers=headers)
    response_amzn = requests.request("GET", url4, headers=headers)
    
    value_aapl = float(response_aapl.text.split(',')[0][10:])  # Convert response text to float
    value_nflx = float(response_nflx.text.split(',')[0][10:])  # Convert response text to float
    value_goog = float(response_goog.text.split(',')[0][10:])  # Convert response text to float
    value_amzn = float(response_amzn.text.split(',')[0][10:])  # Convert response text to float
    
    price.append(value_aapl)
    price.append(value_nflx)
    price.append(value_goog)
    price.append(value_amzn)
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('./real time stock data.csv',mode='a',header = False)
    print(col)