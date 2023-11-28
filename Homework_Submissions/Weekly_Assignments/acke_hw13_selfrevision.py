# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:36:58 2023

@author: claire
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# User input for forecast (date that you are creating the forecast)
forecast_date = '2023-11-27'

# Define the USGS parameters
site_usgs = '09506000' 
start_date = '1989-01-01'
end_date = '2023-11-25'

# Make functions to assist with pulling data
def pull_usgs_data(station_id, start, end):
    url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=' + site_usgs + \
        '&referred_module=sw&period=&begin_date=' + start + '&end_date' + end
    data = pd.read_table(url, skiprows = 30, names = ['agency_cd', 'site_no', 
                                                      'datetime', 'flow', 'code'],
                         parse_dates = ['datetime'], index_col = ['datetime'])
    return data
    
# I am unsure how to make a function with a linear regression because it is so finicky, so
# I'm going to switch it up this week and utilize a mean like I used to since it makes the 
# most sense for my forecasts conceptually
def calculate_mean(data, period, column, start, end):
    df = data[start:end]
    flow_mean = df.resample(period).mean(column) 
    return flow_mean

# Now, let's grab the data that we want using the function
usgs_data = pull_usgs_data(site_usgs, start_date, end_date)

# Name variables for analysis
forecast_date_dt = datetime.strptime(forecast_date, '%Y-%m-%d').date()
month_start = forecast_date_dt - timedelta(days=14)
month_end = forecast_date_dt + timedelta(days=14)
week1_forecast_date = forecast_date_dt + timedelta(days=7)
week2_forecast_date = forecast_date_dt + timedelta(days=14)

# Break down the data
data_month = usgs_data[month_start:month_end]

# Calculate the mean flow per week in month
mean_weekly = calculate_mean(data_month, 'W', 'flow', month_start, month_end)
mean_weekly  = mean_weekly.reset_index()
mean_weekly['date'] = mean_weekly['datetime'].dt.date
mean_weekly = mean_weekly.drop(['datetime'], axis=1)
mean_weekly = mean_weekly.set_index('date')

# Calculate differences
difference = mean_weekly['flow'][1] - mean_weekly['flow'][0]

# Create week 1 and 2 forecasts based off of the mean difference
week1_forecast = mean_weekly['flow'][1] + difference
week2_forecast = week1_forecast + difference
forecast = pd.DataFrame({'date': [week1_forecast_date, week2_forecast_date], 
                         'forecast': [week1_forecast, week2_forecast]})
forecast = forecast.set_index('date')

# Create a dataframe with the past two weeks and next 2 week outlook 
outlook = pd.DataFrame()
outlook['flows'] = pd.concat([mean_weekly['flow'], forecast['forecast']])

# Create plot showing the last two weeks, along with the 2 week forecast
plt.plot(outlook.index, outlook['flows'], marker='o')
plt.title('Forecasted Flow')
plt.xlabel('Date')
plt.ylabel('Flow (cfs)')
