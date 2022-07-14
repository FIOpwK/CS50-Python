import math


def addCalculator():
    # ask user for num1 and num2 to add
    x, y = input('What are two numbers you wish to add? Enter them as "num1 num2" ').split()

    # calculate num1 and num2 from string input
    result = int(x) + int(y)


    # tell user what the result of num1 + num2
    print(result)


def addFloatCalculator():
    x = float(input("Enter a floating point number. "))
    y = float(input("Input another floating point number. "))

    z = round(x + y)

    print(f'Result is {z:_}')


def squarCalculator():
    x = int(input("Enter an integer to square. "))
    print(f' {x} squared is: {square(x)}')

def square(n):
    return pow(n, 2)

# run add functions here
addCalculator()

# run add float function here
addFloatCalculator()

# run squar function here
squarCalculator()