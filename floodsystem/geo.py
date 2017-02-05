"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
# Taking well-tested function haversine to calculate distance

# from haversine import haversine
# if module not installed, install it with pip
try:
    from haversine import haversine
except ImportError:
    import pip
    pip.main(['install', 'haversine'])
    from haversine import haversine


def stations_by_distance(stations, p):
    """Given a list of stations and a coordinate p,
    returns a list of (station, distance) tuples,
    where distance (float) is the distance of the station (MonitoringStation) from the coordinate p.
    The returned list is sorted by distance."""

    # Create the list of tuple to be returned
    ans = []
    for station in stations:
        distance = haversine(p, station.coord)
        ans.append((station, distance))
    # Sort the list by the distances of elements to the given coordinates
    ans = sorted_by_key(ans, 1)
    return ans


def stations_within_radius(stations, centre, r):
    """Returns a list of all stations (type MonitoringStation)
    within radius r of a geographic coordinate x."""

    # Create the list of stations to be returned
    ans = []
    for station in stations:
        if (haversine(centre, station.coord) <= r):  # if distance<radius then pick it
            ans.append(station)
    return ans


def rivers_with_station(stations):
    """Given a list of stations, returns all rivers (by name) with a monitoring station."""

    # Create the list of rivers then change its type to set to get unique
    # elements
    ans = []
    for station in stations:
        ans.append(station.river)  # Get all rivers' names
    return set(ans)


def stations_by_river(stations):
    """Returns a Python dict (dictionary) that maps river names (the ‘key’)
    to a list of stations on that given river."""

    # Create the dictionary of river->[station] to be returned
    ans = {}
    for station in stations:
        if (station.river not in ans):
            # Create a new list for a not existing river
            ans[station.river] = []
        ans[station.river].append(station.name)
        ans[station.river].sort()
    return ans


def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of monitoring stations.
    It returns a list of (river name, number of stations) tuples,
    sorted by the number of stations.
    In the case that there are more rivers with the same number of stations as the N th entry,
    these rivers are included in the list."""

    # First, get a complete list of (river name, number of stations) tuples
    complete_list = []
    stations_on_river = stations_by_river(stations)
    for river in stations_on_river:
        complete_list.append((river, len(stations_on_river[river])))
 
    # Now sort it by numbers of stations in descending order
    complete_list = sorted_by_key(complete_list, 1, reverse=True)
    # The threshold value: the N-th greatest value
    threshold = complete_list[N - 1][1]
    greatest_N = []
    for river in complete_list:
        if river[1] >= threshold:
            greatest_N.append((river))
    return greatest_N
