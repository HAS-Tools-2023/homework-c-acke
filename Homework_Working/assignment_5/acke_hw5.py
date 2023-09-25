# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:02:55 2023

@author: claire
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'streamflow_week5.txt'
filepath = os.path.join('C:\\Users\\clair\\OneDrive\\Desktop\\HASTools\\forecasting\\data\\', filename)
print(os.getcwd())
print(filepath)

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

flow_count = np.sum((flow_data[:,3] > 150) & (flow_data[:,1] == 9))


criteria = (flow_data[:, 3] > 150) & (flow_data[:, 1] == 9)
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)

# Calculate the average flow for the same criteria as above 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 150) & (flow_data[:,1] == 9), 3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

