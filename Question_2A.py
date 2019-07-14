#Final Program for Question 2A.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import csv
count = 1
data = []
with open('calendar.csv','rt', encoding='cp850')as f:
    csv_data = csv.reader(f, )
    flag = True
    for row in csv_data:
        if flag:
            flag = False
            continue
        if row[2] == 'f':
            data.append(row[1])

avail_map = {}
for date in data:
    date_str = date.split('.')[0]
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    day = date_obj.timetuple().tm_yday
    if day in avail_map.keys():
        avail_map[day] += 1
    else:
        avail_map[day] = 1


customers = []
days = list(range(1,365))
for day in days:
    if day in avail_map.keys():
        count = avail_map[day]
        customers.append(count)
    else:
        customers.append(0)
#plot customers per day from 'f' availability
plt.plot(days, customers, linestyle = ':')
