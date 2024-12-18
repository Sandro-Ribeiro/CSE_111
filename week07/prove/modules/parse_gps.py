# Copyright 2024, Sandro Ribeiro. All rights reserved.

from datetime import datetime

def convert_to_decimal_degrees(dms, ref):

    """
    Converts coordinates from DMS to Decimal Degrees (DD).
    """

    degrees, minutes, seconds = dms
    dd = degrees + (minutes / 60.0) + (seconds / 3600.0)

    if ref in ['S', 'W']:
        dd = -dd  # Negative for South and West
    
    return dd

def parse_gps_coordinates(gps_data):

    """
    Parses GPS metadata into decimal degrees 
    (latitude and longitude).
    """

    if not gps_data:
        return None, None

    try:
        # Extract latitude and longitude in decimal degrees
        lat = convert_to_decimal_degrees(
            gps_data["GPSLatitude"], 
            gps_data["GPSLatitudeRef"])
        lon = convert_to_decimal_degrees(
            gps_data["GPSLongitude"], 
            gps_data["GPSLongitudeRef"])

        return lat, lon
    
    except KeyError:

        return None, None

def parse_gps_datetime(gps_data):

    """
    Combines GPSDateStamp and GPSTimeStamp into 
    a datetime object.
    """
    if not gps_data:
        return None

    # Extract date of gps_data
    try:
        date_stamp = gps_data["GPSDateStamp"]
        time_stamp = gps_data["GPSTimeStamp"]
    except:
        return None

    date_str = date_stamp.replace(':', '-')
    hours, minutes, seconds = time_stamp
    time_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    return date_str, time_str
