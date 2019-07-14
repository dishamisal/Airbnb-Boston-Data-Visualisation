import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import csv
count = 1
data = []
listing_map = {}
with open('C:/Users/Disha/Desktop/Data Science/calendar.csv','rt', encoding='cp850')as f:
    csv_data = csv.reader(f, )
    flag = True
    for row in csv_data:
        if flag:
            flag = False
            continue
        if row[3] == 'f':
            data.append((row[1]))
        if row[1] in listing_map:
            listing_map[row[1]].add(row[0])
        else:
            listing_map[row[1]] = {row[0]}


avail_map = {}
for date in data:
    date_str = date.split('.')[0]
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    day = date_obj.timetuple().tm_yday
    if day in avail_map.keys():
        count = avail_map[day]
        avail_map[day] = count + 1
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
#plt.plot(days, customers, linestyle = ':')

listing_map_day = {}
for date, listings in listing_map.items():
    date_str = date.split('.')[0]
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    day = date_obj.timetuple().tm_yday
    listing_map_day[day] = listings

sorted(listing_map_day)
#sorted(listing_map_day)

buffer_listings = {}
new_listings = []
days = list(range(1, 365))
for day in days:
    if day in listing_map_day.keys():
        print(len(listing_map_day[day]))
        if not buffer_listings:
            buffer_listings = listing_map_day[day]
            new_listings.append(0)
        else:
            n = 0
            for l in listing_map_day[day]:
                if l not in buffer_listings:
                    buffer_listings.add(l)
                    
                    n+=1
            new_listings.append(n) 
    else:
        new_listings.append(0)
#print(listing_map_day.keys())

#plot new listings count
plt.plot(days, new_listings, linestyle = ':')

#plt.plot(days,customers,":",
#days,new_listings,"*-")



