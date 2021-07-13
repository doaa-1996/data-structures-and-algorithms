# Challenge Summary

## Quick sort

Create a function that uses the quick sort algorithm to sort a list of values.


## Whiteboard Process

![cc28](code%20challenge28.png)


## Approach & Efficiency

we start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element.


Time: O(n Log(n))

Space: O(n)

## Solution

[Code](quick_sort/quick_sort.py)

[Tests](tests/test_quick_sort.py)