# Data Structures

# Challenge Summary

Write methods for the Linked List class:

.append(value) which adds a new node with the given value to the end of the list
.insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
.insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

## Whiteboard Process
![ll](code%20challenge6.png)

## Approach & Efficiency

append:iterate over the ll then add the value.
insertBefore: create new node,find target node to insert,search nodes,add the new node
insertAfter:create a new node ,iterate over the ll to find the target and insert the node.

append: O(n)
insertBefore: O(n)
insertAfter:O(n)

## Solution

append:iterate over the ll then add the value.
insertBefore: create new node,find target node to insert,search nodes,add the new node
insertAfter:create a new node ,iterate over the ll to find the target and insert the node.

```
ll=1->2->3->4
input => ll.append(2)
output => 1->2->3->4->2->NULL

input => ll.insertBefore(3,7)
output =>1->2->7->3->4->NULL
input => ll.insertAfter(3,7)
output =>1->2->3->7->4->NULL
```