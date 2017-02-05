"""This module provides functionality for retrieving real-time and
latest time history level data

"""

import os
import json

import datetime

# Extension: smart_import()
# How it works: smart_import() automatically installs missing modules using
# pip, which makes Anaconda no longer a requirement.
from floodsystem.smart_import import smart_import
# Usage: returned_module_object = smart_import('module')
# Example:       np = smart_import('numpy')
# Equivalent to: import numpy as np

# import requests
requests = smart_import('requests')

# import dateutil.parser
dateutil_parser = smart_import('dateutil.parser', module_pip_name='python-dateutil')
# Equivalent to:  #####################
# try:
#     import dateutil.parser as dateutil_parser
# except ImportError:
#     import pip
#     pip.main(['install', 'python-dateutil'])
#     import dateutil.parser as dateutil_parser


def fetch(url):
    """Fetch data from url and return fetched JSON object"""
    r = requests.get(url)
    data = r.json()
    return data


def dump(data, filename):
    """Save JSON object to file"""
    with open(filename, 'w') as f:
        data = json.dump(data, f)


def load(filename):
    """Load JSON object from file"""
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


def fetch_station_data(use_cache=True):
    """Fetch data from Environment agency for all active river level
    monitoring stations via a REST API and return retrieved data as a
    JSON object.

    Fetched data is dumped to a cache file so on subsequent call it
    can optionally be retrieved from the cache file. This is faster
    than retrieval over the Internet and avoids excessive calls to the
    Environment Agency service.

    """

    # URL for retrieving data for active stations with river level
    # monitoring (see
    # http://environment.data.gov.uk/flood-monitoring/doc/reference)
    url = "http://environment.data.gov.uk/flood-monitoring/id/stations?status=Active&parameter=level&qualifier=Stage&_view=full"

    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except:
        pass
    cache_file = os.path.join(sub_dir, 'station_data.json')

    # Attempt to load station data from file, otherwise fetch over
    # Internet
    if use_cache:
        try:
            # Attempt to load from file
            data = load(cache_file)
        except:
            # If load from file fails, fetch and dump to file
            data = fetch(url)
            dump(data, cache_file)
    else:
        # Fetch and dump to file
        data = fetch(url)
        dump(data, cache_file)

    return data


def fetch_latest_water_level_data(use_cache=False):
    """Fetch latest levels from all 'measures'. Returns JSON object"""

    # URL for retrieving data
    url = "http://environment.data.gov.uk/flood-monitoring/id/measures?parameter=level&qualifier=Stage&qualifier=level"

    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except:
        pass
    cache_file = os.path.join(sub_dir, 'level_data.json')

    # Attempt to load level data from file, otherwise fetch over
    # Internet
    if use_cache:
        try:
            # Attempt to load from file
            data = load(cache_file)
        except:
            data = fetch(url)
            dump(data, cache_file)
    else:
        data = fetch(url)
        dump(data, cache_file)

    return data


def fetch_measure_levels(measure_id, dt):
    """Fetch measure levels from latest reading and going back a period
    dt. Return list of dates and a list of values.

    """

    # Current time (UTC)
    now = datetime.datetime.utcnow()

    # Start time for data
    start = now - dt

    # Construct URL for fetching data
    url_base = measure_id
    url_options = "/readings/?_sorted&since=" + start.isoformat() + 'Z'
    url = url_base + url_options

    # Fetch data
    data = fetch(url)

    # Extract dates and levels
    dates, levels = [], []
    for measure in data['items']:
        # Convert date-time string to a datetime object
        d = dateutil_parser.parse(measure['dateTime'])

        # Append data
        dates.append(d)
        levels.append(measure['value'])

    return dates, levels
