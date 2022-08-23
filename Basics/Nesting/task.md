# Nesting
You can link conditions that depend on the result of other conditions. 

Whenever an if statement is inside another if statement or if/else statement, we say that it is nested.

### Example 1: Taxes
```
if income > 9950:
    if income > 40525:
        if income > 86375:
            print(" You are in a higher tax bracket. Consider getting an accountant")
        else:
            print(" You are in the 12% tax bracket")
    else:
        print(" You are in the 10% tax bracket")
else:
    print(" You are in the 0% tax bracket")
```

### Example 2: Shirt sizes
```
chest_width = 59951
if chest_width < 37:
    print("Get a S size")
else:
    if chest_width < 40:
        print("Get a M size")
    else:
        if chest_width < 43:
            print("Get a XL size")
        else:
            print("Get a XXL size")
```


## Elif

Python has a special feature that implements nesting of if and else statements: the elif. 

The ```elif``` construct combines an else and an if, and this reduces the amount of indenting that has to be done when you have nested if within else statements.

<div class="hint">
  An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.
</div>


```
chest_width = 59951
if chest_width < 37:
    print("Get a S size")
elif chest_width < 40:
    print("Get a M size")
elif chest_width < 43:
    print("Get a XL size")
else:
    print("Get a XXL size")
```