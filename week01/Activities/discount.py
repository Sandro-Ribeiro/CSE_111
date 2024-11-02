from datetime import datetime;
import os;

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

dt = datetime.now(tz=None)
day = dt.weekday()

option = 1;

while option != 0:
  
  clear()
  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
  print('+                       DISCOUNTS                      +')
  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
  print('\n')

  subtotal = float(input("Please enter the subtotal: "))
  print('\n')

  if subtotal < 50.00:

    diff = round(50.00 - subtotal, 2);
    tax = round(subtotal * 0.06, 2);
    total = round(subtotal + tax, 2);

    print(f'Sales tax amount: {tax}')
    print(f'Total: {total}')
    print('\n')

    if day == 1 or day == 2:

      print(f'There are {diff} left for you to receive a 10% discount on your purchase. Do you want to complete this amount?')
      option = int(input('Enter with 1 if yes and 0 if not: '))
      print('\n')

    else:

      print('Do you want enter with other subtotal?')
      option = int(input('Enter with 1 if yes or 0 if not: '))
      print('\n')

  else:
    if day == 1 or day == 2:

      discount = round(subtotal * 0.10, 2);
      tax = round((subtotal - discount) * 0.06, 2);
      total = round(subtotal - discount + tax, 2);

      print(f'Discount amount: {discount}')
      print(f'Sales tax amount: {tax}')
      print(f'Total: {total}')
      print('\n')

      print('Do you want enter with other subtotal?')
      option = int(input('Enter with 1 if yes or 0 if not: '))
      print('\n')

    else:
      
      tax = round(subtotal * 0.06, 2);
      total = round(subtotal + tax, 2);
      print(f'Sales tax amount: {tax}')
      print(f'Total: {total}')
      print('\n')

      print('Do you want enter with other subtotal?')
      option = int(input('Enter with 1 if yes or 0 if not: '))
      print('\n')

clear()
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+    Thank you for your preference, come back always!  +')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('\n')
input('Press enter to finish...')
clear()

  