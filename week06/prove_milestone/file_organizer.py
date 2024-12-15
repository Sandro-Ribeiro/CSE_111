# Copyright 2024, Sandro Ribeiro. All rights reserved.

"""
The program reorganizes and renames files in a specified folder 
based on user-defined criteria. The application is useful for 
organizing large volumes of files, using metadata and other 
information to categorize and rename files efficiently.
"""

import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import requests
from datetime import datetime
import time


def get_exif_data(image_path):
    """
    Extracts the EXIF metadata from an image, 
    including GPS and date information.
    """
    image = Image.open(image_path)
    exif_data = image._getexif()
    if not exif_data:
        return None

    # Map EXIF tags to their names
    exif = {TAGS.get(k, k): v for k, v in exif_data.items()}
    gps_data = {}
    if "GPSInfo" in exif:
        for key in exif["GPSInfo"].keys():
            name = GPSTAGS.get(key, key)
            gps_data[name] = exif["GPSInfo"][key]

    return {
        "date_taken": exif.get("DateTimeOriginal"),
        "gps": gps_data
    }


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
    Parses GPS metadata into decimal degrees (latitude and longitude).
    """
    if not gps_data:
        return None, None

    try:
        # Extract latitude and longitude in decimal degrees
        lat = convert_to_decimal_degrees(gps_data["GPSLatitude"], gps_data["GPSLatitudeRef"])
        lon = convert_to_decimal_degrees(gps_data["GPSLongitude"], gps_data["GPSLongitudeRef"])
        return lat, lon
    except KeyError:
        return None, None


def parse_gps_datetime(date_stamp, time_stamp):
    """
    Combines GPSDateStamp and GPSTimeStamp into a datetime object.
    """
    date_str = date_stamp.replace(':', '-')
    hours, minutes, seconds = time_stamp
    time_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")

import requests
import time  # Certifique-se de importar o módulo
import os

def format_location(address):
    """
    Formats the location name based on the address data.
    """
    city = address.get("city", "Unknown City")
    suburb = address.get("suburb", "")
    state = address.get("state", "")
    if suburb:
        return f"{suburb}, {city}, {state}"
    return f"{city}, {state}"

def get_location_name(lat, lon):
    """
    Uses the Nominatim API to retrieve and format the location name from coordinates.
    """
    print(f"Requesting location for Coordinates: Latitude = {lat}, Longitude = {lon}")
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json"
    }
    headers = {
        "User-Agent": "PhotoOrganizer/1.0 (santunesribeiro@outlook.com)"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        print(f"API Response Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            address = data.get("address", {})
            location = format_location(address)
            print(f"Location Found: {location}")
            return location
        elif response.status_code == 429:
            print("Rate limit exceeded. Retrying after a delay...")
            time.sleep(1)
            return get_location_name(lat, lon)  # Retry
        else:
            print(f"Unexpected API Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error while connecting to the API: {e}")
    
    return "Unknown Location"


def organize_photo(file_path, location, date):
    """
    Organizes a photo into a folder structure by location and year.
    """
    base_dir = "C:/Users/santu/Pictures/Photos"
    location_dir = os.path.join(base_dir, location)
    year_dir = os.path.join(location_dir, str(date.year))
    os.makedirs(year_dir, exist_ok=True)
    os.rename(file_path, os.path.join(year_dir, os.path.basename(file_path)))


def organize_photos_by_location_and_date(directory):
    """
    Organizes photos into folders by location and year based on metadata.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if not os.path.isfile(file_path):
            continue

        exif_data = get_exif_data(file_path)
        if not exif_data:
            # Handle photos without metadata
            unknown_dir = os.path.join(directory, "Unknown Location")
            os.makedirs(unknown_dir, exist_ok=True)
            os.rename(file_path, os.path.join(unknown_dir, filename))
            continue

        # Parse GPS and date metadata
        gps_data = exif_data["gps"]
        date_taken = exif_data["date_taken"]
        lat, lon = parse_gps_coordinates(gps_data)

        # Determine location
        if lat and lon:
            location_name = get_location_name(lat, lon)
        else:
            location_name = "Unknown Location"

        # Determine date
        if date_taken:
            try:
                date = datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
            except ValueError:
                date = datetime.now()
        else:
            date = datetime.now()

        # Organize the photo
        organize_photo(file_path, location_name, date)


# Example usage
if __name__ == "__main__":
    directory = "C:/Users/santu/Pictures/Photos"
    organize_photos_by_location_and_date(directory)
