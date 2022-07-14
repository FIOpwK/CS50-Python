name = input("What's your player name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("G-house")
        
    case "Juan":
        print("House.py")
    case _:
        print("Who knows? ")
