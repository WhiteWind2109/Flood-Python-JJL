from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task1F"""

    print(sorted(inconsistent_typical_range_stations(build_station_list())))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")

    # Run Task1F
    run()
