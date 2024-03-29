"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Checks the typical high/low range data for consistency.
        This method returns True if the data is consistent and False if the data is inconsistent or unavailable."""

        # Check if the data is unavailable
        if self.typical_range is None:
            return False

        """
        In build_station_list():
        typical_range = (float(e['stageScale']['typicalRangeLow']),
                             float(e['stageScale']['typicalRangeHigh']))"""
        return self.typical_range[0] < self.typical_range[1]

    def relative_water_level(self):
        """This method returns the latest water level as a fraction of the typical range
            if the data is unavailable or inconsistent return None"""

        # The data is not available
        if self.latest_level is None or self.typical_range is None:
            return None

        # The data is not consistent
        if not self.typical_range_consistent():
            return None

        return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])


def inconsistent_typical_range_stations(stations):
    """Given a list of stations objects, returns a list of stations that have inconsistent data.
    The function uses MonitoringStation.typical_range_consistent."""

    # Use list comprehension
    return [s for s in stations if not s.typical_range_consistent()]
