import math

def water_column_height(tower_height, tank_height):
    """
    water_colunm-height function calculates and returns the height
    of a column of water from a tower height and a tank wall height. 
    """

    wh = tower_height + (3 * tank_height)/ 4

    return wh

def pressure_gain_from_water_height(height):
    """
    pressure_gain_from_water_height function calculates and returns 
    pressure caused by Earth’s gravity pulling on the water stored 
    in an elevated tank from density of water and acceleration 
    from Earths gravity in meter / second^2 (g) and height of the 
    water column in meters (height). 
    """

    wd = WATER_DENSITY
    g = EARTH_ACCELERATION_OF_GRAVITY

    P = (wd*g*height)/1000

    return P

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    pressure_loss_from_pipe function calculates and returns the water 
    pressure lost because of the friction between the water and the 
    walls of a pipe that it flows through from pipe’s friction factor, 
    length of the pipe in meters (l), density of water in kilogram/ meter^3 (wd), 
    velocity of the water flowing through the pipe in meters/ second (v)
    and diameter of the pipe in meters (d).
    """
    wd = WATER_DENSITY
    d = pipe_diameter
    l = pipe_length
    f = friction_factor
    v = fluid_velocity

    P = (- f * l * wd * pow(v,2))/(2000*d)

    return P

def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    """
    pressure_loss_from_fittings calculates and return the water pressure lost 
    because of fittings such as 45° and 90° bends that are in a pipeline from
    density of water in kilogram/ meter³ (wd), velocity of the water flowing 
    through the pipe in meters/ second (v) and the quantity of fittings (n).
    """

    wd = WATER_DENSITY
    v = fluid_velocity
    n = quantity_fittings

    P = (-0.04 * wd * pow(v,2) * n)/2000

    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    reynolds_number function calculates and returns the Reynolds number for 
    a pipe with water flowing through it from density of water in 
    kilogram/ meter³ (wd), velocity of the water flowing through the pipe 
    in meters/ second (v) and hydraulic diameter of a pipe in meters (dh) (For a round 
    pipe, the hydraulic diameter is the same as the pipe’s inner diameter (d))
    and dynamic viscosity of water in Pascoal seconds(u)
    """

    wd = WATER_DENSITY
    v = fluid_velocity
    dh = hydraulic_diameter
    u = WATER_DYNAMIC_VISCOSITY

    R = (wd * dh * v)/u

    return R

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """
    pressure_loss_from_pipe_reduction function calculates and return the water 
    pressure lost because of water moving from a pipe with a large diameter into 
    a pipe with a smaller diameter from constant k, Reynolds number that corresponds 
    to the pipe with the larger diameter (R), the diameter of the larger pipe in 
    meters (D), diameter of the smaller pipe in meters (d), density of water in
    kilogram / meter^3 (wd) and  velocity of the water flowing through the larger 
    diameter pipe in meters / second (v)
    """
    wd = WATER_DENSITY
    D = larger_diameter
    v = fluid_velocity
    R = reynolds_number
    d = smaller_diameter


    k = (0.1 + (50/R))*(pow((D/d),4)-1)

    P = (-k * wd * pow(v,2))/2000

    return P

PVC_SCHED80_INNER_DIAMETER = 0.28687         # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013          # (unitless)
SUPPLY_VELOCITY = 1.65                       # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692         # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018           # (unitless)
HOUSEHOLD_VELOCITY = 1.75                    # (meters / second)
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500    # (meter / second^2)
WATER_DENSITY = 998.2000000                  # (kilogram / meter^3)
WATER_DYNAMIC_VISCOSITY = 0.0010016          # (Pascoal seconds)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()



