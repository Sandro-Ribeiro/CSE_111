# Copyright 2024, Sandro Ribeiro. All rights reserved.

import os

def organize_photo(file_path, location, date):

    """
    Organizes a photo into a folder structure by location and year.
    """

    base_dir = "/home/sandro/Imagens/Photos"
    
    path_dir = os.path.join(base_dir, location[2], location[1], location[0])

    if location[1] == "Unknown":
        path_dir = os.path.join(base_dir, location[2], location[1])

    if location[2] == "Unknown":
        path_dir = os.path.join(base_dir, location[2])

    path_dir = os.path.join(path_dir, str(date.year))

    os.makedirs(path_dir, exist_ok=True)
    os.rename(file_path, os.path.join(path_dir, os.path.basename(file_path)))


