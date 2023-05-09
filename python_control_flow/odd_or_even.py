# Python Control Flow Task 2 - 1. Odd or Even Program

# cast the input to integer
num = int(input("Enter a number (must be integer): "))

# check if remainder of num is 0 when divided by 2 (even)
if num % 2 == 0:
    print("The number is even!")
# otherwise it must be an odd number
else:
    print("The number is odd!")
