"""
Plotting OpenPaths data on a map
"""

import numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mpdates

#~ lat,lon,alt,date,device,os,version
#~ 49.9761505127,8.00768661499,86.5952682495,2014-01-18 16:17:04,"iPhone4,1",7.0.4,1.1



Lat, Lon, Altitude, Date, = numpy.loadtxt('openpaths_habi.csv', delimiter=',',
                            converters={3: mpdates.strpdate2num('%Y-%m-%d %H:%M:%S')},
                            skiprows=1, usecols=(0, 1, 2, 3), unpack=True)
plt.plot_date(Date, Altitude)
plt.xlabel('Date')
plt.ylabel('Altitude')
plt.show()

# We could use [Folium](http://folium.readthedocs.org/en/latest/) to present the map...
import folium
WhichOne = 666
print 'Centering map on Lat: %s and Lon: %s' % (Lat[WhichOne], Lon[WhichOne])
whereabouts = folium.Map(location=[Lat[WhichOne], Lon[WhichOne]],
                         tiles='Stamen Toner')
for i in range(WhichOne-333,WhichOne+333):
    whereabouts.simple_marker([Lat[i], Lon[i]], popup='Datapoint %s' % i)
whereabouts.create_map(path='map.html')
