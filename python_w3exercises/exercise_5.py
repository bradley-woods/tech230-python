# Write a Python program that accepts the user's first and last name
# and prints them in reverse order with a space between them.

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")

combined = " ".join([firstname, lastname])

empty = []
for n in range(1, len(combined) + 1):
    n = n * -1
    empty.append(combined[n])
joined = "".join(empty)

print(joined)
print(f"{lastname} {firstname}")
