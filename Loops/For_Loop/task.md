# For Loop

The while loop is in fact the only kind of loop that is required in order to implement any program. However, there are many cases in which loops need to be executed a fixed or semi-fixed number of times. These type of loops requires you to keep track of how many times the loop has been done.

The ```for``` loop is a loop that supports the type of loops mentioned. In particular, the ```for``` loop has a control variable and a sequence of variables to iterate over.The for loop iterates over the items of any sequence of variables in the order that they appear in the sequence. 

Just like while loops, the for loop executes the lines of code within its suite at each iteration.

Take the following ```for``` loop for example:

```
for i in (1,2,3,4,5):
    print i
```

The loop above will print the numbers 1 2 3 4 5 each on a separate line. The variable i takes on each of the values in the collection provided in parentheses, and the loop executes once for each value of i. 
The collection (1,2,3,4,5) is called a tuple, and can contain any type of variable in any order.


# The range() Function

If you need to iterate over a sequence of numbers, you can use the ```range()``` function to generate an appropriate sequence. The range function generates arithmetic progressions given an end point. The given end point is never part of the generated sequence.

For instance, ```range(10)``` generates 10 values. Namely, it generates the sequence ```(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)``` which would be the legal indices for items of a list of length 10.

By default, range starts at zero. However, it is possible to let the range start at another number.

For instance, ```range(2, 5)``` generates 3 values. Namely, it generates the sequence ```(2, 3, 4)```.

You may also specify a different increment/decrement "step" in the sequence.

For instance, ```range(15, 2, -2)``` generates the sequence ```(15, 13, 9, 7, 5, 3)```. It starts at 15, ends at 2, each item in the sequence is decreased by 2