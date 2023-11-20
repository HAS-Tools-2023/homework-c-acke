# %%
#Claire Acke
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
# import dataretrieval.nwis as nwis
import json
import urllib.request as req
import urllib

# %%
# Exercise 1: 
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 
site = '09506000'
start = '1989-01-01'
end = '2023-11-13'
# url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=' + site + \
#     '&referred_module=sw&period=&begin_date=' + start + '&end_date' + end
# data = pd.read_table(url, skiprows = 30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates = ['datetime'], index_col = ['datetime'])

def USGS_river_data(site_flow, start_date, end_date):
    url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=' + site_flow + \
        '&referred_module=sw&period=&begin_date=' + start_date + '&end_date' + end_date
    data = pd.read_table(url, skiprows = 30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates = ['datetime'], index_col = ['datetime'])
    return(print(data.head()))

# USGS_river_data(site, start, end)

# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 
start = '2023-01-01'
end = '2023-11-13'

clarkdale = USGS_river_data(siteID='09504950', start_date=start, end_date=end)
camp_verde = USGS_river_data(siteID='09504950', start_date=start, end_date=end)
paulden = USGS_river_data(siteID='09503700', start_date=start, end_date=end)

#3. Make a timeseries plot showing the data from all 3 gauges. 
ax = plt.axes()
ax.plot(camp_verde['flow'], color= 'red', linestyle = 'dashed', label = 'Camp Verde')
ax.plot(clarkdale['flow'], color= 'blue', linestyle = 'dashed', label = 'Clarkdale')
ax.plot(paulden['flow'], color= 'green', linestyle = 'dashed', label = 'Paulden')

ax.set(title="Observed Flow", xlabel="Date",
       ylabel="log(Streamflow [cfs])",
       yscale='log')
ax.legend()


# %%
# Exercise 2: 

#1. Download the dataset from the class notes and determine what (1) type of python object the station observations are and (2) what all variables are included in the observations. 
# Dictonary, with datetime and observations variables
mytoken = '47b8b8d2ff1848b9a48a598f4e453829'
base_url = 'http://api.mesowest.net/v2/stations/timeseries'

args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
# print(apiString)

fullUrl = base_url + '?' + apiString
#Now request the data
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())


#2. Modify the API call to return accumulated precipitation instead (variable name = 'precip_accum', set the units to 'metric') and make a plot of the daily max accumulated precipitation
mytoken = '47b8b8d2ff1848b9a48a598f4e453829'
base_url = 'http://api.mesowest.net/v2/stations/timeseries'

args = {
    'start': '202301010000',
    'end': '202311160000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QDPA3',
    'units': 'metric',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)

fullUrl = base_url + '?' + apiString
#Now request the data
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip_acum = responseDict["STATION"][0]['OBSERVATIONS']['precip_accum_set_1']

units = responseDict['UNITS']

precip_data = pd.DataFrame({'Precip': precip_acum}, index = pd.to_datetime(dateTime))
precip_resample = precip_data.resample('D').max()



