# %% Setup- before you start create a new 'mapping' environment following the instructions from class and make sure you have the following packages installed
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx

# %%
# Exercise 1: 
# 1. Open the arizona_huc8_shapefil and the arizona_shapefile following the example we did in class. 
arizona_huc8_file = 'C://Users//clair//OneDrive//Desktop//HASTools//forecasting//data//arizona_huc8_shapefile//WBDHU8.shp'
arizona_huc8 = gpd.read_file(arizona_huc8_file)
arizona_shape_file = 'C://Users//clair//OneDrive//Desktop//HASTools//forecasting//data//arizona_shapefile//tl_2016_04_cousub.shp'
arizona_shape = gpd.read_file(arizona_shape_file)

# 2. Explore their properties and attributes and be able to explain (1) what type of geometry each is, (2) how many features there are, (3) what attributes each feature has. 
type(arizona_huc8)
arizona_huc8.head()
arizona_huc8.columns
arizona_huc8.shape

type(arizona_shape)
arizona_shape.head()
arizona_shape.columns
arizona_shape.shape

# 3. Plot each dataset. You can plot them separately but also try plotting subsets and plotting them on top of each other. 
#fig, ax = plt.subplots(figsize = (10, 10))
#arizona_huc8.plot(ax = ax)

gages_AZ = arizona_huc8[arizona_huc8['states'] == 'AZ']
gages_AZ.shape

fig, ax = plt.subplots(figsize = (10, 10))
arizona_shape.plot(ax = ax)
gages_AZ.plot(ax = ax, color = 'grey')
#%%
# Exercise 2: 
# 1. Open the WBD_15_HU2_GDB geodatabase and select a different layer to plot than the one I showed (i.e. not HUC6)
geobase_file = 'C:/Users/clair/OneDrive/Desktop/HASTools/forecasting/data/WBD_15_HU2_GDB/WBD_15_HU2_GDB.gdb'
fiona.listlayers(geobase_file)
HU8 = gpd.read_file(geobase_file, layer = 'WBDHU8')

# type(HU16)
# HU16.head()
# 2. Create a geodatabase with the two points of interest I showed (i.e. UA and the stream gauge) as well as two additional points of your choosing

# fig, ax = plt.subplots(figsize = (10,10))
# HU16.plot(ax = ax)
# ax.set_title('HUC16 Boundaries')

#Add points to plot
# UA:  32.22877495, -110.97688412
# Stream gauge:  34.44833333, -111.7891667
# Flagstaff: 35.1983, -111.6513
# Nothing, AZ: 34.4800, -113.3359
locations_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333], [-111.6513, 35.1983], [-113.3359, 34.4800]])
#Make them into spatial features
point_geom = [Point(xy) for xy in locations_list]
point_geom

#Make a dataframe of this 
points_df = gpd.GeoDataFrame(point_geom, columns = ['geometry'], crs = HU8.crs)


#3. Make a map of your selected datasets. If you have time experiment with changing the markers and lines/fill colors on your plot 
fig, ax = plt.subplots(figsize = (10, 10))
HU8.plot(ax = ax)
points_df.plot(ax = ax, color = 'red', marker = 'o')
ax.set_title('HUC8 Boundaries')



