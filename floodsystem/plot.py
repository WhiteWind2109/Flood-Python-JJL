import matplotlib as plt
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
    plt.pyplot.plot(t, levels)
    # Add axis labels, rotate date labels and add plot title
    plt.pyplot.xlabel('date')
    plt.pyplot.ylabel('water level (m)')
    plt.pyplot.xticks(rotation=45);
    plt.pyplot.title("{}".format(station.name))
    # Display plot
    plt.pyplot.tight_layout() # This makes sure plot does not cut off date labels
    plt.pyplot.show()
    
def plot_water_level_with_fit(station, dates, levels, p):
    x = plt.dates.date2num(dates)
    plt.plot(x, levels, '.')
    x1 = np.linspace(x[0], x[-1], 30)
    poly, d0 = polyfit(x, levels, p)
    plt.plot(x1, poly(x1-d0))
    plt.show()