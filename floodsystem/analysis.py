import numpy as np
import matplotlib as plt

def polyfit(dates, levels, p):
    x = plt.dates.date2num(dates)
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])