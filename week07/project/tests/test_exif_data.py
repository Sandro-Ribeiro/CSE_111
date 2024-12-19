import pytest
from modules.exif_data import get_exif_data
from tests.helpers import create_image_with_metadata, create_non_image_file


@pytest.fixture
def setup_test_files(tmp_path):
    """
    Creates different types of files for testing purposes.
    """
    files = {}

    # Image with all metadata
    files["image_with_all_metadata"] = create_image_with_metadata(
        tmp_path,
        "image_with_all_metadata.jpg",
        {
            "DateTimeOriginal": "2019:12:09 11:52:30",
            "GPSLatitude": "21.14.34.908",
            "GPSLatitudeRef": "S",
            "GPSLongitude": "48.17.35.8943",
            "GPSLongitudeRef": "W",
        },
    )

    # Image without metadata
    files["image_without_metadata"] = create_image_with_metadata(
        tmp_path, "image_without_metadata.jpg"
    )

    # Non-image file
    files["non_image_file"] = create_non_image_file(tmp_path, "not_an_image.txt")

    return files


def test_get_exif_data_with_metadata(setup_test_files):
    image_path = setup_test_files["image_with_all_metadata"]
    exif_data = get_exif_data(image_path)

    assert exif_data is not None
    assert exif_data["date_taken"] == "2019:12:09 11:52:30"
    gps_info = exif_data["gps"]
    assert gps_info["GPSLatitudeRef"] == "S"
    assert gps_info["GPSLongitudeRef"] == "W"


def test_get_exif_data_no_metadata(setup_test_files):
    image_path = setup_test_files["image_without_metadata"]
    exif_data = get_exif_data(image_path)

    assert exif_data is not None
    assert exif_data["error"] == "No EXIF metadata"


def test_get_exif_data_non_image_file(setup_test_files):
    file_path = setup_test_files["non_image_file"]
    exif_data = get_exif_data(file_path)

    assert exif_data is None
