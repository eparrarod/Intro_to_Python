# Guess A Number Revisited

On our previous version of the guessing game, the user had only one attempt to guess the number. The user reviews said the game was frustrating, so we will make a new version.

Focus groups said that the game would be better if it allowed the player to guess again until a correct guess was achieved.
We will revisit the guessing game and allow the player to continue guessing numbers until they get it right.

Now, the program will continue until the win-condition is met

## Using a While Loop
Since our program will continue to ask for input until the user has guessed correctly.
In other words, we have a loop that should end when the player guesses the correct number.
We can use the while loop. Next, think about what the condition might be. 
 
The condition is one for continuation of the loop, not termination, so the loop must be constructed in such a way that it continues when the condition is ```True```.

The condition in the loop depends on two values, computer_choice and player_choice.
Therefore, we must define the variables computer_choice and player_choice at the beginning of the loop.
We must also initialize player_choice in such a way that the loop runs at least once.

Task:
- Complete the code using what you have learned
- OPTIONAL: Create a version of this game using less lines of code
<div class="hint">
  start the player_choice as a wrong value
</div>
<div class="hint">
  use input()
</div>
<div class="hint">
  use the == operator
</div>
