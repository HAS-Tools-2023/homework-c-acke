# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:33:22 2023

@author: claire
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
# import dataretrieval.nwis as nwis

# %%
# Exercise 1: 
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 
site = '09506000'
start = '1989-01-01'
end = '2020-10-16'
# url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=' + site + \
#     '&referred_module=sw&period=&begin_date=' + start + '&end_date' + end
# data = pd.read_table(url, skiprows = 30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates = ['datetime'], index_col = ['datetime'])

def USGS_river_data(site_flow, start_date, end_date):
    url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=' + site_flow + \
        '&referred_module=sw&period=&begin_date=' + start_date + '&end_date' + end_date
    data = pd.read_table(url, skiprows = 30, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates = ['datetime'], index_col = ['datetime'])
    return(print(data.head()))

USGS_river_data(site, start, end)

# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 



#3. Make a timeseries plot showing the data from all 3 gauges. 