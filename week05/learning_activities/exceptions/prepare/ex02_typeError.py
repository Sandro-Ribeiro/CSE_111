# Example 2
"""
The computer raises a ValueError when the code that calls 
a function passes an argument with the correct data type 
but with an invalid value
"""

def main():
  try:
    text = input("Please enter a number: ")
    integer = round(text)
    print(integer)
  except TypeError as type_err:
    print(type_err)
if __name__ == "__main__":
  main()