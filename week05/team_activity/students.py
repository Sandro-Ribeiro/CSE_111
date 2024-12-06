import csv
import re

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    dict_students = {}

    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            dict_students[row[0]] = row[1]

    return dict_students

def main():
    filename = "./data/students.csv"
    dict_students = read_dictionary(filename)
    i_number = input("Please enter an I-Number: ").strip()
    i_number = i_number.replace("-", "")

    if re.search(r"[^0-9]", i_number):
        print("Invalid I-Number")
        return
    
    if len(i_number) < 9:
        print("Invalid I-Number: too few digits")
        return
    
    if len(i_number) > 9:
        print("Invalid I-Number: too many digits")
        return
    
    try:
        student = dict_students[i_number]
        print(f"Student: {student}")
    except KeyError:
        print(f"No student found with I-Number: {i_number}")

if __name__ == "__main__":
    main()