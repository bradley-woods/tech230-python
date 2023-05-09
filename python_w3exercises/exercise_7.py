# Write a Python program that accepts a filename from the user and prints the extension of the file.

filename = input("Enter a file name: ")
extension = filename.rsplit(".")
print(f"Extension: {extension[-1]}")
