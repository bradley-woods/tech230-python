# Task 2 - Waiter helper
"""
You are going to make a program that helps a waiter with their menu
3-5 starters
3-5 mains
3-5 desserts
"""
# As a user, I want to be able to see the menu in a formatted way so that I can order my meal.
starters = ["tomato_soup", "nachos", "chicken_wings", "garlic_bread"]
mains = ["pepperoni_pizza", "beef_burger", "vegetable_lasagne", "cauliflower_curry", "mixed_grill"]
desserts = ["chocolate_brownie", "lemon_sorbet", "apple_pie"]

print("Menu\n====")
print("\nStarters\n--------")
for starter in starters:
    print(starter)
print("\nMains\n-----")
for main in mains:
    print(main)
print("\nDesserts\n--------")
for dessert in desserts:
    print(dessert)

# As a user, I want to be able to order three separate times and have my responses added to a list, so they are not
# forgotten.
items = ["starter", "main", "dessert"]
order = []
for item in items:
    order.append(input(f"\nWhat do you want for {item}?\n"))

# As a user, I want to have my order read back to me in a formatted way, so I know what I ordered.
print("\nYou ordered the following:")
for item in order:
    print(f"- {item}")
