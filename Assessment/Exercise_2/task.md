# Speeding

You are driving a little too fast, and a police officer stops you. 

Write a function speeding to return one of 3 possible results: "No Ticket", "Small Ticket", or "Big Ticket". 

- If your speed is 60 or less, the result is "No Ticket". 
- If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
- If speed is 81 or more, the result is "Big Ticket". 
 
The limits above apply unless it is your birthday. On your birthday, your speed can be 5 higher in all cases.

Use a boolean value in the parameters of the function to indicate whether today is your birthday or not:
- 0 means it is not your birthday
- 1 means it is your birthday

<div class="hint" xmlns="http://www.w3.org/1999/html">
  Your class definition should look like this: <code>def speeding(speed, birthday):</code>

- The name of the parameters might be different
</div>
