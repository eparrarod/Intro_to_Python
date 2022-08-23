# Lists

A Python list is a variable that can store multiple items. You can access any item in the list by using it's index

They have many properties of an array of the sort one might find in Java or C, in thatthey can be used as a place to store things and have random access to them.

A list can be initialized by using a series of comma-separated values (items) enclosed in square brackets.
Examples:
- ```lst = [item1, item2]```
- ```lst = []``` # An empty list

Lists might contain items of different types, but usually all the items in a list are of the same type. 

The content of a lists can be changed using their index in square brackets ```lst[index] = new_item```.

```
cubes = [1, 8, 27, 65, 125]  # something's wrong here
# the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
cubes
[1, 8, 27, 64, 125]
```

### Wait a Minute

Why did we modify index 3 if the wrong value is at the fourth position?

The indices of a list on python start at 0. Below is a representation of what the indices of the cubes list and their corresponding values

list_values = [1, 8, 27, 64, 125]

list_indices = [0, 1, 2, 3, 4]

In general, for any list with N elements:
- The index of the first element is ```0```
- The index of the last element is ```N-1```

You can add new items at the end of the list by using the append() method or list concatenation.

```
squares = [1, 4, 9, 16, 25]
squares.append(6**2)  # The ** operator is the Exponentiation operator
```
squares is updated to [1, 4, 9, 16, 25, 36]

```
squares += [49, 64]  # Add two items to the list using list concatenation
```

squares is updated to [1, 4, 9, 16, 25, 36, 49, 64]