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
    ITEM_ID_INDEX = 0
    ITEM_NAME_INDEX = 1
    ITEM_PRICE_INDEX = 2
    ITEM_QTD_INDEX = 3

    request_list = []
    qtd_sum = 0
    price_sum = 0
    subtotal1 = 0
    subtotal2 = 0
    sales_tax_rate = 0.06

    try:
        filename = "./data/products.csv"
        products_dict = read_dictionary(filename, REQ_ID_INDEX)
    except FileNotFoundError:
        print("No such file or directory: 'products.csv'")
    
    try:
        with open("./data/request.csv", "rt") as file:
            request_file = csv.reader(file)
            next(request_file)
            for line in request_file:
                key = line[REQ_ID_INDEX]
                try:
                    item = list(products_dict[key])
                    item.append(line[REQ_QTD_INDEX])
                    item[ITEM_PRICE_INDEX] = float(item[ITEM_PRICE_INDEX])
                    item[ITEM_QTD_INDEX] = int(item[ITEM_QTD_INDEX])
                    if request_list == []:
                        request_list.append(item)
                    else:
                        item_found = False 
                        for request_item in request_list:
                            if item[ITEM_ID_INDEX] == request_item[ITEM_ID_INDEX]:
                                request_item[ITEM_QTD_INDEX] = request_item[ITEM_QTD_INDEX] + item[ITEM_QTD_INDEX]
                                item_found = True
                        if not item_found:
                            request_list.append(item)
                except KeyError:
                    print(f"the {key} isn't known product ID in the request.csv file")
                    print()
                    input("Press Enter to continue ...")
    except PermissionError:
        print("No such file or directory: 'request.csv'")

    request_list_order = sorted(request_list, key = lambda x: x[2])

    for item in request_list_order:
        if item[ITEM_QTD_INDEX] >= 2:
            subtotal1 += ((item[ITEM_PRICE_INDEX] * 0.50) + (item[ITEM_PRICE_INDEX] * (item[ITEM_QTD_INDEX] - 1)))
            subtotal2 += ((item[ITEM_QTD_INDEX] * item[ITEM_PRICE_INDEX]))
        else:
            subtotal1 += ((item[ITEM_QTD_INDEX] * item[ITEM_PRICE_INDEX]))
            subtotal2 += ((item[ITEM_QTD_INDEX] * item[ITEM_PRICE_INDEX]))
        price_sum = price_sum + item[ITEM_PRICE_INDEX]
        qtd_sum = qtd_sum + item[ITEM_QTD_INDEX]         

    sales_tax = subtotal1 * sales_tax_rate
    discount = subtotal2 - subtotal1
    total = subtotal1 + sales_tax
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
    print()
    print("----------------------------------------------")
    print("                   Summary                    ")
    print("----------------------------------------------")
    print(f"Number of items: {qtd_sum}")
    print("----------------------------------------------")
    print(f"Subtotal without discount: {subtotal2: .2f}")
    print("----------------------------------------------")
    print(f"Discount: {discount: .2f}")
    print("----------------------------------------------")
    print(f"Subtotal with discount: {subtotal1: .2f}")
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

