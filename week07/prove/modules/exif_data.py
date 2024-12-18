# Copyright 2024, Sandro Ribeiro. All rights reserved.

from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(photo_path):

    """
    Extracts the EXIF metadata from an photo,
    including GPS and date information. 
    Prioritizes GPS metadata.
    """
    try:
        # Opens the photo file
        photo = Image.open(photo_path)
    
        # Retrieves EXIF metadata
        exif_data = photo._getexif()

        if not exif_data:
            print(f"No EXIF metadata found for {photo_path}")
            return {"error": "No EXIF metadata"}

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
        print(f"Skipping non-photo file: {photo_path}")
        return None
    
def main():
    dict_data = get_exif_data("/home/sandro/Imagens/Photos/IMG_20191209_115228337.jpg")
    print(dict_data.items())

if __name__=="__main__":
    main()
