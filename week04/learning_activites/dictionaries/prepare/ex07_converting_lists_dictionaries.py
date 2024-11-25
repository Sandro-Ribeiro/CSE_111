# Example 7
"""
It is possible to convert two lists into a dictionary by 
using the built-in zip and dict functions. The contents 
of the first list will become the keys in the dictionary, 
and the contents of the second list will become the values. 
This implies that the two lists must have the same length, 
and the elements in the first list must be unique because 
keys in a dictionary must be unique.

It is also possible to convert a dictionary into two lists 
by using the keys and values methods and the built-in list 
function. The following code example starts with two lists, 
converts them into a dictionary, and then converts the 
dictionary into two lists.
"""

def main():
    # Create a list that contains five student numbers.
    numbers_list = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]
    # Create a list that contains five student names.
    names_list = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]
    # Convert the numbers and names lists into a dictionary.
    student_dict = dict(zip(numbers_list, names_list))
    # Print the entire student dictionary.
    print("Dictionary:", student_dict)
    print()
    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())
    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)
    
# Call main to start this program.
if __name__ == "__main__":
    main()