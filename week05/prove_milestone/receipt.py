import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dict_products = {}

    with open(filename, "rt") as file:
        products = csv.reader(file)
        next(products)
        for line in products:
            try:
                dict_products[line[key_column_index]] = line
            except IndexError:
                print("Line skipped due to missing key column:", line)
    
    return dict_products

def main():
    ID_INDEX = 0
    NAME_INDEX = 1
    QTD_INDEX = 1
    PRICE_INDEX = 2

    filename = "./data/products.csv"
    products_dict = read_dictionary(filename, ID_INDEX)
    print(products_dict)

    with open("./data/request.csv", "rt") as file:
            request_file = csv.reader(file)
            next(request_file)
            print("Request Items")
            for line in request_file:
                for key, valor in products_dict.items():
                        if line[ID_INDEX] == key:
                            print(f"{valor[NAME_INDEX]}: {line[QTD_INDEX]} @ {valor[PRICE_INDEX]}")


if __name__ == "__main__":
    main()

