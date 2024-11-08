import math;
import os;
from datetime import datetime;

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

pi = math.pi;

clean()
print("|***************************************************|")
print("|                   Tire Volume                     |")
print("|***************************************************|\n")

print("Welcome to Tire Volume \n");


w = int(input("Enter the width of the tire in mm: "));
a = int(input("Enter the aspect ratio of the tire: "));
d = int(input("Enter the diameter of the wheel in inches: "));

v = round((pi*math.pow(w,2)*a*(w*a+2540*d))/10000000000, 2);

price = 300;

if w > 200:
    price = price + 120;
if a > 55:
    price = price + 80;
if d > 16:
    price = price + 70;
    
print(f"\nThe approximate volume is {v} liters\n")
print(f"The price is {price}\n");

print("Are you interested in purchasing this product?")
answer = input("Answer 'y' for yes or 'n' for no: ")

if answer == "y":
    phone = input("\nPlease, enter your phone number: ")
    dt = datetime.now().date();
    with open("volume.txt", mode="at") as volumefile:
        print(dt, w, a, d, v, phone, sep=",", file=volumefile, flush=False)
    print("\nYour order has been recorded! Thank you for your preference. Come back soon!!\n")
else:
    print("\nThank you for your preference, come back soon!!\n")

input("Press Enter to finish...")
clean()



