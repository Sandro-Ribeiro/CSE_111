# Example 3
"""
The reason Python dictionaries were developed is to make finding items 
easy and fast. As explained in example 1, to find an item in a dictionary, 
a programmer needs to write just one line of code that follows this template:
value = dictionary_name[key]. That one line of code will cause the computer 
to search the dictionary until it finds the key. Then the computer will return 
the value that corresponds to the key. Some programmers forget how easy it is 
to find items in a dictionary, and when asked to write code to find an item, 
they write complex code like lines 32–35 in this example.
"""

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # This is a difficult and slow way to find an item in a
    # dictionary. Don't write code like this to find an item
    # in a dictionary!
    # For each item in the dictionary, check if
    # its key is the same as the variable id.
    student = None
    for key, value in students_dict.items(): # Bad example!
        if key == id:                        # Don't use a loop
            student = value                  # like this to find an
            break                            # item in a dictionary.