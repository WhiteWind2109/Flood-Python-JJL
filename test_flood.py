"""Unit test for the flood module"""

import pytest
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood

def test_stations_level_over_threshold():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    present = flood.stations_level_over_threshold(stations, 0.8)
    assert present[0][1] > 0.8