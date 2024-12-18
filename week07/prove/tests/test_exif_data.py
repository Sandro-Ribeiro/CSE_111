import pytest
from modules.exif_data import get_exif_data

def test_get_exif_data_valid_image():
    image_path = "tests/images/valid_image.jpg"
    result = get_exif_data(image_path)
    assert "date_taken" in result
    assert "gps" in result

def test_get_exif_data_no_metadata():
    image_path = "tests/images/no_metadata.jpg"
    result = get_exif_data(image_path)
    assert result == {"error": "No EXIF metadata"}

def test_get_exif_data_invalid_image():
    image_path = "tests/images/not_an_image.txt"
    result = get_exif_data(image_path)
    assert result is None
