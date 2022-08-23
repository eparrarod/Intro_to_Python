# Else Clause

An if statement is a two-way or binary decision. If the expression is ```True```, then the indicated
statements are executed. If it is ```False```, then it is possible to execute a distinct set of
statements. 

The else is not really a statement on its own, because it MUST be preceded by an if, so it is
part of the if statement. It marks the part of the statement that is executed only when the
condition in the if statement is ```False```. 

The else clause, consists of the word ```else``` followed by a colon, followed by a set of indented statements. 
A  simple example is:
```
if True:
    print ("The condition was true")
else:
    print ("the condition was false")
```
The else as a clause is not required to accomplish any specific programming goals, and it
can be implemented using another if. The code:
```
if a < b:
  print ("a < b")
else:
  print ("a >= b")
```
Could also be written as:
```
if a < b:
  print ("a < b")
if a >= b :
  print ("a >= b")
```


