This is an example of an infinite loop. It will never stop.
```
a = 0
b = 0
while b < 10:
    a = a + 1
    print(a)
```


The loop does not stop because the condition b<10 is always true
- The value of b starts at 0
- The value of b is never updated
- b will always 0
- How can we fix this?

If your code enters into an infinte loop, it will NOT stop until:
- It is manually stopped/killed
- The computer crashes

To stop the program in PyCharm, you do NOT need to close out of PyCharm.

Use ```Ctrl + F2```  or press the suspend/stop button in the bottom left or top right menu ![](https://intellij-icons.jetbrains.design/icons/AllIcons/actions/suspend.svg) 