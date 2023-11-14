# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:31:58 2023

@author: claire
"""

import pandas as pd
import matplotlib.pyplot as plt

# LC - could use a comment here. 
file = 'streamflow_week8.txt' #LC you don't need to define file if you are going to write out the filename below you can skip this. 

#LC - you need to have relative paths in order for someone else to be able to run it
path = 'C:/Users/clair/OneDrive/Desktop/HASTools/forecasting/data/streamflow_week8.txt'

data = pd.read_table(path, sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime',
        'flow''code'], parse_dates=['datetime'], index_col=['datetime'])

# I want to make a copy of the data dataframe so I can work with it in a function and not ruin anything
#LC - no need to do this the data is really small and you can just read it in again if you have trouble 
data_copy = data.copy()

# Make some dataframes to pull out this year's October, and Oct-Nov 2022 and 2021
# Want the first one to be a little empty to be on the same timescale

#LC -- this is something you could turn into a function that would take the year an argument and pull out the october flow as a return. 
octnov2023_flow = data.loc['2023'].loc['2023-10-01':'2023-11-30']['flow']
octnov2022_flow = data.loc['2022'].loc['2022-10-01':'2022-11-30']['flow']
octnov2021_flow = data.loc['2021'].loc['2021-10-01':'2021-11-30']['flow']

# Make a function to find the mean of each of these new sets of data
def octnov_meanflow(dataframe):
    vals = dataframe #LC - no need to define 'vals' you can just work from dataframe directly
    mean_vals = vals.mean()
    return mean_vals


octnov_meanflow(octnov2023_flow)

# Plot historical Oct-Nov including what we have from this October
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

# It would be cool to make a function for this, but I'm not positive how especially because the first week is split over October and Nov
# To me, it makes most sense to do some sort of mean for a prediction, but probably for just the two weeks we are forecasting for this week
# oct22to28_all = data[(data.index.month == 10) & (data.index.day >= 22) & (data.index.day <= 28)]

## LC - I would think you could accomplish this using the date function rather than days and months then you can just look for days that are within a specific window of your forecast date. 

#LC To mek this more general you could name the variables something like 1 week and 2 week and have the current date as an input that way you don't have to update everything if you change the date. 
week1_flow = df[(df.index >='2023-10-29') & (df.index <='2023-11-4')]
#Note you could also put this in a function that takes dataframe start and end date as inputs. 

oct29tonov4_all = data[((data.index.month == 10) & (data.index.day >= 29) | (data.index.month == 11) & (data.index.day <= 4))]
nov5to11_all = data[(data.index.month == 11) & (data.index.day >= 5) & (data.index.day <= 11)]


# oct22to28_mean = oct22to28_all.groupby(oct22to28_all.index.year)['flow'].mean()
oct29tonov4_mean = oct29tonov4_all.groupby(oct29tonov4_all.index.year)['flow'].mean()
nov5to11_mean = nov5to11_all.groupby(nov5to11_all.index.year)['flow'].mean()


week1_prediction = oct29tonov4_mean.mean() - 50
week2_prediction = nov5to11_mean.mean() - 50

print('The week one forecast is', week1_prediction, 'cfs')
print('The week two forecast is', week2_prediction, 'cfs')

# Plot the overall means and see where the predictions are
# plt.plot(oct22to28_mean)
plt.plot(nov5to11_mean)
plt.plot(oct29tonov4_mean)
plt.title('Oct22-28, Oct29-Nov4 Historical Mean')
