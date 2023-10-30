# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:31:22 2023

@author: claire
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 'streamflow_week8.txt'
path = 'C:/Users/clair/OneDrive/Desktop/HASTools/forecasting/data/streamflow_week8.txt'

data = pd.read_table(path, sep = '\t', skiprows=30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates = ['datetime'], index_col = ['datetime'])

#Make some dataframes to pull out this year's October, and Oct-Nov 2022 and 2021
#Want the first one to be a little empty to be on the same timescale
octnov2023_flow = data.loc['2023'].loc['2023-10-01':'2023-11-30']['flow']
octnov2022_flow = data.loc['2022'].loc['2022-10-01':'2022-11-30']['flow']
octnov2021_flow = data.loc['2021'].loc['2021-10-01':'2021-11-30']['flow']
# octnov2020_flow = data.loc['2020'].loc['2020-10-01':'2020-11-30']['flow']
# octnov2019_flow = data.loc['2019'].loc['2019-10-01':'2019-11-30']['flow']
# octnov2018_flow = data.loc['2018'].loc['2018-10-01':'2018-11-30']['flow']

#Plot historical Oct-Nov including what we have from this October
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.supylabel('Average Daily Flow (cfs)')
fig.supxlabel('Day')
fig.suptitle('Daily Flow Oct-Nov')

ax1.plot(octnov2023_flow)
ax1.title.set_text('2023')
ax1.set_xticks([])

ax2.plot(octnov2022_flow)
ax2.title.set_text('2022')
ax2.set_xticks([])

ax3.plot(octnov2021_flow)
ax3.title.set_text('2021')
ax3.set_xticks([])

#To me, it makes most sense to do some sort of mean for a prediction, but probably for just the two weeks we are forecasting for this week
oct22to28_all = data[(data.index.month == 10) & (data.index.day >= 22) & (data.index.day <= 28)]
oct29tonov4_all = data[((data.index.month == 10) & (data.index.day >= 29) | (data.index.month == 11) & (data.index.day <= 4))]

oct22to28_mean = oct22to28_all.groupby(oct22to28_all.index.year)['flow'].mean()
oct29tonov4_mean = oct29tonov4_all.groupby(oct29tonov4_all.index.year)['flow'].mean()

week1_prediction = oct22to28_mean.mean() 
week2_prediction = oct29tonov4_mean.mean() 

print('The week one forecast is', week1_prediction, 'cfs')
print('The week two forecast is', week2_prediction, 'cfs')

#Plot the overall means and see where the predictions are
plt.plot(oct22to28_mean)
plt.plot(oct29tonov4_mean)
plt.title('Oct22-28, Oct29-Nov4 Historical Mean')


