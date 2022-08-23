#let's count how many dogs you have seen today

# We start at 0
dog_counter = 0
print("I saw {} dogs".format(dog_counter))

# You see five dogs at a distance
dog_counter += 3
print("I saw {} dogs".format(dog_counter))

# You realize 2 of them were not dogs but dos statues
dog_counter -= 2
print("I saw {} dogs".format(dog_counter))

# A Dog walker passes by with many dogs
dog_counter += 10  # Increase the counter by your desired amount
print("I saw {} dogs".format(dog_counter))

# You see one more dog
dog_counter += 1
print("I saw {} dogs".format(dog_counter))

# The dog you saw was part of the dogs you saw with the dog walker
dog_counter -= 1
print("I saw {} dogs".format(dog_counter))
