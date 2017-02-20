from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.analysis import polyfit


def predicted_relative_water_level(station, prediction):
    """predicted_relative_water_level(station, prediction) -> float
    Calculate the predicted relative water level."""
    return (prediction - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])


def run():
    """Task2G:
    Using your implementation, list the towns where you assess the risk of flooding
    to be greatest. Explain the criteria that you have used in making your assessment,
    and rate the risk at ‘severe’, ‘high’, ‘moderate’ or ‘low’."""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Define N
    N = 20

    # Setting the time interval to 2 days
    dt = 2

    # Run curve fitting with degree of 4
    p = 4

    shortlist = flood.stations_highest_rel_level(stations, N)

    # First find the stations at risk
    target_stations = []

    for station in shortlist:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
        # print('station.measure_id =', station.measure_id)
        # print('len(dates) =', len(dates))
        # print('len(levels) =', len(levels))
        if len(dates) < 1 or len(levels) < 1:
            # if there is no data, fitting will throw an error
            continue

        # calculate the fitting polynomial
        poly, d0 = polyfit(dates, levels, p)
        x = matplotlib.dates.date2num(dates)

        # get the latest data point
        now = max(x - d0)

        # predict the water level one day later
        # using the fitted polynomial
        prediction = poly(now + 1)

        r_level = station.relative_water_level()
        predicted_r_level = predicted_relative_water_level(station, prediction)

        # calculate the predicted rise in relative water level
        rise = predicted_r_level - r_level

        if predicted_r_level > r_level:
            target_stations.append([station.name, rise])
            print("{}:\n\tRelative water level: {}\n\tPredicted relative water level: {}\n\tRise: {}".format(
                station.name, r_level, predicted_r_level, rise))

    # now the stations at risk are marked
    # get towns at risk
    # elements: [town, number_of_nearest_stations_at_risk]
    target_towns = []

    for i, stations_risk in enumerate(target_stations):
        if stations_risk[0] in [towns for towns, count in target_towns]:
            target_towns[i][1] += stations_risk[1]
        else:
            target_towns.append(stations_risk[:])

    # sort target_towns by risks in descending order
    target_towns.sort(key=lambda x: x[1], reverse=True)
    print('-' * 70)
    print('List of target towns and the estimated flood risk:')
    print(target_towns)

    print('-' * 70)
    print('The towns where the risk of flooding is assessed to be the greatest:')

    ratings = ['low', 'moderate', 'high', 'severe']
    for town, risk in target_towns:
        rating_factor = 0  # low
        if risk > 0.5:
            rating_factor = 1  # moderate
        if risk > 5:
            rating_factor = 2  # high
        if risk > 10:
            rating_factor = 3  # severe
        print('{}:\n\t{}'.format(town, ratings[rating_factor]))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()
