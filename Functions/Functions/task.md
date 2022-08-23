# Functions

Functions are a way to divide your code into useful blocks, make it more readable, and reuse it. 

You define a function by using the keyword ```def``` followed by the function name and the parenthesized list of formal parameters (which can be empty). The statements that form the body of the function start at the next line and must be indented.

<details>
Formal parameters are enclosed in parentheses; they are the variables defined by the function that receive values when the function is called. The list consists of variable names of all the necessary values for the function. Each formal parameter is separated by a comma. When you have a function that does not need any input values, the function should have an empty set of parentheses after the function name. e.g. addition().
</details>

Functions only run when they are called. To call a function, use its name followed by parentheses:

```
def my_function():  # function definition
  print("Hello from a function")

my_function()  # function call
```

Functions may return a value to the caller, using the keyword ```return``` . You can use the returned value to assign it to a variable or just print the result. 

In fact, even functions without a return statement do return a value. This value is called ```None```. While ```None``` is normally suppressed by the interpreter, you can use print (E.g., ```print(my_function())```)

Task:
- Call the function my_function inside the loop to repeat its invocation 5 times
- Define a function that can replace the duplicated print statements in the file.