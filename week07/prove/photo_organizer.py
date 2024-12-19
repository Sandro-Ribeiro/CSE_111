# Copyright 2024, Sandro Ribeiro. All rights reserved.

"""
The program reorganizes and renames photos in a specified 
folder based on user-defined criteria. The application is 
useful for organizing large volumes of photos, using metadata 
to categorize photos.
"""

import os
from datetime import datetime
from modules.exif_data import get_exif_data
from modules.parse_gps import parse_gps_coordinates
from modules.location_name import get_location_name
from modules.organize import organize_photo


def main(photos_dir):

    """
    Organizes photos into folders by location 
    and year based on metadata.
    """

    for photo in os.listdir(photos_dir):

        photo_path = os.path.join(photos_dir, photo)

        if not os.path.isfile(photo_path):
            continue

        exif_data = get_exif_data(photo_path)

        if not exif_data:
            # Handle photos without metadata
            unknown_dir = os.path.join(photos_dir, ["","","Unknown"])
            os.makedirs(unknown_dir, exist_ok=True)
            os.rename(photo_path, os.path.join(unknown_dir, photo))

            continue

        # Parse GPS coordinates and data
        gps_data = exif_data.get("gps", None)
        date_taken = exif_data.get("date_taken", None)

        if gps_data:
            coordinates = parse_gps_coordinates(gps_data)
            if coordinates:
                lat, lon = coordinates
            else:
                lat, lon = None, None
        else:
            lat, lon = None, None


        # Determine location
        if lat and lon:
            location_name = get_location_name(lat, lon)
        else:
            location_name = ["","","Unknown"]

       # Determine date
        if date_taken:
            try:
                date = datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
                print(date)
            except ValueError:
                date = "Unknown"
        else:
            date = "Unknown"

        # Organize the photo
        organize_photo(photo_path, location_name, date)


if __name__ == "__main__":
    photos_dir = "./photos"
    main(photos_dir)
