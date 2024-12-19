from datetime import datetime
from modules.exif_data import get_exif_data
from modules.parse_gps import parse_gps_coordinates
from modules.location_name import get_location_name
from modules.organize import organize_photo
from tests.helpers import create_image_with_metadata


def test_full_integration(tmp_path, mocker):
    # Mock location API
    mocker.patch(
        "modules.location_name.requests.get",
        return_value=mocker.Mock(
            status_code=200,
            json=lambda: {"address": {"city": "Uberaba", "state": "MG"}}
        )
    )

    # Create an image with metadata
    photo_path = create_image_with_metadata(
        tmp_path,
        "test_photo.jpg",
        {
            "DateTimeOriginal": "2019:12:09 11:52:30",
            "GPSLatitude": "21.14.34.908",
            "GPSLatitudeRef": "S",
            "GPSLongitude": "48.17.35.8943",
            "GPSLongitudeRef": "W",
        },
    )

    # Extract metadata using get_exif_data
    exif_data = get_exif_data(photo_path)
    assert exif_data is not None

    # Parse GPS coordinates
    lat, lon = parse_gps_coordinates(exif_data["gps"])
    assert lat is not None and lon is not None

    # Get location name
    location = get_location_name(lat, lon)
    assert location == ["Unknown_suburb", "Uberaba", "MG"]

    # Convert 'date_taken' to a datetime object
    date_taken = datetime.strptime(exif_data["date_taken"], "%Y:%m:%d %H:%M:%S")

    # Organize photo
    organize_photo(photo_path, location, date_taken)
