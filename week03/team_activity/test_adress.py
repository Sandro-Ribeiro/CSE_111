"""
Verify that the extract_city and extract_state and 
extract_zipcode functions work correctly.
"""

from address import extract_city, extract_state, \
extract_zipcode
import pytest

def test_extract_city():
    """ 
    Verify that the extract_city function works correctly.
    Parameters: none
    Return: string
    """

    city = extract_city("531 do Carmo, Uberaba, MG 38025000")
    assert isinstance(city, str), "extract_city function must \
        return a string"

    assert extract_city("531 do Carmo, Uberaba, MG 38025000") == "Uberaba"


def test_extract_state():
    """
    Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """

    state = extract_state("531 do Carmo, Uberaba, MG 38025000")
    assert isinstance(state, str), "extract_family_name function must \
        return a string"

    assert extract_state("531 do Carmo, Uberaba, MG 38025000") == "MG"


def test_extract_zipcode():
    """
    Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    given_name = extract_zipcode("531 do Carmo, Uberaba, MG 38025000")
    assert isinstance(given_name, str), "extract_given_name function must \
        return a string"

    assert extract_zipcode("531 do Carmo, Uberaba, MG 38025000") == "38025000"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])