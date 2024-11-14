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

def found_highest_cost_efficiency(name, cost_efficiency, highest_efficiency = 0):
    if cost_efficiency > highest_efficiency:
        highest_efficiency = cost_efficiency
    return highest_name

def main():
    with open("data.txt", mode="+r") as data:
        for linha in data:
            parameters = linha.strip().split()
            name = parameters[0].replace('_', ' ')
            radius = float(parameters[1])
            height = float(parameters[2])
            cost = float(parameters[3])
            storage_efficiency = compute_storage_efficiency(radius, height)
            cost_efficiency = compute_cost_efficiency(radius, height, cost)
            print(f"{name}: {storage_efficiency:.2f} - {cost_efficiency: .2f}")
            highest_name = found_highest_cost_efficiency(name, )
            print(f"The Stell Can that show highest cost efficiency is: {name}")
            
                
main()

