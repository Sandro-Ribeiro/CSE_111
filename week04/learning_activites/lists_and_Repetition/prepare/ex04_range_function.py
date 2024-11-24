# Example 4
"""
The Python built-in range function creates and 
returns a sequence of numbers. The range function 
accepts one, two, or three parameters as shown 
in example 4 and its output
"""

def main():
    # Count from zero to nine by one.
    for i in range(10):
        print(i)
    print()
    # Count from five to nine by one.
    for i in range(5, 10):
        print(i)
    print()
    # Count from zero to eight by two.
    for i in range(0, 10, 2):
        print(i)
    print()
    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)
        
# Call main to start this program.
if __name__ == "__main__":
    main()