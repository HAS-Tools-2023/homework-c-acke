import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'streamflow_week7.txt'
path = os.path.join('data', file)

path = 'C:/Users/clair/OneDrive/Desktop/HASTools/forecasting/data/streamflow_week7.txt'

data = pd.read_table(path, sep = '\t', skiprows=30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'])

data[['year', 'month', 'day']] = data['datetime'].str.split('-', expand=True)
data['date'] = pd.to_datetime(data['datetime'])
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

monthly_flow = data.groupby(['month'])[['flow']].describe()

sorting = data.sort_values(by='flow', ascending=False)

#Plotting overall view of parameters
fig, axs = plt.subplots(2,2)
axs[0,0].plot(monthly_flow['flow']['min'])
axs[0,0].set_ylabel('Flow (cfs)')
axs[0,0].set_xticks([0, 2, 4, 6, 8, 10, 12])
axs[0,1].plot(monthly_flow['flow']['25%'])
axs[0,1].set_xticks([0, 2, 4, 6, 8, 10, 12])
axs[1,0].plot(monthly_flow['flow']['50%'])
axs[1,0].set_ylabel('Flow (cfs)')
axs[1,0].set_xlabel('Month')
axs[1,0].set_xticks([0, 2, 4, 6, 8, 10, 12])
axs[1,1].plot(monthly_flow['flow']['75%'])
axs[1,1].set_xlabel('Month')
axs[1,1].set_xticks([0, 2, 4, 6, 8, 10, 12])
fig.suptitle('Monthly Min Flow and Quartile (25%, 50%, 75%)')

#Plotting monthly mean
plt.bar(monthly_flow.index.values, monthly_flow['flow']['mean'])
plt.xlabel('Month')
plt.ylabel('Flow (cfs)')
plt.title('Monthly Mean Flow Values')

#Plotting std
plt.bar(monthly_flow.index.values, monthly_flow['flow']['std'])
plt.xlabel('Month')
plt.ylabel('Flow (cfs)')
plt.title('Monthly Standard Deviation Flow Values')

#Plotting max values
plt.plot(monthly_flow['flow']['max'])
plt.xlabel('Month')
plt.ylabel('Flow (cfs)')
plt.title('Monthly Maximum Flow Values')

#Plot a spicy plot that idk if it will work
plt.plot(monthly_flow['flow']['mean'])
plt.fill_between(monthly_flow.index.values, monthly_flow['flow']['min'], monthly_flow['flow']['max'], color='orange')
plt.ylabel('Flow (cfs)')
plt.xlabel('Month')
plt.title('Flow Mean within Min and Max Values')
plt.ylim(0, 1100)
plt.legend()

# print(data['flow'].quantile([.25, .5, .75]))

#Percentile
# forecast = [76, 82]
# avg_for = np.average(forecast)
# m10p = avg_for * 1.10
# b10p = avg_for * .90
# within_10p = data[(data['flow'] > b10p) & (data['flow'] < m10p)]