# Python Control Flow Task 1 - Improved Movie Ratings Program

# Ask the user for their age and ensure it is an integer between 1 and 117
while True:
    age = input("What is your age?\n")
    # check string for digits only (positive integers only)
    if age.isdigit():
        # cast string to integer
        age = int(age)
        # check for correct age range
        if 1 <= age <= 117:
            break
        else:
            # user prompt to try again
            print("Please enter your age between 1 and 117")
    else:
        # user prompt to try again
        print("Please enter your age in positive integers")

# Tell the user what rated movies they can watch
# conditions for age ratings
if age >= 18:
    print("You can watch movies with the following ratings: 18, 15, 12/12A, PG and U")
elif age >= 15:
    print("You can watch movies with the following ratings: 15, 12/12A, PG and U")
elif age >= 12:
    print("You can watch movies with the following ratings: 12/12A, PG and U")
elif age >= 8:
    print("You can watch movies with the following ratings: PG and U")
else:
    print("You can watch movies with the following ratings: U")
