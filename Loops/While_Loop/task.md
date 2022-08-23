# While loop
A ```while``` loop allows you to execute a set of code as long as a condition is ```True```.
The set of lines of code to be executed is determined by increasing their identation level.

If the condition on the while loop is ```False```, it will not execute the lines within the loop.

## Structure

```
while condition:
    do this
    do this
    do this
this line will not be executed
```

The set of lines of code that are part of the while loop end the moment a non-idented line appears

## Example

This is an example of a ```while``` loop 

```
a = 15
while a >= 10
    print("{} is larger than 10")
    a = a-1
```
- The condition is ```a>=10```
- If the value of variable ```a``` is larger or equal than 10
- Will execute the idented lines if the variable ```a``` has a value less or equals to 10
