# Variables
Variables are elements used to store values. 
A variable is like a label, and in Python we use the ``` = ``` symbol, known as the assignment operator, to assign a value to a variable.
The first time you create a variable is known as declaration.

```cd = 0``` Declaration of the variable cd with an initial value of 0. In Python, you need to assign a value when declaring a variable.

An assignment can be chained, e.g., ``` a = b = 2```.

# Value vs address
When you create a variable, Python will store each of them at a particular memory address in your computer's memory.



## Naming convention
In Python, you may name variables the same way as Java. However, the most commonly used notation for naming variables in Python is to use lowercase and to use ```_``` between words.
Examples:
```
user
username
last_name
temporary_pass 
```
```very_important_value_temporary_storage``` is a valid variable name. But aim to keep your variable names short.

```temp_value``` Sometimes you can use abbreviations

```GPA``` Sometimes acronyms are helpful. GPA is easy to understand if it is a program dealing with grades (in the US)

```DAO``` Other times acronyms are not so helpful.   


## Basic types
A type defines a family of values that a programming language understands. 
The basic types are:
- integer: The variable holds a whole number (e.g., ```0```, ```2```, ```853```, ```-58```)
- double: The variable holds a decimal point value (e.g., ```0.5```, ```1.2```, ```256.14```, ```-2.5```)
- string: The variable holds a series of characters surround by double quotes (```"```) (e.g., ```"a"```, ```"This"```, ```"This is a longer text"```) 
- boolean: A variable holds either the value of ```True```  or ```False``` 

## Casting (Type Conversion)
Is the process of converting a variable from one type to a different type.

The most common casting you will do is to convert a variable of another type into a string.
This is achieved by using ```str(variable_to_convert)```
Example:
```
variable_1 = 1 # variable_1 is an integer holding the number 1
variable_2 = str(variable_1) # variable_2 is a string holding the value "1"
```

If you need to print an integer you do not need to do an assignment. You can do:
```
variable_1 = 25
print(str(variable_1)
```

Tasks:
- Change the value stored in the variable greetings to be the following string ```"Hi there"```.
- Use the chain assignment to store 20 in both a and b on line 13.
- use casting to print b on line 13

<div class="hint">
  Follow the example from line 12
</div>
