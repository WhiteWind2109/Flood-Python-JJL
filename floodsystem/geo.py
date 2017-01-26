"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
# Taking well-tested function haversine to calculate distance
from haversine import haversine

def stations_by_distance(stations, p):
    # Create the list of tuple to be returned
    sta_dis = list()
    for station in stations:
        distance = haversine(p, station.coord)
        sta_dis.append((station, distance))
    # Sort the list by the distances of elements to the given coordinates
    sta_dis = sorted_by_key(sta_dis, 1)
    return sta_dis