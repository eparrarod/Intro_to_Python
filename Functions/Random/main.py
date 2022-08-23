from random import randint, random

print(random())  # Generates a random number

# Flipping a Coin
if randint(1, 2) == 1:
    print("Heads")
else:
    print("Tails")

# You can get a random integer using random()
random_number = random()
print("Here: % is a number between 0.0 and 1.0" % random_number)

# You can get a random integer using random()
random_number = randint(1, 100)
print("Here: % is an integer number between 1 and 100" % random_number)