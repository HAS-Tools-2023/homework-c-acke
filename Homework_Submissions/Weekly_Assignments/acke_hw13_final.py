# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:37:47 2023

@author: claire
"""

from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# User input for forecast
# The forecast is one week and two weeks from the date of forecast generation

# LC - you are correct to have these in all caps because you are setting them as constants. 
FORECAST_DATE = '2022-10-1'

# Define the USGS parameters
SITE_USGS = '09506000'
START_DATE = '1989-01-01'
# LC it would be nice to have your end date be set automatically from your forecast date. Could they just be the same thing or is there a reason this one needs to be two days earlier? 
END_DATE = '2023-11-25'

# Make functions to assist with pulling data
# LC - Very nice doc strings that even include examples! Also nice job pulling your functions to the top of the script this makes it easier to read. 
def pull_usgs_data(start, end):
    """
    Retrieve USGS water flow data for a specified site and time range.

    Parameters:
    - site_id (str): The USGS site identifier.
    - start (str): The start date for data retrieval in the format 'YYYY-MM-DD'.
    - end (str): The end date for data retrieval in the format 'YYYY-MM-DD'.

    Returns:
    - pd.DataFrame: A Pandas DataFrame containing USGS water flow data, with columns:
        - 'agency_cd': Agency code
        - 'site_no': Site number
        - 'datetime': Date and time of the measurement
        - 'flow': Water flow data
        - 'code': Code associated with the data

    Example:
    >>> site_id = '09506000'
    >>> start_date = '2023-01-01'
    >>> end_date = '2023-01-31'
    >>> water_data = pull_usgs_data(site_id, start_date, end_date)
    >>> print(water_data.head())
                agency_cd   site_no    flow  code
        datetime
        2023-01-01    USGS  09506000  150.0     A
        2023-01-02    USGS  09506000  160.0     A
        2023-01-03    USGS  09506000  145.0     A
        2023-01-04    USGS  09506000  140.0     A
        2023-01-05    USGS  09506000  155.0     A
    """

    url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=' + SITE_USGS + \
        '&referred_module=sw&period=&begin_date=' + start + '&end_date' + end
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                                  'datetime', 'flow', 'code'],
                         parse_dates=['datetime'], index_col=['datetime'])
    return data

def calculate_mean(data, period, column, start, end):
    """
    Calculate the mean of a specified column in a Pandas DataFrame over a specified time period.

    Parameters:
    - data (pd.DataFrame): Input DataFrame containing time-series data.
    - period (str): Resampling period, e.g., 'D' for daily, 'W' for weekly.
    - column (str): Name of the column for which the mean is calculated.
    - start (str): Start date for the time period in the format 'YYYY-MM-DD'.
    - end (str): End date for the time period in the format 'YYYY-MM-DD'.

    Returns:
    - pd.Series: A Pandas Series containing the mean values over the specified time period.

    Example:
    >>> import pandas as pd
    >>> data = pd.DataFrame({'datetime': pd.date_range('2023-01-01', '2023-01-31'),
    ...                      'flow': [150.0, 160.0, 145.0, 140.0, 155.0]})
    >>> data = data.set_index('datetime')
    >>> start_date = '2023-01-01'
    >>> end_date = '2023-01-31'
    >>> period = 'W'
    >>> column_name = 'flow'
    >>> mean_values = calculate_mean(data, period, column_name, start_date, end_date)
    >>> print(mean_values)
    datetime
    2023-01-01    150.0
    2023-01-08    152.5
    2023-01-15    142.5
    2023-01-22    140.0
    2023-01-29    155.0
    Freq: W-SUN, Name: flow, dtype: float64
    """

    dataframe = data[start:end]
    flow_mean = dataframe.resample(period).mean(column)
    return flow_mean

# Now, let's grab the data that we want using the function
usgs_data = pull_usgs_data(START_DATE, END_DATE)

# Name variables for analysis
# LC -- note that the comment above doesn't really description what is happening below.  A little more detail in teh comment would help. 
# LC - nice job using the datetime functionality to make your date math easier and cleaner to follow. 

forecast_date_dt = datetime.strptime(FORECAST_DATE, '%Y-%m-%d').date()
month_start = forecast_date_dt - timedelta(days=14)
month_end = forecast_date_dt + timedelta(days=14)
week1_forecast_date = forecast_date_dt + timedelta(days=7)
week2_forecast_date = forecast_date_dt + timedelta(days=14)

# Break down the data
data_month = usgs_data[month_start:month_end]

# Calculate the mean flow per week in the month
# LC - I'm getting an error here because the mean_weekly is not actually returning anything. I wonder if its because the month end is in the future (i.e. it puts the month end as 12/11/2023
mean_weekly = calculate_mean(data_month, 'W', 'flow', month_start, month_end)
# I'm a little confused about exactly what is happening here I can't check very well because this part isn't working but I wonder if you could get the same result by just setting the index from the beginning rather than first resetting the index and then dropping and setting an new one? 
mean_weekly = mean_weekly.reset_index()
mean_weekly['date'] = mean_weekly['datetime'].dt.date
mean_weekly = mean_weekly.drop(['datetime'], axis=1)
mean_weekly = mean_weekly.set_index('date')

# Calculate differences
# LC differences between what? Expand your comment a bit. 
difference = mean_weekly['flow'][1] - mean_weekly['flow'][0]

# Create week 1 and 2 forecasts based off of the mean difference
week1_forecast = mean_weekly['flow'][1] + difference
week2_forecast = week1_forecast + difference
forecast = pd.DataFrame({'date': [week1_forecast_date, week2_forecast_date],
                         'forecast': [week1_forecast, week2_forecast]})
forecast = forecast.set_index('date')

# Create a dataframe with the past two weeks and the next 2-week outlook
outlook = pd.DataFrame()
outlook['flows'] = pd.concat([mean_weekly['flow'], forecast['forecast']])

# Create a plot showing the last two weeks, along with the 2-week forecast
plt.plot(outlook.index, outlook['flows'], marker='o')
plt.title('Forecasted Flow')
plt.xlabel('Date')
plt.ylabel('Flow (cfs)')

# Display the plot
plt.show()

print('Week one forecast is:', week1_forecast)
print('Week two forecast is:', week2_forecast)
