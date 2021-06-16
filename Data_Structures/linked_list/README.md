# Singly Linked List

a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence.

## Challenge

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node's value somewhere within the list.
Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List.

## Approach & Efficiency $ API

 Using many methods ,insert, append, include and str, the insert method is for when the user wants to insert a value at the beginning of the Linked list, the append is for if the user wants to insert a value at the end of the Linked list, the str prints a string containing all the elements inside the linked list in an organized matter, and the include checks if the value is in the linked list or not
append,include,str O(n)
insert O(1)