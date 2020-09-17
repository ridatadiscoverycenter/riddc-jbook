<a href="https://colab.research.google.com/github/austinbennysmith/OSOM-ERDDAP/blob/master/Wind_%26_Wind_Stress.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Wind and Wind Stress

This notebook will try to map wind and wind stress over some of the waters near Rhode Island, using the NOAA/NCDC datasets in the [RIDDC ERDDAP server](https://pricaimcit.services.brown.edu/erddap/index.html).

**Note: The urls used in this code constrain latitude & longitude in a way that may or may not be ideal. I haven't yet figured out what the best lat/lon constraints are for this.**

!pip install netCDF4
import requests
from netCDF4 import Dataset as NetCDFFile
import matplotlib.pyplot as plt
#To use cartopy in a Colab notebook, I need a particular sequence of installs (as shown at this notebook: https://colab.research.google.com/github/adamlamee/CODINGinK12/blob/master/notebooks/quakes.ipynb#scrollTo=3LkZkXvnMAr4)
!apt-get -qq install python-cartopy python3-cartopy;
!pip uninstall -y shapely;
!pip install shapely --no-binary shapely;
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from matplotlib.axes import Axes
from cartopy.mpl.geoaxes import GeoAxes
GeoAxes._pcolormesh_patched = Axes.pcolormesh

The following code should make a pcolormesh of wind speed, but as you can see, it is not working for some reason...

#the code dealing with datetime here is based on code at this link: https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
#from google.colab import drive
#drive.mount('/content/gdrive')
#images_dir = '/content/gdrive/Shared drives/BFK_BOG/SURF_UG/Benny/Images/erdMH1par08day'
import numpy as np
from datetime import date, timedelta
#generating a list of dates:
dates2 = []
start_date = date(2003, 1, 5) #can change dates if you want. This may  or may not be the actual start date of the dataset, and the end date will change as it is updated
end_date = date(2020, 5, 20)
delta = timedelta(weeks=20)
while start_date<=end_date:
  dates2.append(str(start_date))
  start_date += delta
#I got the following url interactively from the ERDDAP server:
url = 'https://pricaimcit.services.brown.edu/erddap/griddap/ncdcOw6hr_LonPM180.nc?u[(2011-09-30T18:00:00Z):1:(2011-09-30T18:00:00Z)][(10):1:(10.0)][(40.5):1:(42.25)][(-72.75):1:(-69.75)],v[(2011-09-30T18:00:00Z):1:(2011-09-30T18:00:00Z)][(10):1:(10.0)][(40.5):1:(41.5)][(-72.65):1:(-70.25)]'
r = requests.get(url, allow_redirects=True)
open('test.nc', 'wb').write(r.content)
nc = NetCDFFile('test.nc')
nc
#defining some variables from the dataset:
lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
time = nc.variables['time'][:]
u = nc.variables['u'][:]
v = nc.variables['v'][:]
#plotting:
plt.pcolormesh(lon, lat, v[0, 0, :, :])
plt.colorbar()
plt.show()
plt.pcolormesh(lon, lat, u[0, 0, :, :])
plt.colorbar()
plt.show()
#since it's not working right now, I haven't bothered to finish with labeling

Graphing wind stress seems to work better, although it is very low resolution. This code will make pcolormesh plots of wind stress for the x and y components separately. Then I attempt to make a quiver plot for it.

#the code dealing with datetime here is based on code at this link: https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
import numpy as np
from datetime import date, timedelta
import xarray as xr
dates2 = []
start_date = date(2003, 1, 5) #can change dates if you want
end_date = date(2020, 5, 20)
delta = timedelta(weeks=20)
while start_date<=end_date:
  dates2.append(str(start_date))
  start_date += delta
#making a url, opening the dataset:
url = 'https://pricaimcit.services.brown.edu/erddap/griddap/ncdcOwDlyStrs_LonPM180.nc?taux[(2002-05-01T09:00:00Z):1:(2002-05-01T09:00:00Z)][(0.0):1:(0.0)][(40.5):1:(42.25)][(-72.75):1:(-69.75)],tauy[(2002-05-01T09:00:00Z):1:(2002-05-01T09:00:00Z)][(0.0):1:(0.0)][(40.5):1:(42.25)][(-72.75):1:(-69.75)]'
#url = 'https://pricaimcit.services.brown.edu/erddap/griddap/ncdcOwDlyStrs_LonPM180.nc?taux[(1987-07-09T09:00:00Z):1:(2011-09-30T09:00:00Z)][(0.0):1:(0.0)][(40.5):1:(42.25)][(-72.75):1:(-69.75)],tauy[(1987-07-09T09:00:00Z):1:(2011-09-30T09:00:00Z)][(0.0):1:(0.0)][(40.5):1:(42.25)][(-72.75):1:(-69.75)]'
r = requests.get(url, allow_redirects=True)
open('test.nc', 'wb').write(r.content)
nc = NetCDFFile('test.nc')
nc
#defining some dataset variables:
lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
time = nc.variables['time'][:]
u = nc.variables['taux'][:]
v = nc.variables['tauy'][:]
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines(resolution='10m', color = 'red')
ax.set_extent([287.25, 290.25, 40.5, 42.25])
plt.pcolormesh(lon, lat, v[0, 0, :, :])
plt.colorbar()
plt.show()
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines(resolution='10m', color = 'red')
ax.set_extent([287.25, 290.25, 40.5, 42.25])
plt.pcolormesh(lon, lat, u[0, 0, :, :])
plt.colorbar()
plt.show()

print(len(u))
print(u)
#ax = plt.axes(projection = ccrs.PlateCarree())
#ax.coastlines(resolution='10m', color = 'red')
#ax.set_extent([287.25, 290.25, 40.5, 42.25])
plt.quiver(lon, lat, u[0,0,:,:], v[0,0,:,:], angles='xy')
plt.show()

