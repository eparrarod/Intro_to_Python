
# Constant expression

if True:  # Since it is constant, the statements below will always be executed
    pi = 3.14
    print("pi is: {}".format(pi))

if False:  # Since it is constant, the statements below will never be executed
    gravity = 0.12
    print("Gravity on earth is: {}".format(gravity))

# Does it make sense to use constant expressions? No

# Logical expression
max_capacity = 5
current_capacity = 7
if current_capacity > max_capacity:
    print("The bus is crowded")

current_capacity = 3
if current_capacity < max_capacity:
    print("Theres room in the bus")

# logical combination
light_color = "red"
car_in_intersection = 5
if light_color != "red" and not car_in_intersection > 0:
    print("Go ahead car")

light_color = "red"
car_in_intersection = 5
if light_color == "red" and not car_in_intersection > 0:
    print("Do not start the car")

a = 1
b = 5
c = b
d = -10

if a < b and c > d:
    print("a < b and c > d")


# Logical variable (Flag)

max_capacity = 5
current_capacity = 2
flag = current_capacity < max_capacity # Frequently used to store the result of some relational expression

if flag:
    print("There is room in the bus for more people (or dogs)")


flag = True  # We can assign a particular value (i.e., True or False)

if flag:
    print("There is room in the bus for more people (or dogs)")




