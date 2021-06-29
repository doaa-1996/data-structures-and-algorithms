## Challenge

Fizz Buzz Tree

Write a function called fizz buzz tree

Arguments: k-ary tree

Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

If the value is divisible by 3, replace the value with “Fizz”

If the value is divisible by 5, replace the value with “Buzz”

If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

If the value is not divisible by 3 or 5, simply turn the number into a String.



## Whiteboard


![cc18](code%20challenge18.png)


## Approach and efficiency

create a method that accepts a tree as a parametere
start traversing at root
if the  value is devided by(3)
change the value to fizz
if the  value is devided by (5) change the value to buzz
if the value is devided by (3) &(5) change the value to fizzbuzz
else return the same value as str

time complexity: O(n)
space complexity: O(n)



## Solution

[code](tree_fizz_buzz/tree_fizz_buzz.py)


[test](tests/test_tree_fizz_buzz.py)