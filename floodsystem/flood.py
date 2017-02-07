"""This module contains a collection of functions needed for Milestone2"""

from floodsystem import stationdata


def stations_level_over_threshold(stations, tol):
    """Given a list of stations whose latest relative water levels are greater than a tolerance value
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
