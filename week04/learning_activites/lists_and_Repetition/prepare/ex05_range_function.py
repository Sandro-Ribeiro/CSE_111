# Example 5
"""
In example 5 at lines 15–16 and lines 20–24, there are two 
for loops. Both loops print each element from a list 
named colors. The first loop iterates over the elements 
in the colors list. The second loop uses the built-in 
len and range functions to iterate over the indexes of 
the colors list. 
"""

def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]
    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)
    print()
    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]
        print(color)
        
# Call main to start this program.
if __name__ == "__main__":
    main()