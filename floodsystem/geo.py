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
