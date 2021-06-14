# Data Structures

# Challenge Summary

Given a Linked List and a number n, write a function that returns the value at the n’th node from the end of the Linked List.

## Whiteboard Process

![ll](code%20challenge%207.png)

## Approach & Efficiency

Maintain two pointers – reference pointer and main pointer. Initialize both reference and main pointers to head. First, move the reference pointer to n nodes from head. Now move both pointers one by one until the reference pointer reaches the end. Now the main pointer will point to nth node from the end. Return the main pointer.

efficiency =O(n)

## Solution


```

ll=1->2->3->4 
input => ll.kthFromEnd(1)
output => 4


ll=1->2->3->4 
input => ll.kthFromEnd(2)
output => 3
```