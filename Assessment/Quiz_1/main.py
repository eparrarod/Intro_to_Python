from random import randint


def cheer_up():
    choice = randint(1, 3)
    if choice == 1:
        print("You are doing great")
    elif choice == 2:
        print("You are pawsome")
    else:
        print("We could use a nap")
