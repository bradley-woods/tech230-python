# Python Control Flow Task 1 - Improved Movie Ratings Program Version 2

# function to get user input age and check it is a positive int between 1 and 117
def check_age():
    # initialise user_age variable
    user_age = 0
    while True:
        # check input for positive integers only
        try:
            user_age = int(input("What is your age?\n"))
        except ValueError:
            print("Please enter your age in positive integers")
            continue

        if 1 <= user_age <= 117:
            break
        else:
            print("Please enter your age between 1 and 117")
    return user_age


# call the check_age() function and assign to 'age' variable
age = check_age()

# Tell the user what rated movies they can watch using if conditions for age ratings
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
