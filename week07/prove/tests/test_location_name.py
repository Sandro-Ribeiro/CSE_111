import pytest
from modules.location_name import get_location_name, format_location


def test_format_location():
    address = {"suburb": "Centro", "city": "Uberaba", "state": "MG"}
    formatted = format_location(address)

    assert formatted == ["Centro", "Uberaba", "MG"]


def test_get_location_name(mocker):
    mock_request = mocker.patch("modules.location_name.requests.get")
    mock_request.return_value.json.return_value = {
        "address": {"city": "Uberaba", "state": "MG"}
    }

    location = get_location_name(-21.2, -48.2)
    assert location == ["Unknown_suburb", "Uberaba", "MG"]
