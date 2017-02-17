from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood

def run():
    """Requirements for Task2C"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Define N
    N = 10

    shortlist = flood.stations_highest_rel_level(stations, N)

    for station in shortlist:
        print("{} {}".format(station.name, station.relative_water_level()))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()
