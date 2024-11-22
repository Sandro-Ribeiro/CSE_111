"""
Verify that the make_full_name and extract_family_name and 
extract_given_name functions work correctly.
"""

from names import make_full_name, extract_family_name, \
    extract_given_name
import pytest

def test_make_full_name():
    """ 
    Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    full_name = make_full_name("Sandro", "Ribeiro")
    assert isinstance(full_name, str), " make_full_name function must \
        return a string"

    assert make_full_name("Sandro", "Ribeiro") == "Ribeiro; Sandro"


def test_extract_family_name():
    """
    Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """

    family_name = extract_family_name("Ribeiro; Sandro")
    assert isinstance(family_name, str), "extract_family_name function must \
        return a string"

    assert extract_family_name("Ribeiro; Sandro") == "Ribeiro"


def test_extract_given_name():
    """
    Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    given_name = extract_given_name("Ribeiro; Sandro")
    assert isinstance(given_name, str), "extract_given_name function must \
        return a string"

    assert extract_given_name("Ribeiro; Sandro") == "Sandro"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])