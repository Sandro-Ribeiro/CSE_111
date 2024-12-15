# Copyright 2024, Sandro Ribeiro. All rights reserved.

"""
This program organizes and renames files in a specified folder
based on user-defined criteria. It is particularly useful for 
organizing large volumes of photos, leveraging metadata such as 
GPS coordinates and timestamps to categorize and rename them efficiently.
"""

import os  # Provides utilities for interacting with the operating system, such as file and directory manipulation.
from PIL import Image  # Used for image processing and accessing metadata.
from PIL.ExifTags import TAGS, GPSTAGS  # Provides mappings for EXIF tags and GPS-related metadata.
import requests  # Facilitates HTTP requests for APIs (e.g., reverse geocoding).
from datetime import datetime  # Used for handling and formatting date and time information.
import time  # Allows for time-based delays.

def get_exif_data(image_path):
    """
        Extracts EXIF metadata from an image file, 
        including GPS and date information.
        Parameters:
            image_path (str): The path to the image file.
        Returns:
            dict: A dictionary containing the date the 
            photo was taken and GPS metadata.
    """

    # Open the image file using Pillow's Image class
    image = Image.open(image_path)

    # Retrieve the EXIF metadata from the image
    exif_data = image._getexif()

    if not exif_data:
        # Return None if the image has no metadata
        return None

    # Map EXIF tags to their readable names
    exif = {TAGS.get(k, k): v for k, v in exif_data.items()}
    gps_data = {}

    if "GPSInfo" in exif:

        # Extract GPS metadata using GPSTAGS for better readability
        for key in exif["GPSInfo"].keys():
            name = GPSTAGS.get(key, key)
            gps_data[name] = exif["GPSInfo"][key]

    return {
        # Extract the original date the photo was taken
        # Include parsed GPS metadata
        "date_taken": exif.get("DateTimeOriginal"),
        "gps": gps_data 
    }

def convert_to_decimal_degrees(dms, ref):
    """
    Converts GPS coordinates from degrees, minutes, and seconds (DMS) format
    to decimal degrees (DD).
    Parameters:
        dms (tuple): A tuple containing degrees, minutes, and seconds.
        ref (str): A reference direction ('N', 'S', 'E', 'W').
    Returns:
        float: Decimal degree representation of the coordinate.
    """

    degrees, minutes, seconds = dms

    # Convert DMS to decimal degrees
    dd = degrees + (minutes / 60.0) + (seconds / 3600.0)

    if ref in ['S', 'W']:
        # South and West should have negative coordinates
        dd = -dd

    return dd

def parse_gps_coordinates(gps_data):
    """
    Extracts and converts GPS coordinates from metadata to 
    decimal degrees.
    Parameters:
        gps_data (dict): GPS-related EXIF metadata.
    Returns:
        tuple: Latitude and longitude in decimal 
        degrees, or (None, None) if unavailable.
    """

    if not gps_data:
        return None, None

    try:

        # Convert latitude and longitude to decimal degrees
        lat = convert_to_decimal_degrees(
            gps_data["GPSLatitude"], 
            gps_data["GPSLatitudeRef"])
        lon = convert_to_decimal_degrees(
            gps_data["GPSLongitude"], 
            gps_data["GPSLongitudeRef"])
        
        return lat, lon
    
    except KeyError:

        return None, None

def parse_gps_datetime(date_stamp, time_stamp):
    """
    Combines GPS date and time into a datetime object.
    Parameters:
        date_stamp (str): Date string in the format 'YYYY:MM:DD'.
        time_stamp (tuple): A tuple containing hours, minutes, and seconds.
    Returns:
        datetime: A datetime object representing the combined GPS date and time.
    """

    # Replace colons in the date with hyphens to match the datetime format
    date_str = date_stamp.replace(':', '-')
    hours, minutes, seconds = time_stamp
    
    # Format the time as HH:MM:SS
    time_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")

def format_location(address):
    """
    Formats a location string from address metadata.
    Parameters:
        address (dict): A dictionary containing address components from reverse geocoding.
    Returns:
        str: A formatted location string (e.g., "Suburb, City, State").
    """

    city = address.get("city", "Unknown City")
    suburb = address.get("suburb", "")
    state = address.get("state", "")

    if suburb:
        return f"{suburb}, {city}, {state}"
    
    return f"{city}, {state}"

def get_location_name(lat, lon):
    """
    Uses the Nominatim API to get a human-readable location name from latitude and longitude.
    Parameters:
        lat (float): Latitude in decimal degrees.
        lon (float): Longitude in decimal degrees.
    Returns:
        str: A formatted location name or 'Unknown Location' if the API call fails.
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

        # Make an HTTP GET request to the Nominatim API
        response = requests.get(url, params=params, headers=headers)

        print(f"API Response Status: {response.status_code}")

        if response.status_code == 200:
            # Parse the JSON response to extract address information
            data = response.json()
            address = data.get("address", {})
            location = format_location(address)

            print(f"Location Found: {location}")

            return location
        
        elif response.status_code == 429:
            # Handle rate-limiting with a retry
            print("Rate limit exceeded. Retrying after a delay...")
            time.sleep(1)

            return get_location_name(lat, lon)
        
        else:
            print(f"Unexpected API Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:

        # Handle network or connection errors
        print(f"Error while connecting to the API: {e}")
    
    return "Unknown Location"

def organize_photo(file_path, location, date):
    """
    Organizes a photo into a directory structure based on location and year.
    Parameters:
        file_path (str): The path to the photo file.
        location (str): The location name derived from metadata or "Unknown Location".
        date (datetime): The date the photo was taken.
    """

    base_dir = "C:/Users/santu/Pictures/Photos"
    
    # Create directories based on location and year
    location_dir = os.path.join(base_dir, location)
    year_dir = os.path.join(location_dir, str(date.year))

    # Ensure directories exist
    os.makedirs(year_dir, exist_ok=True)  

    # Move the file into the target directory
    os.rename(file_path, os.path.join(year_dir, os.path.basename(file_path)))

def organize_photos_by_location_and_date(directory):
    """
    Organizes photos in the specified directory into subfolders by location and year.
    Parameters:
        directory (str): The directory containing the photos to organize.
    """

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if not os.path.isfile(file_path):  # Skip non-file entries
            continue

        # Extract EXIF metadata from the photo
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
