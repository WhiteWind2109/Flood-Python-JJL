"""This module contains a collection of functions needed for Milestone2"""

from floodsystem import stationdata
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Given a list of stations, this function is to get those with latest relative water levels greater than a tolerance value
        return a list of tuple, for each tuple the first element is the station's name and the second is its relative water level"""

    ans = []
    for station in stations:
        # Problem: How can station.latest_level be a list for one station?
        # ------------
        # Answer:
        # Sometimes station.latest_level is a list, e.g.[0.777, 0.888]
        # Maybe it means a range given by visual guesswork
        if isinstance(station.latest_level, float):

            # Store the returned value to avoid repetitive calls
            # to slightly improve performance
            r_level = station.relative_water_level()

            if r_level is not None:  # "is not None" is easier to read

                # Only valid data can be compared
                if r_level > tol:
                    ans.append((station.name, r_level))
    return ans


def stations_highest_rel_level(stations, N):
    """Given a list of stations and a number N
        return a list of N stations with their relative levels in descending order"""

    ans = []
    for station in stations:
        if isinstance(station.latest_level, float): #Still about the type problem (need modifications in station.py?)
            r_level = station.relative_water_level()
            if not r_level is None:
                ans.append((station, station.relative_water_level()))
    ans = sorted_by_key(ans, 1, reverse=True)
    return [station for station, level in ans[:N]]