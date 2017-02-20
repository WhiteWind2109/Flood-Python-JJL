from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B
    Prints a list of tuples (station name, town, distance)
    for the 10 closest and the 10 furthest stations from
    the Cambridge city centre, (52.2053, 0.1218)"""

    # Define the coordinates of Cambridge City Centre
    Cambridge_City_Centre = (52.2053, 0.1218)
    # Sort the stations by their distances to CCC
    stations_dis_order = stations_by_distance(
        build_station_list(), Cambridge_City_Centre)

    # Display the closest ten stations
    print([(station.name, station.town, dis)
           for station, dis in stations_dis_order[:10]])

    # Display the farthest ten stations
    print([(station.name, station.town, dis)
           for station, dis in stations_dis_order[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")

    # Run Task1B
    run()
