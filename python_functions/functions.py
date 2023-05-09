# Functions

# Functions allow us to not duplicate code!
# DRY - Don't Repeat Yourself
# Makes code clearner and easier to read

# Create a function
# def print_something(print_string):
#     print(print_string)


# print_something("Luke")
# print_something("Yasmin")

# def greeting(name):
#     print(f"Hello, my name is {name}")
#
#
# greeting("Bradley")

# This function adds two ints together
def addition(int1=10, int2=6):
    return int1 + int2


#
#
# print(addition())
# print(addition(4, 4))


# Multiple arguments
# This function showcases how to use multi-arguments
def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

    print(multiargs[3])


multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Functions good practices

# Define your functions at the start
# Each function should do one thing
# Name them properly
# Always use return
# Comments to showcase what your functions do
