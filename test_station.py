"""Unit test for the station module"""

import pytest
import floodsystem.station as station


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = station.MonitoringStation(
        s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    # Building test station
    test_station = station.MonitoringStation(station_id="test_station_id", measure_id="test_measure_id", label="test_label",
                                             coord=(52.845991, -0.100848), town="Cambridge", river="River Cam",
                                             typical_range=None)
    assert test_station.typical_range_consistent() is False
    test_station.typical_range = (0.895, 0.15)
    assert test_station.typical_range_consistent() is False
    test_station.typical_range = (0.895, 1.1)
    assert test_station.typical_range_consistent() is True


def test_inconsistent_typical_stations():
    test_station1 = station.MonitoringStation(station_id="test_station_id", measure_id="test_measure_id", label="test_label",
                                              coord=(52.845991, -0.100848), town="Cambridge", river="River Cam",
                                              typical_range=None)
    test_station2 = station.MonitoringStation(station_id="test_station_id", measure_id="test_measure_id", label="test_label",
                                              coord=(52.845991, -0.100848), town="Cambridge", river="River Cam",
                                              typical_range=(1.2, 0.8))
    test_station3 = station.MonitoringStation(station_id="test_station_id", measure_id="test_measure_id", label="test_label",
                                              coord=(52.845991, -0.100848), town="Cambridge", river="River Cam",
                                              typical_range=(0.8, 1.2))
    stations = [test_station1, test_station2, test_station3]
    assert set([test_station1, test_station2]) == set(
        station.inconsistent_typical_range_stations(stations))
