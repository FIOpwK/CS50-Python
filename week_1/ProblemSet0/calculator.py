def addCalculator():
    # ask user for num1 and num2 to add
    x, y = input('What are two numbers you wish to add? Enter them as "num1 num2" ').split()

    # calculate num1 and num2 from string input
    result = int(x) + int(y)


    # tell user what the result of num1 + num2
    print(result)

# run functions here
addCalculator()