# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:12:51 2023

@author: claire
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


## Import the flow data to use
data = pd.read_table("./streamflow_demo.txt",  sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

## Plot 1: Simple line plot
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
y1=np.sin(x)
y2=np.cos(x)
plt.style.use('Solarize_Light2')
ax = plt.axes()
ax.plot(x, y1, linestyle='dashed', label='sinx', color='blue')
ax.plot(x, y2, label='cosx', color='red')
plt.axhline(y = 0, color = 'black')
ax.legend(loc='upper right')
plt.title('Comparing sine and cosine')
plt.ylim(-1.5, 1.5)
plt.xlim(-10, 10)
plt.grid(True, color = 'grey', linewidth=1)



## Plot 2: Scatter Plot
plt.style.use('default')
ax=data.plot.scatter(x='month', y='flow',
                     c='year', colormap='viridis', marker='x')
ax.set_title("Monthly stream Flow")

## Plot 3: Histogram 
mybins = np.linspace(0, np.log10(np.max(data["flow"])), num=15)
plt.hist(np.log10(data["flow"]), bins=mybins)
plt.title('Streamflow')
plt.ylabel('Count')

## Plot 4: Filled plot
monthly_max = data.groupby(data.month).max()
monthly_min = data.groupby(data.month).min()
monthly_mean = data.groupby(data.month)["flow"].mean()

ax = plt.axes()
ax.plot(monthly_mean)
ax.fill_between(monthly_min.flow.index,
                monthly_min.flow.values, monthly_max.flow.values, alpha=0.2)
ax.set_yscale("log")
ax.set_xlabel("month")
plt.axvline(3, color='black', linestyle='--')