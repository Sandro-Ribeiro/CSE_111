# Example 5
"""
In Python, lists are objects with attributes and methods, 
and a programmer can modify a list by calling those methods.

Example below contains a program that is similar to example 2 
in the preparation content 1 of Week 4. Now that you know what 
an object is, that objects have methods, and that Python lists 
are objects, this example code should make more sense than it 
did in week 4. Notice that the append method is called on lines 
19–21, insert is called on line 10, index is called on line 29 
pop is called on line 36, and remove is called on line 39.
"""

def main():
    # Create an empty list that will hold fabric names.
    fabrics = []

    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    print(fabrics)

    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)

    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")
    print(i)

    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"
    print(fabrics)

    # Remove the last element from the fabrics list.
    fabrics.pop()
    print(fabrics)

    # Remove denim from the fabrics list.
    fabrics.remove("denim")
    print(fabrics)

# Call main to start this program.
if __name__ == "__main__":
    main()