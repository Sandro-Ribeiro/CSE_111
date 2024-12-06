# Example 7
"""
if we write code that attempts to find a key in a dictionary 
and that key doesn’t exist in the dictionary, then the computer 
will raise a KeyError.
"""

def main():
  students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
  }

  # Get a student ID from the user.
  id = input("Enter a student ID: ")
  
  # Check if the student ID is in the dictionary.
  if id in students:
    # Find the student ID in the dictionary and
    # retrieve the corresponding student name.
    name = students[id]
    # Print the student's name.
    print(name)
  else:
    print("No such student")

if __name__ == "__main__":
  main()