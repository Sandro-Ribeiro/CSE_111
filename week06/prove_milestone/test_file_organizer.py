import os
import shutil
import pytest
from unittest.mock import patch
from file_organizer import get_location_name, format_location, organize_photos_by_location_and_date


# Funções do seu código principal importadas aqui (exemplo abaixo)
# from file_organizer import get_location_name, format_location, organize_photos_by_location_and_date

@pytest.fixture
def setup_test_environment():
    """
    Create a temporary test environment with sample files.
    """
    test_dir = "test_photos"
    os.makedirs(test_dir, exist_ok=True)

    # Cria arquivos simulando fotos
    test_files = [
        os.path.join(test_dir, f"photo_{i}.jpg") for i in range(3)
    ]
    for file in test_files:
        with open(file, "wb") as f:
            f.write(b"Simulated photo content")  # Conteúdo fictício

    yield test_dir, test_files

    # Limpa o ambiente após os testes
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

# Mock de dados GPS e endereços
mock_gps_data = [
    {"lat": -19.755574, "lon": -47.934063},
    {"lat": -19.719045, "lon": -47.957264},
    {"lat": None, "lon": None},  # Sem coordenadas
]

mock_addresses = [
    "Centro, Uberaba, Minas Gerais",
    "Fabrício, Uberaba, Minas Gerais",
    "Unknown Location",
]

mock_dates = ["2022:08:12 15:23:00", "2023:01:01 10:00:00", None]


@patch("file_organizer.get_location_name")
def test_get_location_name(mock_get_location_name):
    """
    Test if get_location_name correctly retrieves and formats location names.
    """
    mock_get_location_name.side_effect = mock_addresses

    for idx, gps in enumerate(mock_gps_data):
        if gps["lat"] is not None and gps["lon"] is not None:
            result = get_location_name(gps["lat"], gps["lon"])
            assert result == mock_addresses[idx]
        else:
            assert "Unknown Location" == mock_addresses[idx]


def test_format_location():
    """
    Test if format_location correctly formats location strings.
    """
    test_address = {
        "city": "Uberaba",
        "suburb": "Centro",
        "state": "Minas Gerais",
    }
    result = format_location(test_address)
    assert result == "Centro, Uberaba, Minas Gerais"

    test_address_missing_suburb = {
        "city": "Uberaba",
        "state": "Minas Gerais",
    }
    result = format_location(test_address_missing_suburb)
    assert result == "Uberaba, Minas Gerais"


@patch("file_organizer.get_location_name")
@patch("file_organizer.get_exif_data")
def test_organize_photos_by_location_and_date(
    mock_get_exif_data, mock_get_location_name, setup_test_environment
):
    """
    Test if photos are organized correctly into folders.
    """
    mock_get_location_name.side_effect = mock_addresses

    def mock_get_exif_data_func(file):
        idx = setup_test_environment[1].index(file)
        return {
            "date_taken": mock_dates[idx],
            "gps": mock_gps_data[idx],
        }

    mock_get_exif_data.side_effect = mock_get_exif_data_func

    test_dir, test_files = setup_test_environment
    organize_photos_by_location_and_date(test_dir)

    # Verifica se as pastas foram criadas corretamente
    expected_dirs = [
        os.path.join(test_dir, "Photos", "Centro, Uberaba, Minas Gerais", "2022"),
        os.path.join(test_dir, "Photos", "Fabrício, Uberaba, Minas Gerais", "2023"),
        os.path.join(test_dir, "Photos", "Unknown Location", "Unknown Year"),
    ]
    for dir in expected_dirs:
        assert os.path.exists(dir)

    # Verifica se os arquivos foram movidos corretamente
    for idx, file in enumerate(test_files):
        if idx == 0:
            expected_path = os.path.join(expected_dirs[0], os.path.basename(file))
        elif idx == 1:
            expected_path = os.path.join(expected_dirs[1], os.path.basename(file))
        else:
            expected_path = os.path.join(expected_dirs[2], os.path.basename(file))
        assert os.path.exists(expected_path)
