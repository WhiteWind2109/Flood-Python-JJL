import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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