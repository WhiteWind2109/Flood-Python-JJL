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
    if len(present) > 1:
        # The returned list should be in descending order
        assert present[0][1] >= present[1][1]


def test_stations_highest_rel_level():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    shortlist = flood.stations_highest_rel_level(stations, 10)
    assert len(shortlist) == 10
    assert shortlist[0].relative_water_level() >= shortlist[1].relative_water_level()
