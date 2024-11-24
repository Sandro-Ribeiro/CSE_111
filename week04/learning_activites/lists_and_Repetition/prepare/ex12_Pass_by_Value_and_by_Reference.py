# Example 12
"""
The fact that the computer copies the value of some data 
types (boolean, integer, float) and copies the reference 
for other data types (list and other large data types) has 
important implications for passing arguments into functions.

In this example, we see that modifying an integer parameter 
changes the integer within the called function only. However, 
modifying a list parameter changes the list within the called 
function and within the calling function
"""

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")
    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)
    print(f"After calling modify_args():  x {x}  lx {lx}")

def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")
    # Change the values of both parameters.
    n += 1
    alist.append(4)
    print(f"   After changing n and alist:  n {n}  alist {alist}")
    
# Call main to start this program.
if __name__ == "__main__":
    main()