# Control Flow

# if statements
# age = 18
#
# if age >= 18:
#     print("You are the correct age to watch this movie")
# elif age < 18:
#     print("You are too young to watch this movie")


# New movie ratings
film_rating = "12"

if film_rating.lower() == "universal":
    print("All age groups can watch this film")

elif film_rating.lower() == "pg":
    print("Parental guidance advised")

elif film_rating.lower() == ("12" or "12a"):
    print("You must be at least 12 years old to watch this movie")

elif film_rating.lower() == "15":
    print("You must be at least 15 years old to watch this movie")

elif film_rating.lower() == "18":
    print("You must be at least 18 years old to watch this movie")

else:
    print("Not correct movie rating")

# There

