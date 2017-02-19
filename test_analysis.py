from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from matplotlib.dates import num2date, date2num
import datetime


dt = 10
dates, levels = fetch_measure_levels("http://environment.data.gov.uk/flood-monitoring/id/measures/48173-level-stage-i-15_min-m",
	dt=datetime.timedelta(days=dt))
poly, x0 = polyfit(dates, levels, 4)
print(poly, x0)
assert poly[0] > 0