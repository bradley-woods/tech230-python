# Loops

# Loop = loop through list/collection to make a decision.

# In Python, you just use for, not for each

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

# Iterating over the list
# for num in list_data:
#     print(num * 2)

# Iterating over nested lists
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# Iterating over dictionaries
# for item in dict_data.values():
#     print(item)
#     for embed_value in item.values():
#         print(embed_value)

# for items in dict_data.values():
#     print(items["name"])

# Loops and if statements
# for num in list_data:
#     if num == 3:
#         print("You found 3!")
#     elif num > 3:
#         print("Gone too far!")
#     else:
#         print("Too soon!")

# While loops

# Do the thing, as long as the condition is true
x = 0

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    # incrementer
    x += 1

# Uses of while loops

# Check something

# Verifying user input

user_prompt = True
age = ""

while user_prompt:
    age = input("please enter your age: ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please enter your age in digits")

print(f"Your age is {age}")

