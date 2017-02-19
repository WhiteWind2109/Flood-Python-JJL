from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime


def run():
    # Get station data and update it
    stations = build_station_list()
    update_water_levels(stations)

    # Getting stations with highest water levels
    most_at_risk_stations = stations_highest_rel_level(stations, 5)

    # Setting the time interval to 2 days
    # Run curve fitting with degree of 4
    dt = 2
    for station in most_at_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
        if len(dates) < 1 or len(levels) < 1:
            continue
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")

    run()
