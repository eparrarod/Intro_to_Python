from random import randint

print("Welcome to Rock Paper Scissors 2.0")
print("How many rounds would you like to play?")
rounds = int(input())  # Get number of rounds from user input


def rock_paper_scissor():
    tie = True  # Initialize this variable with a value such that the while loop executes at least once

    while tie:
        computer_choice = randint(1, 3)  # Random choice of rock, paper, scissors
        print("Please enter your choice. Enter 1 for rock, 2 for paper, 3 for scissors")
        player_choice = int(input())
        if player_choice != computer_choice:  # when should the loop end?
            tie = False
        else:
            print("It was a tie. Try again")

    if computer_choice == 1:  # rock
        if player_choice == 2:  # paper
            winner = 0  # Player wins
        else:  # scissors
            winner = 1  # Computer wins
    if computer_choice == 2:  # paper
        if player_choice == 3:  # scissors
            winner = 0  # Player wins
        else:  # rock
            winner = 1  # Computer wins
    if computer_choice == 3:  # scissors
        if player_choice == 1:  # rock
            winner = 0  # Player wins
        else:  # paper
            winner = 1  # Computer wins
    if winner == 0:
        print("You won this round")
    else:
        print("Computer won this round")
    return winner


rounds_player_won = 0  # Initialize a variable to count how many rounds the player wins
for round in range(rounds):
    round_winner = rock_paper_scissor()
    if round_winner == 0:  # The player won the round
        rounds_player_won += 1

rounds_computer_won = rounds - rounds_player_won

print("The player won: %i rounds" % rounds_player_won)
print("The computer won: %i rounds" % rounds_computer_won)
