# Stacks and Queues

Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle. Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

## Challenge

1. Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
2. Create a Stack class that has a top property. It creates an empty Stack when instantiated. This object should be aware of a default empty value assigned to top when the stack is created.
3. Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
4. Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
5. Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
6. Create a Queue class that has a front property. It creates an empty Queue when instantiated. This object should be aware of a default empty value assigned to front when the queue is created.
7. Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
8. Define a method called dequeue that does not take any argument, removes the node from the ftront of the queue, and returns the node’s value.
9. Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.



## Approach & Efficiency


I implemented both data structures using a basic node class with a next and a value set to none For the stack, I created a class '''Stack()''' and initialized it with self, top and length properties.



## API

for the Stack class:

1. push.

2. pop.

3. peek.

4. isEmpty. 

for the Queue class:

1. enqueue.

2. dequeue. 

3. peek. 

4. isEmpty.