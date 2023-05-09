# Python Control Flow Task 2 - 2. Number Guess Program
from random import randrange

num = randrange(20)

i = 0

while i < 3:

    i += 1

    while True:
        guess = input("Guess a number between 1 and 20: ")
        # check string for digits only (positive integers only)
        if guess.isdigit():
            # cast string to integer
            guess = int(guess)
            # check for correct number range
            if 1 <= guess <= 20:
                break
            else:
                # user prompt to try again
                print("Please enter your number between 1 and 20")
        else:
            # user prompt to try again
            print("Please enter your number in positive integers")

    if guess == num:
        print("Well done, you guessed correctly!")
        break
    elif guess > num:
        print("Try lower")
    else:
        print("Try higher")
