from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood
from floodsystem import datafetcher
from floodsystem import plot
import datetime


def run():
    """Requirements for Task2E"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    shortlist = flood.stations_highest_rel_level(stations, 5)

    for station in shortlist:
        dt = 10
        for target in stations:
            if target.name == station.name:
                dates, levels = datafetcher.fetch_measure_levels(target.measure_id,
                                                                 dt=datetime.timedelta(days=dt))
                plot.plot_water_levels(target, dates, levels)
                break


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()
