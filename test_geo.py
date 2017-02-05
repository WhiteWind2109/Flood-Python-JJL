"""Unit test for the geo module"""

import pytest
from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
from haversine import haversine


def test_geo_stations_by_distance():

    # Build list of stations
    stations = build_station_list()

    # Use Cambridge City Centre (52.2053, 0.1218)
    distance_sorted = geo.stations_by_distance(stations, (52.2053, 0.1218))

    assert distance_sorted[0][0].town == "Cambridge"


def test_stations_within_radius():

    # Build list of stations
    stations = build_station_list()

    # Use Cambridge City Centre (52.2053, 0.1218)
    centre = (52.2053, 0.1218)
    ans = geo.stations_within_radius(stations, centre, 10)

    assert haversine(centre, ans[0].coord) <= 10


def test_rivers_with_station():

    # Build list of stations
    stations = build_station_list()

    ans = geo.rivers_with_station(stations)
    assert len(ans) == len(set(ans))  # All elements should be unique


def test_stations_by_river():

    # Build a list of stations
    stations = build_station_list()

    ans = geo.stations_by_river(stations)

    assert 'Apperley Bridge' in ans['River Aire']
    assert 'Cam' in ans['River Cam']
    assert 'Cambridge' in ans['River Cam']
    assert 'Benson Lock' in ans['Thames']
    assert 'Kings Lock' in ans['Thames']


def test_rivers_by_staion_number():

    # Build a list of staions
    stations = build_station_list()
    ans = geo.rivers_by_station_number(stations, 9)
    assert len(ans) >= 9
