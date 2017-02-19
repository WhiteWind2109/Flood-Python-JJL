"""This module contains a collection of functions needed for Milestone2"""

from floodsystem import stationdata
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, where each tuple holds:
    (1) a station at which the latest relative water level is over tol and
    (2) the relative water level at the station. The returned list should
    be sorted by the relative level in descending order.
    Only stations with consistent typical low/high data are considered."""

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
    # Return list sorted by the relative level in descending order
    return sorted(ans, key=lambda ans: ans[1], reverse=True)


def stations_highest_rel_level(stations, N):
    """Given a list of stations and a number N
        return a list of N stations with their relative levels in descending order"""

    ans = []
    for station in stations:
        # Still about the type problem (need modifications in station.py?)
        if isinstance(station.latest_level, float):
            r_level = station.relative_water_level()
            if r_level is not None:
                ans.append((station, station.relative_water_level()))
    ans = sorted_by_key(ans, 1, reverse=True)
    return [station for station, level in ans[:N]]
