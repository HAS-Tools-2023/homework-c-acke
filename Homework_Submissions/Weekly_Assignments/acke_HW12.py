# -*- coding: utf-8 -*-
"""
@author: claire
"""

import pandas as pd
import matplotlib.pyplot as plt
import json
import urllib.request as req
import urllib
from sklearn import datasets, linear_model

#read in usgs data 
site = '09506000'
start = '1989-01-01'
end = '2023-11-16'

url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=' + site + \
    '&referred_module=sw&period=&begin_date=' + start + '&end_date' + end
data = pd.read_table(url, skiprows = 30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates = ['datetime'], index_col = ['datetime'])
#Let's get this November and later try to find the linear regression, specifically the slope
nov_flow = data.loc['2023'].loc['2023-11-01':'2023-11-15']['flow']
nov_flow = nov_flow.to_frame()
nov_flow['days'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#read in second dataset
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

#November precip
nov_precip = precip_resample.loc['2023'].loc['2023-11-01':'2023-11-16']['Precip']
nov_precip = nov_precip.to_frame()
nov_precip['days'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Let's check out the precip around the area of interest
plt.plot(nov_precip.index, nov_precip['Precip'])
#Wow not much going on this month 


#Plot 
length = 15
x = nov_flow['days'].values
y = nov_flow['flow'].values

x = x.reshape(length, 1)
y = y.reshape(length, 1)
x = x.astype('float64')

regr = linear_model.LinearRegression()
regr.fit(x, y)
slope = regr.coef_
#2.45

plt.plot(x, y, label = 'November Flow')
plt.plot(x, regr.predict(x), color = 'red', label = 'Linear Regression')
plt.plot(nov_precip['days'], nov_precip['Precip'], label = 'Precip at Dry Park')
plt.title('November Flow with Linear Regression Prediction')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Flow')





