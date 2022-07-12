def getUserName() -> str:
    # ask user for username
    username = input("What's your name? ").strip()
    codingCourseName = "intro to programming with python!".title()

    # say hello to username
    print("hello, {}".format(username))
    print(f'Welcome to "{codingCourseName}", ' + username)
    fullname = input("What is your first and last name? ")
    firstName, lastName = fullname.split(" ")

    print(f'Should I call you by, {firstName}, or, {lastName}')

getUserName()