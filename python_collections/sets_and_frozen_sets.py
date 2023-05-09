# Sets and Frozen Sets

# Sets = Unordered Lists

# no duplicates
car_parts = {"wheels", "doors", "windows", "wheels"}
print(car_parts)

# sets can be changed
car_parts.add("horn")
print(car_parts)

# remove from set
car_parts.discard("doors")
print(car_parts)

# Frozen sets - a set that cannot be changed
x = frozenset([1, 2, 3, 4])
print(x)
