# Lists and Tuples

# Lists

# shopping_list = ["jam", "bread", "yoghurt", "milk"]
#
# print(shopping_list[0])
# print(shopping_list[-1])
#
# shopping_list[0] = "sugar"
# print(shopping_list)

# List methods

# add to the end of a list
# shopping_list.append("carrots")
# print(shopping_list)

# remove items
# shopping_list.remove("milk")
# print(shopping_list)
#
# shopping_list.pop(0)
# print(shopping_list)

# List can be mixed data types

# mix = [1, 2, 3.5, "one", "two", "three", "four"]
# print(mix)

# list slicing
# print(mix[1:3]) # 2, 3.5
# print(mix[-2::]) # :: reverses
# print(mix[::3]) # skipped over

# Tuples

# Lists = mutable, Tuple = immutable

essentials = ("bread", "eggs", "cheese")
print(type(essentials))

