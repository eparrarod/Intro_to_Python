# This is a loop that will execute as long as a has a value less than 10

a = 0
while a < 10:
    a = a + 1  # Everytime the loop run, the variable is updated
    print("current value of variable a is: {}".format(a))


square = 1  # Variable introduced to keep track of the iterations

while square <= 10:
    print(square)    # This code is executed 10 times
    square += 1      # This code is executed 10 times

print("Finished")  # This code is executed once
