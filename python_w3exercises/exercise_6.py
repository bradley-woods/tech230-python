# Write a Python program that accepts a sequence of comma-separated numbers
# from the user and generates a list and a tuple of those numbers.

numbers = input("Enter comma-seperated numbers: ")

num_list = numbers.split(', ')
num_tuple = tuple(num_list)

print(f"List: {num_list}")
print(f"Tuple: {num_tuple}")
