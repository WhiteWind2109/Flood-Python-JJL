"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
# Taking well-tested function haversine to calculate distance
from haversine import haversine

def stations_by_distance(stations, p):
    # Create the list of tuple to be returned
    ans = list()
    for station in stations:
        distance = haversine(p, station.coord)
        ans.append((station, distance))
    # Sort the list by the distances of elements to the given coordinates
    ans = sorted_by_key(ans, 1)
    return ans

def stations_within_radius(stations, centre, r):
    ans = []
    for station in stations:
        if (haversine(centre, station.coord) <= r):
            ans += station
    return ans

def rivers_with_station(stations):
    ans = []
    for station in stations:
        ans.append(station.river)
    return set(ans)

def stations_by_river(stations):
    ans = {}
    for station in stations:
        if (not station.river in ans):
            ans[station.river] = []
        ans[station.river].append(station.name)
    return ans

def rivers_by_station_number(stations, N):
    ans = list()
    stations_on_river = stations_by_river(stations)
    for river in stations_on_river:
        ans.append((river, len(stations_on_river[river])))
    ans = sorted_by_key(ans, 1, reverse=True)
    threshold = ans[N-1][1]
    greatest_N = list()
    for river in ans:
        if river[1] >= threshold:
            greatest_N.append((river))
    return greatest_N