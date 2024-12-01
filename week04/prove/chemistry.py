from formula import parse_formula
import math

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

# Mole
MOL = 6.02214076 * pow(10,23)

def make_known_molecules_table():
    """The make_periodic_table function takes no parameters and creates and 
    returns a compound list. The compound list must contain all the data 
    in the table of elements presents in periodic table.
    """
    known_molecules_dict = {
        "H2O": "water",
        "O2": "molecular oxygen",
        "CO2": "carbon dioxide",
        "N2": "molecular nitrogen",
        "CH4": "methane",
        "NH3": "ammonia",
        "H2": "molecular hydrogen",
        "CO": "carbon monoxide",
        "SO2": "sulfur dioxide",
        "H2SO4": "sulfuric acid",
        "NaCl": "sodium chloride (table salt)",
        "C6H12O6": "glucose",
        "HCl": "hydrochloric acid",
        "CaCO3": "calcium carbonate",
        "HNO3": "nitric acid",
        "O3": "ozone",
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite"
    }

    return known_molecules_dict

def make_periodic_table():
    """The make_periodic_table function takes no parameters and creates and 
    returns a compound list. The compound list must contain all the data 
    in the table of elements presents in periodic table.
    """
    periodic_table_dict = {
        # [symbol, name, atomic_mass, atomic_number]
        "Ac": ["Actinium", 227, 89],
        "Ag": ["Silver", 107.8682, 47],
        "Al": ["Aluminum", 26.9815386, 13],
        "Ar": ["Argon", 39.948, 18],
        "As": ["Arsenic", 74.9216, 33],
        "At": ["Astatine", 210, 85],
        "Au": ["Gold", 196.966569, 79],
        "B": ["Boron", 10.811, 5],
        "Ba": ["Barium", 137.327, 56],
        "Be": ["Beryllium", 9.012182, 4],
        "Bi": ["Bismuth", 208.9804, 83],
        "Br": ["Bromine", 79.904, 35],
        "C": ["Carbon", 12.0107, 6],
        "Ca": ["Calcium", 40.078, 20],
        "Cd": ["Cadmium", 112.411, 48],
        "Ce": ["Cerium", 140.116, 58],
        "Cl": ["Chlorine", 35.453, 17],
        "Co": ["Cobalt", 58.933195, 27],
        "Cr": ["Chromium", 51.9961, 24],
        "Cs": ["Cesium", 132.9054519, 55],
        "Cu": ["Copper", 63.546, 29],
        "Dy": ["Dysprosium", 162.5, 66],
        "Er": ["Erbium", 167.259, 68],
        "Eu": ["Europium", 151.964, 63],
        "F": ["Fluorine", 18.9984032, 9],
        "Fe": ["Iron", 55.845, 26],
        "Fr": ["Francium", 223, 87],
        "Ga": ["Gallium", 69.723, 31],
        "Gd": ["Gadolinium", 157.25, 64],
        "Ge": ["Germanium", 72.64, 32],
        "H": ["Hydrogen", 1.00794, 1],
        "He": ["Helium", 4.002602, 2],
        "Hf": ["Hafnium", 178.49, 72],
        "Hg": ["Mercury", 200.59, 80],
        "Ho": ["Holmium", 164.93032, 67],
        "I": ["Iodine", 126.90447, 53],
        "In": ["Indium", 114.818, 49],
        "Ir": ["Iridium", 192.217, 77],
        "K": ["Potassium", 39.0983, 19],
        "Kr": ["Krypton", 83.798, 36],
        "La": ["Lanthanum", 138.90547, 57],
        "Li": ["Lithium", 6.941, 3],
        "Lu": ["Lutetium", 174.9668, 71],
        "Mg": ["Magnesium", 24.305, 12],
        "Mn": ["Manganese", 54.938045, 25],
        "Mo": ["Molybdenum", 95.96, 42],
        "N": ["Nitrogen", 14.0067, 7],
        "Na": ["Sodium", 22.98976928, 11],
        "Nb": ["Niobium", 92.90638, 41],
        "Nd": ["Neodymium", 144.242, 60],
        "Ne": ["Neon", 20.1797, 10],
        "Ni": ["Nickel", 58.6934, 28],
        "Np": ["Neptunium", 237, 93],
        "O": ["Oxygen", 15.9994, 8],
        "Os": ["Osmium", 190.23, 76],
        "P": ["Phosphorus", 30.973762, 15],
        "Pa": ["Protactinium", 231.03588, 91],
        "Pb": ["Lead", 207.2, 82],
        "Pd": ["Palladium", 106.42, 46],
        "Pm": ["Promethium", 145, 61],
        "Po": ["Polonium", 209, 84],
        "Pr": ["Praseodymium", 140.90765, 59],
        "Pt": ["Platinum", 195.084, 78],
        "Pu": ["Plutonium", 244, 94],
        "Ra": ["Radium", 226, 88],
        "Rb": ["Rubidium", 85.4678, 37],
        "Re": ["Rhenium", 186.207, 75],
        "Rh": ["Rhodium", 102.9055, 45],
        "Rn": ["Radon", 222, 86],
        "Ru": ["Ruthenium", 101.07, 44],
        "S": ["Sulfur", 32.065, 16],
        "Sb": ["Antimony", 121.76, 51],
        "Sc": ["Scandium", 44.955912, 21],
        "Se": ["Selenium", 78.96, 34],
        "Si": ["Silicon", 28.0855, 14],
        "Sm": ["Samarium", 150.36, 62],
        "Sn": ["Tin", 118.71, 50],
        "Sr": ["Strontium", 87.62, 38],
        "Ta": ["Tantalum", 180.94788, 73],
        "Tb": ["Terbium", 158.92535, 65],
        "Tc": ["Technetium", 98, 43],
        "Te": ["Tellurium", 127.6, 52],
        "Th": ["Thorium", 232.03806, 90],
        "Ti": ["Titanium", 47.867, 22],
        "Tl": ["Thallium", 204.3833, 81],
        "Tm": ["Thulium", 168.93421, 69],
        "U": ["Uranium", 238.02891, 92],
        "V": ["Vanadium", 50.9415, 23],
        "W": ["Tungsten", 183.84, 74],
        "Xe": ["Xenon", 131.293, 54],
        "Y": ["Yttrium", 88.90585, 39],
        "Yb": ["Ytterbium", 173.054, 70],
        "Zn": ["Zinc", 65.38, 30],
        "Zr": ["Zirconium", 91.224, 40]
    }

    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    total_molar_mass = 0
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
    # Separate the inner list into symbol and quantity.
    for inner_list in symbol_quantity_list:
        list_symbol = inner_list[SYMBOL_INDEX]
        quantity = inner_list[QUANTITY_INDEX]
        # Get the atomic mass for the symbol from the dictionary.
        for dict_symbol, dict_list in periodic_table_dict.items():
            if dict_symbol == list_symbol:
                # Multiply the atomic mass by the quantity.
                # Add the product into the total molar mass.
                atomic_mass = dict_list[ATOMIC_MASS_INDEX]
                total_molar_mass += (atomic_mass * quantity)
    # Return the total molar mass.

    return total_molar_mass

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total number of protons of all
        the elements in symbol_quantity_list.
    """
    total_protons = 0
    for inner_list in symbol_quantity_list:
        list_symbol = inner_list[SYMBOL_INDEX]
        quantity = inner_list[QUANTITY_INDEX]
        # Get the atomic mass for the symbol from the dictionary.
        for dict_symbol, dict_list in periodic_table_dict.items():
            if dict_symbol == list_symbol:
                # Multiply the atomic mass by the quantity.
                # Add the product into the total molar mass.
                atomic_number = dict_list[ATOMIC_NUMBER_INDEX]
                total_protons += (atomic_number * quantity)
    # Return the total molar mass.
    return total_protons

def number_moles(total_molar_mass, grams_of_the_sample):
    """This function calculates and returns the number of 
    moles in the sample from the total molar mass and weight 
    in grams of the sample.
    """
    if grams_of_the_sample != 0:
        total_moles_sample =  grams_of_the_sample/total_molar_mass
        return total_moles_sample
    else:
        return 0


def number_protons(total_protons, total_moles_sample):
    """This function calculates and returns the number of protons in
    the sample from the number of protons in each molecule and the 
    number of moles in the sample.
    """
    total_protons_sample = total_protons * total_moles_sample * MOL 
    return total_protons_sample

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """

    for formula_dict, name_dict in known_molecules_dict.items():
        if formula == formula_dict:
            return name_dict
        
    return f"{formula} isn't in our registers"
    
def main():
    # Get a chemical formula for a molecule from the user.
    molecular_formula = input("Enter the molecular formula of the sample: ")

    # Get the mass of a chemical sample in grams from the user.
    grams_of_the_sample = float(input("Enter the mass in grams of the sample: "))

    # Call the make_known_molecules_table function and
    # store the periodic table in a variable.
    known_molecules_dict = make_known_molecules_table()

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()

    # Call the parse_formula function to convert the chemical formula given by 
    # the user to a compound list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(molecular_formula, periodic_table_dict)
    
    # Call the compute_molar_mass function to compute the molar mass of the 
    # molecule from the compound list.
    total_molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)

    # Call the sum_protons function to compute the total of protons in the 
    # molecule from the compound list.
    total_protons = sum_protons(symbol_quantity_list, periodic_table_dict)

    # Call the sum_protons function to compute the number of moles in the sample.
    number_moles_sample = number_moles(total_molar_mass, grams_of_the_sample)

    # Call the sum_protons function to compute the number of protons in the sample.
    number_protons_sample = number_protons(total_protons, number_moles_sample)

    # call the get_formula_name function to return the name of the chemical formula
    formula_name = get_formula_name(molecular_formula, known_molecules_dict)

    # Print the name of the chemical formula
    print(f"{formula_name}")

    # Print the molar mass.
    print(f"{total_molar_mass:.5f} grams/mole")

    # print total number of protons in the molecula
    print(f"{total_protons} protóns/molecula")

    # Print the number of moles.
    print(f"{number_moles_sample:.5f} moles in the sample")
    
    # Print the number of protons in the sample
    print(f"{number_protons_sample:.5e} protóns in the sample")


if __name__ == "__main__":
    main()