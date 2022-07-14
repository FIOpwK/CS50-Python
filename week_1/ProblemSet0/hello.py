from xml.dom import InuseAttributeErr


def main():
    name = input("Hello, how can i help you? ")
    getUserName(name) 


def getUserName(to="username") -> str:
    # ask user for username
    codingCourseName = "intro to programming with python!".title()

    # say hello to username using format method
    print("hello, {}".format(to))

    # using f-string and concatenation
    print(f'Welcome to "{codingCourseName}", ' + to)
    fullname = input("What is your first and last name? ")
    firstName, lastName = fullname.split(" ")

    #using f-string
    print(f'Should I call you by, {firstName}, or, {lastName}')

main()