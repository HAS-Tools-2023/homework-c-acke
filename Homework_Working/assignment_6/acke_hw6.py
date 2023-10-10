# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:16:21 2023

@author: claire
"""

import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'streamflow_week6.txt'
path = os.path.join('data', file)

path = 'C:/Users/clair/OneDrive/Desktop/HASTools/forecasting/data/streamflow_week6.txt'

data = pd.read_table(path, sep = '\t', skiprows=30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'])

data[['year', 'month', 'day']] = data['datetime'].str.split('-', expand=True)
data['date'] = pd.to_datetime(data['datetime'])
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

monthly_flow = data.groupby(['month'])[['flow']].describe()

sorting = data.sort_values(by='flow', ascending=False)
    
print(data['flow'].quantile([.25, .5, .75]))

#Percentile
forecast = [76, 82]
avg_for = np.average(forecast)
m10p = avg_for * 1.10
b10p = avg_for * .90
within_10p = data[(data['flow'] > b10p) & (data['flow'] < m10p)]


# october = pd.DataFrame()
# mean = pd.DataFrame()
# index = data['datetime'].str[5:7] == '10'
# october['date'] = data['datetime'][index]
# october['year'] = data['year'][index]
# october['streamflow'] = data['flow']
# october['Date'] = pd.to_datetime(october['date'])
# mean['averages'] = october.groupby(october.Date.dt.year)['streamflow'].mean()



