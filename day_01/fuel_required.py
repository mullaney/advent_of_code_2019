
import math

def fuel_required(mass):
  return math.floor(mass / 3) - 2

def total_fuel_required(mass):
  fuel = fuel_required(mass)
  if fuel <= 0:
    return 0
  else:
    return fuel + total_fuel_required(fuel)

if __name__ == '__main__':
  f = open("../data/input.txt", "r")
  modules = f.readlines()
  fuel_requirements = []
  total_fuel_requirements = []
  for line in modules:
    mass = int(line.strip())
    fuel_requirements.append(fuel_required(mass))
    total_fuel_requirements.append(total_fuel_required(mass))
  print(sum(fuel_requirements))
  print(sum(total_fuel_requirements))

