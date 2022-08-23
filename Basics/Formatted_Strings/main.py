# Formatting using +
day = "Friday"
formatted = "Is it " + day + " yet?"
print(formatted)

item = "Funko Pops"
n = 4
price = 25
print(""
      "I got a great deal on " + item + ". Buy " + str(n) + " for $" + str(price))

# Formatting using %
artist = "Hazel Fernandes"
song = "Number One"
length = 9.43
formatted = "Have you heard \"%s\" by %s ? It is %f minutes long" % (song, artist, length)
print(formatted)


# Formatting using format()
dog_counter = 12
location = "Music Row"
print("I saw {} dogs at {}".format(dog_counter, location))


field_1 = "template"
field_2 = "replacement fields"
field_3 = 3
text = "This is a {}. You can have as many {} as needed. Here I had {}.".format(field_1, field_2, field_3)

# Formatting using an f-String
name = "Fred"
fingers = 9
formatted = f"He said his name is {name}."
print(formatted)

print(f"{name} is funny and has {fingers} fingers")

# Set the values of the variables with your own details
name = "Kenny"
age = 100

# Complete the string formatting here

print("Hello, My name is " + name + " and I am " + str(age) + " years old.")  # Use +

print("Hello, My name is %s and I am %d years old." % (name, age))  # Use %

print(f"Hello, My name is {name} and I am {age} years old.")  # Use an f-string

print("Hello, My name is {} and I am {} years old.".format(name, age))  # Use {} and format