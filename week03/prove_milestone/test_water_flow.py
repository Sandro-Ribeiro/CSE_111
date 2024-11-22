"""
Verify that the water_column_height and extract_state 
and extract_zipcode functions work correctly.
"""

from water_flow import water_column_height
from water_flow import pressure_gain_from_water_height
from water_flow import pressure_loss_from_pipe
from pytest import approx
import pytest
import pandas as pd

def test_water_column_height():
    """ 
    Verify that the water_column_height function works 
    correctly.
    Parameters: none
    Return: nothing
    """

    data = [
        [0.0,0.0,0.0],
        [0.0,10.0,7.5],
        [25.0,0.0,25.0],
        [48.3,12.8,57.9]
    ]

    columns = ["tower_height", "tank_height", "expected_value" ]
    df = pd.DataFrame(data, columns=columns)

    for _,row in df.iterrows():
        assert water_column_height(
            row["tower_height"], 
            row["tank_height"]
            ) == approx(
                row["expected_value"])


def test_pressure_gain_from_water_height():
    """ 
    Verify that the pressure_gain_from_water_height function works 
    correctly.
    Parameters: none
    Return: nothing
    """

    data = [
        [0.0,0.000,0.001],
        [30.2,295.628,0.001],
        [50.0,489.450,0.001]
    ]

    columns = ["height", "expected_pressure", "approx_abs_value" ]
    df = pd.DataFrame(data, columns=columns)

    for _,row in df.iterrows():
        assert pressure_gain_from_water_height(
            row["height"]
            ) == approx(
                row["expected_pressure"], 
                abs=row["approx_abs_value"])


def test_pressure_loss_from_pipe():
    """ 
    Verify that the pressure_loss_from_pipe function works correctly.
    Parameters: none
    Return: nothing
    """

    data = [
        [0.048692,0.00,0.018,1.75,0.000,0.001],
        [0.048692,200.00,0.000,1.75,0.000,0.001],
        [0.048692,200.00,0.018,0.00,0.000,0.001],
        [0.048692,200.00,0.018,1.75,-113.008,0.001],
        [0.048692,200.00,0.018,1.65,-100.462,0.001],
        [0.286870,1000.00,0.013,1.65,-61.576,0.001],
        [0.286870,1800.75,0.013,1.65,-110.884,0.001]
    ]

    columns = ["pipe_diameter", "pipe_length", 
               "friction_factor", "fluid_velocity",
               "expected_pressure_loss","approx_abs_value"]
    df = pd.DataFrame(data, columns=columns)

    for _,row in df.iterrows():
        assert pressure_loss_from_pipe(
            row["pipe_diameter"], 
            row["pipe_length"], 
            row["friction_factor"], 
            row["fluid_velocity"]
            ) == approx(
                row["expected_pressure_loss"],
                abs=row["approx_abs_value"])


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

