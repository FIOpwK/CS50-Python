def getUserName() -> str:
    # ask user for username
    username = input("What's your name? ").strip()
    codingCourseName = "intro to programming with python!".title()

    # say hello to username
    print("hello, {}".format(username))
    print(f'Welcome to "{codingCourseName}", ' + username)

getUserName()