def say_hello(number):  # Function named my_function
    print("Hello #{}!".format(number))


print(say_hello(55)) # print the return value of say_hello

for i in range(5):
    say_hello(i)   # Call function defined above passing i as parameter

print(5 + 2)
print(1 + 1)
print(7 + 6)


def fun(a, b):
    return a + b


# After writing your function, comment out lines 8, 9, and 10 and Run
fun(5, 2)
fun(1, 1)
fun(7, 6)
