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
    assert len(ans) == len(set(ans)) # All elements should be unique
    
def test_stations_by_river():
    
    # Build a list of stations
    stations = build_station_list()
    
    ans = geo.stations_by_river(stations)
    assert ans['River Aire'] == ['Airmyn', 'Apperley Bridge',
             'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 
             'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 
             'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave',
             'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point',
             'Saltaire', 'Snaygill', 'Stockbridge']
    assert ans['River Cam'] == ['Cam', 'Cambridge', 'Cambridge Baits Bite', 
            'Cambridge Jesus Lock', 'Dernford', 'Weston Bampfylde']
    assert ans['Thames'] == ['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock',
             'Bray Lock', 'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock',
             'Clifton Lock', 'Cookham Lock', 'Cricklade', 'Culham Lock', 'Days Lock', 'Ewen',
             'Eynsham Lock', 'Farmoor', 'Godstow Lock', 'Goring Lock', 'Grafton Lock',
             'Hannington Bridge', 'Hurley Lock', 'Iffley Lock', 'Kings Lock',
             'Kingston', 'Maidenhead', 'Mapledurham Lock', 'Marlow Lock',
             'Marsh Lock', 'Molesey Lock', 'Northmoor Lock', 'Old Windsor Lock',
             'Osney Lock', 'Penton Hook', 'Pinkhill Lock', 'Radcot Lock', 'Reading',
             'Romney Lock', 'Rushey Lock', 'Sandford-on-Thames', 'Shepperton Lock',
             'Shifford Lock', 'Shiplake Lock', 'Somerford Keynes', 'Sonning Lock',
             'St Johns Lock', 'Staines', 'Sunbury  Lock', 'Sutton Courtenay',
             'Teddington Lock', 'Thames Ditton Island', 'Trowlock Island', 'Walton', 'Whitchurch Lock', 'Windsor Park']
    
def test_rivers_by_staion_number():
    
    #Build a list of staions
    stations = build_station_list()
    ans = geo.rivers_by_station_number(stations, 9)
    assert set(ans) == set([('Thames', 55), ('River Great Ouse', 31), ('River Avon', 30), 
                   ('River Calder', 24), ('River Aire', 21), ('River Severn', 20),
                   ('River Derwent', 19), ('River Stour', 16), ('River Wharfe', 14),
                   ('River Trent', 14), ('Witham', 14)])