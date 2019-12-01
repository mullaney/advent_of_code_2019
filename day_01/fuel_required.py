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
  masses = list(map(lambda l: int(l.strip()), f.readlines()))
  print(sum(map(fuel_required, masses)))
  print(sum(map(total_fuel_required, masses)))
