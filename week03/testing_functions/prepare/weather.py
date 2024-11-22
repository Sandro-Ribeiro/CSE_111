#weather.py
def cels_from_fahr(fahr):
    """
    Convert a tempeature in Fahrenheit to
    Celisius and return the celsius temperature
    """

    cels = (fahr - 32) * 5 / 9
    return cels