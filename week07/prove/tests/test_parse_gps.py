from modules.parse_gps import parse_gps_coordinates, convert_to_decimal_degrees


def test_parse_gps_coordinates_valid():
    gps_data = {
        "GPSLatitude": (21, 14, 34.908),
        "GPSLatitudeRef": "S",
        "GPSLongitude": (48, 17, 35.8943),
        "GPSLongitudeRef": "W",
    }
    lat, lon = parse_gps_coordinates(gps_data)

    assert lat == -21.242474444444444  # Negative due to 'S'
    assert lon == -48.29330397222222  # Negative due to 'W'


def test_parse_gps_coordinates_invalid():
    gps_data = {}
    lat, lon = parse_gps_coordinates(gps_data)

    assert lat is None
    assert lon is None
