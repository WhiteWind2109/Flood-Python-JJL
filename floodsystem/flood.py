"""This module contains a collection of functions needed for Milestone2"""

from floodsystem import stationdata

def stations_level_over_threshold(stations, tol):
    """Given a list of stations whose latest relative water levels are greater than a tolerance value
        return a list of tuple, for each tuple the first element is the station's name and the second is its relative water level"""

    ans = []
    for station in stations:
        # Problem: How can station.latest_level be a list for one station?
        if isinstance(station.latest_level, float):
            if not station.relative_water_level() is None:
                if station.relative_water_level() > tol:
                    ans.append((station.name, station.relative_water_level()))
    return ans