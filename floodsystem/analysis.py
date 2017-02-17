import numpy as np
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
	# Get the number version of dates for analysis
    x = date2num(dates)
	
	# Subtracting first term for fitting the curve
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])