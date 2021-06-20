# Challenge Summary

Implement a Queue using two Stacks.
The goal is to write a Queue class that has the functions of both enqueue and dequeue while only relying on stacks. The stack class has the methods push pop and peek to help you.

## Whiteboard Process


![cc11](code%20challenge11.png)



## Approach & Efficiency


Enqueue: Time: O(1) Space: O(1)
Dequeue: Time: O(n) Space: O(n)



## Solution

```
class Pseudo_Queue:
  def __init__(self):
    self.stack = Stack()

  def enqueue(self, val):
    self.stack.push(val)

  def dequeue(self):
    rev_stack = Stack()
    while self.stack.top:
      rev_stack.push(self.stack.pop())
    removed = rev_stack.pop()
    while rev_stack.top:
      self.enqueue(rev_stack.pop())
    return removed
```