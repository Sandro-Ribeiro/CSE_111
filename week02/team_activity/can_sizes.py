import math;

pi = math.pi

def compute_volume(radius, height):
    volume = pi*pow(radius,2)*height
    return volume

def compute_surface_area(radius, height):
    surface_area =  2*pi*radius*(radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    storre_efficiency = compute_volume(radius, height)/compute_surface_area(radius, height)
    return storre_efficiency

def compute_cost_efficiency(radius, height, cost):
    cost_efficiency = compute_volume(radius, height)/cost
    return cost_efficiency

def found_highest_storage_efficiency(name, storage_efficiency, highest_storage_name, highest_storage_efficiency):
    if storage_efficiency > highest_storage_efficiency:
        highest_storage_efficiency = storage_efficiency
        highest_storage_name = name
    return [highest_storage_name, highest_storage_efficiency]

def found_highest_cost_efficiency(name, cost_efficiency, highest_cost_name, highest_cost_efficiency):
    if cost_efficiency > highest_cost_efficiency:
        highest_cost_efficiency = cost_efficiency
        highest_cost_name = name
    return [highest_cost_name, highest_cost_efficiency]
def main():

    dados = [
    ["#1 Picnic", 6.83, 10.16, 0.28],
    ["#1 Tall", 7.78, 11.91, 0.43],
    ["#2", 8.73, 11.59, 0.45],
    ["#2.5", 10.32, 11.91, 0.61],
    ["#3 Cylinder", 10.79, 17.78, 0.86],
    ["#5", 13.02, 14.29, 0.83],
    ["#6Z", 5.40, 8.89, 0.22],
    ["#8Z short", 6.83, 7.62, 0.26],
    ["#10", 15.72, 17.78, 1.53],
    ["#211", 6.83, 12.38, 0.34],
    ["#300", 7.62, 11.27, 0.38],
    ["#303", 8.10, 11.11, 0.42]
]
    
    highest_storage_efficiency = 0
    highest_storage_name = ""
    highest_cost_efficiency = 0
    highest_cost_name = ""

    print("\nTeam Activity: Can Efficiency\n")

    for dado in dados:
        name = dado[0]
        radius = dado[1]
        height = dado[2]
        cost = dado[3]
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        print(f"{name}: {storage_efficiency:.2f} - {cost_efficiency: .2f}")
        answer_storage = found_highest_cost_efficiency(name, storage_efficiency, highest_storage_name, highest_storage_efficiency)
        highest_storage_efficiency = answer_storage[1]
        highest_storage_name = answer_storage[0]
        answer_cost = found_highest_cost_efficiency(name, cost_efficiency, highest_cost_name, highest_cost_efficiency)
        highest_cost_efficiency = answer_cost[1]
        highest_cost_name = answer_cost[0]
    print(f"\nThe Highest Storage Efficiency is {highest_storage_efficiency:.2f} and belongs to {highest_storage_name}")
    print(f"The Highest Cost Efficiency is {highest_cost_efficiency:.2f} and belongs to {highest_cost_name}\n")
            
main()

