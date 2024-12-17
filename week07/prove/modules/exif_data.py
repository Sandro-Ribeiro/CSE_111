# Copyright 2024, Sandro Ribeiro. All rights reserved.

from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif_data(image_path):

    """
    Extracts the EXIF metadata from an image, 
    including GPS and date information.
    """
    try:
        # Opens the image file
        image = Image.open(image_path)

        # Retrieves EXIF metadata
        exif_data = image._getexif()

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
    
    except UnidentifiedImageError:
        print(f"Skipping non-image file: {image_path}")
        return None
