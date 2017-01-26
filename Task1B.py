from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

Cambridge_City_Centre =  (52.2053, 0.1218)
stations_dis_order = stations_by_distance(build_station_list(), Cambridge_City_Centre)
for station, dis in stations_dis_order[:10]:
    print(station)
for station, dis in stations_dis_order[-10:]:
    print(station)