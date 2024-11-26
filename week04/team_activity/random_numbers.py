import random

def append_random_numbers(numbers, quantity = 1):
    """
    This function generates pseudorandom numbers in a defined 
    quantity by calling the random uniform function, rounds the 
    pseudorandom numbers to one digit after the decimal, and 
    appends the pseudorandom numbers at the end of the 
    numbers_list.
    """
    for i in range(0, quantity):
        number = round(random.uniform(10, 100), 1)
        numbers.append(number)

    return numbers

def append_random_words(words_list, quantity = 1):
    """
    This functions randomly selects quantity words from a list of 
    words and appends the selected words at the end of words_list.
    """

    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    
    for i in range(0,quantity):
        word = random.choice(words)
        words_list.append(word)

    return words_list

def main():

    numbers = [16.2, 75.1, 52.3]
    words_list = []

    print(numbers)

    numbers = append_random_numbers(numbers)
    print(numbers)
    
    numbers = append_random_numbers(numbers, 3)
    print(numbers)

    words_list = append_random_words(words_list, 6)
    print(words_list)

if __name__ == "__main__":
    main()



