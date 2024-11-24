# Example 11
"""
Why does it appear that appending the number 5 onto lx 
also appends the number 5 onto ly ? Because lx and ly 
refer to the same list. There is really only one list 
with two references to that list. Because lx and ly 
refer to the same list, a change to the list through 
variable lx can be seen through variable ly.
"""

def main():
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")
    
# Call main to start this program.
if __name__ == "__main__":
    main()