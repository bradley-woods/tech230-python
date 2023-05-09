# Functional calculator:

# function to add two numbers
def add(int1, int2):
    return int1 + int2


# function to subtract two numbers
def minus(int1, int2):
    return int1 - int2


# function to multiply two numbers
def times(int1, int2):
    return int1 * int2


# function to divide two numbers
def divide(int1, int2):
    return int1 / int2


# function to use modulo on two numbers
def mod(int1, int2):
    return int1 % int2


def cm_to_m(int1):
    return int1 / 100


def m_to_ft(int1):
    return int1 * 3.28084


# main code for calculator
print("Functional Calculator")
print("---------------------")

# loop to choose if user wants to calculate or convert values
while True:
    option = input("Do you want to 'calculate' or 'convert'?\n")

    # if user chose calculate option
    if option == "calculate":
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        while True:
            op = input("Enter your operator (+, -, *, /, %): ")

            # if statements dependent on user chosen operator
            if op == "+":
                ans = add(num1, num2)
                print(f"Answer: {num1:g} + {num2:g} = {ans:g}")
                break
            elif op == "-":
                ans = minus(num1, num2)
                print(f"Answer: {num1:g} - {num2:g} = {ans:g}")
                break
            elif op == "*":
                ans = times(num1, num2)
                print(f"Answer: {num1:g} * {num2:g} = {ans:g}")
                break
            elif op == "/":
                ans = divide(num1, num2)
                print(f"Answer: {num1:g} / {num2:g} = {ans:g}")
                break
            elif op == "%":
                ans = mod(num1, num2)
                print(f"Answer: {num1:g} % {num2:g} = {ans:g}")
                break
            else:
                print("Please enter a valid operator")
        break
    # if user chose convert option
    elif option == "convert":
        val = float(input("Enter your value to convert (in cm or m): "))
        while True:
            unit = input("Enter your conversion as follows:\n- For cm to m, type: cm2m\n- For m to ft, type: m2ft\n")

            # if statements dependent on user chosen conversion
            if unit == "cm2m":
                conv = cm_to_m(val)
                print(f"Answer: {conv:g} m")
                break
            elif unit == "m2ft":
                conv = m_to_ft(val)
                print(f"Answer: {conv:g} ft")
                break
            else:
                print("Please enter a valid conversion")
        break
    else:
        print("You did not choose a valid option")
