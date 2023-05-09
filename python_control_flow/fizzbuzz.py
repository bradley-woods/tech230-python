# Python Control Flow Task 2 - 3. FizzBuzz Program
# set a range 1 to 100
for num in range(101):
    # if remainder = 0 when divided by 3 and 5, print FizzBuzz
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # if remainder = 0 when divided by 3, print Fizz
    elif num % 3 == 0:
        print("Fizz")
    # if remainder = 0 when divided by 5, print Buzz
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)