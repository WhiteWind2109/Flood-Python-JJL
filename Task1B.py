from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

# Define the coordinates of Cambridge City Centre
Cambridge_City_Centre =  (52.2053, 0.1218)
# Sort the stations by their distances to CCC
stations_dis_order = stations_by_distance(build_station_list(), Cambridge_City_Centre)
# Display the closest ten stations
for station, dis in stations_dis_order[:10]:
    print(station)
# Display the farest ten stations
for station, dis in stations_dis_order[-10:]:
    print(station)