"""
Punchcard visualization of my step data
"""

import numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mpdates

Date, Steps = numpy.loadtxt('Steps.csv', delimiter=',',
                            converters={0: mpdates.strpdate2num('%d-%b-%Y %H:%M')},
                            skiprows=1, usecols=(0, 2), unpack=True)

print mpdates.num2date(Date[111]), Steps[111]
plt.plot_date(Date, Steps)
plt.grid(True)
plt.show()
