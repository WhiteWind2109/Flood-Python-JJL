import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime
from floodsystem.analysis import polyfit

def do_something(x):
    """A useless function just for pytest"""
    return x

def plot_water_levels(station, dates, levels):
    """Given a station and lists of dates and levels
        this function plot levels against dates for the station"""

    t = []
    for date in dates:
        t.append(datetime(date.year, date.month, date.day))
    # Plot
    plt.plot(t, levels)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("{}".format(station.name))
    # Display plot
    plt.tight_layout() # This makes sure plot does not cut off date labels
    plt.show()
    
def plot_water_level_with_fit(station, dates, levels, p):
	poly, d0 = polyfit(dates, levels, p)
	x = matplotlib.dates.date2num(dates)
	plt.plot(x, levels, '.')
	x1 = np.linspace(x[0], x[-1], 30)
	plt.plot(x1, poly(x1-d0))
	plt.show()