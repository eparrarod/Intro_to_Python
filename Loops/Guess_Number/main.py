computer_choice = 2
player_choice = -1  #Declare and initialize player_choice
min = 1
max = 10

while player_choice != computer_choice:
    print("Please guess a number between %i and %i: " % (min, max))
    player_choice = int(input())

    if computer_choice == player_choice:
        print("You win!")
    else:
        print("Sorry, not correct. Guess again: ")
