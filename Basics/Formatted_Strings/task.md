# String Formatting

Whenever you are displaying information to the user in the form of text you may need to combine different types of variables into a message for the user.

String formatting is the process of combining strings and variables of different types.

## Formatting Using +
You can combine Strings and variables by using the + operator to add up strings.
Any variable that is not a string needs to be converted to a string. You can use ```str()```.

## Formatting Using %
You can use the % operator after a string is used to combine the string with variables. 
The %s special symbol is used as a placeholder for a string. 
The %d special symbol is used as a placeholder for numeric or decimal values
The %i special symbol is used as a placeholder for integer values
The %f special symbol is used as a placeholder for float values

## Formatting Using f-string
A formatted string literal, or an f-string, is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}.

The parts of the string outside curly braces are treated literally. Escape sequences are decoded like in ordinary string literals. Replacement expressions can contain line breaks (e.g., in triple-quoted strings), but they cannot contain comments. Each expression is evaluated in the context where the formatted string literal appears, in order from left to right.

## Formatting Using ```format()```
You can use format() to perform a string formatting operation. 
To use it you need to have a string that contains literal text and replacement fields delimited by braces {}. 
Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. 
format() will produce a copy of the string where each replacement field is replaced with the string value of the corresponding variables within the parenthesis.


Tasks:
- Fill in the blanks for the name and age variables with your own
- Print a message that looks similar to the one below using the three ways of formatting a string:

```Hello, My name is Thom and I am 556 years old.```

- Create a formatted string using +
- Create a formatted string using %
- Create a formatted using an f-string
- Create a formatted string using format()