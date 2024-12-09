
def main():
    # Creates a list named fruit and...
    fruit_list = ["pear", "banana", "apple", "mango"]

    # prints a list
    print(f"This is original list: {fruit_list}")

    # reverseS fruit_list and...
    fruit_list.reverse()

    # prints the list.
    print(f"This is reversed list: {fruit_list}")

    # appendS "orange" to the end of fruit_list and...
    fruit_list.append("orange")

    # prints the list.
    print(f"The list with orange added at the end: {fruit_list}")

    # finds where "apple" is located in fruit_list and...
    i_apple = fruit_list.index("apple")

    # inserts "cherry" before "apple" in the list and...
    fruit_list.insert(i_apple, "cherry")

    # prints the list.
    print(f"The list with cherry inserted before apple: {fruit_list}")

    # removes "banana" from fruit_list and...
    fruit_list.remove("banana")

    # prints the list.
    print(f"The list after to remove banana: {fruit_list}")

    # pops the last element from fruit_list and... 
    last_element = fruit_list.pop()    

    # prints the popped element and...
    print(f"The last element of the list: {last_element}")

    # prints the list
    print(f"The list without {last_element} element: {fruit_list}")

    # sorts fruit_list and...
    fruit_list.sort()

    # print fruit_list.
    print(f"The sorted list: {fruit_list}")

    # clears fruit_list and...
    fruit_list.clear()

    # print fruit_list.
    print(f"The clean list: {fruit_list}")

    # Thanks
    print("Thank you for attention!")


# If this file is executed like this:
# > python check_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()