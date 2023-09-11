# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:48:22 2023

@author: claire
"""

import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'streamflow_week3.txt'
filepath = os.path.join('C:\\Users\\clair\\OneDrive\\Desktop\\HASTools\\forecasting\\data\\', filename)

data = pd.read_table(filepath, sep = '\t', skiprows = 30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'])

data = data.drop(labels = 0, axis = 0)
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

new_flow = [float(x) for x in flow]

new_list = []

# for i in range(len(new_flow)):
#     if new_flow [i] > 95 and month[i] == 9:
#         new_list.append(i)
        
# subset = [new_flow[j] for j in new_list]

# for i in range(len(new_flow)):
#     if new_flow [i] > 89 and month[i] == 9 and year[i] <= 2000: 
#         new_list.append(i)
        
# subset = [new_flow[j] for j in new_list]

for i in range(len(new_flow)):
    if month[i] == 9:
        new_list.append(i)


subset = [new_flow[j] for j in new_list]
