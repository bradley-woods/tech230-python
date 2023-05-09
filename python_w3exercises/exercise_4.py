# Write a Python program that calculates the area of a circle based on the radius entered by the user.

import math

radius = float(input("Enter Radius: "))
area = math.pi * radius ** 2
print(f"r = {radius}\nArea = {area}")
