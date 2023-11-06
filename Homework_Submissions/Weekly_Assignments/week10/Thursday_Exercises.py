## Exercises for thursday's class


import pandas as pd
import matplotlib.pyplot as plt 


# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'], index_col = ['datetime'], parse_dates =['datetime'])
# print(data.info)
# print(data.index)

# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 
daymet_data = pd.read_csv('daymet.csv', index_col = ['date'], parse_dates = ['date'])

#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 
# print(daymet_data.info())
#There is the date as the index, year, yday, dayl, prcp, srad, swe, tmax, tmin, vp 
#Date range: 9-25-1992 to 9-25-2022, daily data

#2.3  Make a scatter plot of day length (dayl) vs maximum temperature. Fit a trend line 
# plt.set_size_inches(10,10)
plt.scatter(daymet_data['dayl (s)'], daymet_data['tmax (deg c)'], s = 5)


#2.4 Make a plot with three lines (1) average, (2) min and (3) max shortwave radiation (srad) vs the day of the year (i.e. 1-365)
#Hint: use the pandas resample function for datetime objects and the plt.fill type for the shading
