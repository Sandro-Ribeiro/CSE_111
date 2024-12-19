import os
import shutil  # Import shutil to handle file moves
from datetime import datetime


def organize_photo(file_path, location, date):
    """
    Organizes a photo into a folder structure by location and year.
    """
    base_dir = "/home/sandro/Imagens/Photos"

    # Determine the folder path based on location
    path_dir = os.path.join(base_dir, location[2], location[1], location[0])

    if location[1] == "Unknown_city":
        path_dir = os.path.join(base_dir, location[2], location[1])

    if location[2] == "Unknown_state":
        path_dir = os.path.join(base_dir, location[2])

    # Ensure 'date' is a valid datetime object
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
        except ValueError:
            date = None

    if date and hasattr(date, "year"):
        path_dir = os.path.join(path_dir, str(date.year))
    else:
        path_dir = os.path.join(path_dir, "Unknown_date")

    # Create the directory if it doesn't exist
    os.makedirs(path_dir, exist_ok=True)

    # Move the photo to the target directory
    shutil.move(file_path, os.path.join(path_dir, os.path.basename(file_path)))
