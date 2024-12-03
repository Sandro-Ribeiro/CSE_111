"""
Write a Python program named provinces.py that reads the contents 
of provinces.txt into a list and then modifies the list
"""

def main():

    # Creates the list with the contents of a text file
    list_provinces = read_to_list("./datas/provinces.txt")

    # Print the entire list
    print(list_provinces)
    print()

    # Removes the first element from the list
    list_provinces.pop(0)
    print(list_provinces)
    print()

    # Removes the last element from the list.
    list_provinces.pop()
    print(list_provinces)
    print()

    # Replaces all occurrences of "AB" in the list 
    # with "Alberta".
    for item in range(len(list_provinces)):
        if item == "AB":
            index = list.index(item)
            list_provinces[index] = "Alberta"
    print(list_provinces)
    print()

    # Count the number of elements that are "Alberta" 
    # and print that number.
    count_alberta = list_provinces.count("Alberta")
    print(count_alberta)

def read_to_list(filename):
    """
    This function creates a list from the contents of a text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Creates empty list
    list_provinces = []

    # Opens the text file 
    with open("./data/provinces.txt", "rt") as provinces:

        # Reads each line of the rtext file
        for line in provinces:

            # Appends each line of the text file in the list 
            # removing all white spaces from begin abnd final 
            # of line
            list_provinces.append(line.strip())

    # Return the list with contents of the text file
    return list_provinces

if __name__ == "__main__":
    main()