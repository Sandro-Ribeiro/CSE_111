import os
from modules.organize import organize_photo


def test_organize_photo_valid(tmp_path):
    photo_path = tmp_path / "photo.jpg"
    photo_path.touch()  # Create an empty file

    location = ["Centro", "Uberaba", "MG"]
    date = None

    organize_photo(photo_path, location, date)

    organized_path = tmp_path / "MG/Uberaba/Centro/Unknown_date/photo.jpg"
    assert organized_path.exists()
