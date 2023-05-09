# Python Calculator Guide

### Introduction

This guide outlines how to build `calculator.py` breaking it down step-by-step. The following list outlines these steps below:
1. Defining the mathematical functions:
    -  `add` Addition (+) function
    -  `minus` Subtraction (-) function
    -  `times` Multiplication (*) function
    -  `divide` Division (/) function
    -  `mod` Modulo (%) function


2. Defining the conversion functions:
    - `cm_to_m` centimetre to metre function
    - `m_to_ft` metre to feet function


3. Writing the code for user input

### 1. Defining the mathematical functions

- First, create and open a python file named `calculator.py`
- Next, as good practice we want to define all functions at the top of our file. A function can be created using `def` which stands for define.
- Then you can name the function, in this case `add`.
- Next, add in the number of arguments, in this case it is two numbers `(int1, int2)`.
- We want to produce a result of adding the two numbers, so we can achieve this using `return` and then expressing the addition formula (+).
- The function should look something similar to the below:

      def add(int1, int2):
          return int1 + int2

- Now, repeat the above to create functions for all mathematical operators (e.g. -, *, /, %)

### 2. Defining the conversion functions

- Secondly, we want to define another set of functions for converting a value from one unit to another, using `def` to define the function with a suitable name, for example `cm_to_m`.
- The conversion functions only requires one argument `(int1)`.
- The value to be returned shall be the converted value depending on the conversion rate, in this case it is divided by 100 to convert from cm to m.
- The function should look something similar to the below:

      def cm_to_m(int1):
          return int1 / 100

- Now, repeat the above to create functions for the other unit conversions (e.g. m to ft)

### 3. Writing the code for user input

- To make the program user-friendly we need user-input. We can start with a simple title that gets printed using the `print("text goes here")` method.
- Now we need to create a `while True` loop so when a user is asked for input it repeats if the wrong thing is entered.
- Then we need to ask the user if they want to calculate or convert using the `input()` method, as shown below:

      option = input("Do you want to 'calculate' or 'convert'?\n")

- Where `\n` means a new line.
- Now we can use an `if` statement to determine if the user entered calculate or convert, as follows:

      if option == "calculate":

- Now, using the same `input` method, ask the user for the first number and the second number which they want to calculate (ensuring the input is cast to a `float` or `int` and save them as suitable variables `num1` and `num2`:

      num1 = float(input("Enter your first number: "))

- Next, create another `while True` loop in a similar fashion as before, to ask the user which operator they would like (e.g. +) so if anything incorrect is entered they can be prompted again. Example shown below:

      while True:
          op = input("Enter your operator (+, -, *, /, %): ")

- We now need `if` statements so depending on which operator the user chooses, will determine which function is called upon to calculate their value. For example:

                  if op == "+":
                ans = add(num1, num2)
                print(f"Answer: {num1:g} + {num2:g} = {ans:g}")
                break

- Shown above, if the operator is +, the answer `ans` is calculated by calling the appropriate function and printed in a formatted way to the user, then a `break` clause is used to exit the while loop.
- Repeat the above method to create the other `if` statements for the other operators.
- In a similar methodology to the mathematical operators, create functions which call upon the functions for the unit conversions. 

### Summary

Once complete, you should have a working calculator that asks the user if they would like to calculate or convert, then if calculate, ask for two numbers and an operator and produce their answer, or if they chose convert, to ask for a single value and the units to convert from/to and produce the converted answer.