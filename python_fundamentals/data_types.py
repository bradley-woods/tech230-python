# # # Data types
# #
# # # 3 main data types
# #
# # # Numbers
# # # Strings
# # # Booleans (True or False)
# #
# # # Numbers
# #
# # # Integers -> Whole numbers (positive or negative)
# # # Float -> Floating point number
# # # Complex -> Huge numbers, that can only be derived by a formula
# #
# # a = 24
# # b = 16
# #
# # # Arithmetic operators
# #
# # # +, -, *, /, %(modulo)
# #
# # print(a + b) # 40
# # print(a - b) # 8
# # print(a * b) # 384
# #
# # # Comparison operators
# #
# # # == equal to
# # # != not equal to
# # # > greater than
# # # < less than
# # # >= greater than or equal to
# # # <= less than or equal to
# #
# # print(a > b) # True
# # print(a == b) # False
# #
# # # Floats
# #
# # Floatnum = 1.356
# # Intnum = 4
# #
# # print(Floatnum + Intnum)
# #
# # one_third = 1 / 3
# # print(one_third)
# # print(one_third * 3)
#
# # Strings
#
# single_quotes = 'Look! Single Quotes'
#
# double_quotes = "Look! Double Quotes"
#
# # print(single_quotes)
# # print(double_quotes)
#
# # string_failure = 'I said 'Wow!''
# escape_example = 'I said \'Wow!\''
# print(escape_example)
#
# reverse_quote = "I said 'Wow!'"
# print(reverse_quote)
#
# # String slicing
# hi = "Hello world!"
#
# #   H   e   l  l  o     w  o  r  l  d  !
# #   0   1   2  3  4  5  6  7  8  9 10 11
# # -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#
# print(hi[0])
# print(hi[6:])
# print(hi[2:6])
# print(hi[-12])
#
# # String methods
#
# # Strip()
# white_space = "There is lot's of white space               "
# print(len(white_space))
# print(len(white_space.strip()))
#
# # Other string methods
# example_text = "This is some text with lot's of text"
#
# # Count a substring within a string
# print(example_text.count("text"))
#
# # make everything lowercase
# print(example_text.lower())
#
# # uppercase
# print(example_text.upper())
#
# # Capitalise
# print(example_text.capitalize())
#
# # Replacing text/characters
# print(example_text.replace("with", ","))
#
# # Replace does not change the variable
# print(example_text)
#
# # Concatenation and Casting
#
# concat1 = "This is a string"
# concat2 = "This is also a string"
#
# print(concat1 + ". " + concat2)
# print(f"{concat1}. {concat2}")
#
# x = 2
# y = 5.4
# z = "string"
#
# print(str(x) + str(y) + " " + z)
#
# int_string = "6"
# print(type(int(int_string)))
#
# f-strings
# name = "Lassie"
# year = 7
# height_cm = 60.2
#
# print(f"{name} is {year} years old and {height_cm} cm tall")
#
# name = "Snoopy"
# years = 52
#
# print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")
#
# pi = 3.14159265359
#
# print(f"Pi to 3 decimal places: {pi:.3f}")
#
# score = 16
# maxscore = 26
#
# print(f"You scored {score/maxscore:.2%}")

# Booleans - True/False

a = True
b = False

# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True
# print(b <= False) # True

# print(True and False) # False
# print(False and False) # False
# print(True and True) # True
# print(True or False) # True

# Booleans with data types

hi = "Hello World!"

# print(hi.isalpha()) # False
# print(hi.islower()) # False
# print(hi.endswith("!")) # True
# print(hi.startswith("H")) # True

# Bools with numbers

x = 0
y = 10

# print(bool(x)) # False - 0
# print(bool(y)) # True - any non-zero

# None and value of None

print(bool(None)) # False

x = None

print(x == False) # False
print(x == True) # False

print(x == None) # True

# This is preferred
print(x is None) # True

# Why do we use None? Placeholder values for variables
