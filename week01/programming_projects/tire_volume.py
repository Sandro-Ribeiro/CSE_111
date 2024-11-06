import math;
import os;

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clean()
print("|***************************************************|")
print("|                   Tire Volume                     |")
print("|***************************************************|\n")

pi = math.pi;

print("Welcome to Tire Volume \n");
w = float(input("Enter the width of the tire in mm: "));
a = float(input("Enter the aspect ratio of the tire: "));
d = float(input("Enter the diameter of the wheel in inches: "));

v = round((pi*math.pow(w,2)*a*(w*a+2540*d))/10000000000, 2);

print(f"\nThe approximate volume is {v} liters\n")
input("Press Enter to finish...")
clean()



