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
    with open("data.txt", mode="+r") as data:
        highest_storage_efficiency = 0
        highest_storage_name = ""
        highest_cost_efficiency = 0
        highest_cost_name = ""
        print("\nTeam Activity: Can Efficiency\n")
        for linha in data:
            parameters = linha.strip().split()
            name = parameters[0].replace('_', ' ')
            radius = float(parameters[1])
            height = float(parameters[2])
            cost = float(parameters[3])
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

