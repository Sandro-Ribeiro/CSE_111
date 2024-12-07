import csv
import time
import os

def clean_screen():
    # Determina o comando de acordo com o sistema operacional
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

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

    try:
        with open(filename, "rt") as file:
            products = csv.reader(file)
            next(products)

            for line in products:
                try:
                    dict_products[line[key_column_index]] = line
                except IndexError:
                    print("Line skipped due to missing key column:", line)
    except PermissionError:
        print(f"Permission denied: Cannot access file {filename}")
    
    return dict_products

def main():
    REQ_ID_INDEX = 0
    REQ_QTD_INDEX = 1
    ITEM_NAME_INDEX = 0
    ITEM_PRICE_INDEX = 1
    ITEM_QTD_INDEX = 2

    try:
        filename = "./data/products.csv"
        products_dict = read_dictionary(filename, REQ_ID_INDEX)
    except FileNotFoundError:
        print("No such file or directory: 'products.csv'")

    request_list = []
    qtd_sum = 0
    price_sum = 0
    subtotal = 0
    sales_tax_rate = 0.06
    
    try:
        with open("./data/request.csv", "rt") as file:
            request_file = csv.reader(file)
            next(request_file)
            for line in request_file:
                key = line[REQ_ID_INDEX]
                try:
                    prod = products_dict[key]
                except KeyError:
                    print(f"the {key} isn't known product ID in the request.csv file")
                    print()
                    input("Press Enter to continue ...")
                item = prod[1:]
                item.append(line[REQ_QTD_INDEX])
                price_item = float(item[ITEM_PRICE_INDEX])
                qtd_item = int(item[ITEM_QTD_INDEX])
                price_sum = price_sum + price_item
                qtd_sum = qtd_sum + qtd_item
                subtotal = subtotal + (qtd_item * price_item)
                request_list.append(item)
    except PermissionError:
        print("No such file or directory: 'request.csv'")        

    request_list_order = sorted(request_list)
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax
    now_time = time.ctime()

    clean_screen() 
    print("*************** Grandma's shop ***************")
    print()
    print("----------------------------------------------")
    print("                Request Items                 ")
    print("----------------------------------------------")
    for item in request_list_order:
        print(f"{item[ITEM_NAME_INDEX]}: {item[ITEM_QTD_INDEX]} @ {item[ITEM_PRICE_INDEX]}")
        print("----------------------------------------------")
    print(f"Number of items: {qtd_sum}")
    print("----------------------------------------------")
    print(f"Subtotal: {subtotal: .2f}")
    print("----------------------------------------------")
    print(f"Sales Tax: {sales_tax: .2f}")
    print("----------------------------------------------")
    print(f"Total: {total: .2f}")
    print("----------------------------------------------")
    print()
    print("Thank you for shopping at the Grandma's shop")
    print(now_time)
    print()
    input("Press Enter to exit")
    clean_screen()   
    

if __name__ == "__main__":
    main()

