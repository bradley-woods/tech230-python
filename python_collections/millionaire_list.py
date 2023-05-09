# Task 1 - Millionaire list
"""
Define a list with some cool things inside. E.g. things you would buy if you were a millionaire.
The list must have at least 5 elements.
"""
# First, print the list and check its type
millionaire = ["ferrari", "island", "avengers_hq", "home_gym", "unlimited_pizza", "climbing_wall"]
print(millionaire)
print(type(millionaire))

# Print the list's first element
print(millionaire[0])

# Print the list's second element
print(millionaire[1])

# Print the list's last element using negative indexing
print(millionaire[-1])

# Replace the first item in the list
millionaire[0] = "bugatti"

# Replace another item in the list and print the list
millionaire[4] = "unlimited_mango_sorbet"
print(millionaire)

# Add a new item to the list, print the list
millionaire.append("games_room")
print(millionaire)

# Remove an item from the list, print the list
millionaire.remove("home_gym")
print(millionaire)

# Remove the last item from the list without specifying what it is
millionaire.pop()
print(millionaire)
