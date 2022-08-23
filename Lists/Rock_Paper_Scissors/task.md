# Rock Paper Scissors

One of the taditional games used by people to settle disputes and make random decisions such as “who goes first”.

In this game each of two players selects one item from the list ```[rock, paper, scissors]``` in
secret, and then both display their choice simultaneously. If both players selected the same
item, then they try again. Otherwise, rock beats scissors, scissors beats paper, and paper beats
rock. 

Your task is to implement this game.

<div class="hint">

Use an integers instead on strings to represent the options in the list. In particular, ``` 1 = rock, 2 = paper, and 3 = scissors```
</div>
<div class="hint">
  Use a while loop
</div>

<div class="hint">
One approach is to do the following:

1. Select a random choice form the three items rock, paper, or scissors. Save this choice in a variable named ```computer_choice```
2. Ask the player for their choice. Use an integer value, where ```1 = rock, 2 = paper, and 3 = scissors```
3. Read the player's selection into a variable named ```player_choice```
4. If ```player_choice``` is equal to ```computer_choice```
5. Print the message "Tie. We'll try again."
6. Repeat from Step 1
7. If ```player_choice``` is equal to rock
8. If ```computer_choice``` is equal to scissors, Print "Computer wins" and terminate
9. Else Print "You win" and terminate
10. If ```player_choice``` is equal to paper
11. If ```computer_choice``` is equal to scissors, Print "Computer wins" and terminate
12. Else Print "You win" and terminate
13. If ```player_choice``` is equal to scissors
14. If ```computer_choice``` is equal to rock, Print "Computer wins" and terminate
15. Else Print "You win" and terminate
</div>
