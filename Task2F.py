from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from datetime import timedelta

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    most_at_risk_stations = stations_highest_rel_level(stations, 5)
    for station in most_at_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt = timedelta(days = 2))
        plot_water_level_with_fit(station, dates, levels, 4)

run()