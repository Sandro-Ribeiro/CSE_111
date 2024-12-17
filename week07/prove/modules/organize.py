# Copyright 2024, Sandro Ribeiro. All rights reserved.

import os

def organize_photo(file_path, location, date):

    """
    Organizes a photo into a folder structure by location and year.
    """

    base_dir = "C:/Users/santu/Pictures/Photos"
    location_dir = os.path.join(base_dir, location)
    year_dir = os.path.join(location_dir, str(date.year))

    os.makedirs(year_dir, exist_ok=True)
    os.rename(file_path, os.path.join(year_dir, os.path.basename(file_path)))


