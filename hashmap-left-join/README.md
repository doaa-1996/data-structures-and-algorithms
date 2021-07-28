# Hashmap LEFT JOIN


## Challenge

The challenge is to create a function that takes in 2 hash tables (python dictionaries). It then returns a structure of values that left joins the two tables.

## [Whiteboard](https://docs.google.com/document/d/1umV-ye5n12U1BPWsObrgjfGzAr1QsHvxQSYKXAFgl5U/edit?usp=sharing)



## Approach & Efficiency

Iterate over each key in the left table. With each key append to the output with it's value and if there is a corresponding key in right add it too else None.


Big O:

Time:O(n)
Space:O(n)




## Solution
[Code](hashmap_left_join/hashmap_left_join.py)

[Test](tests/test_hashmap_left_join.py)

