from floodsystem.stationdata import build_station_list
from floodsystem import geo

def run():
    """Requirements for Task1C"""
    
    # Define the coordinates of Cambridge City Centre
    Centre =  (52.2053, 0.1218)
    #Define target distance
    dis = 10
    #Build a list of stations
    stations = build_station_list()
    #Get a list of stations in the range
    stations_within_radius = geo.stations_within_radius(stations,Centre,dis)
    #Retrieve name list and sort in alphabetical order
    result = []
    for station in stations_within_radius:
        result += station.name
    result.sort()
    #Output
    print(result)
    
    
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
