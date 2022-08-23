computer_choice = 2
min = 1
max = 10

print("Please guess a number between %i and %i: " % (min, max))
player_choice = int(input())

if computer_choice == player_choice:
    print("You win!")
else:    # Complete the if statement
    print("Sorry, You lose.")
