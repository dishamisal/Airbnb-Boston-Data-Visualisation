#Final program for Question 2B

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def price_format(price):
    if price.count('$'):
        price = price.split('$')[1]
    try:
        return float(price)
    except:
        return 0

import csv
count = 1
data = []
with open('C:/Users/Disha/Desktop/Data Science/calendar.csv','rt', encoding='cp850')as f:
    csv_data = csv.reader(f, )
    flag = True
    for row in csv_data:
        if flag:
            flag = False
            continue
        data.append((row[1], price_format(row[3])))

price_map = {}
for date, price in data:
    date_str = date.split('.')[0]
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    day = date_obj.timetuple().tm_yday
    if day in price_map.keys():
        (old_price, count) = price_map[day]
        price_map[day] = (old_price + price, count + 1)
    else:
        price_map[day] = (price, 1)

prices = []
days = list(range(1,365))
for day in days:
    if day in price_map.keys():
        (price, count) = price_map[day]
        prices.append(price/count)
    else:
        prices.append(0)

#plot average price per day
plt.plot(days, prices, linestyle = ':')
