# Example 4
"""
Clearly, writing one line of code is easier for a programmer than writing the 
for loop. Not only is the one line of code easier to write, but the computer 
will execute it much, much faster than the for loop. Therefore, when you need 
to write code to find an item in a dictionary, don’t write a loop. Instead, 
write one line of code that uses the square brackets ([ and ]) and a key to 
find an item. This example shows the correct way to find an item in a dictionary.
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
    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Check if the student ID is in the dictionary.
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding value, which is a list.
        value = students_dict[id]
        # Retrieve the student's given name (first name) and
        # surname (last name or family name) from the list.
        given_name = value[GIVEN_NAME_INDEX]
        surname = value[SURNAME_INDEX]
        # Print the student's name.
        print(f"{given_name} {surname}")
    else:
        print("No such student")
        
# Call main to start this program.
if __name__ == "__main__":
    main()