# Example 6
"""
Python dictionaries are objects with attributes and methods, 
and a programmer can modify a dictionary by calling those 
methods. There doesn’t seem to be an official Python web page 
that documents the dictionary methods, so here is a list of 
the built-in dictionary methods:

d.clear()	    Removes all the elements from the dictionary d.

d.copy()	    Returns a copy of the dictionary d.

d.get(key)	    Returns the value of the specified key. Calling 
                the get method is almost equivalent to using 
                square brackets ([ and ]) to find a key in a 
                dictionary.

d.items()	    Returns a list that contains the key value pairs 
                that are in the dictionary d.

d.keys()	    Returns a list that contains the keys that are in 
                the dictionary d.

d.pop(key)	    Removes the element with the specified key from 
                the dictionary d.

d.update(other)	Updates the dictionary d with the key value pairs 
                that are in the other dictionary.

d.values()	    Returns a list that contains the values that are 
                in the dictionary d.

The following example code, which is similar to example 1 from the 
preparation content 2 of week 4, calls dictionary methods at lines 
53, 59, and 67.
"""

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis",
        "81-298-9238": "Sama Patel"
    }
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Lookup the student ID in the dictionary and
    # retrieve the corresponding student name.
    name = students.get(id)
    if name:
        # Print the student name.
        print(name)
        # Remove the student that the user
        # specified from the dictionary.
        students.pop(id)
    else:
        print("No such student")
    print()
    # Use a for loop to print each key value pair
    # in the dictionary. Of course, the code in
    # the body of a loop can do much more with
    # each key value pair than simply print it.
    for key, value in students.items():
        print(key, value)
# Call main to start this program.
if __name__ == "__main__":
    main()