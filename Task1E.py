from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""
    print(rivers_by_station_number(build_station_list(), 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")

    # Run Task1E
    run()
