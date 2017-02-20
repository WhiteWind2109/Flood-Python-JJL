"""This module contains a collection of functions needed for Milestone2"""

from floodsystem import stationdata
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """stations_level_over_threshold(stations, tol) --
    Returns a list of tuples, where each tuple holds:
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
    """stations_highest_rel_level(stations, N) --
    Returns a list of the N stations at which the water level, relative to the typical range,
    is highest. The list is sorted in descending order by relative level."""

    ans = []
    for station in stations:
        if isinstance(station.latest_level, float):

            # Store the returned value to avoid repetitive calls
            # to slightly improve performance
            r_level = station.relative_water_level()

            # Only valid data can be compared by sorted_by_key()
            if r_level is not None:

                # Make a decorated list
                ans.append((station, r_level))

    # Sort the decorated list by relative water level
    ans = sorted_by_key(ans, 1, reverse=True)

    # Return the undecorated list
    return [station for station, rel_level in ans[:N]]
