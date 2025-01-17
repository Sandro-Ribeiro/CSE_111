# Example 3
"""
When we use functional programming to program a 
computer, we focus on the functions necessary to 
accomplish a task.
"""

from functools import reduce

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()