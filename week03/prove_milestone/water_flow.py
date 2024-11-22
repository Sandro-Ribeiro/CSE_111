import math

def water_column_height(tower_height, tank_height):
    """
    water_colunm-height function calculates and returns the height
    of a column of water from a tower height and a tank wall height. 
    """

    water_height = tower_height + (3 * tank_height)/ 4

    return water_height

def pressure_gain_from_water_height(height):
    """
    pressure_gain_from_water_height function calculates and returns 
    pressure caused by Earth’s gravity pulling on the water stored 
    in an elevated tank from density of water (p) and acceleration 
    from Earths gravity in meter / second² (g) and height of the 
    water column in meters (height). 
    """

    wd = 998.2
    g = 9.80665

    pressure_water = (wd*g*height)/1000

    return pressure_water

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    pressure_loss_from_pipe function calculates and returns the water 
    pressure lost because of the friction between the water and the 
    walls of a pipe that it flows through from pipe’s friction factor, 
    length of the pipe in meters, density of water in kilogram/ meter³ (wd), 
    velocity of the water flowing through the pipe in meters/ second 
    and diameter of the pipe in meters.
    """
    wd = 998.2
    d = pipe_diameter
    L = pipe_length
    f = friction_factor
    v = fluid_velocity

    pressure_loss = (- f * L * wd * pow(v,2))/(2000*d)

    return pressure_loss
