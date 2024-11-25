# Example 2
"""
A simple value is a value that doesn’t contain parts, such as an integer. 
A compound value is a value that has parts, such as a list. Example 2 shows 
a students dictionary where each value is a Python list. Because each list 
contains multiple parts, we say that the dictionary stores compound values.
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