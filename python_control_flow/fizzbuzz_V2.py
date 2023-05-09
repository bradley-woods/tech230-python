# Python Control Flow Task 2 - 3. FizzBuzz Program Version 2

# function to get the remainder of a number divided by 3
def mod3(num):
    return num % 3


# function to get the remainder of a number divided by 5
def mod5(num):
    return num % 5


# set a range 1 to 100
for n in range(101):
    # if remainder = 0 when divided by 3 and 5, print FizzBuzz
    if mod3(n) == 0 and mod5(n) == 0:
        print("FizzBuzz")
    # if remainder = 0 when divided by 3, print Fizz
    elif mod3(n) == 0:
        print("Fizz")
    # if remainder = 0 when divided by 5, print Buzz
    elif mod5(n) == 0:
        print("Buzz")
    else:
        print(n)
