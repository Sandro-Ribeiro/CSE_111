# Example 10
"""
In a Python program, the computer assigns values 
to variables differently based on their data type.
"""

def main():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")
    
# Call main to start this program.
if __name__ == "__main__":
    main()