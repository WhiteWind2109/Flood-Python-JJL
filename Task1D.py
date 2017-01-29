from floodsystem.stationdata import build_station_list
from floodsystem import geo

def run():
    """Requirements for Task1D"""
    
    #Build a list of stations
    stations = build_station_list()
    #Get a list of rivers with stations
    RiverWithStation = list(geo.rivers_with_station(stations))
    RiverWithStation.sort()
    #Get first 10
    print(RiverWithStation[:10])
    
    #Get a dict of river->stations on this river
    RiverByStation = geo.stations_by_river(stations)
    #Get required things
    RiverByStation['River Aire'].sort()
    print(RiverByStation['River Aire'])
    
    RiverByStation['River Cam'].sort()
    print(RiverByStation['River Cam'])
    
    RiverByStation['Thames'].sort()
    print(RiverByStation['Thames'])
    
    
if __name__=="__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Run Task1D
    run()