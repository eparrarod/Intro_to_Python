from random import randint

player_choice = -1  #Declare and initialize player_choice
min = 1
max = 100
computer_choice = randint(min, max)

while player_choice != computer_choice:
    print("Please guess a number between %i and %i: " % (min, max))
    player_choice = int(input())

    if computer_choice == player_choice:
        print("You win!")
    else:
        if player_choice > computer_choice:
            print("Sorry, your guess was too high. Guess again: ")
        else:
            print("Sorry, your guess was too low. Guess again: ")


