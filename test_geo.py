"""Unit test for the geo module"""

import pytest
from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def test_geo_stations_by_distance():

    # Build list of stations
    stations = build_station_list()

    # Use Cambridge City Centre (52.2053, 0.1218)
    distance_sorted = geo.stations_by_distance(stations, (52.2053, 0.1218))

    assert distance_sorted[0][0].town == "Cambridge"
