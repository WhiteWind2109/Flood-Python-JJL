from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood


def run():
    """Requirements for Task2B"""
    
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Define tolerance
    tol = 0.8

    # Get the list of stations (tuples) whose water level is over tol to present
    present = flood.stations_level_over_threshold(stations, tol)

    for station in present:
         print("{} {}".format(station[0], station[1]))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()
